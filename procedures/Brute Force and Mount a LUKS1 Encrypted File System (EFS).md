---
id: fc0a25f6-0f3b-448c-b657-717c408de95b
name: Brute Force and Mount a LUKS1 Encrypted File System (EFS)
type: procedure
verified: true
submitted: true
created_at: '2019-09-11T22:47:56.062057+00:00'
updated_at: '2023-05-26T00:42:13.946593+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
platforms:
- Linux
tags:
- '[[Cryptography]]'
- '[[data encryption]]'
commands:
- '[[cryptsetup Extract a LUKS v1 Payload Offset]]'
- '[[cryptsetup Open a LUKS Encrypted Volume]]'
- '[[dd Extract a LUKS v1 Hash]]'
- '[[hashcat Brute Force a LUKS v1 Hash]]'
- '[[Mount a Filesystem]]'
---

# Brute Force and Mount a LUKS1 Encrypted File System (EFS)

**Status**: ✓ Verified

## Summary

Extract the cryptographic hash from a LUKS version 1 encrypted file system, and perform a dictionary brute force to crack the password. 

## Description

# Description

Extract the cryptographic hash from a LUKS version 1 encrypted file system, and perform a dictionary brute force to crack the password.



# Instructions



1.  Determine the hash offset from the raw encrypted image.





**Command** ([[cryptsetup Extract a LUKS v1 Payload Offset]]):

```bash
cryptsetup luksDump $_FILE.img
```



Take the Payload offset value, add 1, then use it in the next step. For this example, if the Payload offset is 4096, use 097.



2. Extract the LUKS hash using the offset determined in Step 1.





**Command** ([[dd Extract a LUKS v1 Hash]]):

```bash
dd if=$_FILE.img of=$_HASH bs=512 count=$_OFFSET
```





3. Brute force the LUKS hash





**Command** ([[hashcat Brute Force a LUKS v1 Hash]]):

```bash
hashcat -m 14600 $HASH $WORDLIST
```





4. Unlock the LUKS encrypted volume, specifying the name of the unlocked volume with $_CRYPT





**Command** ([[cryptsetup Open a LUKS Encrypted Volume]]):

```bash
cryptsetup luksOpen $_FILE.img $_CRYPT
```



Note: Unlocked LUKS filesystems are populated in `/dev/mapper`. For example, if the filesystem is unlocked with the name `crypt-home`, it can be found and mounted from `/dev/mapper/crypt-home`



5. Mount the volume.





**Command** ([[Mount a Filesystem]]):

```bash
mount $_FILESYSTEM $_MOUNT_POINT
```





## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[cryptsetup Extract a LUKS v1 Payload Offset]]
- [[cryptsetup Open a LUKS Encrypted Volume]]
- [[dd Extract a LUKS v1 Hash]]
- [[hashcat Brute Force a LUKS v1 Hash]]
- [[Mount a Filesystem]]

## Tags

- [[Cryptography]]
- [[data encryption]]


