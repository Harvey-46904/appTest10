from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class manage(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('State', default=True)
    create_date = models.DateField('Create date',auto_now=False, auto_now_add=True)
    modify_date = models.DateField('Modify date',auto_now=True, auto_now_add=False)
    delete_date = models.DateField('Delete date',auto_now=True, auto_now_add=False)
    class Meta:
        abstract=True
class Category(manage):
    name=models.CharField('Name',max_length=150,unique=True)
    image=models.ImageField('Image',upload_to='category/')
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name
class social (models.Model):
    facebook=models.URLField('Facebook',null=True,blank=True)
    twitter=models.URLField('Twitter',null=True,blank=True)
    class Meta:
        abstract = True

class Author(manage, social):
    firstname=models.CharField('First name',max_length=150)
    lastname=models.CharField('Lirst name',max_length=150)
    email=models.EmailField('E-mail',max_length=200)
    description = models.TextField('Descripcion')
    image =models.ImageField('Author image',null=True,blank=True,upload_to='authors/')
    class Meta:
        verbose_name='Author'
        verbose_name_plural='Author'
    def __str__(self):
        return '{0},{1},{2}'.format(self.lastname," ", self.firstname)

class Post(manage):
    title =models.CharField('Title',max_length=200)
    description = models.CharField('Description',max_length=200)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    content=RichTextField()
    image=models.ImageField('Image',upload_to='images/',max_length=200)
    published=models.BooleanField('Published/ No published',default=False)
    published_date=models.DateField('Published date')
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
    def __str__(self):
        return self.title



