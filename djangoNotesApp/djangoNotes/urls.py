from django.urls import path
from .views import*

urlpatterns = [
    path('djangonotes/', NoteListView.as_view()),
    path('delete/<int:pk>/',DeleteNoteView.as_view())
]

'''urlpatterns = [
    path('notes/', NoteListCreateView.as_view(),name='note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyView.as_view(), name='note-retrieve-update-destroy'),
]'''