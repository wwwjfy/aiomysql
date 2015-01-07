import aiomysql
from tests import base

class TestExample(base.AIOPyMySQLTestCase):

    def test_example(self):
        conn = yield from aiomysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='mysql')


        cur = conn.cursor()

        cur.execute("SELECT Host,User FROM user")

        # print cur.description

        # r = cur.fetchall()
        # print r
        # ...or...
        u = False

        for r in cur.fetchall():
            u = u or conn.user in r

        self.assertTrue(u)

        cur.close()
        conn.close()