import sqlite3

conn = sqlite3.connect("roster.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
""")

cur.execute("DELETE FROM Roster")

# Inserting values:
cur.executemany("""
    INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

cur.execute("""
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'
""")

# Display Name and Age of everyone classified as Bajoran
cur.execute("""
    SELECT Name, Age
    FROM Roster
    WHERE Species = 'Bajoran'
""")
results = cur.fetchall()

# Output th results:
print("Bajoran Members:")
for name, age in results:
    print(f"{name} - {age} years old")

conn.commit()
conn.close()
