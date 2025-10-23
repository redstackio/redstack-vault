---
id: 25a46503-3bca-4e4b-ab8a-2fdc49089b92
name: Gopher Server-Side Request Forgery via SMTP Spoofing Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.905051+00:00'
updated_at: '2023-04-10T20:24:03.221425+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Gopher]]'
- '[[Server-Side Request Forgery]]'
- '[[SSRF exploitation via URL Scheme]]'
---

# Gopher Server-Side Request Forgery via SMTP Spoofing Attack

## Summary

Gopher Server-Side Request Forgery via SMTP Spoofing Attack is a technique used by attackers to exploit SSRF vulnerabilities in web applications that allow the attacker to send crafted requests to the server. The attacker sends a specially crafted URL that contains a Gopher scheme, which tricks the

## Description

# Description

Gopher Server-Side Request Forgery via SMTP Spoofing Attack is a technique used by attackers to exploit SSRF vulnerabilities in web applications that allow the attacker to send crafted requests to the server. The attacker sends a specially crafted URL that contains a Gopher scheme, which tricks the server into making requests to internal resources. By sending a SMTP Spoofing Attack request, the attacker can then send emails from the server to other users, allowing them to perform phishing attacks or spread malware. This technique can be used to bypass network restrictions and access sensitive information.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the internal resources of the target system

1. Tools to craft Gopher URLs and SMTP Spoofing Attack requests

 

## Defense

1. Implement input validation to prevent SSRF attacks

1. Use a web application firewall to block requests containing Gopher schemes

1. Monitor outgoing network traffic for unusual activity

 

## Objectives

1. Exploit SSRF vulnerabilities in web applications

1. Send crafted requests to the server

1. Send emails from the server to other users

 

# Instructions

1. To execute this SMTP Spoofing Attack, follow these steps:
1. Execute ssrf.php with the provided URL.
2. The request will be made to the server with the specified IP and port (127.0.0.1:25).
3. The HELO command is used to identify the domain name of the sending host.
4. The MAIL FROM command specifies the email address of the sender.
5. The RCPT TO command specifies the email address of the recipient.
6. The DATA command indicates that the email message is about to be sent.
7. The From, To, Date, and Subject fields are specified in the email message.
8. The message body is specified after the Subject field.
9. The period (.) indicates the end of the message.
10. The QUIT command is used to terminate the connection.

 



**Code**: [[ssrf.php?url=gopher://127.0.0.1:25/xHELO%20localho]]



> This command is used to send a spoofed email to a victim. The attacker can specify any sender email address and any recipient email address. The email message can contain any text that the attacker desires. This attack can be used to trick the victim into revealing sensitive information or taking some other action that is detrimental to their security. It is important to note that this attack requires access to an SMTP server that allows unauthenticated email sending.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Gopher]]
- [[Server-Side Request Forgery]]
- [[SSRF exploitation via URL Scheme]]


