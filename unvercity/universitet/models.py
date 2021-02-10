from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=100,null=False)
    group = models.CharField(max_length=50,null=False)
    age = models.IntegerField(null=False)

    def __str__(self):
        return self.name


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)