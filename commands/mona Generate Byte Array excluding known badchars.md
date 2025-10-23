---
id: 20278b71-6685-4fcd-b449-eed6d39aeac9
name: mona Generate Byte Array excluding known badchars
type: command
executor: ''
data: '!mona bytearray -cpb "\x00\x0a"'
output: "[+] Command used:\n!mona bytearray -cpb \"\\x00\\x0a\"\nGenerating table,\
  \ excluding 2 bad chars...\nDumping table to file\n[+] Preparing output file 'bytearray.txt'\n\
  \    - (Re)setting logfile bytearray.txt\n\"\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\\
  x08\\x09\\x0b\\x0c\\x0d\\x0e\\x0f\\x10\\x11\\x12\\x13\\x14\\x15\\x16\\x17\\x18\\\
  x19\\x1a\\x1b\\x1c\\x1d\\x1e\\x1f\\x20\\x21\"\n..."
created_at: '2019-09-21T00:36:54.556085+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mona Generate Byte Array excluding known badchars

```bash
!mona bytearray -cpb "\x00\x0a"
```

## Expected Output

```
[+] Command used:
!mona bytearray -cpb "\x00\x0a"
Generating table, excluding 2 bad chars...
Dumping table to file
[+] Preparing output file 'bytearray.txt'
    - (Re)setting logfile bytearray.txt
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21"
...
```


