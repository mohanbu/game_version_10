# start up the game

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from core.support import build_route, default_route, build_form
from forms.shirtchoice import ShirtChoiceHandler

# define our routes
game_routes = [build_form('shirtchoice', ShirtChoiceHandler),
               build_route('restart','RestartHandler'),
               build_route('startingpoint','StartingPointHandler'),
               build_route('pharmacy_room','PharmacyRoomHandler'),
               build_route('atrium','AtriumHandler'),
               build_route('vaccination_room','VaccinationRoomHandler'),
               build_route('monster_room','MonsterRoomHandler'),
               build_route('party_room','PartyRoomHandler'),
               build_route('dead_monster_room','DeadMonsterRoomHandler'),
               default_route('startingpoint', 'StartingPointHandler'),
               ]

application = webapp.WSGIApplication(game_routes, debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
