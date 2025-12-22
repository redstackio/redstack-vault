---
type: procedure
verified: true
submitted: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - '[[tags/Cryptography]]'
  - '[[tags/data encryption]]'
commands:
  - '[[commands/cryptsetup-luksDump-to-get-payload-offset]]'
  - '[[commands/dd-extract-luks-v1-hash]]'
  - '[[commands/hashcat-brute-force-luks-v1-hash]]'
  - '[[commands/cryptsetup-luksOpen-encrypted-volume]]'
  - '[[commands/mount-filesystem-to-mount-point]]'
platforms:
  - Linux
tools: []
validated: true
---

# Brute-Force-and-Mount-LUKS1-Encrypted-Filesystem

## Summary

This procedure extracts the cryptographic hash from a LUKS version 1 encrypted filesystem image, performs a dictionary-based brute force attack to recover the passphrase using Hashcat, unlocks the volume with the cracked passphrase, and mounts the decrypted filesystem for access to the underlying data. It is useful in forensic analysis, penetration testing, or recovery scenarios where an attacker has obtained a LUKS-encrypted disk image and needs to access its contents.

## Description

LUKS (Linux Unified Key Setup) version 1 is a standard for disk encryption on Linux systems, using a header that stores the master key and key slots encrypted with user passphrases. This procedure targets the header to extract the relevant hash material (key slots), which can be brute-forced offline using tools like Hashcat. Once the passphrase is recovered, the volume is opened as a device mapper entry and mounted to a directory. This approach assumes the attacker has physical or forensic access to the encrypted image file and a wordlist for brute-forcing. It works on raw disk images or files containing LUKS partitions and requires computational resources for cracking, especially for strong passphrases.

## Requirements

1. Access to the LUKS-encrypted filesystem image file (e.g., a raw disk dump or .img file).
2. A wordlist or dictionary file for brute-forcing (e.g., rockyou.txt).
3. Sufficient computational power (GPU recommended for Hashcat) to perform the brute-force attack.
4. Root or sudo privileges on a Linux system with cryptsetup, dd, mount, and Hashcat installed.
5. A target mount point directory with write permissions.

## Defense

Defensive measures and detection strategies:

- Use LUKS2 instead of LUKS1, as it supports stronger PBKDF iterations and anti-forensic features.
- Enforce strong passphrase policies (length >12 characters, no dictionary words) to resist brute-force attacks.
- Monitor for unauthorized access to disk images or forensic tools like cryptsetup and Hashcat on endpoints.
- Enable full disk encryption auditing and alert on attempts to dump or manipulate LUKS headers.
- Use hardware security modules (HSMs) or TPM for key protection to prevent offline attacks.

## Objectives

1. Extract and identify the LUKS header offset and hash material from the encrypted image.
2. Recover the passphrase through offline brute-force using a dictionary attack.
3. Unlock the LUKS volume and map it as a decrypted device.
4. Mount the decrypted filesystem to access and exfiltrate data.
5. Verify successful access without corrupting the original image.

## Instructions

### Step 1: Determine LUKS Payload Offset

**Context**: Analyze the LUKS header to find the payload offset, which indicates where the encrypted data begins. This offset is needed to extract the hash slots accurately. Adding 1 to the offset ensures the full header is captured for Hashcat.

**Command** ([[commands/cryptsetup-luksDump-to-get-payload-offset]]):
```bash
cryptsetup luksDump $_FILE.img
```

> Run this command to display the LUKS header details. Note the "Payload offset" value (e.g., 4096). For the next step, use this value plus 1 (e.g., 4097) as the count parameter. This step verifies the image is a valid LUKS1 container and provides the extraction parameters.

### Step 2: Extract the LUKS Hash

**Context**: Use the offset from Step 1 to carve out the LUKS header containing the encrypted key slots. This creates a hash file that can be fed into cracking tools, isolating the cryptographic material without processing the entire image.

**Command** ([[commands/dd-extract-luks-v1-hash]]):
```bash
dd if=$_FILE.img of=$_HASH bs=512 count=$_OFFSET
```

> The dd command reads from the input file (if=), writes to an output hash file (of=), using a block size of 512 bytes (bs=) and the calculated offset count. Success is indicated by the byte count copied; the resulting $_HASH file should be small (e.g., ~2MB) and contain the LUKS header data.

### Step 3: Brute-Force the LUKS Hash

**Context**: Perform an offline dictionary attack on the extracted hash using Hashcat's LUKS mode (14600). This attempts passphrases from the wordlist against the key slots until a match is found, revealing the plaintext passphrase.

**Command** ([[commands/hashcat-brute-force-luks-v1-hash]]):
```bash
hashcat -m 14600 $_HASH $_WORDLIST
```

> Hashcat will load the hash, process the wordlist, and output cracked passphrases to a file (e.g., hashcat.potfile) or stdout if successful. Monitor progress; if no match, try a larger wordlist or rules. Expected output includes session statistics and any recovered passwords.

### Step 4: Unlock the LUKS Encrypted Volume

**Context**: Use the cracked passphrase to open the LUKS container, decrypting it and mapping it to /dev/mapper/$_CRYPT for access. This step transforms the encrypted image into a usable block device.

**Command** ([[commands/cryptsetup-luksOpen-encrypted-volume]]):
```bash
cryptsetup luksOpen $_FILE.img $_CRYPT
```

> Enter the cracked passphrase when prompted. On success, no errors occur, and the device appears in /dev/mapper/ (e.g., /dev/mapper/crypt). Verify with ls /dev/mapper/. If the passphrase is incorrect, it will fail with an authentication error.

### Step 5: Mount the Filesystem

**Context**: Attach the unlocked LUKS device to a mount point to access the decrypted files. This final step exposes the filesystem contents for reading or exfiltration.

**Command** ([[commands/mount-filesystem-to-mount-point]]):
```bash
mount /dev/mapper/$_CRYPT $_MOUNT_POINT
```

> The mount command binds the device to the directory. Success shows no output or errors; verify by ls $_MOUNT_POINT revealing files. Use umount $_MOUNT_POINT and cryptsetup luksClose $_CRYPT to clean up afterward.
