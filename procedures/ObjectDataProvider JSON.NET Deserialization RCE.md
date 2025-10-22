---
id: 8d4170e9-54a5-4fbd-8587-4c61685d3f8c
name: ObjectDataProvider JSON.NET Deserialization RCE
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.181914+00:00'
updated_at: '2023-04-06T03:55:59.192452+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Regsvr32|T1117 - Regsvr32]]'
- '[[Server Software Component|T1505 - Server Software Component]]'
sub_techniques:
- '[[Web Shell|T1505.003 - Web Shell]]'
tags:
- '[[Formatters]]'
- '[[JSON.NET]]'
- '[[.NET Serialization]]'
---

# ObjectDataProvider JSON.NET Deserialization RCE

## Summary

ObjectDataProvider is a class in the .NET framework that allows developers to create objects that can be used as a binding source for a variety of UI elements. JSON.NET is a popular third-party library for serializing and deserializing JSON data in .NET applications. This technique abuses the deser

## Description

# Description

ObjectDataProvider is a class in the .NET framework that allows developers to create objects that can be used as a binding source for a variety of UI elements. JSON.NET is a popular third-party library for serializing and deserializing JSON data in .NET applications. This technique abuses the deserialization functionality of JSON.NET to execute arbitrary code on a target system. An attacker can craft a malicious JSON payload that exploits the ObjectDataProvider class to execute a command on the target system. Successful exploitation of this vulnerability can lead to remote code execution on the target system, allowing an attacker to take complete control of the system.

## Requirements

1. Access to a system running a vulnerable version of JSON.NET

1. Ability to craft a malicious JSON payload

1. Ability to deliver the payload to the target system

## Defense

1. Ensure that all systems running JSON.NET are updated to the latest version

1. Implement strict input validation to prevent malicious JSON payloads from being processed

1. Consider using alternative serialization libraries that are not vulnerable to this attack

## Objectives

1. Execute arbitrary code on the target system

1. Gain remote access to the target system

1. Maintain persistence on the target system

# Instructions

1. Execute the following command:

**Code**: [[.\ysoserial.exe -f Json.Net -g ObjectDataProvider ]]

> This command uses the ysoserial tool to generate a malicious JSON payload that exploits the ObjectDataProvider class in JSON.NET to execute the calc.exe process on the target system. The payload is then delivered to the target system where it is deserialized by the vulnerable JSON.NET library, resulting in the execution of the calc.exe process.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Regsvr32|T1117 - Regsvr32]]
- [[Server Software Component|T1505 - Server Software Component]]

### Sub-Techniques

- [[Web Shell|T1505.003 - Web Shell]]

## Tags

- [[Formatters]]
- [[JSON.NET]]
- [[.NET Serialization]]
