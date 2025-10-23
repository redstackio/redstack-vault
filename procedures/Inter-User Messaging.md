---
id: 6ce5e24e-661a-4026-9847-37940f4a0a03
name: Inter-User Messaging
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.861809+00:00'
updated_at: '2023-04-06T03:56:21.885506+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]'
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Miscellaneous & Tricks]]'
- '[[Send a message to another user]]'
commands:
- '[[Send message to all users on Linux]]'
- '[[Send message to all users on Linux with specific time]]'
- '[[Send message to all users on Windows]]'
- '[[Send message to specific user on Linux]]'
- '[[Send message to specific user on Windows]]'
- '[[Show currently logged in users on Linux]]'
---

# Inter-User Messaging

## Summary

Inter-User Messaging is a technique for sending messages to other users on Windows and Linux systems. This can be useful for communicating with other users on the same system, or for sending alerts or notifications. From an offensive perspective, this technique can be used to communicate with other

## Description

# Description

Inter-User Messaging is a technique for sending messages to other users on Windows and Linux systems. This can be useful for communicating with other users on the same system, or for sending alerts or notifications. From an offensive perspective, this technique can be used to communicate with other users on a compromised system, or to send messages to users on a targeted system as part of a social engineering campaign.

To send a message on Windows, the 'net send' command can be used. On Linux, the 'write' command can be used. Both commands require the name or IP address of the target system, as well as the username of the target user. The message can be up to 128 characters long.

The business value of Inter-User Messaging is that it can be used to quickly and easily communicate with other users on the same system, which can be useful for collaboration or for sending alerts or notifications. However, it is important to note that this technique can also be used by attackers for malicious purposes, such as communicating with other attackers on a compromised system or for social engineering attacks.

 

## Requirements

1. Authenticated access to the target system

1. Permission to send messages to other users

1. Knowledge of the target user's username

 

## Defense

1. Limit user permissions to prevent unauthorized use of Inter-User Messaging

1. Monitor for suspicious messages or activity related to Inter-User Messaging

1. Use endpoint protection software to detect and block malicious use of Inter-User Messaging

 

## Objectives

1. To send messages to other users on a Windows or Linux system

1. To communicate with other users on a compromised system

1. To send messages to users on a targeted system as part of a social engineering campaign

 

# Instructions

1. To send a message to a user on Windows, use the 'msg' command followed by the username and the message. To send a message to all users on a Windows server, use the '*' wildcard instead of a username. On Linux, use the 'wall' command followed by the message to send a message to all users. Use the '-n' option with 'wall' command only for root. To send a direct message to a user on Linux, use the 'write' command followed by the username and press Ctrl+D after typing the message.

 



**Code**: [[# Windows
PS C:\> msg Swissky /SERVER:CRASHLAB "St]]



> The 'msg' command on Windows is used to send messages to users on the same network. The '/SERVER' option is used to specify the name of the server to which the message is to be sent. The '/V' option is used to display the message in the title bar of the recipient's screen. The '/W' option is used to wait for the recipient to acknowledge the message before continuing. On Linux, the 'wall' command is used to send messages to all users on the system. The '-n' option is used to prevent the message from being broadcasted to all terminals. The 'who' command is used to display the list of all logged-in users. The 'write' command is used to send a direct message to a specific user on the system.



**Command** ([[Send message to specific user on Windows]]):

```bash
msg Swissky /SERVER:CRASHLAB "Stop rebooting the XXXX service !"
```





**Command** ([[Send message to all users on Windows]]):

```bash
msg * /V /W /SERVER:CRASHLAB "Hello all !"
```





**Command** ([[Send message to all users on Linux]]):

```bash
$ wall "Stop messing with the XXX service !"
```





**Command** ([[Send message to all users on Linux with specific time]]):

```bash
$ wall -n "System will go down for 2 hours maintenance at 13:00 PM"
```





**Command** ([[Show currently logged in users on Linux]]):

```bash
$ who
```





**Command** ([[Send message to specific user on Linux]]):

```bash
$ write root pts/2	# press Ctrl+D  after typing the message.
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]
- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Commands Used

- [[Send message to all users on Linux]]
- [[Send message to all users on Linux with specific time]]
- [[Send message to all users on Windows]]
- [[Send message to specific user on Linux]]
- [[Send message to specific user on Windows]]
- [[Show currently logged in users on Linux]]

## Tags

- [[Miscellaneous & Tricks]]
- [[Send a message to another user]]


