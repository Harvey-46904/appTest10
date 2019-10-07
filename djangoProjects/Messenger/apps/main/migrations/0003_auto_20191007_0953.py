# Generated by Django 2.2.4 on 2019-10-07 14:53

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_social_uthor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Create date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete date')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('firstname', models.CharField(max_length=150, verbose_name='First name')),
                ('lastname', models.CharField(max_length=150, verbose_name='Lirst name')),
                ('email', models.EmailField(max_length=200, verbose_name='E-mail')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='authors/', verbose_name='Author image')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Create date')),
                ('modify_date', models.DateField(auto_now=True, verbose_name='Modify date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Delete date')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(max_length=200, upload_to='images/', verbose_name='Image')),
                ('published', models.BooleanField(default=False, verbose_name='Published/ No published')),
                ('published_date', models.DateField(verbose_name='Published date')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Author')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.DeleteModel(
            name='social',
        ),
        migrations.DeleteModel(
            name='uthor',
        ),
    ]