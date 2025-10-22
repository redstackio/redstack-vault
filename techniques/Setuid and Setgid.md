---
id: ba8f3d3f-8b4f-4d64-896c-06ede7ee3538
name: Setuid and Setgid
type: technique
mitre_id: T1166
mitre_url: null
created_at: '2019-08-28T21:17:27.594074+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[Find Linux Files with Elevated Privileges]]'
- '[[Linux - Find SUID Binaries Privilege Escalation]]'
- '[[Linux Privilege Escalation Enumeration]]'
- '[[Linux Privilege Escalation via LXC/LXD Alpine Image]]'
- '[[Linux Privilege Escalation via SUID]]'
- '[[Linux - SUID Privilege Escalation via SetUID Binary Creation]]'
- '[[Linux - Writable /etc/sysconfig/network-scripts/ Privilege Escalation]]'
- '[[Nmap Interactive Mode Shell Escape]]'
---

# Setuid and Setgid

**MITRE ID**: T1166

## Description

When the setuid or setgid bits are set on Linux or macOS for an application, this means that the application will run with the privileges of the owning user or group respectively  [1]. Normally an application is run in the current user’s context, regardless of which user or group owns the application. There are instances where programs need to be executed in an elevated context to function properly, but the user running them doesn’t need the elevated privileges. Instead of creating an entry in the sudoers file, which must be done by root, any user can specify the setuid or setgid flag to be set for their own applications. These bits are indicated with an "s" instead of an "x" when viewing a file's attributes via ls -l. The chmod program can set these bits with via bitmasking, chmod 4777 [file] or via shorthand naming, chmod u+s [file].An adversary can take advantage of this to either do a shell escape or exploit a vulnerability in an application with the setsuid or setgid bits to get code running in a different user’s context. Additionally, adversaries can use this mechanism on their own malware to make sure they're able to execute in elevated contexts in the future  [2].

# Detection

Monitor the file system for files that have the setuid or setgid bits set. Monitor for execution of utilities, like chmod, and their command-line arguments to look for setuid or setguid bits being set.

# Mitigation

Applications with known vulnerabilities or known shell escapes should not have the setuid or setgid bits set to reduce potential damage if an application is compromised. Additionally, the number of programs with setuid or setgid bits set should be minimized across a system.

# Footnotes

[1] Michael Kerrisk. (2017, September 15). Linux Programmer's Manual. Retrieved September 21, 2018.

[2] Marc-Etienne M.Leveille. (2016, July 6). New OSX/Keydnap malware is hungry for credentials. Retrieved July 3, 2017.

## Defense

Applications with known vulnerabilities or known shell escapes should not have the setuid or setgid bits set to reduce potential damage if an application is compromised. Additionally, the number of programs with setuid or setgid bits set should be minimiz

## Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (8)

- [[Find Linux Files with Elevated Privileges]]
- [[Linux - Find SUID Binaries Privilege Escalation]]
- [[Linux Privilege Escalation Enumeration]]
- [[Linux Privilege Escalation via LXC/LXD Alpine Image]]
- [[Linux Privilege Escalation via SUID]]
- [[Linux - SUID Privilege Escalation via SetUID Binary Creation]]
- [[Linux - Writable /etc/sysconfig/network-scripts/ Privilege Escalation]]
- [[Nmap Interactive Mode Shell Escape]]
