#!/usr/bin/python3
from models import *
import services
from views.main_view import MainView

def main():
    MainView(services)

if __name__ == '__main__':
    main()