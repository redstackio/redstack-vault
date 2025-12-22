---
id: d28cacec-c73a-4e34-a835-a8e0a5c98715
name: john-dictionary-attack-on-hash-file
type: command
executor: bash
data: john --wordlist=$_WORDLIST $_HASH_FILE
output: >-
  root@kali:~# john --wordlist=wordlist.txt hash.txt

  Using default input encoding: UTF-8

  Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])

  Cost 1 (iteration count) is 5000 for all loaded hashes

  Will run 4 OpenMP threads

  Press 'q' or Ctrl-C to abort, almost any other key for status

  toor             (?)

  1g 0:00:00:00 DONE (2019-09-24 18:10) 25.00g/s 3950p/s 3950c/s 3950C/s
  configuration..packages

  Use the "--show" option to display all of the cracked passwords reliably

  Session completed


  root@kali:~# john hash.txt --show

  ?:toor


  1 password hash cracked, 0 left
created_at: '2019-09-24T22:44:39.860867+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - cracking
verified: true
validated: true
---

# john-dictionary-attack-on-hash-file

## Command

```bash
john --wordlist=$_WORDLIST $_HASH_FILE
```

## Description

This command uses John the Ripper to perform a dictionary-based attack on a password hash file, testing words from a specified wordlist against the hashes to identify potential matches. It is typically used after extracting password hashes from captured data, such as files or network traffic, to recover plaintext credentials offline.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --wordlist=$_WORDLIST | Path to the wordlist file containing potential passwords for the dictionary attack | Yes |
| $_HASH_FILE | Path to the file containing one or more password hashes to crack | Yes |

## Examples

### Basic Usage

```bash
john --wordlist=rockyou.txt hash.txt
```

### Advanced Usage

```bash
john --wordlist=rockyou.txt --format=sha512crypt hash.txt
```

## Expected Output

When the command runs successfully, John loads the hashes, performs the attack, and reports any cracked passwords. If a match is found, it displays the password; otherwise, it shows progress and completion status. Use `john --show $_HASH_FILE` afterward to view all cracked passwords.

```
root@kali:~# john --wordlist=wordlist.txt hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
toor             (?)
1g 0:00:00:00 DONE (2019-09-24 18:10) 25.00g/s 3950p/s 3950c/s 3950C/S configuration..packages
Use the "--show" option to display all of the cracked passwords reliably
Session completed

root@kali:~# john hash.txt --show
?:toor

1 password hash cracked, 0 left
```

## Related

- [[procedures/Brute-Force-Password-Protected-XLSX-File]]
- [[tools/John-the-Ripper]]
