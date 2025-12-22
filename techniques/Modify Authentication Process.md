---
id: b01feee9-87d9-439d-9e8d-fdcbf547a351
name: Modify Authentication Process
type: technique
mitre_id: T1556
mitre_url: null
created_at: '2023-04-06T00:31:27.191739+00:00'
updated_at: '2023-04-06T03:56:41.323161+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[AWS-ECR-Repository-Policy-Enumeration]]'
- '[[dns-poisoning-and-credential-dumping-via-mitm6-relay-attack]]'
- '[[Detect-Secrets-in-Git-Repositories-with-Gitleaks]]'
- '[[Git-Repository-Secrets-Harvesting-with-TruffleHog]]'
- '[[Golden-SAML-Attack-via-ADFS]]'
- '[[Insecure-Docker-Registry-Pentest]]'
- '[[jwt-signature-key-confusion-attack-rs256-to-hs256-cve-2016-5431]]'
- '[[JWT-Token-Forgery-via-JWKS-Header-Injection]]'
- '[[Obtain-Microsoft-Graph-API-Access-Token-via-Device-Code-Flow]]'
- '[[ntlm-reflection-smb-relay-attack]]'
- '[[SAML-Injection-Authentication-Bypass]]'
- '[[Shadow-Credentials-for-Windows-Hello]]'
- '[[SSL-MITM-Network-Discovery-with-OpenSSL]]'
- '[[Web-Sockets-Authentication-Exploitation]]'
---

# Modify Authentication Process

**MITRE ID**: T1556

## Description

Adversaries may modify authentication mechanisms and processes to access user credentials or enable otherwise unwarranted access to accounts. The authentication process is handled by mechanisms, such as the Local Security Authentication Server (LSASS) process and the Security Accounts Manager (SAM) on Windows, pluggable authentication modules (PAM) on Unix-based systems, and authorization plugins on MacOS systems, responsible for gathering, storing, and validating credentials. By modifying an authentication process, an adversary may be able to authenticate to a service or system without using [Valid Accounts](https://attack.mitre.org/techniques/T1078).

Adversaries may maliciously modify a part of this process to either reveal credentials or bypass authentication mechanisms. Compromised credentials or access may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access and remote desktop.



## Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

## Related Procedures (14)

- [[AWS-ECR-Repository-Policy-Enumeration]]
- [[dns-poisoning-and-credential-dumping-via-mitm6-relay-attack]]
- [[Detect-Secrets-in-Git-Repositories-with-Gitleaks]]
- [[Git-Repository-Secrets-Harvesting-with-TruffleHog]]
- [[Golden-SAML-Attack-via-ADFS]]
- [[Insecure-Docker-Registry-Pentest]]
- [[jwt-signature-key-confusion-attack-rs256-to-hs256-cve-2016-5431]]
- [[JWT-Token-Forgery-via-JWKS-Header-Injection]]
- [[Obtain-Microsoft-Graph-API-Access-Token-via-Device-Code-Flow]]
- [[ntlm-reflection-smb-relay-attack]]
- [[SAML-Injection-Authentication-Bypass]]
- [[Shadow-Credentials-for-Windows-Hello]]
- [[SSL-MITM-Network-Discovery-with-OpenSSL]]
- [[Web-Sockets-Authentication-Exploitation]]


