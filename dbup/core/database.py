import psycopg2

class Database():
    """
        A class to handle doing stuff to a database
    """

    def __init__(self, db_name='', username='', password=''):
        """ init the Database object

            Args:
                db_name: name of the postgres database to connect to
                username: db_name login username
                password: username's password in plaintext (yeah sue me)
        """
        self.db_name = db_name
        self.username = username
        self.password = password

    def create(self):
        """ create the database

            returns 0 on sucess, 1 on failure
        """
        rc = 0
        sql = (""" create database {0} """.format(self.db_name))

        try:
            with psycopg2.connect(database='postgres', user=self.username, password=self.password) as conn:
                conn.autocommit = True
                with conn.cursor() as c:
                    c.execute(sql)
        except:
            rc = 1
        return rc

