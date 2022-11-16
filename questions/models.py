from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Category(models.Model):
    category_name_dr=models.CharField(max_length=240)
    category_name_pa=models.CharField(max_length=240)
    category_name_en=models.CharField(max_length=240)
    

    def __str__(self):
        return self.category_name_dr


def upload_question_image(instance,filename):
    return "updates/{question}/{filename}".format(question=instance.question_image, filename=filename)


class Question(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    question_image=models.ImageField(upload_to=upload_question_image, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="questions",
                               default=1)
    questions_category = models.ManyToManyField(Category,
                                        related_name="qcategory",
                                        default=1)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name="qvotes",
                                        default=1)

    def __str__(self):
        return self.content








class Faq(models.Model):
    faq_name=models.CharField(max_length=240)
    faq_questions = models.ManyToManyField(Question,
                                        related_name="faq_questions",
                                        default=1)
    
    def __str__(self):
        return self.faq_name

    


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name="answers")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               default=1)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="votes",
                                    default=1)

    def __str__(self):
        return self.author.username