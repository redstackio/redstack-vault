---
id: 328bf236-8e6f-4fcc-9dba-1e24d0dd9649
name: YAML Deserialization in Ruby
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.524386+00:00'
updated_at: '2023-04-06T03:55:59.536702+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Scheduled Transfer|T1029 - Scheduled Transfer]]'
tags:
- '[[Ruby]]'
- '[[YAML Deserialization]]'
---

# YAML Deserialization in Ruby

## Summary

YAML is a data serialization language that is commonly used in Ruby applications. Attackers can abuse the deserialization process in Ruby YAML to execute arbitrary code. By crafting a malicious YAML file, an attacker can potentially execute code on the target system with the privileges of the appli

## Description

# Description

YAML is a data serialization language that is commonly used in Ruby applications. Attackers can abuse the deserialization process in Ruby YAML to execute arbitrary code. By crafting a malicious YAML file, an attacker can potentially execute code on the target system with the privileges of the application that parses the YAML file. This technique can be used to gain initial access to a system or to execute code on a targeted system.

When Ruby parses the YAML file, it creates Ruby objects based on the data in the file. If the YAML file contains a malicious Ruby object, the code within that object will be executed when the YAML file is parsed. This can lead to remote code execution or other types of attacks depending on the code executed.

 

## Requirements

1. Access to a vulnerable Ruby application

 

## Defense

1. Avoid using YAML to deserialize untrusted data

1. Implement input validation to ensure that only trusted data is deserialized

1. Use a secure YAML parser that is not vulnerable to deserialization attacks

 

## Objectives

1. Execute arbitrary code on a target system

1. Gain initial access to a system

 

# Instructions

1. Craft a YAML file that contains a malicious Ruby object

 



**Code**: [[ ---
 - !ruby/object:Gem::Installer
     i: x
 - !]]



> The data field contains an example of a malicious YAML file that could be used to execute arbitrary code on a target system. The file contains a Ruby object that will be executed when the YAML file is parsed. The attacker can modify this file to include their own Ruby code to execute on the target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Scheduled Transfer|T1029 - Scheduled Transfer]]

## Tags

- [[Ruby]]
- [[YAML Deserialization]]


