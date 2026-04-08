import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable()
def get_kurs_info():
  conn = sqlite3.connect("Wörz_Jakob_fitnessstudio.db")
  cur = conn.cursor()
  cur.execute("""
    SELECT K.KID, K.Bezeichnung, K.Wochentag, K.Uhrzeit, K.Teilnehmer,
    T.Vorname 
    FROM Kurse K
    JOIN Trainer T ON K.TID = T.TID
    """)
  return cur.fetchall()

@anvil.server.callable()
def mitglieder_anmelden():
  conn = sqlite3.connect("Wörz_Jakob_fitnessstudio.db")
  cur = conn.cursor()
  cur.execute("SELECT Vorname FROM Mitglieder")
  return cur.fetchall()