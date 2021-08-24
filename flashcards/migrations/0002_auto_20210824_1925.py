# Generated by Django 3.2.6 on 2021-08-24 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='deck',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='parent_deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flashcards', to='flashcards.deck'),
        ),
    ]
