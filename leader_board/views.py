from django.shortcuts import render
from leader_board.leaderBoard import getToppers

def dashboard(request):
    return render(request,"leader_board/dashboard.html")

def innovationConcept(request):
    return render(request,"leader_board/innovation_concept.html")


def leaderBoard(request):
    data=getToppers()
    return render(request,"leader_board/leaderBoard.html",{"toppers":data})

