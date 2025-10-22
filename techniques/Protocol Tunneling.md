---
id: d0cd3067-08a1-4b6a-9712-2abbdc1e06b0
name: Protocol Tunneling
type: technique
mitre_id: T1572
mitre_url: null
created_at: '2023-04-06T00:31:26.085656+00:00'
updated_at: '2023-04-06T03:56:44.597668+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
procedures:
- '[[Azure AD Administrative Unit Management]]'
- '[[Octal IP Format Server-Side Request Forgery]]'
- '[[SSRF via URL Scheme File Retrieval]]'
- '[[uWSGI Configuration Magic Variables Procedure]]'
- '[[XXE Injection in SOAP Messages]]'
---

# Protocol Tunneling

**MITRE ID**: T1572

## Description

Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid detection/network filtering and/or enable access to otherwise unreachable systems. Tunneling involves explicitly encapsulating a protocol within another. This behavior may conceal malicious traffic by blending in with existing traffic and/or provide an outer layer of encryption (similar to a VPN). Tunneling could also enable routing of network packets that would otherwise not reach their intended destination, such as SMB, RDP, or other traffic that would be filtered by network appliances or not routed over the Internet. 

There are various means to encapsulate a protocol within another protocol. For example, adversaries may perform SSH tunneling (also known as SSH port forwarding), which involves forwarding arbitrary data over an encrypted SSH tunnel.(Citation: SSH Tunneling) 

[Protocol Tunneling](https://attack.mitre.org/techniques/T1572) may also be abused by adversaries during [Dynamic Resolution](https://attack.mitre.org/techniques/T1568). Known as DNS over HTTPS (DoH), queries to resolve C2 infrastructure may be encapsulated within encrypted HTTPS packets.(Citation: BleepingComp Godlua JUL19) 

Adversaries may also leverage [Protocol Tunneling](https://attack.mitre.org/techniques/T1572) in conjunction with [Proxy](https://attack.mitre.org/techniques/T1090) and/or [Protocol Impersonation](https://attack.mitre.org/techniques/T1001/003) to further conceal C2 communications and infrastructure. 

## Tactics

- [[Command and Control|TA0011 - Command and Control]]

## Related Procedures (5)

- [[Azure AD Administrative Unit Management]]
- [[Octal IP Format Server-Side Request Forgery]]
- [[SSRF via URL Scheme File Retrieval]]
- [[uWSGI Configuration Magic Variables Procedure]]
- [[XXE Injection in SOAP Messages]]
