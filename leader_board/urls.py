from django.urls import path,include
from leader_board.views import leaderBoard,innovationConcept,dashboard



urlpatterns = [
    path("",dashboard,name="dashboard"),
    path("innovationConcept/",innovationConcept,name="innovationConcept"),
    path("leaderBoard/",leaderBoard,name="leaderboard")
]