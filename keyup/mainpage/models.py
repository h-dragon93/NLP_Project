from django.db import models



class dummy_for_histo_and_cloud(models.Model):
    objects = models.Manager()
    # 기업의 이름으로 열을 더 만들어서 이걸 기준으로 가져올 수 있다.
    # 그러나 노가다를 해야 하는데 이것을 어떻게 해결하지..?
    
    # "id" serial NOT NULL PRIMARY KEY 자동 생성

    company_name = models.CharField(max_length=100)
    # IoT, 머신러닝, 이런게 x축에 박힌다고 생각하고
    x_axis_keyword = models.CharField(max_length=50)
    # 빈도수가 정수형으로 박힌다고 생각하자
    y_axis_quantity = models.IntegerField()

    def __str__(self):
        return self.company_name

