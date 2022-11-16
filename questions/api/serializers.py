from rest_framework import serializers
from questions.models import Answer, Question, Category, Faq




class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    question_slug = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ["question", "voters", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_question_slug(self, instance):
        return instance.question.slug



class FaqSerializer(serializers.ModelSerializer):
    faq_name = serializers.StringRelatedField(read_only=True)
    questions_count = serializers.SerializerMethodField()
    category_questions = serializers.SerializerMethodField()
  


    class Meta:
        model = Faq
        exclude = []

    def questions_count(self, instance):
        return instance.faq_questions.count()

 

    def category_questions(self, instance):
        return instance.question.content




   

class CategorySerializer(serializers.ModelSerializer):
    cateory_name_en = serializers.StringRelatedField(read_only=True)
    cateory_name_dr = serializers.StringRelatedField(read_only=True)
    cateory_name_pa = serializers.StringRelatedField(read_only=True)


    class Meta:
        model = Category
        exclude = []

    
from rest_framework import serializers    

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
















#https://stackoverflow.com/questions/28036404/django-rest-framework-upload-image-the-submitted-data-was-not-a-file/28036805#28036805
#https://stackoverflow.com/questions/44271450/upload-image-file-using-django-rest-framework-in-a-single-page-application
class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    # question_image = serializers.ImageField(max_length=None, use_url=True)

    question_image  = Base64ImageField(max_length=None, use_url=True, )

    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()

