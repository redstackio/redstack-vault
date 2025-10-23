---
id: a15a003d-758f-4318-ae1c-2ea4fbc1132b
name: hashcat Brute Force a sha-512 crypt password
type: command
executor: ''
data: hashcat -m 1800 $_HASH_FILE $_WORDLIST
output: "root@kali:~# hashcat -m 1800 hash.txt wordlist.txt\nhashcat (v5.1.0) starting...\n\
  \nOpenCL Platform #1: The pocl project\n====================================\n*\
  \ Device #1: pthread-Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz, 1024/2959 MB allocatable,\
  \ 4MCU\n\nHashes: 1 digests; 1 unique digests, 1 unique salts\nBitmaps: 16 bits,\
  \ 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates\nRules: 1\n\nApplicable\
  \ optimizers:\n* Zero-Byte\n* Single-Hash\n* Single-Salt\n* Uses-64-Bit\n\nMinimum\
  \ password length supported by kernel: 0\nMaximum password length supported by kernel:\
  \ 256\n\nDictionary cache built:\n* Filename..: wordlist.txt\n* Passwords.: 158\n\
  * Bytes.....: 1336\n* Keyspace..: 158\n* Runtime...: 0 secs\n\nApproaching final\
  \ keyspace - workload adjusted.  \n\n$6$fN8i1AxB$0Z9xZy3X/NzJVWjyS1YhPpz7uy5vHsXA1Yxh57dZfYPhac6mPQAFdjow1NMY0OLOYkJFLJC5rIja7FsIneWJz0:toor\n\
  \                                                 \nSession..........: hashcat\n\
  Status...........: Cracked\nHash.Type........: sha512crypt $6$, SHA512 (Unix)\n\
  Hash.Target......: $6$fN8i1AxB$0Z9xZy3X/NzJVWjyS1YhPpz7uy5vHsXA1Yxh57d...neWJz0\n\
  Time.Started.....: Tue Sep 24 18:14:49 2019 (0 secs)\nTime.Estimated...: Tue Sep\
  \ 24 18:15:49 2019 (0 secs)\nGuess.Base.......: File (wordlist.txt)\nGuess.Queue......:\
  \ 1/1 (100.00%)\nSpeed.#1.........:      670 H/s (1.39ms) @ Accel:128 Loops:32 Thr:1\
  \ Vec:4\nRecovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts\nProgress.........:\
  \ 158/158 (100.00%)\nRejected.........: 0/158 (0.00%)\nRestore.Point....: 0/158\
  \ (0.00%)\nRestore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4992-5000\nCandidates.#1....:\
  \ configuration -> packages\n\nStarted: Tue Sep 24 18:14:43 2019\nStopped: Tue Sep\
  \ 24 18:15:51 2019"
created_at: '2019-09-24T22:44:39.861672+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# hashcat Brute Force a sha-512 crypt password

```bash
hashcat -m 1800 $_HASH_FILE $_WORDLIST
```

## Expected Output

```
root@kali:~# hashcat -m 1800 hash.txt wordlist.txt
hashcat (v5.1.0) starting...

OpenCL Platform #1: The pocl project
====================================
* Device #1: pthread-Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz, 1024/2959 MB allocatable, 4MCU

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Single-Hash
* Single-Salt
* Uses-64-Bit

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Dictionary cache built:
* Filename..: wordlist.txt
* Passwords.: 158
* Bytes.....: 1336
* Keyspace..: 158
* Runtime...: 0 secs

Approaching final keyspace - workload adjusted.  

$6$fN8i1AxB$0Z9xZy3X/NzJVWjyS1YhPpz7uy5vHsXA1Yxh57dZfYPhac6mPQAFdjow1NMY0OLOYkJFLJC5rIja7FsIneWJz0:toor
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: sha512crypt $6$, SHA512 (Unix)
Hash.Target......: $6$fN8i1AxB$0Z9xZy3X/NzJVWjyS1YhPpz7uy5vHsXA1Yxh57d...neWJz0
Time.Started.....: Tue Sep 24 18:14:49 2019 (0 secs)
Time.Estimated...: Tue Sep 24 18:15:49 2019 (0 secs)
Guess.Base.......: File (wordlist.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:      670 H/s (1.39ms) @ Accel:128 Loops:32 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 158/158 (100.00%)
Rejected.........: 0/158 (0.00%)
Restore.Point....: 0/158 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4992-5000
Candidates.#1....: configuration -> packages

Started: Tue Sep 24 18:14:43 2019
Stopped: Tue Sep 24 18:15:51 2019
```


