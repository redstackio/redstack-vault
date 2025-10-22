---
id: d28cacec-c73a-4e34-a835-a8e0a5c98715
name: John the Ripper Brute Force a Hash File
type: command
executor: bash
data: john --wordlist=$_WORDLIST $_HASH_FILE
output: 'root@kali:~# john --wordlist=wordlist.txt hash.txt

  Using default input encoding: UTF-8

  Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])

  Cost 1 (iteration count) is 5000 for all loaded hashes

  Will run 4 OpenMP threads

  Press ''q'' or Ctrl-C to abort, almost any other key for status

  toor             (?)

  1g 0:00:00:00 DONE (2019-09-24 18:10) 25.00g/s 3950p/s 3950c/s 3950C/s configuration..packages

  Use the "--show" option to display all of the cracked passwords reliably

  Session completed

  root@kali:~# john hash.txt --show

  ?:toor

  1 password hash cracked, 0 left'
created_at: '2019-09-24T22:44:39.860867+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# John the Ripper Brute Force a Hash File

```bash
john --wordlist=$_WORDLIST $_HASH_FILE
```

## Expected Output

```
root@kali:~# john --wordlist=wordlist.txt hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
toor             (?)
1g 0:00:00:00 DONE (2019-09-24 18:10) 25.00g/s 3950p/s 3950c/s 3950C/s configuration..packages
Use the "--show" option to display all of the cracked passwords reliably
Session completed

root@kali:~# john hash.txt --show
?:toor

1 password hash cracked, 0 left
```
