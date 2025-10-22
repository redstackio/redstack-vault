---
id: c840a79f-f7a8-4521-9825-71077ff9ecc7
name: POP Gadget .NET Serialization
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.228269+00:00'
updated_at: '2023-04-06T03:55:59.238309+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Application Shimming|T1138 - Application Shimming]]'
- '[[Code Signing|T1116 - Code Signing]]'
- '[[Component Object Model Hijacking|T1122 - Component Object Model Hijacking]]'
tags:
- '[[.NET Serialization]]'
- '[[POP Gadgets]]'
---

# POP Gadget .NET Serialization

## Summary

POP gadgets are a type of gadget chain that can be used to exploit vulnerabilities in .NET serialization. This technique involves manipulating the serialized data to create a chain of objects that results in the execution of arbitrary code. The ExpandedWrapper class and the AssemblyInstaller class 

## Description

# Description

POP gadgets are a type of gadget chain that can be used to exploit vulnerabilities in .NET serialization. This technique involves manipulating the serialized data to create a chain of objects that results in the execution of arbitrary code. The ExpandedWrapper class and the AssemblyInstaller class are two examples of .NET classes that can be used in POP gadget attacks. By exploiting vulnerabilities in these classes, an attacker can execute code in the context of the application or system that is deserializing the data. This technique can be used to bypass security controls and gain access to sensitive data or systems.

## Requirements

1. Access to a vulnerable .NET application or system

1. Knowledge of the vulnerability being exploited

1. Ability to craft malicious serialized data

## Defense

1. Implement input validation and filtering to prevent the deserialization of untrusted data

1. Use a secure serialization format, such as JSON, instead of .NET serialization

1. Apply security updates and patches to .NET libraries and applications

## Objectives

1. Execute arbitrary code in the context of the deserializing application or system

1. Bypass security controls

# Instructions

1. Create an instance of the ExpandedWrapper class

**Code**: [[ExpandedWrapper<Process, ObjectDataProvider> myExp]]

> The ExpandedWrapper class is a .NET class that can be used to create a POP gadget chain. The class takes two generic types as parameters, which specify the types of the objects that will be used in the chain. In this example, the types are Process and ObjectDataProvider.

2. Create an instance of the AssemblyInstaller class

**Code**: [[// System.Configuration.Install.AssemblyInstaller
]]

> The AssemblyInstaller class is a .NET class that can be used to create a POP gadget chain. The class has a vulnerability that can be exploited by passing a specially crafted serialized object to the constructor. In this example, the set_Path method is used to set the path to the assembly that will be loaded. By passing a path to a malicious assembly, an attacker can execute arbitrary code in the context of the application or system that is deserializing the data.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Application Shimming|T1138 - Application Shimming]]
- [[Code Signing|T1116 - Code Signing]]
- [[Component Object Model Hijacking|T1122 - Component Object Model Hijacking]]

## Tags

- [[.NET Serialization]]
- [[POP Gadgets]]
