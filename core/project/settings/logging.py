LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standart': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s '
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standart',
            'filters': [],
        },
    },
    'loggers': {
        logger_name: {
            'level': 'WARNING',
            'propagata': True,
        } for logger_name in ('django', 'django.request', 'django.db.backends', 'django.template', 'core')
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
}
