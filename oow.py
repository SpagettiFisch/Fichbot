import sqlite3
con = sqlite3.connect("BotFiles\BotThings.sqlite")
cur = con.cursor()

cur.execute("DROP TABLE reactionRoles")
con.commit()