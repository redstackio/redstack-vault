---
id: 0868da57-379f-45ad-a149-b9e11fe15a4c
name: Werkzeug Debugger Panel Read/Write RCE
type: procedure
verified: false
submitted: false
created_at: '2019-10-09T23:01:08.421637+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Accessibility Features|T1015 - Accessibility Features]]'
platforms:
- Linux
tags:
- '[[Web Applications]]'
---

# Werkzeug Debugger Panel Read/Write RCE

## Summary

Werkzeug is a popular WSGI application library, which includes a Debugger console that allows remote users to execute code. This feature is turned off by default, but if enabled makes Remote Code Execution trivial. The Debugger page which contains the console appears when an error is generated. 

## Description

# Description

Werkzeug is a popular WSGI application library, which includes a Debugger console that allows remote users to execute code. This feature is turned off by default, but if enabled makes Remote Code Execution trivial. The Debugger page which contains the console appears when an error is generated. 

# Instructions

In order access the Debugger, an error page needs to be triggered as it contains the console. One approach is to find  pages which load by index, then change the index to a value that is out of range.

Example

Original URL:

[http://10.10.10.10/articles/1](http://10.10.10.10/articles/1)

Modified URL:

[http://10.10.10.10/articles/1000](http://10.10.10.10/articles/1000)

1. Trigger an error page.

2. On the error page, the Debugger console can be opened by clicking on the console icon near the top right of each box.

## Read System Files Using Werkzeug's Debugger

1. Determine a target file to read. In this example, `/etc/passwd `is chosen.

2. Execute a basic file read command in Python.

**Code**: [[target = "/etc/passwd"; f = open(target, "r"); pri]]

## Write Files Using Werkzeug's Debugger

1. Determine a target file to write. In this example, `/home/bob/.ssh/authorized_keys` is chosen.

2. Create a variable in the Debugger console named pwn, and set it to the value of the attacker's SSH public key.

**Code**: [[pwn = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwCUg]]

3. Execute a basic file write command in Python.

**Code**: [[target = "/home/bob/.ssh/authorized_keys"; f = ope]]

## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Accessibility Features|T1015 - Accessibility Features]]

## Tags

- [[Web Applications]]
