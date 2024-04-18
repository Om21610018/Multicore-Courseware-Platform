# Generated by Django 5.0.3 on 2024-04-18 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_quiz_coursecontent_quiz_quizquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.DeleteModel(
            name='QuizQuestion',
        ),
    ]
