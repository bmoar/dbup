class SyslogtagFilter():
    """ Injects a syslogtag into a log format """

    def __init__(self, syslogtag):
        self.syslogtag = syslogtag

    def filter(self, record):
        record.syslogtag = self.syslogtag
        return True

def init_logger(syslogtag='dbup', logger='debug'):
    import logging, logging.config

    loggers = {
            'version': 1,
            'disable_existing_loggers': True,
            'filters': {
                'syslogtag': {
                    '()': SyslogtagFilter,
                    'syslogtag': syslogtag,
                    },
                },
            'formatters': {
                'detailed': {
                    'format': '[%(syslogtag)s] [%(levelname)s] (%(filename)s:%(funcName)s:%(lineno)s) %(message)s'
                    },
                },
            'handlers': {
                'stderr': {
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://sys.stderr',
                    'formatter': 'detailed',
                    'filters': ['syslogtag'],
                    },
                'syslog': {
                    'class': 'logging.handlers.SysLogHandler',
                    'address': '/dev/log',
                    'formatter': 'detailed',
                    'filters': ['syslogtag'],
                    },
                },
            'loggers': {
                'stderr': {
                    'level': 'INFO',
                    'handlers': ['stderr'],
                    'propagate': False,
                    },
                'debug': {
                    'level': 'DEBUG',
                    'handlers': ['stderr'],
                    'propagate': False,
                    },
                'prod': {
                    'level': 'INFO',
                    'handlers': ['syslog'],
                    'propagate': False,
                    },
                'prod_debug': {
                    'level': 'DEBUG',
                    'handlers': ['syslog'],
                    'propagate': False,
                    },
                },
            'root': {
                'level': 'INFO',
                'handlers': ['stderr'],
                },
            }
    logging.config.dictConfig(loggers)
    return logging.getLogger(logger)
