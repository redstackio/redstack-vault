---
id: 43d1829d-e23f-4440-ace7-f1fde2765b57
name: Compromise Client Software Binary
type: technique
mitre_id: T1554
mitre_url: null
created_at: '2023-04-06T00:31:26.597021+00:00'
updated_at: '2023-04-06T03:56:32.199971+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[SAML Injection Authentication Bypass]]'
- '[[SAML Injection for Authentication Bypass and User Enumeration]]'
---

# Compromise Client Software Binary

**MITRE ID**: T1554

## Description

Adversaries may modify client software binaries to establish persistent access to systems. Client software enables users to access services provided by a server. Common client software types are SSH clients, FTP clients, email clients, and web browsers.

Adversaries may make modifications to client software binaries to carry out malicious tasks when those applications are in use. For example, an adversary may copy source code for the client software, add a backdoor, compile for the target, and replace the legitimate application binary (or support files) with the backdoored one. Since these applications may be routinely executed by the user, the adversary can leverage this for persistent access to the host.

## Tactics

- [[Persistence|TA0003 - Persistence]]

## Related Procedures (2)

- [[SAML Injection Authentication Bypass]]
- [[SAML Injection for Authentication Bypass and User Enumeration]]
