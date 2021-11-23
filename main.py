import logging
import discord

logging.basicConfig(level=logging.INFO)

dbhost = "f2296a0.online-server.cloud"

from Sqltest import SQL_DB
sql_db = SQL_DB(dbhost)
sql_db.connect_to_db('werwolfbot')
sql_db.show_all_tabels()

from GameLogic import GameLogic
game_logic = GameLogic(sql_db)
