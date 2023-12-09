'''from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import NoteSerializers
# Create your views here.

class NoteListCreateView(generics.ListCreateAPIView):
    queryset=Note.objects.all()
    serializer_class=NoteSerializers

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Note.objects.all()
    serializer_class=NoteSerializers
'''

#import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializers

'''class RoutesView(APIView):

    def get(self, request):
        routes = [
            {
                'Endpoint': '/notes/',
                'method': 'GET',
                'body': None,
                'description': 'Returns an array of notes'
            },
            {
                'Endpoint': '/notes/id',
                'method': 'GET',
                'body': None,
                'description': 'Returns a single note object'
            },
            {
                'Endpoint': '/notes/create/',
                'method': 'POST',
                'body': {'body': ""},
                'description': 'Creates new note with data sent in post request'
            },
            {
                'Endpoint': '/notes/id/update/',
                'method': 'PUT',
                'body': {'body': ""},
                'description': 'Creates an existing note with data sent in post request'
            },
            {
                'Endpoint': '/notes/id/delete/',
                'method': 'DELETE',
                'body': None,
                'description': 'Deletes an existing note'
            },
        ]

        return Response(routes)'''

class NoteListView(APIView):

    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializers(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class DeleteNoteView(APIView):

    def delete(self, request, note_id):
        try:
            note = Note.objects.get(id=note_id)
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Note.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        
'''
            else:   
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # Assuming the note_id is passed in the request data or URL parameters
        note_id = request.data.get('note_id')
        if note_id:
            try:
                note = Note.objects.get(id=note_id)
                note.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Note.DoesNotExist:
                return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"error": "Missing note_id"}, status=status.HTTP_400_BAD_REQUEST)
        
        except Note.DoesNotExist:
        return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)
        '''
    
