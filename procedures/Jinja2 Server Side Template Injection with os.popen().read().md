---
id: 85ad3828-95ed-4dfe-b5fd-954c55c878ba
name: Jinja2 Server Side Template Injection with os.popen().read()
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.782623+00:00'
updated_at: '2023-04-10T20:23:48.140427+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
tags:
- '[[Exploit the SSTI by calling os.popen().read()]]'
- '[[Jinja2]]'
- '[[Jinja2 - Remote Code Execution]]'
- '[[Server Side Template Injection]]'
---

# Jinja2 Server Side Template Injection with os.popen().read()

## Summary

Jinja2 is a popular templating engine for Python web applications. It is vulnerable to Server Side Template Injection (SSTI) attacks, where an attacker can inject arbitrary code into a template. By calling os.popen().read() in the template, an attacker can execute arbitrary commands on the server. 

## Description

# Description

Jinja2 is a popular templating engine for Python web applications. It is vulnerable to Server Side Template Injection (SSTI) attacks, where an attacker can inject arbitrary code into a template. By calling os.popen().read() in the template, an attacker can execute arbitrary commands on the server. This can lead to complete compromise of the server and sensitive data theft. This attack is particularly dangerous as it can bypass input validation and server-side security controls.

Technical Explanation: An attacker can inject code into a Jinja2 template by using the {{ }} syntax. By calling os.popen().read() in the template, the attacker can execute arbitrary commands on the server. This can lead to complete compromise of the server and sensitive data theft.

Business Value: An attacker can use this attack to gain access to sensitive data stored on the server, such as user credentials, financial data, and customer information. This can lead to reputational damage, loss of customer trust, and legal liabilities.

 

## Requirements

1. Access to a Jinja2 template on the target server

 

## Defense

1. Ensure that input validation is performed on user input, especially in templates

1. Implement server-side security controls to prevent unauthorized access to sensitive data

1. Regularly update and patch the server and its dependencies to prevent known vulnerabilities

 

## Objectives

1. Execute arbitrary commands on the server

1. Gain access to sensitive data stored on the server

 

# Instructions

1. To get the user ID, run the following command:

 



**Code**: [[{{ self.__init__.__globals__.__builtins__.__import]]



> This command imports the 'os' module in Python and uses the 'popen' method to execute the 'id' command in the underlying operating system. The output of the command is then read and returned as a string, which contains the user ID information.

2. Python has numerous built-in functions that can be used to perform various operations. Some of the commonly used built-in functions are print(), len(), range(), input(), etc.

 



**Code**: [[__builtins__]]



> The '__builtins__' module provides a namespace containing all the built-in names defined by Python. These built-in functions are always available to use without the need for importing any module. The 'print()' function is used to print the specified message to the console. The 'len()' function is used to get the length of an object. The 'range()' function is used to generate a sequence of numbers. The 'input()' function is used to get user input from the console. There are many more built-in functions available in Python that can be used to perform various operations.

3. Execute multiple system commands

 



**Code**: [[{{ self._TemplateReference__context.cycler.__init_]]



> This command executes multiple system commands. The command output will depend on the specific commands executed, which can be defined in the 'data' field of the JSON object. The 'lang' field specifies the programming language used for the commands. Please use with caution as executing system commands can have unintended consequences.

4. The 'id' command is used to display the user and group IDs of the current user. Here, the command is being executed using the 'os.popen' method in Python. This allows us to execute arbitrary commands on the target system.

 



**Code**: [[{{ cycler.__init__.__globals__.os.popen('id').read]]



> The 'cycler', 'joiner', and 'namespace' objects are being used to execute the 'id' command. The output of each command is being concatenated and returned. This payload can be used to test for command injection vulnerabilities in web applications that use Python as their server-side language.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

## Tags

- [[Exploit the SSTI by calling os.popen().read()]]
- [[Jinja2]]
- [[Jinja2 - Remote Code Execution]]
- [[Server Side Template Injection]]


