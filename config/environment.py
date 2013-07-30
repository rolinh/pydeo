import os

from config import settings

if settings.environment == 'production':
    import config.environments.production as env
elif settings.environment == 'development':
    import config.environments.development as env
elif settings.environment == 'test':
    import config.environments.test as env
else:
    raise RuntimeError("Environment not set or incorrect")

debug = env.debug
reloader = env.reloader
db_echo = env.db_echo
