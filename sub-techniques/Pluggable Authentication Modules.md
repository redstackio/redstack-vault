---
id: aee4880a-3d7c-43f0-9e44-20749945703a
name: Pluggable Authentication Modules
type: sub-technique
mitre_id: T1556.003
mitre_url: null
created_at: '2023-04-06T00:31:25.458034+00:00'
updated_at: '2023-04-06T00:31:25.458034+00:00'
parent_technique: '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Insecure Docker Registry Pentest]]'
- '[[Web Sockets Authentication Exploitation]]'
---

# Pluggable Authentication Modules

**MITRE ID**: T1556.003

**Parent Technique**: [[Modify Authentication Process|T1556 - Modify Authentication Process]]

This is a sub-technique of T1556 - Modify Authentication Process.

## Summary

Adversaries may modify pluggable authentication modules (PAM) to access user credentials or enable otherwise unwarranted access to accounts. PAM is a modular system of configuration files, libraries, and executable files which guide authentication for many services. The most common authentication mo

## Description

Adversaries may modify pluggable authentication modules (PAM) to access user credentials or enable otherwise unwarranted access to accounts. PAM is a modular system of configuration files, libraries, and executable files which guide authentication for many services. The most common authentication module is <code>pam_unix.so</code>, which retrieves, sets, and verifies account authentication information in <code>/etc/passwd</code> and <code>/etc/shadow</code>.(Citation: Apple PAM)(Citation: Man Pam_Unix)(Citation: Red Hat PAM)

Adversaries may modify components of the PAM system to create backdoors. PAM components, such as <code>pam_unix.so</code>, can be patched to accept arbitrary adversary supplied values as legitimate credentials.(Citation: PAM Backdoor)

Malicious modifications to the PAM system may also be abused to steal credentials. Adversaries may infect PAM resources with code to harvest user credentials, since the values exchanged with PAM components may be plain-text since PAM does not store passwords.(Citation: PAM Creds)(Citation: Apple PAM)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[Insecure Docker Registry Pentest]]
- [[Web Sockets Authentication Exploitation]]
