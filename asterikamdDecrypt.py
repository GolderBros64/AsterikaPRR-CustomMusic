from pathlib import Path

name = input(".asterikamd: ").strip().strip('"')
src = Path(name)

data = bytearray(src.read_bytes())

key = bytes.fromhex(
    "4153544552494b4153555349434b657931"
)

# Remove ARCO + header byte
encrypted = data[5:]

# Exact algorithm used by the game
for i in range(len(encrypted)):
    encrypted[i] ^= key[i % len(key)]

x = name.strip().strip(".asterikamd").strip(".preview").strip('"').strip(".")
out = Path(x+".ogg")
out.write_bytes(encrypted)

print("Output:", out)
print("Size:", len(encrypted))
print("Signature:", encrypted[:4])