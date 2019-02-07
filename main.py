#!/usr/bin/python3
from models import *
from services import *
from views.main_view import MainView

def main():
    season_service = SeasonService()
    score_service = ScoreService()

    MainView(score_service, season_service)

if __name__ == '__main__':
    main()