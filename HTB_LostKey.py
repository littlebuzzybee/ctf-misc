from hashlib import sha1
from Crypto.Cipher import AES


def main():
    iv = bytes.fromhex("baf9137b5bb8fa896ca84ce1a98b34e5")
    ct = bytes.fromhex("df572f57ac514eeee9075bc0ff4d946a80cb16a6e8cd3e1bb686fabe543698dd8f62184060aecff758b29d92ed0e5a315579b47f6963260d5d52b7ba00ac47fd")

    n_max = 38685626227668133590597631
    r = 82438979720724695506
    mod = 134876030111980880301
    
    for k in range(int(n_max/mod)):
        n = r + k*mod
        key = sha1(str(n).encode('ascii')).digest()[0:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = cipher.decrypt(ct)
        if b'HTB' in pt:
            print(pt)
            return
    
if __name__ == "__main__":
    main()
