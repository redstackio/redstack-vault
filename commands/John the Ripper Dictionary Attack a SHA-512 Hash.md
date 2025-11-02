---
id: d746a09b-3b70-4a88-b75f-a7564151003c
name: John the Ripper Dictionary Attack a SHA-512 Hash
type: command
executor: bash
data: john --format=sha512crypt --wordlist=$_WORDLIST $_HASH_FILE
output: 'root@hackers:~# john --format=sha512crypt --wordlist=/opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt
  sha512.hash

  Using default input encoding: UTF-8

  Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])

  Cost 1 (iteration count) is 5000 for all loaded hashes

  Will run 2 OpenMP threads

  Press ''q'' or Ctrl-C to abort, almost any other key for status

  RedStack         (?)

  1g 0:00:00:00 DONE (2019-09-16 15:21) 50.00g/s 700.0p/s 700.0c/s 700.0C/s 123456..RedStack

  Use the "--show" option to display all of the cracked passwords reliably

  Session completed

  root@hackers:~/Content/crypto# john sha512.hash --show

  ?:RedStack


  1 password hash cracked, 0 left'
created_at: '2019-09-16T22:24:57.350683+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[John the Ripper]]'
- '[[SecLists]]'
---

# John the Ripper Dictionary Attack a SHA-512 Hash

```bash
john --format=sha512crypt --wordlist=$_WORDLIST $_HASH_FILE
```

## Expected Output

```
root@hackers:~# john --format=sha512crypt --wordlist=/opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt sha512.hash
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
RedStack         (?)
1g 0:00:00:00 DONE (2019-09-16 15:21) 50.00g/s 700.0p/s 700.0c/s 700.0C/s 123456..RedStack
Use the "--show" option to display all of the cracked passwords reliably
Session completed
root@hackers:~/Content/crypto# john sha512.hash --show
?:RedStack

1 password hash cracked, 0 left
```


