---
id: 7e2b0bda-cbce-4488-a184-fe8218ba8fc3
name: XXE File Retrieval via XInclude Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.218474+00:00'
updated_at: '2023-04-10T20:24:36.737249+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Create Account|T1136 - Create Account]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
sub_techniques:
- '[[DNS|T1071.004 - DNS]]'
- '[[Local Account|T1136.001 - Local Account]]'
- '[[Web Protocols|T1071.001 - Web Protocols]]'
tags:
- '[[Exploiting XXE to retrieve files]]'
- '[[XInclude attacks]]'
- '[[XML External Entity]]'
---

# XXE File Retrieval via XInclude Attack

## Summary

XML External Entity (XXE) Injection is a type of attack against applications that parse XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. By exploiting this vulnerability, an attacker can access sensitive data o

## Description

# Description

XML External Entity (XXE) Injection is a type of attack against applications that parse XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. By exploiting this vulnerability, an attacker can access sensitive data on the targeted system. One way to achieve this is through XInclude attacks, which allow an attacker to include files from the local file system or remote system.

In technical terms, an attacker can craft an XML payload that includes a reference to an external entity, which can be a file on the system. When the XML parser processes the payload, it will attempt to retrieve the external entity, providing the attacker with access to the file. This attack can be used to retrieve sensitive files, such as configuration files, credentials, or other sensitive data.

The business value of this attack is that it allows an attacker to gain access to sensitive data that can be used for further attacks or sold on the black market. It can also be used to gain a foothold in a system, which can be used to launch additional attacks.


 

## Requirements

1. Knowledge of the target system's XML parser and configuration.

1. Access to a vulnerable application that parses XML input.

 

## Defense

1. Use a strong XML parser that is configured to prevent XXE attacks.

1. Sanitize user input to prevent malicious XML payloads.

1. Implement network segmentation to prevent attackers from accessing sensitive data.

 

## Objectives

1. Retrieve sensitive files from the target system.

1. Gain access to sensitive data that can be used for further attacks or sold on the black market.

1. Gain a foothold in a system, which can be used to launch additional attacks.

 

# Instructions

1. To mitigate XXE injection, ensure that untrusted XML input is not parsed by the application. If parsing is necessary, then disable external entities and use a secure parser that is not vulnerable to XXE injection. If external entities are necessary, then use a whitelist of allowed entities and validate all user input against this whitelist.

 



**Code**: [[<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<]]



> XXE injection is a type of attack where an attacker can inject malicious XML content into an XML document that is then processed by a vulnerable parser. This can lead to sensitive information disclosure, denial of service, and even remote code execution. In this specific example, the attacker is attempting to include the contents of the /etc/passwd file using the XInclude element. By properly configuring the parser to disable external entities, this attack can be prevented.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Create Account|T1136 - Create Account]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

### Sub-Techniques

- [[DNS|T1071.004 - DNS]]
- [[Local Account|T1136.001 - Local Account]]
- [[Web Protocols|T1071.001 - Web Protocols]]

## Tags

- [[Exploiting XXE to retrieve files]]
- [[XInclude attacks]]
- [[XML External Entity]]


