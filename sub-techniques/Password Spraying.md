---
id: ceefbcf8-9119-407a-9c33-2763f26d2618
name: Password Spraying
type: sub-technique
mitre_id: T1110.003
mitre_url: null
created_at: '2023-04-06T00:31:26.289391+00:00'
updated_at: '2023-04-06T00:31:26.289391+00:00'
parent_technique: '[[Brute Force|T1110 - Brute Force]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Kerberos Pre-Auth Bruteforcing]]'
---

# Password Spraying

**MITRE ID**: T1110.003

**Parent Technique**: [[Brute Force|T1110 - Brute Force]]

This is a sub-technique of T1110 - Brute Force.

## Summary

Adversaries may use a single or small list of commonly used passwords against many different accounts to attempt to acquire valid account credentials. Password spraying uses one password (e.g. 'Password01'), or a small list of commonly used passwords, that may match the complexity policy of the doma

## Description

Adversaries may use a single or small list of commonly used passwords against many different accounts to attempt to acquire valid account credentials. Password spraying uses one password (e.g. 'Password01'), or a small list of commonly used passwords, that may match the complexity policy of the domain. Logins are attempted with that password against many different accounts on a network to avoid account lockouts that would normally occur when brute forcing a single account with many passwords. (Citation: BlackHillsInfosec Password Spraying)

Typically, management services over commonly used ports are used when password spraying. Commonly targeted services include the following:

* SSH (22/TCP)
* Telnet (23/TCP)
* FTP (21/TCP)
* NetBIOS / SMB / Samba (139/TCP & 445/TCP)
* LDAP (389/TCP)
* Kerberos (88/TCP)
* RDP / Terminal Services (3389/TCP)
* HTTP/HTTP Management Services (80/TCP & 443/TCP)
* MSSQL (1433/TCP)
* Oracle (1521/TCP)
* MySQL (3306/TCP)
* VNC (5900/TCP)

In addition to management services, adversaries may "target single sign-on (SSO) and cloud-based applications utilizing federated authentication protocols," as well as externally facing email applications, such as Office 365.(Citation: US-CERT TA18-068A 2018)

In default environments, LDAP and Kerberos connection attempts are less likely to trigger events over SMB, which creates Windows "logon failure" event ID 4625.

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Kerberos Pre-Auth Bruteforcing]]
