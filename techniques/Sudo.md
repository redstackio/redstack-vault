---
id: 32f890cb-8852-4abe-816b-8a0c735c2aeb
name: Sudo
type: technique
mitre_id: T1169
mitre_url: null
created_at: '2019-08-28T21:17:48.005946+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Linux Privilege Escalation Enumeration]]'
- '[[Spawn a Root Shell using Sudo and Perl]]'
---

# Sudo

**MITRE ID**: T1169

## Description

The sudoers file, /etc/sudoers, describes which users can run which commands and from which terminals. This also describes which commands users can run as other users or groups. This provides the idea of least privilege such that users are running in their lowest possible permissions for most of the time and only elevate to other users or permissions as needed, typically by prompting for a password. However, the sudoers file can also specify when to not prompt users for passwords with a line like user1 ALL=(ALL) NOPASSWD: ALL [1]. Adversaries can take advantage of these configurations to execute commands as other users or spawn processes with higher privileges. You must have elevated privileges to edit this file though.

# Detection

On Linux, auditd can alert every time a user's actual ID and effective ID are different (this is what happens when you sudo).

# Mitigation

The sudoers file should be strictly edited such that passwords are always required and that users can’t spawn risky processes as users with higher privilege. By requiring a password, even if an adversary can get terminal access, they must know the password to run anything in the sudoers file.

# Footnotes

[1] Thomas Reed. (2017, July 7). New OSX.Dok malware intercepts web traffic. Retrieved July 10, 2017.

## Defense

The sudoers file should be strictly edited such that passwords are always required and that users can’t spawn risky processes as users with higher privilege. By requiring a password, even if an adversary can get terminal access, they must know the passwor

## Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (2)

- [[Linux Privilege Escalation Enumeration]]
- [[Spawn a Root Shell using Sudo and Perl]]
