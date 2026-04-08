import sqlite3

# Datenbank erstellen / verbinden
conn = sqlite3.connect("Wörz_Jakob_fitnessstudio.db")
cursor = conn.cursor()

# =========================
# Tabellen erstellen
# =========================

# Trainer
cursor.execute("""
CREATE TABLE IF NOT EXISTS Trainer (
    TID INTEGER PRIMARY KEY,
    Vorname TEXT,
    Spezialgebiet TEXT,
    Nachname TEXT
)
""")

# Mitglieder
cursor.execute("""
CREATE TABLE IF NOT EXISTS Mitglieder (
    MID INTEGER PRIMARY KEY,
    Beitrittsdatum DATETIME,
    Vorname TEXT,
    Nachname TEXT,
    Email TEXT
)
""")

# Kurse
cursor.execute("""
CREATE TABLE IF NOT EXISTS Kurse (
    KID INTEGER PRIMARY KEY,
    Uhrzeit DATETIME,
    Teilnehmer INTEGER,
    Wochentag TEXT,
    Bezeichnung TEXT,
    TID INTEGER,
    FOREIGN KEY (TID) REFERENCES Trainer(TID)
)
""")

# hat (Anmeldungen)
cursor.execute("""
CREATE TABLE IF NOT EXISTS hat (
    HID INTEGER PRIMARY KEY,
    MID INTEGER,
    KID INTEGER,
    FOREIGN KEY (MID) REFERENCES Mitglieder(MID),
    FOREIGN KEY (KID) REFERENCES Kurse(KID)
)
""")

# =========================
# Beispieldaten einfügen
# =========================

# Trainer (≥ 3)
trainer = [
    (1, "Max", "Krafttraining", "Müller"),
    (2, "Anna", "Yoga", "Schmidt"),
    (3, "Lukas", "Cardio", "Weber")
]
cursor.executemany("INSERT INTO Trainer VALUES (?, ?, ?, ?)", trainer)

# Mitglieder (≥ 6)
mitglieder = [
    (1, "2024-01-10", "Paul", "Meier", "paul@example.com"),
    (2, "2024-02-15", "Lisa", "Huber", "lisa@example.com"),
    (3, "2024-03-01", "Tom", "Bauer", "tom@example.com"),
    (4, "2024-03-20", "Emma", "Fischer", "emma@example.com"),
    (5, "2024-04-05", "Noah", "Wagner", "noah@example.com"),
    (6, "2024-04-18", "Mia", "Hofer", "mia@example.com")
]
cursor.executemany("INSERT INTO Mitglieder VALUES (?, ?, ?, ?, ?)", mitglieder)

# Kurse (≥ 5)
kurse = [
    (1, "2025-06-01 10:00", 15, "Montag", "Yoga Basics", 2),
    (2, "2025-06-02 18:00", 20, "Dienstag", "HIIT", 3),
    (3, "2025-06-03 17:00", 12, "Mittwoch", "Krafttraining", 1),
    (4, "2025-06-04 09:00", 10, "Donnerstag", "Morning Yoga", 2),
    (5, "2025-06-05 19:00", 18, "Freitag", "Cardio Blast", 3)
]
cursor.executemany("INSERT INTO Kurse VALUES (?, ?, ?, ?, ?, ?)", kurse)

# Anmeldungen (≥ 8)
anmeldungen = [
    (1, 1, 1),
    (2, 2, 1),
    (3, 3, 2),
    (4, 4, 2),
    (5, 5, 3),
    (6, 6, 3),
    (7, 1, 4),
    (8, 2, 5)
]
cursor.executemany("INSERT INTO hat VALUES (?, ?, ?)", anmeldungen)

# Änderungen speichern
conn.commit()

print("Datenbank erfolgreich erstellt und befüllt!")

# Verbindung schließen
conn.close()