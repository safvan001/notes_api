from django.contrib import admin
from django.urls import path
from notes.views import *

urlpatterns = [
    path('notes/',CreateNoteView.as_view(),name='create-notes'),
    path('notes/<int:pk>/',RetrieveNoteView.as_view(),name='fetch-note'),
    path('notes/<int:pk>/update/',UpdateNoteView.as_view(),name='update-note'),
    path('notes/query/',QueryNotesListView.as_view(),name='query-notes')
]
