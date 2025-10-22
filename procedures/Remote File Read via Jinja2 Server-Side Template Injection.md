---
id: 027e0a13-cac2-44c2-bcae-f350b46df486
name: Remote File Read via Jinja2 Server-Side Template Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.689236+00:00'
updated_at: '2023-04-10T20:23:31.729185+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
sub_techniques:
- '[[Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 - Exfiltration Over Unencrypted
  Non-C2 Protocol]]'
tags:
- '[[Jinja2]]'
- '[[Jinja2 - Read remote file]]'
- '[[Server Side Template Injection]]'
---

# Remote File Read via Jinja2 Server-Side Template Injection

## Summary

Remote File Read via Jinja2 Server-Side Template Injection is a technique used by attackers to read sensitive information from remote files. This technique involves exploiting a vulnerability in a web application that uses the Jinja2 templating engine. The attacker can inject malicious code into th

## Description

# Description

Remote File Read via Jinja2 Server-Side Template Injection is a technique used by attackers to read sensitive information from remote files. This technique involves exploiting a vulnerability in a web application that uses the Jinja2 templating engine. The attacker can inject malicious code into the application, which allows them to read files on the server that the application has access to.

From a technical perspective, this attack works by injecting a Jinja2 template that includes a file read operation. The attacker can specify the file path they want to read, and the contents of the file will be included in the template output. This technique can be used to read sensitive configuration files, credentials, or other sensitive data that may be stored on the server.

The business value of this attack lies in the ability of the attacker to gain access to sensitive information that can be used to further compromise the organization. For example, the attacker may be able to use stolen credentials to gain access to other systems or applications within the organization.

## Requirements

1. Access to a web application that uses the Jinja2 templating engine

1. Ability to inject malicious code into the application

## Defense

1. Ensure that web applications are kept up-to-date with the latest security patches

1. Use input validation and output encoding to prevent injection attacks

1. Implement access controls to limit the ability of attackers to access sensitive files

## Objectives

1. Read sensitive information from remote files

1. Gain access to credentials or other sensitive data

1. Further compromise the organization

# Instructions

1. To read sensitive information from files, execute the following commands:

**Code**: [[# ''.__class__.__mro__[2].__subclasses__()[40] = F]]

> The above commands demonstrate how to read sensitive information from files. The first two commands use the `File` class to read the contents of the `/etc/passwd` and `/tmp/flag` files. The third command uses the `open` function to read the contents of the `/etc/passwd` file. Note that these commands can be used to read any file on the system that the current user has read access to.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

### Sub-Techniques

- [[Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 - Exfiltration Over Unencrypted Non-C2 Protocol]]

## Tags

- [[Jinja2]]
- [[Jinja2 - Read remote file]]
- [[Server Side Template Injection]]
