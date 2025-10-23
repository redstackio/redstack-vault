---
id: 5d8b8578-30fd-48e8-81b0-e78712331cc4
name: Error Based XXE Injection Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.337325+00:00'
updated_at: '2023-04-10T20:24:40.335472+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
tags:
- '[[Exploiting Error Based XXE]]'
- '[[XML External Entity]]'
---

# Error Based XXE Injection Attack

## Summary

Error-based XXE injection is a type of attack that exploits the way XML parsers handle external entities. An attacker can inject specially crafted XML data that causes the parser to disclose sensitive information or perform unintended actions. This attack is called 'error-based' because it relies o

## Description

# Description

Error-based XXE injection is a type of attack that exploits the way XML parsers handle external entities. An attacker can inject specially crafted XML data that causes the parser to disclose sensitive information or perform unintended actions. This attack is called 'error-based' because it relies on the parser generating an error message that includes the sensitive data.

In technical terms, an attacker can use an XXE injection attack to reference an external entity that contains sensitive data, such as local files, network resources, or system configuration files. When the parser encounters the reference, it will attempt to retrieve the entity and process its contents. If the entity is not accessible, the parser will generate an error message that may include the sensitive data. This attack can be used to perform reconnaissance, escalate privileges, or execute arbitrary code.

The business value of this attack lies in its ability to extract sensitive information from a target system, which can be used for further attacks, such as social engineering, phishing, or password cracking.

 

## Requirements

1. Access to the target system

1. Knowledge of the target XML parser

1. Ability to inject XML data

 

## Defense

1. Use input validation and sanitization to prevent XXE injection attacks

1. Disable external entity parsing in XML parsers

1. Use XML parsers that have built-in protection against XXE injection attacks

 

## Objectives

1. Extract sensitive information from a target system

1. Perform reconnaissance

1. Escalate privileges

1. Execute arbitrary code

 

# Instructions

1. This command is used to execute an XXE injection attack on a vulnerable application. The payload used in the 'data' field can be modified to suit the specific application being targeted. The 'DOCTYPE' declaration in the payload is used to define the structure of the XML document. The 'ENTITY' declaration can be used to define entities that can be referenced within the XML document. An attacker can use this vulnerability to read local files, execute arbitrary code, and perform other malicious actions.

 



**Code**: [[<?xml version="1.0" ?>
<!DOCTYPE message [
    <!E]]



> The 'data' field contains the payload used to trigger the XXE vulnerability. The 'lang' field specifies the language used in the payload, which in this case is XML. The 'text' field provides additional information about the payload. The 'instruction' field provides instructions on how to use this command, including how to modify the payload for a specific application. The 'explain' field provides a detailed explanation of what the command does and how it can be used by an attacker.

2. This command is used to exploit a file inclusion vulnerability in an XML parser. The '%file' parameter is used to specify the file to be included. The '%eval' parameter is used to define an entity that will evaluate the '%error' parameter. The '%error' parameter is used to specify the file that will be evaluated. In this case, it is set to 'file:///nonexistent/%file;', which will cause an error if the specified file cannot be found. By exploiting this vulnerability, an attacker can potentially gain access to sensitive files on the system.

 



**Code**: [[<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENT]]



> The '%file' parameter specifies the file to be included. The '%eval' parameter defines an entity that will evaluate the '%error' parameter. The '%error' parameter specifies the file that will be evaluated. In this case, it is set to 'file:///nonexistent/%file;', which will cause an error if the specified file cannot be found. By exploiting this vulnerability, an attacker can potentially gain access to sensitive files on the system.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

## Tags

- [[Exploiting Error Based XXE]]
- [[XML External Entity]]


