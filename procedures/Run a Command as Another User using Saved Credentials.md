---
id: 8c83daf1-663e-4000-b16a-a2f98d2cb3dd
name: Run a Command as Another User using Saved Credentials
type: procedure
verified: true
submitted: true
created_at: '2019-12-03T23:33:32.539667+00:00'
updated_at: '2023-05-25T19:48:40.514288+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Valid Accounts|T1078 - Valid Accounts]]'
platforms:
- Windows
tags:
- '[[access control]]'
- '[[authentication]]'
commands:
- '[[runas.exe Execute a Command using Saved Credentials]]'
---

# Run a Command as Another User using Saved Credentials

**Status**: ✓ Verified

## Summary

Windows allows users to execute command from the terminal as other users using "runas.exe". This command can be invoked with or without saved credentials, but if "runas.exe" is not being invoked from a standard shell run locally on the target, it will not properly display the password prompt, and t

## Description

# Description

Windows allows users to execute command from the terminal as other users using "runas.exe". This command can be invoked with or without saved credentials, but if "runas.exe" is not being invoked from a standard shell run locally on the target, it will not properly display the password prompt, and the command will fail. This manifests when a user is using remote access tools such as netcat or a nishang shell for example.

Using the "/savedcreds" argument will bypass the password prompt, but credentials must have been previously saved with Credential Manager



# Instructions





**Command** ([[runas.exe Execute a Command using Saved Credentials]]):

```bash
runas.exe /profile /user:$_DOMAIN\$_USERNAME /savedcred "$_COMMAND"
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[runas.exe Execute a Command using Saved Credentials]]

## Tags

- [[access control]]
- [[authentication]]


