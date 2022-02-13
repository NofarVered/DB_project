import mysql.connector


def run_sql_file(CONNECTOR, sql_path, pt):
    cur = CONNECTOR.cursor()
    with open(sql_path, "r") as f:
        query = f.read()
        cur.execute(query, (pt))
        result = cur.fetchone()
    for row in result:
        print(row)
    cur.close()
