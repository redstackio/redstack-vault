---
id: a6d802d4-bc7a-42ca-8452-6750d72b2948
name: TE Header Obfuscation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.025015+00:00'
updated_at: '2023-04-10T20:23:24.613827+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
- '[[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]'
sub_techniques:
- '[[Steganography|T1001.002 - Steganography]]'
tags:
- '[[Request Smuggling]]'
- '[[TE.TE behavior: obfuscating the TE header]]'
commands:
- '[[Transfer Encoding]]'
---

# TE Header Obfuscation

## Summary

TE Header Obfuscation is a technique used to obfuscate the TE header in HTTP requests. This technique is used in Request Smuggling attacks to bypass security controls and smuggle requests to the backend server. By obfuscating the TE header, attackers can make it difficult for security controls to d

## Description

# Description

TE Header Obfuscation is a technique used to obfuscate the TE header in HTTP requests. This technique is used in Request Smuggling attacks to bypass security controls and smuggle requests to the backend server. By obfuscating the TE header, attackers can make it difficult for security controls to detect and block malicious traffic. This technique is commonly used in combination with other Request Smuggling techniques to create complex and sophisticated attacks.

From a technical perspective, TE Header Obfuscation involves sending HTTP requests with a modified TE header that contains non-standard values. This can cause some web servers and security controls to misinterpret the request and allow it to pass through to the backend server. This technique can be used to bypass security controls that rely on the TE header to detect and block malicious traffic.

From a business perspective, TE Header Obfuscation can be used to bypass security controls and gain unauthorized access to sensitive data. This can lead to data theft, data manipulation, and other types of cyber attacks.

## Requirements

1. Access to HTTP requests

## Defense

1. Implement strict input validation to prevent injection attacks.

1. Implement a Web Application Firewall (WAF) to detect and block Request Smuggling attacks.

1. Monitor network traffic for suspicious activity and investigate any anomalies.

## Objectives

1. Bypass security controls and gain unauthorized access to sensitive data

# Instructions

1. To use this command, follow these steps:
1. Go to the Repeater menu in Burp Suite.
2. Ensure that the "Update Content-Length" option is unchecked.
3. Include the trailing sequence \r\n\r\n following the final 0 in the request.

**Code**: [[Transfer-Encoding: xchunked
Transfer-Encoding : ch]]

> The Transfer-Encoding command is used to specify the form of encoding used to transfer the entity to the recipient. This command can take multiple arguments such as xchunked, chunked, and x. The arguments specify the encoding format used to transfer the data. When using Burp Repeater, it is important to ensure that the "Update Content-Length" option is unchecked to avoid issues with the request. Additionally, it is important to include the trailing sequence \r\n\r\n following the final 0 to ensure that the request is properly formatted.

**Command** ([[Transfer Encoding]]):

```bash
Transfer-Encoding: xchunked
Transfer-Encoding : chunked
Transfer-Encoding: chunked
Transfer-Encoding: x
Transfer-Encoding:[tab]chunked
[space]Transfer-Encoding: chunked
X: X[\n]Transfer-Encoding: chunked
Transfer-Encoding
: chunked
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Data Obfuscation|T1001 - Data Obfuscation]]
- [[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]

### Sub-Techniques

- [[Steganography|T1001.002 - Steganography]]

## Commands Used

- [[Transfer Encoding]]

## Tags

- [[Request Smuggling]]
- [[TE.TE behavior: obfuscating the TE header]]
