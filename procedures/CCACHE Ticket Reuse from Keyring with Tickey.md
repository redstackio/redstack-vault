---
id: 6ddb46bd-ec8a-4688-bea0-0b846cf7c985
name: CCACHE Ticket Reuse from Keyring with Tickey
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.573574+00:00'
updated_at: '2023-04-10T20:26:02.870042+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[Golden Ticket|T1558.001 - Golden Ticket]]'
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[CCACHE ticket reuse from keyring]]'
commands:
- '[[Change directory to tickey]]'
- '[[Clone tickey repository]]'
- '[[Inject tickets]]'
- '[[Make release build]]'
---

# CCACHE Ticket Reuse from Keyring with Tickey

## Summary

CCACHE ticket reuse from keyring is a technique used by attackers to steal Kerberos tickets from memory. This technique can be used to gain access to systems, services, and sensitive data within the target network. Tickey is a tool that can be used to extract Kerberos tickets from the keyring and r

## Description

# Description

CCACHE ticket reuse from keyring is a technique used by attackers to steal Kerberos tickets from memory. This technique can be used to gain access to systems, services, and sensitive data within the target network. Tickey is a tool that can be used to extract Kerberos tickets from the keyring and reuse them for privilege escalation or lateral movement.

Tickey works by extracting CCACHE tickets from the keyring and saving them to a file. These tickets can then be reused with other tools to gain access to systems or services. This technique is particularly effective against older systems that do not have the latest security updates or have weak passwords.

## Requirements

1. Access to a target system

1. Administrator or system-level privileges

1. Tickey tool

## Defense

1. Use strong passwords and enforce password policies

1. Implement the latest security updates and patches

1. Monitor for suspicious activity such as ticket reuse

## Objectives

1. Extract Kerberos tickets from memory

1. Reuse Kerberos tickets for privilege escalation or lateral movement

# Instructions

1. To extract Kerberos tickets from Linux kernel keys, follow these steps:
1. Clone the Tickey repository using 'git clone https://github.com/TarlogicSecurity/tickey'
2. Navigate to the tickey/tickey directory using 'cd tickey/tickey'
3. Build the tool using 'make CONF=Release'
4. Run the tool using '/tmp/tickey -i'

**Code**: [[# Configuration and build
git clone https://github]]

> The tool will try to extract the Kerberos tickets from the Linux kernel keys. If root privileges are detected, all the tickets will be dumped. The tool will then try to inject into the specified user sessions, and the extracted tickets can be found in the respective /tmp/__krb_<uid>.ccache files.

**Command** ([[Clone tickey repository]]):

```bash
git clone https://github.com/TarlogicSecurity/tickey
```

**Command** ([[Change directory to tickey]]):

```bash
cd tickey/tickey
```

**Command** ([[Make release build]]):

```bash
make CONF=Release
```

**Command** ([[Inject tickets]]):

```bash
/tmp/tickey -i
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[Golden Ticket|T1558.001 - Golden Ticket]]
- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[Change directory to tickey]]
- [[Clone tickey repository]]
- [[Inject tickets]]
- [[Make release build]]

## Tags

- [[Active Directory Attacks]]
- [[CCACHE ticket reuse from keyring]]
