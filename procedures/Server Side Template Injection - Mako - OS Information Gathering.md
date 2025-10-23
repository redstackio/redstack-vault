---
id: b9287f9e-2aca-4a1b-b1db-d604f65b8005
name: Server Side Template Injection - Mako - OS Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.096701+00:00'
updated_at: '2023-04-10T20:23:30.330991+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Direct access to os from TemplateNamespace:]]'
- '[[Mako]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Print OS module path]]'
---

# Server Side Template Injection - Mako - OS Information Gathering

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into the server-side template, which can lead to code execution on the server. Mako is a template engine that allows developers to create dynamic web pages. This procedure describes how to use 

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into the server-side template, which can lead to code execution on the server. Mako is a template engine that allows developers to create dynamic web pages. This procedure describes how to use Mako's TemplateNamespace to gain OS information from the server. By using the 'Operating System Information' and 'Print OS Module Path' commands, an attacker can gather information about the operating system running on the server.

Technical Explanation: The 'TemplateNamespace' object in Mako allows direct access to the operating system from the template. This can be exploited by an attacker to execute arbitrary commands on the server. The 'Operating System Information' command executes the 'uname -a' command on the server, which returns information about the operating system. The 'Print OS Module Path' command executes the 'python -c "import os;print(os.__file__)"' command on the server, which returns the path of the 'os' module on the server.

Business Value: This procedure can be used by an attacker to gather information about the target server, which can be used to plan further attacks or to sell the information on the black market.

 

## Requirements

1. Direct access to the server-side template.

1. Knowledge of Mako's TemplateNamespace syntax.

 

## Defense

1. Implement input validation to prevent injection attacks.

1. Disable direct access to the operating system from the template.

1. Regularly monitor and analyze server logs for suspicious activity.

 

## Objectives

1. Gather information about the operating system running on the target server.

 

# Instructions

1. Use the following commands to retrieve information about the operating system:
- 'os.name' - Returns the name of the operating system.
- 'os.version' - Returns the version of the operating system.
- 'os.architecture' - Returns the architecture of the operating system.

 



**Code**: [[os]]



> The 'os' payload provides information about the operating system. The 'os.name' command returns the name of the operating system. The 'os.version' command returns the version of the operating system. The 'os.architecture' command returns the architecture of the operating system. These commands can be used to retrieve information about the operating system that can be used for troubleshooting or system administration purposes.

2. This command prints the path of the 'os' module in Python.

 



**Code**: [[>>> print(Template("${self.module.cache.util.os}")]]



> The 'os' module in Python provides a way of using operating system dependent functionality like reading or writing to the file system. This command uses the 'Template' class from the 'string' module to substitute the module path in the string and then prints it using the 'print' function. The output shows the path of the 'os' module in the system where the code is executed.



**Command** ([[Print OS module path]]):

```bash
print(Template(\"${self.module.cache.util.os}\").render())
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Print OS module path]]

## Tags

- [[Direct access to os from TemplateNamespace:]]
- [[Mako]]
- [[Server Side Template Injection]]


