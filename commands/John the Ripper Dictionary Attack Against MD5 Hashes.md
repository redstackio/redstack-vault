---
id: 90d1c228-e8dd-4453-8a3c-a36bd16bbc96
name: John the Ripper Dictionary Attack Against MD5 Hashes
type: command
executor: bash
data: john --format=md5crypt --wordlist=$_PASSWORD_FILE $_HASH_FILE
output: "root@hackers:~# john --format=md5crypt --wordlist=/opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt\
  \ md5.hash \nUsing default input encoding: UTF-8\nLoaded 1 password hash (md5crypt,\
  \ crypt(3) $1$ [MD5 256/256 AVX2 8x3])\nWill run 2 OpenMP threads\nPress 'q' or\
  \ Ctrl-C to abort, almost any other key for status\nWarning: Only 14 candidates\
  \ left, minimum 48 needed for performance.\nRedStack         (?)\n1g 0:00:00:00\
  \ DONE (2019-09-16 16:13) 100.0g/s 1400p/s 1400c/s 1400C/s 123456..RedStack\nUse\
  \ the \"--show\" option to display all of the cracked passwords reliably\nSession\
  \ completed\n"
created_at: '2019-09-16T23:24:10.097830+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# John the Ripper Dictionary Attack Against MD5 Hashes

```bash
john --format=md5crypt --wordlist=$_PASSWORD_FILE $_HASH_FILE
```

## Expected Output

```
root@hackers:~# john --format=md5crypt --wordlist=/opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt md5.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ [MD5 256/256 AVX2 8x3])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 14 candidates left, minimum 48 needed for performance.
RedStack         (?)
1g 0:00:00:00 DONE (2019-09-16 16:13) 100.0g/s 1400p/s 1400c/s 1400C/s 123456..RedStack
Use the "--show" option to display all of the cracked passwords reliably
Session completed

```


