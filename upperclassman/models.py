from django.db import models

class Upperclassman(models.Model):
	name = models.CharField(max_length=35)
	netid = models.CharField(max_length=10)
	year = models.CharField(max_length=100)
	college = models.CharField(max_length=100)
	major1 = models.CharField(max_length=200)
	major2 = models.CharField(max_length=200)
	major3 = models.CharField(max_length=200, null=True)
	finished = models.BooleanField(default=False)
	survey = models.TextField()
	organization = models.TextField()

	def __unicode__(self):
		return u'%s %s' % (self.name, self.netid)