---
id: d798bfe2-0dbe-4a98-8e2c-1738832a9f8a
name: Linux File Inclusion to Remote Code Execution via Credentials Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.721047+00:00'
updated_at: '2023-04-10T20:22:16.991021+00:00'
tags:
- '[[File Inclusion]]'
- '[[LFI to RCE via credentials files]]'
- '[[Linux version]]'
commands:
- '[[Process Status]]'
- '[[View /etc/passwd file]]'
- '[[View /etc/shadow file]]'
---

# Linux File Inclusion to Remote Code Execution via Credentials Files

## Summary

Linux File Inclusion to Remote Code Execution via Credentials Files is a technique used by attackers to escalate their privileges on a target Linux machine. It involves exploiting a Local File Inclusion vulnerability to read sensitive files such as /etc/shadow, /etc/passwd, and SSH private key file

## Description

# Description

Linux File Inclusion to Remote Code Execution via Credentials Files is a technique used by attackers to escalate their privileges on a target Linux machine. It involves exploiting a Local File Inclusion vulnerability to read sensitive files such as /etc/shadow, /etc/passwd, and SSH private key files. With the credentials obtained, attackers can then escalate their privileges and execute remote code on the target machine. This technique is commonly used in combination with other techniques to achieve initial access to a target environment.

 

## Requirements

1. Access to a vulnerable Linux machine

1. Knowledge of the target Linux system

 

## Defense

1. Implement input validation to prevent LFI vulnerabilities

1. Limit access to sensitive files such as /etc/shadow and SSH private key files

1. Use strong passwords and enforce password policies to make it harder for attackers to crack passwords

 

## Objectives

1. Gain access to sensitive files on a target Linux machine

1. Escalate privileges on the target machine

1. Execute remote code on the target machine

 

# Instructions

1. cat /etc/shadow

 



**Code**: [[/etc/shadow]]



> This command will display the contents of the /etc/shadow file, which contains the encrypted passwords of the users on the system.



**Command** ([[View /etc/shadow file]]):

```bash
/etc/shadow
```



2. curl http://example.com/index.php?page=../../../../../../etc/shadow

 



**Code**: [[http://example.com/index.php?page=../../../../../.]]



> This command will exploit the LFI vulnerability to read the /etc/shadow file, which contains the encrypted passwords of the users on the system. With the credentials obtained, attackers can then escalate their privileges and execute remote code on the target machine.

3. cat /proc/self/status

 



**Code**: [[/proc/self/status]]



> This command will display the contents of the /proc/self/status file, which contains information about the current process. Attackers can use this file to determine which user is running the process and then try to access the /<HOME>/.ssh/id_rsa file to gain SSH access to the target machine.



**Command** ([[Process Status]]):

```bash
cat /proc/self/status
```



4. cat /etc/passwd
ls -la /<HOME>/.ssh/id_rsa

 



**Code**: [[/etc/passwd]]



> This command will display the contents of the /etc/passwd file, which contains information about the users on the system. Attackers can use this file to determine the home directory of the user they are targeting and then try to access the /<HOME>/.ssh/id_rsa file to gain SSH access to the target machine.



**Command** ([[View /etc/passwd file]]):

```bash
/etc/passwd
```



## Commands Used

- [[Process Status]]
- [[View /etc/passwd file]]
- [[View /etc/shadow file]]

## Tags

- [[File Inclusion]]
- [[LFI to RCE via credentials files]]
- [[Linux version]]


