from rest_framework import serializers 
from Profile.models import ProfileDB
 
 
class ProfileSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ProfileDB
        fields='__all__'
        # fields = ('firstName',
        #           'lastName',
        #           'email',
        #           'password'
        #         #   'created_at'
        #           )