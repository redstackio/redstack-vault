---
id: 1dc13f79-b22c-4402-baff-4fedd94b1d44
name: Hashcat Dictionary Attack a SHA-512 Hash
type: command
executor: bash
data: ' hashcat -m 1800 -a0 -o $_OUTPUT.txt --remove $_HASH_FILE $_PASSWORD_LIST'
output: 'root@hackers:~/Content/crypto# hashcat -m 1800 -a 0 -o output.txt --remove
  sha512.hash /opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt --force

  hashcat (v5.1.0) starting...


  OpenCL Platform #1: The pocl project

  ====================================

  * Device #1: pthread-Intel(R) Core(TM) i9-8950HK CPU @ 2.90GHz, 1024/2942 MB allocatable,
  2MCU


  Hashes: 1 digests; 1 unique digests, 1 unique salts

  Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

  Rules: 1


  Applicable optimizers:

  * Zero-Byte

  * Single-Hash

  * Single-Salt

  * Uses-64-Bit


  Minimum password length supported by kernel: 0

  Maximum password length supported by kernel: 256Dictionary cache built:

  * Filename..: /opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt

  * Passwords.: 14

  * Bytes.....: 113

  * Keyspace..: 14

  * Runtime...: 0 secs


  Session..........: hashcat

  Status...........: Cracked

  Hash.Type........: sha512crypt $6$, SHA512 (Unix)

  Hash.Target......: $6$16BytesXX16Bytes$C.8MWwRdswldKtrUY3bgGaPlMvJYAFh...YG.x9.

  Time.Started.....: Mon Sep 16 15:03:04 2019 (1 sec)

  Time.Estimated...: Mon Sep 16 15:03:05 2019 (0 secs)

  Guess.Base.......: File (/opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt)

  Guess.Queue......: 1/1 (100.00%)

  Speed.#1.........:       23 H/s (0.66ms) @ Accel:128 Loops:64 Thr:1 Vec:4

  Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts

  Progress.........: 14/14 (100.00%)

  Rejected.........: 0/14 (0.00%)

  Restore.Point....: 0/14 (0.00%)

  Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4992-5000

  Candidates.#1....: 123456 -> RedStack


  Started: Mon Sep 16 15:02:54 2019

  Stopped: Mon Sep 16 15:03:06 2019'
created_at: '2019-09-16T22:24:57.351529+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Hashcat Dictionary Attack a SHA-512 Hash

```bash
 hashcat -m 1800 -a0 -o $_OUTPUT.txt --remove $_HASH_FILE $_PASSWORD_LIST
```

## Expected Output

```
root@hackers:~/Content/crypto# hashcat -m 1800 -a 0 -o output.txt --remove sha512.hash /opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt --force
hashcat (v5.1.0) starting...

OpenCL Platform #1: The pocl project
====================================
* Device #1: pthread-Intel(R) Core(TM) i9-8950HK CPU @ 2.90GHz, 1024/2942 MB allocatable, 2MCU

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Single-Hash
* Single-Salt
* Uses-64-Bit

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256Dictionary cache built:
* Filename..: /opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt
* Passwords.: 14
* Bytes.....: 113
* Keyspace..: 14
* Runtime...: 0 secs

Session..........: hashcat
Status...........: Cracked
Hash.Type........: sha512crypt $6$, SHA512 (Unix)
Hash.Target......: $6$16BytesXX16Bytes$C.8MWwRdswldKtrUY3bgGaPlMvJYAFh...YG.x9.
Time.Started.....: Mon Sep 16 15:03:04 2019 (1 sec)
Time.Estimated...: Mon Sep 16 15:03:05 2019 (0 secs)
Guess.Base.......: File (/opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:       23 H/s (0.66ms) @ Accel:128 Loops:64 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 14/14 (100.00%)
Rejected.........: 0/14 (0.00%)
Restore.Point....: 0/14 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4992-5000
Candidates.#1....: 123456 -> RedStack

Started: Mon Sep 16 15:02:54 2019
Stopped: Mon Sep 16 15:03:06 2019
```


