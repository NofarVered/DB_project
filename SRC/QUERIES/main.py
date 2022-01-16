import pymysql

CONNECTOR = pymysql.connect(
    host='localhost',
    port=3305,
    user='DbMysql36',
    password='DbMysql36',
    database='DbMysql36'
)

what_to_predict = """
Welcome to .....
"""

navigate = input(what_to_predict)
