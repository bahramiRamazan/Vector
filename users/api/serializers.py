from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    ModelSerializer,
    CharField,
)
from rest_framework import serializers
from users.models import User
   

from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(RegisterSerializer):
    language_prefered = serializers.CharField(
        required=False,
        max_length=24,
    )
    mobil = serializers.CharField(
        required=False,
        max_length=24,
    )
   


    def get_cleaned_data(self):
      
        data_dict = super().get_cleaned_data()
        data_dict['language_prefered'] = self.validated_data.get('language_prefered', '')
        data_dict['mobil'] = self.validated_data.get('mobil', '')
        return data_dict

 



class ChangePasswordSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    new_password = CharField(write_only=True)
    old_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'old_password', 'new_password','confirm_password']



    def update(self, instance, validated_data):

        instance.password = validated_data.get('password', instance.password)

        if not validated_data['new_password']:
                raise serializers.ValidationError({'new_password': 'not found'})

        if not validated_data['old_password']:
                raise serializers.ValidationError({'old_password': 'not found'})

        if not instance.check_password(validated_data['old_password']):
                raise serializers.ValidationError({'old_password': 'wrong password'})

        if validated_data['new_password'] != validated_data['confirm_password']:
            raise serializers.ValidationError({'passwords': 'passwords do not match'})

        if validated_data['new_password'] == validated_data['confirm_password'] and instance.check_password(validated_data['old_password']):
            # instance.password = validated_data['new_password'] 
            print(instance.password)
            instance.set_password(validated_data['new_password'])
            print(instance.password)
            instance.save()
            return instance
        return instance




class PreferenceSerializer(ModelSerializer):
    language_prefered = CharField(read_only=True)
    username=CharField(read_only=True)
  

    class Meta:
        model = User
        fields = [ 'username',  'language_prefered']



    # def update(self, instance, validated_data):

    #     instance.language_prefered = validated_data.get('language_prefered', instance.language_prefered)

    #     if not validated_data['language_prefered']:
    #             raise serializers.ValidationError({'language_prefered': 'not found'})



       
    #     # instance.password = validated_data['new_password'] 
    #     print(instance.language_prefered)
        
    #     print(instance.language_prefered)
    #     instance.save()
    #     return instance
    #     return instance