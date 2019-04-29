from django.shortcuts import render
import plotly
#from plotly.graph_objs import Scatter, Layout
import plotly.offline as opy
import plotly.graph_objs as go
from django.views.generic.base import TemplateView

from .models import dummy_for_histo_and_cloud

# 4.11
# 만약 검색 기업별로 그거 한다고 치면 검색했을 때 form 에서 기업 이름이 함수의 인자로 넘어와서
# heese_blog = Blog.objects.get(name="KT")
# 이런식으로 오브젝트 만들고 난 뒤에 아래에 해당하는 것을 그려주면 될것 같다.


class Graph(TemplateView):
    template_name = 'result.html'

# 최빈값 뽑아내는 알고리즘 -------------------------------------------------------
    list_x = []
    list_x = list(dummy_for_histo_and_cloud.objects.values_list('x_axis_keyword', flat=True))

    list_y = []
    list_y = list(dummy_for_histo_and_cloud.objects.values_list('y_axis_quantity', flat=True))

    ordinary_dict = {}
    ordinary_dict = dict(zip(list_x, list_y))

    max5_y_list = []
    max5_x_list = []


    for i in range(0, 5, 1):
        max_v = max(list_y)
        max5_y_list.append(max_v)
        list_y.remove(max_v)

    for elem in max5_y_list:
        for name, age in ordinary_dict.items():
            if elem == age:
                max5_x_list.append(name)
    
# 이전에 각각의 DB에서 가장 빈도수가 높은 5개의 list_y에 해당하는 list_x 값을 가져와야 한다!!!!!!!!!!

# 최빈값 종료 --------------------------------------------------------


    # 히스토 그램 뽑아내기
    def get_context_data(self, **kwargs):

        context = super(Graph, self).get_context_data(**kwargs)

        data = [go.Bar(x=[self.max5_x_list[0], self.max5_x_list[1], self.max5_x_list[2], self.max5_x_list[3], self.max5_x_list[4]], y=[self.max5_y_list[0], self.max5_y_list[1], self.max5_y_list[2], self.max5_y_list[3], self.max5_y_list[4]])]
        
        layout=go.Layout(title="키워드 분석 결과", xaxis={'title':'키워드'}, yaxis={'title':'빈도'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['Graph'] = div

        return context

def home(request):
    return render(request, 'home.html')

# 분석 결과 보여주는 페이지 --------
def result(request):
    graph = Graph()
    context =  graph.get_context_data()
    return render(request, 'result.html', context)

