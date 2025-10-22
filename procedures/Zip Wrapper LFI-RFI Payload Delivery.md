---
id: 0051375c-b192-4855-b640-2e2138c7239b
name: Zip Wrapper LFI/RFI Payload Delivery
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.357177+00:00'
updated_at: '2023-04-10T20:22:12.377445+00:00'
tags:
- '[[File Inclusion]]'
- '[[LFI / RFI using wrappers]]'
- '[[Wrapper zip://]]'
commands:
- '[[Zip and rename payload.php to shell.jpg]]'
---

# Zip Wrapper LFI/RFI Payload Delivery

## Summary

This procedure aims to deliver a payload to a vulnerable server through a zip wrapper LFI/RFI attack. The attack takes advantage of the zip wrapper to deliver a malicious payload disguised as a harmless image. Once the server processes the image, the payload is executed, allowing the attacker to ga

## Description

# Description

This procedure aims to deliver a payload to a vulnerable server through a zip wrapper LFI/RFI attack. The attack takes advantage of the zip wrapper to deliver a malicious payload disguised as a harmless image. Once the server processes the image, the payload is executed, allowing the attacker to gain access to the server and execute arbitrary commands. This technique can be used to bypass security measures such as firewalls or intrusion detection systems, making it a useful tool for attackers. From a technical standpoint, the attack involves crafting a zip file with a payload.php file and changing its extension to .jpg. The server then processes the file as an image, but executes the payload instead, giving the attacker control over the server. This procedure can be used to gain access to sensitive data, escalate privileges, or perform other malicious activities.

## Requirements

1. Access to a vulnerable server with a zip wrapper LFI/RFI vulnerability

## Defense

1. Implement input validation to prevent LFI/RFI attacks

1. Implement file type validation to prevent disguised payloads from being executed

1. Monitor server logs for suspicious activity

## Objectives

1. Deliver a payload to a vulnerable server

1. Bypass security measures such as firewalls or intrusion detection systems

1. Gain access to the server and execute arbitrary commands

# Instructions

1. The following commands can be used to create the zip file and rename it to shell.jpg:
1. zip payload.zip payload.php
2. mv payload.zip shell.jpg
3. rm payload.php

**Code**: [[zip payload.zip payload.php;
mv payload.zip shell.]]

> The first command creates a zip file containing the payload.php file. The second command renames the zip file to shell.jpg, disguising it as an image file. The third command removes the original payload.php file to avoid detection.

**Command** ([[Zip and rename payload.php to shell.jpg]]):

```bash
zip payload.zip payload.php;
mv payload.zip shell.jpg;
rm payload.php
```

## Commands Used

- [[Zip and rename payload.php to shell.jpg]]

## Tags

- [[File Inclusion]]
- [[LFI / RFI using wrappers]]
- [[Wrapper zip://]]
