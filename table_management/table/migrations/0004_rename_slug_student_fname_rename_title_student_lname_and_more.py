# Generated by Django 4.0.3 on 2022-04-04 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_remove_student_fname_remove_student_lname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='slug',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='title',
            new_name='lname',
        ),
        migrations.AddField(
            model_name='student',
            name='roll',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sclass',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]