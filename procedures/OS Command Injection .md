---
id: 7f0997b7-3ce7-4cd3-9022-dd526dd04c15
name: 'OS Command Injection '
type: procedure
verified: true
submitted: true
created_at: '2020-07-28T16:52:08.361140+00:00'
updated_at: '2023-05-26T01:07:41.096072+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[os command injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# OS Command Injection 

**Status**: ✓ Verified

## Summary

OS command injection allows an attacker to execute arbitrary OS commands on the server. The commands can be injected through user input fields. 

## Description

# Description

OS command injection allows an attacker to execute arbitrary OS commands on the server. The commands can be injected through user input fields.

# Instructions

1. In the below image there is an option to look for dns information of a website .

2. Manipulate the *DNS lookup *text box by placing an *or *operator which will ignore the *dnslookup *execution and will execute the command after *or *operator.

3.We can observe that  the response for *ping *command will be executed with significant delay as mentioned in the command which confirms the OS command injection.

## Platforms

- Web

## Tags

- [[injection]]
- [[os command injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
