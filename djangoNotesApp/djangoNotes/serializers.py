from rest_framework import serializers
from .models import *

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model=Note
        #fields=('id','noteText','date')
        fields='__all__'