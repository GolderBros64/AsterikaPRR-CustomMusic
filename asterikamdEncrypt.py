from pathlib import Path

key = bytes.fromhex(
    "4153544552494b4153555349434b657931"
)

def Encrypt(srcin: str,id: str,type: bool = False):
    src = Path(srcin.strip().strip('"'))
    out_name = id.strip().strip('"')

    if not out_name.lower().endswith(".asterikamd"):
        if type:
            out_name += ".preview.asterikamd"
        else:
            out_name += ".asterikamd"

    BASE_DIR = Path(__file__).resolve().parent
    out = BASE_DIR / "EncryptedSongs" / out_name
    out.parent.mkdir(parents=True, exist_ok=True)

    ogg = bytearray(src.read_bytes())

    for i in range(len(ogg)):
        ogg[i] ^= key[i % len(key)]

    result = b"ARCO\x01" + ogg

    out.write_bytes(result)

    print()
    print("Created:", out)
    print("Size:", len(result))
    print("Header:", result[:5])