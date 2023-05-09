from django.db import models


class Word(models.Model):
    word = models.TextField()
    word_translate = models.TextField()

    def __str__(self):
        return f'{self.word} - {self.word_translate}'