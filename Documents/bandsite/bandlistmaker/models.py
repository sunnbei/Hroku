from django.db import models


class Members(models.Model):
	id = models.CharField(max_length=6,primary_key=True)
	name = models.CharField(max_length=50)
	email = models.EmailField(blank=True)
	def __str__(self):
		return self.name
		
class Seasons(models.Model):
	
	name = models.CharField(max_length=50)
	year = models.CharField(max_length=4)
	def __str__(self):
		return self.name
		
class Bands(models.Model):
	seasons = models.ForeignKey(Seasons, on_delete=models.PROTECT,null=True,blank=True)
	members = models.ManyToManyField(Members,null=True,blank=True)
	name = models.CharField(max_length=50)
	video_url = models.URLField(max_length=200,blank=True)
	def __str__(self):
		return self.name
		
class Hello(models.Model):
    your_name = models.CharField(max_length=10)
 
    def __str__(self):
        return self.your_name