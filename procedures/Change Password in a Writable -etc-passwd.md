---
id: cda165a9-28fc-47a0-9d32-eec598181075
name: Change Password in a Writable /etc/passwd
type: procedure
verified: false
submitted: false
created_at: '2019-10-10T00:49:03.893825+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[File System Permissions Weakness|T1044 - File System Permissions Weakness]]'
platforms:
- Linux
tags:
- '[[misconfiguration]]'
- '[[Setup]]'
commands:
- '[[OpenSSL Generate a SHA512-crypt hash]]'
---

# Change Password in a Writable /etc/passwd

## Summary

When /etc/passwd is writable, it is possible to change a user's password by entering the password hash. Passwords in /etc/passwd take priority over those found in /etc/shadow  for legacy reasons, though the same technique can be applied when /etc/shadow is writable. 

## Description

# Description

When `/etc/passwd` is writable, it is possible to change a user's password by entering the password hash. Passwords in `/etc/passwd` take priority over those found in `/etc/shadow`  for legacy reasons, though the same technique can be applied when `/etc/shadow` is writable.

# `Instructions`

1. Identify a user whose password will be changed. In this example, root will be targeted.

2. Generate a sha512-crypt password

**Command** ([[OpenSSL Generate a SHA512-crypt hash]]):

```bash
openssl passwd -6 -salt $_SALT $_PASSWORD
```

3. Update `/etc/passwd` or `/etc/shadow`, adding the password hash to the desired user after the first colon, replacing the placeholder `x`.

For example:

Original entry:

**Code**: [[root:x:0:0:root:/root:/bin/bash]]

Modified entry:

**Code**: [[root:$6$12345678$DgaVYkZjVTY58m0juyhsvwGEjwMI9RB5U]]

## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[File System Permissions Weakness|T1044 - File System Permissions Weakness]]

## Commands Used

- [[OpenSSL Generate a SHA512-crypt hash]]

## Tags

- [[misconfiguration]]
- [[Setup]]
