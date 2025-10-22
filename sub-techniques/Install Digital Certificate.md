---
id: 3337d11d-ef90-4aa7-b480-c15469756cd8
name: Install Digital Certificate
type: sub-technique
mitre_id: T1608.003
mitre_url: null
created_at: '2023-04-06T00:31:26.855692+00:00'
updated_at: '2023-04-06T00:31:26.855692+00:00'
parent_technique: '[[Stage Capabilities|T1608 - Stage Capabilities]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Install Digital Certificate

**MITRE ID**: T1608.003

**Parent Technique**: [[Stage Capabilities|T1608 - Stage Capabilities]]

This is a sub-technique of T1608 - Stage Capabilities.

## Summary

Adversaries may install SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are files that can be installed on servers to enable secure communications between systems. Digital certificates include information about the key, information about its owner's identity, and the dig

## Description

Adversaries may install SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are files that can be installed on servers to enable secure communications between systems. Digital certificates include information about the key, information about its owner's identity, and the digital signature of an entity that has verified the certificate's contents are correct. If the signature is valid, and the person examining the certificate trusts the signer, then they know they can use that key to communicate securely with its owner. Certificates can be uploaded to a server, then the server can be configured to use the certificate to enable encrypted communication with it.(Citation: DigiCert Install SSL Cert)

Adversaries may install SSL/TLS certificates that can be used to further their operations, such as encrypting C2 traffic (ex: [Asymmetric Cryptography](https://attack.mitre.org/techniques/T1573/002) with [Web Protocols](https://attack.mitre.org/techniques/T1071/001)) or lending credibility to a credential harvesting site. Installation of digital certificates may take place for a number of server types, including web servers and email servers. 

Adversaries can obtain digital certificates (see [Digital Certificates](https://attack.mitre.org/techniques/T1588/004)) or create self-signed certificates (see [Digital Certificates](https://attack.mitre.org/techniques/T1587/003)). Digital certificates can then be installed on adversary controlled infrastructure that may have been acquired ([Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)) or previously compromised ([Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)).

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]
