import sqlite3

class Data:
    def __init__(self):
        self.conn = sqlite3.connect('perpus.db')
        self.cursor = self.conn.cursor()

    def Run(self, query, returnData = False):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.conn.commit()
        if returnData :
            return result