---
id: 06be9137-5ef0-44ad-b4b5-66ba5916452b
name: Mimikatz LSA Protection Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.155959+00:00'
updated_at: '2023-04-10T20:37:14.396997+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[LSA Protection Workaround]]'
- '[[Windows - Mimikatz]]'
---

# Mimikatz LSA Protection Bypass

## Summary

The Mimikatz LSA Protection Bypass procedure is designed to circumvent the LSA Protection feature in Windows and extract sensitive credential information from the Local Security Authority (LSA) process. This procedure involves injecting Mimikatz into a protected process, which allows it to access t

## Description

# Description

The Mimikatz LSA Protection Bypass procedure is designed to circumvent the LSA Protection feature in Windows and extract sensitive credential information from the Local Security Authority (LSA) process. This procedure involves injecting Mimikatz into a protected process, which allows it to access the LSA secrets. This technique is commonly used by attackers to obtain domain credentials and escalate privileges. From a technical perspective, this procedure involves injecting Mimikatz into a protected process using the 'Process Check and Mimikatz Injection' command and then using the 'Dump LSA Passwords as a Protected Process' command to extract the credential information. The business value of this procedure lies in the ability to obtain sensitive information that can be used to further compromise the target network.

## Requirements

1. Local administrator or SYSTEM-level access

1. Access to the target system

## Defense

1. Implement strong password policies and multi-factor authentication to make credential theft more difficult

1. Monitor for suspicious process injection techniques and detect the presence of Mimikatz on systems

1. Restrict administrative access to critical systems

## Objectives

1. Extract sensitive credential information from the LSA process

1. Obtain domain credentials

1. Escalate privileges

# Instructions

1. To dump LSA passwords as a protected process, follow these steps:

1. Check if LSA runs as a protected process by looking if the variable "RunAsPPL" is set to 0x1.
2. Upload the mimidriver.sys from the official mimikatz repository to the same folder as your mimikatz.exe.
3. Import the mimidriver.sys to the system.
4. Remove the protection flags from lsass.exe process.
5. Run the logonpasswords function to dump lsass.
6. Re-add the protection flags to the lsass.exe process.
7. Unload the service created.
8. Use PPLdump.exe to dump the LSA process.

Note: PPLdump.exe is available at https://github.com/itm4n/PPLdump.

**Code**: [[# Check if LSA runs as a protected process by look]]

> This command is used to dump the passwords stored in the LSA process as a protected process. The command first checks if LSA is running as a protected process. If not, it imports the mimidriver.sys to the system and sets the protection flags for lsass.exe. After dumping the LSA passwords, the protection flags are re-added to the lsass.exe process. Finally, PPLdump.exe is used to dump the LSA process.

2. To check if a process called lsaiso.exe exists on the running processes, run the command 'tasklist | findstr lsaiso'. To inject a malicious Security Support Provider into memory, run the command 'mimikatz # misc::memssp' (requires mimilib.dll in the same folder). This will log every user session and authentication into the machine and capture plaintext credentials, which will be dumped into c:\windows\system32\mimilsa.log.

**Code**: [[# Check if a process called lsaiso.exe exists on t]]

> The first command checks if a process called lsaiso.exe exists on the running processes. The second command injects a malicious Security Support Provider into memory, which will log every user session and authentication into the machine and capture plaintext credentials. This is done by using mimikatz with the misc::memssp command, which requires mimilib.dll in the same folder. The captured plaintext credentials will be dumped into c:\windows\system32\mimilsa.log.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Tags

- [[LSA Protection Workaround]]
- [[Windows - Mimikatz]]
