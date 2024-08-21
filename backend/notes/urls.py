from django.urls import path

from . import views

urlpatterns = [
    path("notes/", views.NoteList.as_view(), name="note_list"),
    path("notes/<int:pk>/", views.NoteDelete.as_view(), name="note_delete"),
]
