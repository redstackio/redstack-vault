---
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
platforms:
  - Linux
  - Unix
tags:
  - password-cracking
  - brute-force
verified: true
validated: true
---

# john-brute-force-hash-with-wordlist

## Command

```bash
john --wordlist=$_WORDLIST $_HASH_FILE
```

## Description

This command uses John the Ripper to perform a dictionary-based brute force attack on a specified hash file using a wordlist. It automatically detects the hash format and attempts to crack passwords by testing entries from the wordlist. Ideal for offline cracking of common passwords in security assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --wordlist=$_WORDLIST | Path to the wordlist file containing potential passwords (e.g., rockyou.txt) | Yes |
| $_HASH_FILE | Path to the input file containing the password hash(es) | Yes |

## Examples

### Basic Usage

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt myhash.txt
```

### Advanced Usage

```bash
john --wordlist=rockyou.txt --fork=4 hash.txt
```

> The --fork option enables multi-threading for faster cracking on multi-core systems.

## Expected Output

Description of what output to expect when the command runs successfully.

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
```

If no password is found, it will show progress until the wordlist is exhausted without a match.

## Related

- [[commands/john-show-cracked-passwords]]
- [[procedures/Brute-Force-Password-Hash-with-John-the-Ripper]]
