#!/usr/bin/python3
from models import *
from serivices import *

def main():
    # season1 = Season('2018 summer', '1/1/2018')
    # season2 = Season('2018 summer', '1/1/2018')
    
    # age_group_service = AgeGroupService()
    # swimmer_service = SwimmerService()
    season_service = SeasonService()
    score_service = ScoreService()

    for season in season_service.getAll():
        print(season.getName())

    for score in score_service.getAllBySeasonName('ethiopia_season1_2018'):
        print(score.getSwimmer().getFullname())

if __name__ == '__main__':
    main()