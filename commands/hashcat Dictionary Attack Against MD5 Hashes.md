---
id: c988ba45-2181-49b4-a20a-c1d9c287d879
name: hashcat Dictionary Attack Against MD5 Hashes
type: command
executor: bash
data: hashcat -m 500 -a 0 -o $_OUTPUT.txt $_HASH_FILE $_PASSWORD_FILE
output: 'root@hackers:~/Content/crypto# hashcat -m 500 -a 0 -o output.txt md5.hash
  /opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt --force

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


  Minimum password length supported by kernel: 0

  Maximum password length supported by kernel: 256

  Dictionary cache hit:

  * Filename..: /opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt

  * Passwords.: 14

  * Bytes.....: 113

  * Keyspace..: 14

  Session..........: hashcat

  Status...........: Cracked

  Hash.Type........: md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)

  Hash.Target......: $1$8Bytesxx$qFcdP9vC4r4EZX.KMjcQQ.

  Time.Started.....: Mon Sep 16 16:22:48 2019 (0 secs)

  Time.Estimated...: Mon Sep 16 16:22:48 2019 (0 secs)

  Guess.Base.......: File (/opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt)

  Guess.Queue......: 1/1 (100.00%)

  Speed.#1.........:       24 H/s (0.22ms) @ Accel:256 Loops:125 Thr:1 Vec:8

  Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts

  Progress.........: 14/14 (100.00%)

  Rejected.........: 0/14 (0.00%)

  Restore.Point....: 0/14 (0.00%)

  Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:875-1000

  Candidates.#1....: 123456 -> RedStack


  Started: Mon Sep 16 16:22:42 2019

  Stopped: Mon Sep 16 16:22:49 2019'
created_at: '2019-09-16T23:24:10.123236+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# hashcat Dictionary Attack Against MD5 Hashes

```bash
hashcat -m 500 -a 0 -o $_OUTPUT.txt $_HASH_FILE $_PASSWORD_FILE
```

## Expected Output

```
root@hackers:~/Content/crypto# hashcat -m 500 -a 0 -o output.txt md5.hash /opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt --force
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

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256
Dictionary cache hit:
* Filename..: /opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt
* Passwords.: 14
* Bytes.....: 113
* Keyspace..: 14
Session..........: hashcat
Status...........: Cracked
Hash.Type........: md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)
Hash.Target......: $1$8Bytesxx$qFcdP9vC4r4EZX.KMjcQQ.
Time.Started.....: Mon Sep 16 16:22:48 2019 (0 secs)
Time.Estimated...: Mon Sep 16 16:22:48 2019 (0 secs)
Guess.Base.......: File (/opt/SecLists/Passwords/Leaked-Databases/rockyou-05.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:       24 H/s (0.22ms) @ Accel:256 Loops:125 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 14/14 (100.00%)
Rejected.........: 0/14 (0.00%)
Restore.Point....: 0/14 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:875-1000
Candidates.#1....: 123456 -> RedStack

Started: Mon Sep 16 16:22:42 2019
Stopped: Mon Sep 16 16:22:49 2019
```


