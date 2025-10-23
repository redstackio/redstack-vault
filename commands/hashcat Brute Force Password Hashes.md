---
id: d0a77568-8751-435e-a7e7-102256247007
name: hashcat Brute Force Password Hashes
type: command
executor: bash
data: hashcat -m $_VALUE $_HASHES $_WORDLIST
output: 'root@kali:~# hashcat -m 1800 test /usr/share/wordlists/rockyou.txt

  hashcat (v5.1.0) starting...


  Hashes: 2 digests; 2 unique digests, 2 unique salts

  Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

  Rules: 1


  Applicable optimizers:

  * Zero-Byte

  * Uses-64-Bit


  Minimum password length supported by kernel: 0

  Maximum password length supported by kernel: 256


  Watchdog: Hardware monitoring interface not found on your system.

  Watchdog: Temperature abort trigger disabled.


  * Device #1: build_opts ''-cl-std=CL1.2 -I OpenCL -I /usr/share/hashcat/OpenCL -D
  LOCAL_MEM_TYPE=2 -D VENDOR_ID=64 -D CUDA_ARCH=0 -D AMD_ROCM=0 -D VECT_SIZE=4 -D
  DEVICE_TYPE=2 -D DGST_R0=0 -D DGST_R1=1 -D DGST_R2=2 -D DGST_R3=3 -D DGST_ELEM=16
  -D KERN_TYPE=1800 -D _unroll''

  * Device #1: Kernel m01800-pure.cc32913d.kernel not found in cache! Building may
  take a while...

  * Device #1: Kernel amp_a0.5086224f.kernel not found in cache! Building may take
  a while...

  Dictionary cache built:

  * Filename..: /usr/share/wordlists/rockyou.txt

  * Passwords.: 14344392

  * Bytes.....: 139921507

  * Keyspace..: 14344385

  * Runtime...: 1 sec


  [s]tatus [p]ause [b]ypass [c]heckpoint [q]uit =>

  $6$GTaHocc2uYy11co$IiOFf4PryLxrWbPE2qmE0sEVUaBFkzTc5qtrDLoHAcyBfBDtWKjQz4AiTGZvSdKKNqYLAsrFwS87QKfJprBPJ0:sunnydays

  [s]tatus [p]ause [b]ypass [c]heckpoint [q]uit => s

  $6$ngUYdXkcMLK$AI23a7brd9zZOgf336W.9a7/M2QstTHC/9Es0t17P/sAkBgxxrPituenv35hG.z/J28T1vfEx2I8nR6ac44AX0:secretpass


  Session..........: hashcat

  Status...........: Cracked

  Hash.Type........: sha512crypt $6$, SHA512 (Unix)

  Hash.Target......: test

  Time.Started.....: Mon Jan 20 15:26:43 2020 (5 mins, 26 secs)

  Time.Estimated...: Mon Jan 20 15:32:09 2020 (0 secs)

  Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)

  Guess.Queue......: 1/1 (100.00%)

  Speed.#1.........:      523 H/s (8.97ms) @ Accel:128 Loops:64 Thr:1 Vec:4

  Recovered........: 2/2 (100.00%) Digests, 2/2 (100.00%) Salts

  Progress.........: 258432/28688770 (0.90%)

  Rejected.........: 0/258432 (0.00%)

  Restore.Point....: 129024/14344385 (0.90%)

  Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4992-5000

  Candidates.#1....: smithfield -> rolltide2


  Started: Mon Jan 20 15:26:33 2020

  Stopped: Mon Jan 20 15:32:09 2020'
created_at: '2020-01-20T20:42:02.727182+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# hashcat Brute Force Password Hashes

```bash
hashcat -m $_VALUE $_HASHES $_WORDLIST
```

## Expected Output

```
root@kali:~# hashcat -m 1800 test /usr/share/wordlists/rockyou.txt
hashcat (v5.1.0) starting...

Hashes: 2 digests; 2 unique digests, 2 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Uses-64-Bit

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

* Device #1: build_opts '-cl-std=CL1.2 -I OpenCL -I /usr/share/hashcat/OpenCL -D LOCAL_MEM_TYPE=2 -D VENDOR_ID=64 -D CUDA_ARCH=0 -D AMD_ROCM=0 -D VECT_SIZE=4 -D DEVICE_TYPE=2 -D DGST_R0=0 -D DGST_R1=1 -D DGST_R2=2 -D DGST_R3=3 -D DGST_ELEM=16 -D KERN_TYPE=1800 -D _unroll'
* Device #1: Kernel m01800-pure.cc32913d.kernel not found in cache! Building may take a while...
* Device #1: Kernel amp_a0.5086224f.kernel not found in cache! Building may take a while...
Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

[s]tatus [p]ause [b]ypass [c]heckpoint [q]uit =>
$6$GTaHocc2uYy11co$IiOFf4PryLxrWbPE2qmE0sEVUaBFkzTc5qtrDLoHAcyBfBDtWKjQz4AiTGZvSdKKNqYLAsrFwS87QKfJprBPJ0:sunnydays
[s]tatus [p]ause [b]ypass [c]heckpoint [q]uit => s
$6$ngUYdXkcMLK$AI23a7brd9zZOgf336W.9a7/M2QstTHC/9Es0t17P/sAkBgxxrPituenv35hG.z/J28T1vfEx2I8nR6ac44AX0:secretpass

Session..........: hashcat
Status...........: Cracked
Hash.Type........: sha512crypt $6$, SHA512 (Unix)
Hash.Target......: test
Time.Started.....: Mon Jan 20 15:26:43 2020 (5 mins, 26 secs)
Time.Estimated...: Mon Jan 20 15:32:09 2020 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:      523 H/s (8.97ms) @ Accel:128 Loops:64 Thr:1 Vec:4
Recovered........: 2/2 (100.00%) Digests, 2/2 (100.00%) Salts
Progress.........: 258432/28688770 (0.90%)
Rejected.........: 0/258432 (0.00%)
Restore.Point....: 129024/14344385 (0.90%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4992-5000
Candidates.#1....: smithfield -> rolltide2

Started: Mon Jan 20 15:26:33 2020
Stopped: Mon Jan 20 15:32:09 2020
```


