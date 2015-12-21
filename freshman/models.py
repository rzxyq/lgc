from django.db import models


class NewStudent(models.Model):
    name = models.CharField(max_length=35)
    netid = models.CharField(max_length=10)
    # hometown = models.CharField(max_length=35)
    # year = models.CharField(max_length=20)
    # college = models.CharField(max_length=50)

    # major = models.CharField(max_length=200)
    # minor = models.TextField()

    # extracurricular = models.TextField()  #multiple choices
    # extra_sa = models.TextField(max_length=75, null=True)  #short answer

    # career = models.TextField()  #multiple choice
    # career_sa = models.TextField(max_length=75, null=True)  #short answer

    # #short answeres - see template to see questions
    # sa1 = models.TextField(max_length=250, null=True)
    # sa2 = models.TextField(max_length=250, null=True)
    # sa3 = models.TextField(max_length=250, null=True)

    # # how did you hear from us question
    # survey = models.TextField()

    # # not shown in survey. shown in database
    # selected = models.BooleanField(default=False)
    # upperclassman = models.ForeignKey('upperclassman.Upperclassman', null=True)
