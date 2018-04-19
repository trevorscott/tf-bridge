import connexion
import os
from api.resolver import tensor_bridge_api_resolver
from connexion.resolver import Resolver
from checks import Checks

DEBUG = True
PORT = os.environ['PORT']

app = connexion.App(__name__, specification_dir='swagger/', debug=DEBUG)
app.add_api('tensor_bridge.json',
            resolver=Resolver(function_resolver=tensor_bridge_api_resolver))

Checks(app.app)

if DEBUG:
    app.run(port=PORT, debug=False)
else:
    application = app.app
