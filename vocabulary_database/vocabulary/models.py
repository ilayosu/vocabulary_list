from django.db import models

# Create your models here.
class Words(models.Model):

    WORD_TYPE_CHOICES = {
        "noun": "noun",
        "verb": "verb",
        "adjective": "adjective",
        "adverb": "adverb",
    }

    word = models.CharField(max_length=50, primary_key=True, default = "testn/a")
    word_type = models.CharField(max_length=9, choices=WORD_TYPE_CHOICES, default="noun")
    definition = models.CharField(max_length=1000)
    example = models.CharField(max_length=255)

class Tag(models.Model):
    tag = models.CharField(max_length=100, primary_key=True)
    word = models.ManyToManyField(Words)

