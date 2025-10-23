---
id: edf1425c-4ba1-448d-b22b-2de67475201b
name: Server Side Template Injection - Expression Language EL Properties Information
  Disclosure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.974271+00:00'
updated_at: '2023-04-10T20:23:39.619654+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Software Discovery|T1518 - Software Discovery]]'
tags:
- '[[Expression Language EL]]'
- '[[Expression Language EL - Properties]]'
- '[[Server Side Template Injection]]'
---

# Server Side Template Injection - Expression Language EL Properties Information Disclosure

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject code into a server-side template, which is then executed on the server. In this specific scenario, the attacker can use Expression Language (EL) to disclose information about the server's Java classes, which 

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject code into a server-side template, which is then executed on the server. In this specific scenario, the attacker can use Expression Language (EL) to disclose information about the server's Java classes, which can be used to further exploit the system. EL is a simple language that allows you to access properties and methods of objects. By accessing the properties of Java classes, the attacker can gain valuable information about the server's configuration and potentially find other vulnerabilities to exploit. This technique can be used for reconnaissance purposes or to aid in further exploitation of the system.

Technical Explanation: The attacker can use the 'Java Class Information' command to inject EL code into a server-side template. This code will then be executed on the server, allowing the attacker to access the properties of Java classes. By accessing the properties of these classes, the attacker can gain valuable information about the server's configuration, such as the operating system, installed software, and other system information. This information can be used to further exploit the system.

Business Value: By gaining access to information about the server's Java classes, an attacker can gain valuable information about the system's configuration, which can be used to further exploit the system. This can lead to data theft, system compromise, and other negative consequences.

 

## Requirements

1. Access to a vulnerable server-side template

1. Ability to inject EL code

1. Knowledge of Java classes and properties

 

## Defense

1. Implement input validation on server-side templates to prevent injection attacks

1. Avoid using user input in server-side templates

1. Regularly update and patch software and systems to prevent known vulnerabilities

 

## Objectives

1. Discover information about the server's Java classes and configuration

1. Aid in further exploitation of the system

 

# Instructions

1. To get information about a Java class, use the following commands:
1. ${2.class} - displays the name of the class of the object
2. ${2.class.forName("java.lang.String")} - displays the name of the class with the specified name
3. ${''.getClass().forName('java.lang.Runtime').getMethods()[6].toString()} - displays the details of the getRuntime() method in the Runtime class

 



**Code**: [[${2.class}
${2.class.forName("java.lang.String")}
]]



> The first command returns the name of the class of the object. The second command returns the name of the class with the specified name. The third command returns the details of the getRuntime() method in the Runtime class. This method returns the runtime object associated with the current Java application.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Software Discovery|T1518 - Software Discovery]]

## Tags

- [[Expression Language EL]]
- [[Expression Language EL - Properties]]
- [[Server Side Template Injection]]


