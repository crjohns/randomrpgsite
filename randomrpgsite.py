import os
import logging

from pyramid.config import Configurator
from pyramid.view import view_config

from wsgiref.simple_server import make_server


logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

# views
@view_config(route_name='index', renderer='index.jinja2')
def index(request):
    return {}

@view_config(route_name='select_game', renderer='select_game.jinja2')
def select_game(request):
    return {}

@view_config(route_name='gm_console', renderer='gm_console.jinja2')
def gm_console(request):
    return {}

@view_config(route_name='player_console', renderer='player_console.jinja2')
def player_console(request):
    return {}

if __name__ == '__main__':
    # configuration settings
    settings = {}
    settings['reload_all'] = True
    settings['debug_all'] = True

    # configuration setup
    config = Configurator(settings=settings)

    #set up jinja2 templates
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path("randomrpgsite:templates")

    # routes setup
    config.add_route('index', '/')
    config.add_route('select_game', '/select-game')
    config.add_route('gm_console', '/gm-console')
    config.add_route('player_console', '/player-console')

    # static view setup
    config.add_static_view('static', os.path.join(here, 'static'))
    # scan for @view_config and @subscriber decorators
    config.scan()
    # serve app
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
