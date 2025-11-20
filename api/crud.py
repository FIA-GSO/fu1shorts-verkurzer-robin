#  Hier liegen Hilfsfunktionen zur Kommunikation mit der Datenbank.
#
# CRUD steht für Create, Read, Update und Delete, den vier grundlegenden
# Operationen einer Datenbank.

from .database import *

class ShortDBClient:
    
    def create_short(self, url: str) -> int:
        """ Fügt einen neuen Short-Link in die Datenbank ein. """
        con = get_connection()
        c = con.cursor()
        c.execute("INSERT INTO shorts (url) VALUES (?)", (url,))
        con.commit()
        id = c.lastrowid
        con.close()
        return id
    
    def update_short(self, id: int, url: str) -> bool:
        """ Aktualisiert einen bestehenden Short-Link in der Datenbank. """
        con = get_connection()
        c = con.cursor()
        c.execute("UPDATE shorts SET url = ? WHERE id = ?", (url, id))
        con.commit()
        con.close()
        return True

    def read_short(self, id: int) -> str:
        """ Holt einen bestimmten Short-Link aus der Datenbank. """
        con = get_connection()
        c = con.cursor()
        c.execute("SELECT url FROM shorts WHERE id = ?", (id,))
        url:list[str] = c.fetchone()
        con.close()
        return url[0]


    def read_all(self) -> list[str]:
        """ Holt alle Short-Links aus der Datenbank. """
        con = get_connection()
        c = con.cursor()
        c.execute("SELECT url FROM shorts")
        rows = c.fetchall()
        url = [row[0] for row in rows]
        con.close()
        return url


    def read_short_random(self) -> str:
        """ Holt einen zufälligen Short-Link aus der Datenbank. """
        con = get_connection()
        c = con.cursor()
        c.execute("SELECT url FROM shorts ORDER BY RANDOM() LIMIT 1")
        url = c.fetchone()
        con.close()
        return url[0]

    def delete_short(self, id: int) -> bool:
        """ Löscht einen Short-Link aus der Datenbank. """
        con = get_connection()
        c = con.cursor()
        c.execute("DELETE FROM shorts WHERE id = ?", (id,))
        con.commit()
        con.close()
        return True


