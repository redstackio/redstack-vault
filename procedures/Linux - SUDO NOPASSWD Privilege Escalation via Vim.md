---
id: bbab094d-f104-4e0f-a442-a570cd056c48
name: Linux - SUDO NOPASSWD Privilege Escalation via Vim
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.970740+00:00'
updated_at: '2023-04-10T20:34:22.673413+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
sub_techniques:
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
- '[[CMSTP|T1218.003 - CMSTP]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[NOPASSWD]]'
- '[[SUDO]]'
commands:
- '[[Check sudo privileges]]'
- '[[Open a file in vim]]'
---

# Linux - SUDO NOPASSWD Privilege Escalation via Vim

## Summary

This procedure involves exploiting a vulnerability in the SUDO configuration file, specifically targeting the NOPASSWD option. By using the Vim text editor, an attacker can edit the SUDO configuration file and add themselves to the list of users with NOPASSWD privileges, effectively granting themse

## Description

# Description

This procedure involves exploiting a vulnerability in the SUDO configuration file, specifically targeting the NOPASSWD option. By using the Vim text editor, an attacker can edit the SUDO configuration file and add themselves to the list of users with NOPASSWD privileges, effectively granting themselves root access. This technique can be used to escalate privileges and gain access to sensitive information or perform malicious actions on the system.

Technical Explanation: The attacker first needs to have access to a user account that has SUDO privileges. They then use the Vim text editor to modify the SUDO configuration file, adding themselves to the list of users with NOPASSWD privileges. This allows them to execute any command as root without being prompted for a password.

Business Value: This procedure can be used by attackers to gain unauthorized access to sensitive data and perform malicious actions on the system. By escalating privileges, an attacker can bypass security controls and gain access to information that they would not normally have access to.

 

## Requirements

1. Access to a user account with SUDO privileges

1. Ability to use the Vim text editor

 

## Defense

1. Regularly monitor and review SUDO configuration files to ensure that there are no unauthorized changes

1. Limit the number of users with SUDO privileges and regularly review and update the list

1. Implement two-factor authentication for SUDO access to prevent unauthorized access

 

## Objectives

1. Escalate privileges from a user account to root access

1. Gain access to sensitive information

1. Perform malicious actions on the system

 

# Instructions

1. To escalate privileges using this vulnerability, run the following command:

`sudo vim -c ':!/bin/sh'`

This will open a Vim editor with root privileges. Then, execute the command `:! /bin/sh` to spawn a shell as root.

 



**Code**: [[$ sudo -l

User demo may run the following command]]



> The `sudo -l` command shows the list of commands that the user is allowed to run with elevated privileges. In this case, the user 'demo' is allowed to run the `vim` command as root without entering a password. This is a vulnerability that can be exploited to escalate privileges. The exploit involves opening Vim editor with root privileges and then executing a shell command within Vim to spawn a shell as root.



**Command** ([[Check sudo privileges]]):

```bash
$ sudo -l
```



2. can use multiple commands to showcase the functionality of the system. The available commands are: command1, command2, and command3.

 



**Code**: [[demo]]



> When using command1, the user can provide arguments X and Y to achieve result Z. Command2 takes in arguments A and B to perform function C. Command3 requires arguments P and Q to execute operation R. Please refer to the documentation for further details on the usage of these commands.

3. vim is a highly configurable text editor built to enable efficient text editing. It is an improved version of the vi editor distributed with most UNIX systems. Vim is often called a "programmer's editor," and so useful for programming that many consider it an entire IDE. It's not just for programmers, though. Vim is perfect for all kinds of text editing, from composing an email to editing configuration files.

 



**Code**: [[vim]]



> The vim command is used to open and edit text files in the terminal. It has a variety of commands and shortcuts that allow for efficient editing. Some arguments that can be used with the vim command include the name of the file to be edited, options to set the number of spaces to use for tabs, and options to enable syntax highlighting. The vim editor also has different modes, such as insert mode and command mode, which can be accessed using specific keyboard shortcuts.



**Command** ([[Open a file in vim]]):

```bash
vim filename.txt
```



4. sudo su

 



**Code**: [[root]]



> This command allows the user to switch to the root user account, giving them unrestricted access to the system. The 'sudo su' command is used to elevate the user's privileges to that of the root user. This command should be used with caution as it can potentially cause harm to the system if used incorrectly.

5. To add an SSH key into the root directory, first generate an SSH key pair using the 'ssh-keygen' command. Then, copy the public key to the remote server's root directory using the 'ssh-copy-id' command. Finally, use the 'ssh' command to connect to the remote server with the specified private key.
To call a shell using SSH, use the 'ssh' command with the '-t' option followed by the remote server's address and the desired shell command.

 



**Code**: [[sh]]



> The 'ssh' command is used to securely connect to a remote server. By adding an SSH key into the root directory or using the '-t' option with the 'ssh' command, a user can easily gain shell access to the remote server. The SSH key provides an extra layer of security by requiring a private key to authenticate the user.

6. To gain root access via Vim, use the following commands:

 



**Code**: [[sudo vim -c '!sh'
sudo -u root vim -c '!sh']]



> This command allows the user to open Vim text editor with elevated privileges, which can then be used to execute shell commands as root. The first command opens Vim with elevated privileges, and the second command opens Vim as the root user. Once inside Vim, the user can execute shell commands by entering the command mode (pressing the ':' key) and typing '!sh'. This will open a shell prompt, where the user can execute any shell command with root privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

### Sub-Techniques

- [[Bypass User Account Control|T1548.002 - Bypass User Account Control]]
- [[CMSTP|T1218.003 - CMSTP]]

## Commands Used

- [[Check sudo privileges]]
- [[Open a file in vim]]

## Tags

- [[Linux - Privilege Escalation]]
- [[NOPASSWD]]
- [[SUDO]]


