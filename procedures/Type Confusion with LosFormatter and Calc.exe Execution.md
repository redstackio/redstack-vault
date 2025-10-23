---
id: 4a70e820-fcc1-4391-a747-009f808103d8
name: Type Confusion with LosFormatter and Calc.exe Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.157663+00:00'
updated_at: '2023-04-06T03:55:59.171618+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Server Software Component|T1505 - Server Software Component]]'
tags:
- '[[Formatters]]'
- '[[LosFormatter]]'
- '[[.NET Serialization]]'
---

# Type Confusion with LosFormatter and Calc.exe Execution

## Summary

This technique abuses the .NET LosFormatter class to deserialize a malicious payload, which in this case is a TypeConfuseDelegate object that tricks the .NET framework into executing arbitrary code. In this example, the payload is set to execute calc.exe, but it could be any other executable or scr

## Description

# Description

This technique abuses the .NET LosFormatter class to deserialize a malicious payload, which in this case is a TypeConfuseDelegate object that tricks the .NET framework into executing arbitrary code. In this example, the payload is set to execute calc.exe, but it could be any other executable or script. This technique is useful for an attacker to gain access to a system and execute code remotely, potentially leading to further compromise of the system.

 

## Requirements

1. Access to the target system

1. Ability to run the ysoserial.exe tool

 

## Defense

1. Ensure that all .NET components are up to date and patched

1. Implement proper input validation and serialization/deserialization controls

1. Restrict access to the ysoserial.exe tool and other utilities that can generate malicious payloads

 

## Objectives

1. Execute arbitrary code on the target system

 

# Instructions

1. Run the following command to generate the payload:

 



**Code**: [[.\ysoserial.exe -f LosFormatter -g TypeConfuseDele]]



> This command uses the ysoserial.exe tool to generate a payload that will execute calc.exe when deserialized using the LosFormatter class. The payload is encoded in base64 format and can be used in an exploit.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Server Software Component|T1505 - Server Software Component]]

## Tags

- [[Formatters]]
- [[LosFormatter]]
- [[.NET Serialization]]


