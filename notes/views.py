from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from notes.models import Note
from notes.serializer import NoteSerializer

class CreateNoteView(generics.CreateAPIView):
    "This view handles the creation of new notes"
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

class RetrieveNoteView(generics.RetrieveAPIView):
    "This view allows you to fetch a single note by its id"
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

class UpdateNoteView(generics.UpdateAPIView):
    "This view is responsible for updating an existing note"
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

class QueryNotesListView(generics.ListAPIView):
    "This view allows querying notes by a substring in their title."
    serializer_class=NoteSerializer

    def get_queryset(self):
        title_substring=self.request.query_params.get('title')
        return Note.objects.filter(title__icontains=title_substring)
        







