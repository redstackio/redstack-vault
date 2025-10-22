---
id: a1e04184-8473-4eed-bf49-d06f0d309348
name: Enumerate and Analyze an SSL/TLS Certificate
type: procedure
verified: false
submitted: false
created_at: '2019-10-23T19:01:03.917164+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Organizational Information Gathering|TA0017 - Organizational Information Gathering]]'
techniques:
- '[[Acquire OSINT data sets and information|T1277 - Acquire OSINT data sets and information]]'
platforms:
- Web
tags:
- '[[Cryptography]]'
- '[[data exposure]]'
- '[[Web Applications]]'
commands:
- '[[Keytool Extract Owner Information from SSL Certificate]]'
- '[[SSLyze Enumerate a Web Server''s SSL/TLS Certificate]]'
---

# Enumerate and Analyze an SSL/TLS Certificate

## Summary

Organizations include information in their SSL certificates which can disclose details and aid attackers in the enumeration and development of attack vectors. SSL certificates will often list alternate DNS names (suggesting virtual hosts are configured on the target), registration dates, validity, 

## Description

# Description

Organizations include information in their SSL certificates which can disclose details and aid attackers in the enumeration and development of attack vectors. SSL certificates will often list alternate DNS names (suggesting virtual hosts are configured on the target), registration dates, validity, etc, and should be enumerated whenever possible.

# Instructions

View SSL Certificate information

**Command** ([[SSLyze Enumerate a Web Server's SSL/TLS Certificate]]):

```bash
sslyze --regular $_TARGET_HOST
```

**Useful fields:**

- X509v3 Subject Alternative Name

- Certificate Chain Received

- Not After (expiry)

- OpenSSL Heartbleed

- Cipher Suites

**Command** ([[Keytool Extract Owner Information from SSL Certificate]]):

```bash
keytool -printcert -sslserver $_TARGET_IP:$_TARGET_PORT
```

## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Organizational Information Gathering|TA0017 - Organizational Information Gathering]]

### Techniques

- [[Acquire OSINT data sets and information|T1277 - Acquire OSINT data sets and information]]

## Commands Used

- [[Keytool Extract Owner Information from SSL Certificate]]
- [[SSLyze Enumerate a Web Server's SSL/TLS Certificate]]

## Tags

- [[Cryptography]]
- [[data exposure]]
- [[Web Applications]]
