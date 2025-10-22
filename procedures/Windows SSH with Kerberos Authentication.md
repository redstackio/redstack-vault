---
id: f5449dc2-326f-43b3-a148-dfee7d589c49
name: Windows SSH with Kerberos Authentication
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.284783+00:00'
updated_at: '2023-04-10T20:38:00.016017+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[SSH Hijacking|T1184 - SSH Hijacking]]'
tags:
- '[[SSH Protocol]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Copy user.ccache to /tmp/krb5cc_1045]]'
- '[[SSH into domain.local with GSSAPI Authentication]]'
---

# Windows SSH with Kerberos Authentication

## Summary

This procedure allows an attacker to copy the Kerberos ticket cache from a compromised Windows machine and use it to authenticate to an SSH server using GSSAPI authentication. This allows the attacker to bypass any SSH authentication mechanisms and gain access to the SSH server. The attacker can th

## Description

# Description

This procedure allows an attacker to copy the Kerberos ticket cache from a compromised Windows machine and use it to authenticate to an SSH server using GSSAPI authentication. This allows the attacker to bypass any SSH authentication mechanisms and gain access to the SSH server. The attacker can then use this access to further their objectives, such as exfiltrating data or pivoting to other systems. From a technical perspective, this attack relies on the attacker having access to the Kerberos ticket cache on the compromised Windows machine and being able to use it to authenticate to the SSH server. From a business value perspective, this attack can result in the compromise of sensitive data and potentially lead to significant financial and reputational damage for the organization.

## Requirements

1. Access to a compromised Windows machine with a valid Kerberos ticket cache

1. Access to an SSH server that supports GSSAPI authentication

## Defense

1. Monitor and restrict access to the Kerberos ticket cache on Windows machines

1. Implement two-factor authentication for SSH servers

1. Monitor SSH logs for unusual authentication activity

## Objectives

1. Gain access to an SSH server using Kerberos authentication

1. Bypass SSH authentication mechanisms

1. Exfiltrate data from the SSH server

1. Pivot to other systems

# Instructions

1. To use this command, first copy the user.ccache file to /tmp/krb5cc_1045 using the 'cp' command. Then, SSH into the domain.local server using the 'ssh' command with the '-o GSSAPIAuthentication=yes' flag to enable GSSAPI authentication. Make sure to replace 'user' with the actual username and 'domain.local' with the actual domain name.

**Code**: [[cp user.ccache /tmp/krb5cc_1045
ssh -o GSSAPIAuthe]]

> This command allows you to connect to a remote server using SSH with GSSAPI authentication, which uses a Kerberos ticket to authenticate the user. The 'cp' command is used to copy the Kerberos ticket cache file (user.ccache) to a location where the SSH client can access it (/tmp/krb5cc_1045). The 'ssh' command is then used to connect to the remote server with the '-o GSSAPIAuthentication=yes' flag, which enables GSSAPI authentication. This command is useful when you have obtained a Kerberos ticket by passing the hash and want to use it to authenticate to a remote server.

**Command** ([[Copy user.ccache to /tmp/krb5cc_1045]]):

```bash
cp user.ccache /tmp/krb5cc_1045
```

**Command** ([[SSH into domain.local with GSSAPI Authentication]]):

```bash
ssh -o GSSAPIAuthentication=yes user@domain.local -vv
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Pass the Hash|T1075 - Pass the Hash]]
- [[SSH Hijacking|T1184 - SSH Hijacking]]

## Commands Used

- [[Copy user.ccache to /tmp/krb5cc_1045]]
- [[SSH into domain.local with GSSAPI Authentication]]

## Tags

- [[SSH Protocol]]
- [[Windows - Using credentials]]
