import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists words")
        ddl = "create table words(word text not null constraint table_name_pk primary key, usage_count int default 1 not null);create unique index table_name_word_uindexon words (word);"
        cur.execute(ddl)
        ddl = "create unique INDEX words_word_uindex ON words(word)"
        cur.execute(ddl)
    conn.close()
# def save_words_to_database(database_path: str, words_list: list):
#
#
# # TODO: save th words to the database
# pass
