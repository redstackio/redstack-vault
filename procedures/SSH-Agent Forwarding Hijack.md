---
id: 51fd2cbe-a80f-494a-b37f-5e0657bd1066
name: SSH-Agent Forwarding Hijack
type: procedure
verified: true
submitted: true
created_at: '2019-10-22T00:49:09.170787+00:00'
updated_at: '2023-05-26T00:52:04.934178+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[SSH Hijacking|T1184 - SSH Hijacking]]'
platforms:
- Linux
tags:
- '[[Network]]'
- '[[Service Attacks]]'
commands:
- '[[SSH with SSH-Agent Hijack]]'
---

# SSH-Agent Forwarding Hijack

**Status**: ✓ Verified

## Summary

SSH-Agent Forwarding is a convenient method of passing SSH keys between computers when there is an intermediary. Instead of passing the SSH key to the intermediary and onto the destination system (potentially exposing it to users on that system), it is passed across using SSH-Forwarding to the fina

## Description

# Description

SSH-Agent Forwarding is a convenient method of passing SSH keys between computers when there is an intermediary. Instead of passing the SSH key to the intermediary and onto the destination system (potentially exposing it to users on that system), it is passed across using SSH-Forwarding to the final host.

Unfortunately SSH-Agent Forwarding can be problematic when an attacker has root access to the intermediary system. By having root access, an attacker can configure their environmental variables to use the same SSH-Agent as a legitimate user, hijacking the session and gaining access for themselves.



# Instructions

1. Identify the SSH session. When a SSH-Agent Forwarding session is active, it is listed in `/tmp` as a directory.

- The directory follows the format: `/tmp/ssh-XXXXXXXXXXX`

- If multiple directories exist, look for the one which correlates closest to the target user's login time.

![b0d1562d-bd3c-43f1-a20e-cca10cc4b404.png](_assets/images/Mark/b0d1562d-bd3c-43f1-a20e-cca10cc4b404.png)

2. After identifying a session, as root enter the directory and list files. Look for a file named “agent.XXX”



![87be2a5b-839f-4ff9-aa44-503d408a08f0.png](_assets/images/Mark/87be2a5b-839f-4ff9-aa44-503d408a08f0.png)



3. Launch a new SSH session, specifying the agent of the target.





**Command** ([[SSH with SSH-Agent Hijack]]):

```bash
SSH_AUTH_SOCK=agent.XXX ssh $_USER@$_TARGET_IP
```





## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[SSH Hijacking|T1184 - SSH Hijacking]]

## Commands Used

- [[SSH with SSH-Agent Hijack]]

## Tags

- [[Network]]
- [[Service Attacks]]


