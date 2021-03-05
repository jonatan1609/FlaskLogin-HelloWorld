from .app import app
from importlib import import_module

import_module('.endpoints', package="HelloWorld")  # executing and adding all endpoints

app.run(port=54321)
