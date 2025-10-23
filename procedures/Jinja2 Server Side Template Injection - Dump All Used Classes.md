---
id: 935c7d1b-96c2-45d0-8087-0bfe222fb769
name: Jinja2 Server Side Template Injection - Dump All Used Classes
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.629435+00:00'
updated_at: '2023-04-10T20:23:32.120859+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Data from Local System|T1005 - Data from Local System]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Jinja2]]'
- '[[Jinja2 - Dump all used classes]]'
- '[[Server Side Template Injection]]'
commands:
- '[[List Subclasses]]'
- '[[List Subclasses]]'
- '[[List Subclasses]]'
---

# Jinja2 Server Side Template Injection - Dump All Used Classes

## Summary

Jinja2 is a popular templating engine for Python web applications. It allows developers to dynamically generate HTML, XML, and other markup languages. However, server-side template injection (SSTI) vulnerabilities in Jinja2 can allow attackers to execute arbitrary code on the server. This specific 

## Description

# Description

Jinja2 is a popular templating engine for Python web applications. It allows developers to dynamically generate HTML, XML, and other markup languages. However, server-side template injection (SSTI) vulnerabilities in Jinja2 can allow attackers to execute arbitrary code on the server. This specific procedure is focused on dumping all used classes in order to gather information about the target system. By executing this procedure, an attacker can learn more about the system architecture and potentially identify additional vulnerabilities. Technical details of the SSTI vulnerability in Jinja2 can be found in the Mitre ATT&CK framework. From a business perspective, this procedure can be used by attackers to gain unauthorized access to sensitive information or to compromise the availability and integrity of the target system.

 

## Requirements

1. Access to a vulnerable Jinja2 web application

1. Python interpreter

 

## Defense

1. Always keep Jinja2 and other web frameworks up to date with the latest patches and security fixes

1. Implement input validation and sanitization to prevent injection attacks

1. Use a web application firewall (WAF) to detect and block SSTI attacks

 

## Objectives

1. Gather information about the target system

1. Identify potential vulnerabilities

1. Compromise the target system

 

# Instructions

1. This command lists all the subclasses of a given class in Python.

 



**Code**: [[{{ [].class.base.subclasses() }}
{{''.class.mro()[]]



> The command uses the `subclasses()` method to list all the subclasses of a given class. The first line of the command lists the subclasses of the `object` class, the second line lists the subclasses of the `str` class and the third line lists the subclasses of the `type` class. This command can be useful in understanding the class hierarchy of a Python program.



**Command** ([[List Subclasses]]):

```bash
{{ [].class.base.subclasses() }}
```





**Command** ([[List Subclasses]]):

```bash
{{''.class.mro()[1].subclasses()}}
```





**Command** ([[List Subclasses]]):

```bash
{{ ''.__class__.__mro__[2].__subclasses__() }}
```



2. To access global variables, use the '__globals__' keyword.

 



**Code**: [[__globals__]]



> Global variables are variables that are defined outside of a function and can be accessed from any part of the code. To access global variables in JSON, use the '__globals__' keyword followed by the name of the variable. For example, '__globals__.myGlobalVar'.

3. The built-in functions and operators are a set of functions and operators that are always available in Python. They do not require any import statements or external libraries. Some examples of built-in functions include `print()`, `len()`, and `range()`. Some examples of built-in operators include `+` for addition, `-` for subtraction, `*` for multiplication, and `/` for division.

 



**Code**: [[__builtins__]]



> The `__builtins__` variable is a module that contains all of the built-in functions and operators. It can be used to access these functions and operators directly without having to import them from a separate module. The `and` operator is a logical operator that returns `True` if both operands are true, and `False` otherwise. It can be used to combine multiple conditions in an `if` statement or a `while` loop.

4. The 'data' field contains a dictionary of all the built-in functions in Python. These functions are available for use without the need for import statements. 

 



**Code**: [[{{ self.__init__.__globals__.__builtins__ }}]]



> The 'data' field is a dictionary that contains all the built-in functions in Python. These functions are available for use in any Python script without the need for import statements. Some examples of these functions include print(), len(), range(), and input(). These functions can be used to perform a wide range of tasks, from printing output to the console to manipulating data structures like lists and dictionaries. To use a built-in function, simply call it by name and pass in any required arguments.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Data from Local System|T1005 - Data from Local System]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[List Subclasses]]
- [[List Subclasses]]
- [[List Subclasses]]

## Tags

- [[Jinja2]]
- [[Jinja2 - Dump all used classes]]
- [[Server Side Template Injection]]


