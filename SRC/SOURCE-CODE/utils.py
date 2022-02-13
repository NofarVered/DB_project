
def run_sql_file(CONNECTOR, sql_path, **fmt):
    cur = CONNECTOR.cursor()
    with open(sql_path, "r") as f:
        cur.execute(f.read().format(**fmt))
        result = cur.fetchone()
    cur.close()
    return result


def get_2(mycursor, pt):
    print(q2)
