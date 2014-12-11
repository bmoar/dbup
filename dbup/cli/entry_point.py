"""
    Entry point for CI scripts
"""

from cement.core import foundation
from cement.core.exc import CaughtSignal, FrameworkError
from cement.core.controller import CementBaseController, expose

from dbup.conf.logger import init_logger
from dbup.lib.database import Database

class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'dbup - create, update, and rollback databases in a transaction'
        arguments = [
            (['-n', '--name'], dict(help='database to connect to')),
            (['-u', '--username'], dict(help='database username')),
            (['-p', '--password'], dict(help='database username\'s password')),
        ]

    @expose(hide=True)
    def default(self):
        self.app.log.info('hello world')

    @expose(help='create a new database')
    def create(self):
        self.app.log.info('creating database: %s' % (self.app.pargs.name))
        db = Database(self.app.pargs.name, self.app.pargs.username)
        if not db.create()
            raise Exception("

class DbupApp(foundation.CementApp):
    class Meta:
        label = 'dbup'
        base_controller = BaseController

def main():
    rc = 0
    log = init_logger(logger='debug')
    app = DbupApp()

    try:
        app.setup()
        app.log = log
        app.run()
    except CaughtSignal as e:
        app.log.error('caught signal %s' % (e))
        rc = 1
    except FrameworkError as e:
        app.log.error('framework error %s' % (e))
        rc = 2
    except Exception as e:
        app.log.error('exception %s' % (e))
        rc = 1

    finally:
        app.close(rc)

if __name__ == '__main__':
    main()

