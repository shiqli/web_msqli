from django.db import models
# Create your models here.

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()
	
	def __unicode__(self):   #when object is called, this is what will be returned
		return self.name

	class Meta:
		ordering = ['name']
	
class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	#The syntax below demonstrate two different things: 1. Make an optional field 2. change the possible label definition
	email = models.EmailField(blank=True, verbose_name='e-mail') #Blank indicates an optional field
	
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

	class Meta:
		ordering = ['last_name']


class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
	
	def __unicode__(self):
		return self.title

class Keyword(models.Model):
	keyword_text = models.CharField(max_length=30)

	def __str__(self):
		return self.keyword_text
	
	class Meta:
		ordering = ('keyword_text',)

class Journal(models.Model):
	name = models.CharField(max_length = 100)
	abreviation = models.CharField(max_length = 100)
	publisher = models.ForeignKey(Publisher)
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ('name',)


class Publication(models.Model):
	headline = models.CharField(max_length=100)
	keywords = models.ManyToManyField(Keyword)
	journal = models.ForeignKey(Journal)
	year = models.IntegerField(default = 2008)
	volume = models.IntegerField(default = 1)
	issue = models.IntegerField(default = 1)
	doi = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author, through = 'AuthorSequencing')
	start_page = models.CharField(max_length=100)
	link = models.URLField(max_length=200)
	image = models.URLField(max_length=200, default ='http://www.acs.org')
	def __unicode__(self):
		return self.headline
	def authorinrank(self):
		return self.authorsequencing_set.order_by('author_rank')
	class Meta:
		ordering = ('year',)

class AuthorSequencing(models.Model):
        author = models.ForeignKey(Author)
        publication = models.ForeignKey(Publication)
        author_rank = models.IntegerField(default = 1)

	def __unicode__(self):
		toDisplay = ','.join([self.author.last_name,str(self.author_rank),self.publication.headline])
		return toDisplay

	class Meta:
		ordering = ('author_rank',)
