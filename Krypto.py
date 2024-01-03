import hashlib

def hash_text(text):
    # Erstelle ein Hash-Objekt mit md5
    hash_object = hashlib.sha512()

    # Aktualisiere das Hash-Objekt mit dem Text (muss im UTF-8-Format sein)
    hash_object.update(text.encode('utf-8'))

    # Gibt den gehashten Text zurück
    hashed_text = hash_object.hexdigest()
    return hashed_text

# Beispieltext
mein_text = "Geheim"

# Verschlüssle den Text
verschlüsselter_text = hash_text(mein_text)

# Gib den ursprünglichen und den verschlüsselten Text aus
print("Ursprünglicher Text:", mein_text)
print("Verschlüsselter Text:", verschlüsselter_text)
