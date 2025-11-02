---
id: b2f1fa45-f585-4f48-a654-d1d89ac2d113
name: hashcat Brute Force a LUKS v1 Hash
type: command
executor: bash
data: hashcat -m 14600 $HASH $WORDLIST
output: "root@kali:~# hashcat -m 14600 hash rockyou.txt  \n\nhashcat (v5.0.0) starting...\n\
  \nHashes: 1 digests; 1 unique digests, 1 unique salts\nBitmaps: 16 bits, 65536 entries,\
  \ 0x0000ffff mask, 262144 bytes, 5/13 rotates\nRules: 1\n\nMinimum password length\
  \ supported by kernel: 0\nMaximum password length supported by kernel: 256\n\nDictionary\
  \ cache hit:\n* Filename..: rockyou.txt\n* Passwords.: 14344385\n* Bytes.....: 139921507\n\
  * Keyspace..: 14344385"
created_at: '2019-10-17T20:33:28.987581+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Hashcat]]'
- '[[unique]]'
---

# hashcat Brute Force a LUKS v1 Hash

```bash
hashcat -m 14600 $HASH $WORDLIST
```

## Expected Output

```
root@kali:~# hashcat -m 14600 hash rockyou.txt  

hashcat (v5.0.0) starting...

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Dictionary cache hit:
* Filename..: rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385
```


