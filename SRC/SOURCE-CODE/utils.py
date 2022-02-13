import mysql.connector


def run_sql_file(CONNECTOR, sql_path, pt, **fmt):
    cur = CONNECTOR.cursor()
    with open(sql_path, "r") as f:
        cur.execute(f.read().format(**fmt))  # to update !
        result = cur.fetchone()
    for row in result:
        print(row)
    cur.close()
