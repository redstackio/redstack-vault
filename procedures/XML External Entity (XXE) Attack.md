---
id: 27139b17-6fcd-4c56-9e98-8aee9d66d562
name: XML External Entity (XXE) Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.946505+00:00'
updated_at: '2023-04-10T20:24:41.930652+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[XML External Entity]]'
commands:
- '[[Define ENTITY]]'
---

# XML External Entity (XXE) Attack

## Summary

An XML External Entity (XXE) attack is a type of attack against an application that parses XML input. The attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This can result in disclosure of confidential data, denial of service, 

## Description

# Description

An XML External Entity (XXE) attack is a type of attack against an application that parses XML input. The attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This can result in disclosure of confidential data, denial of service, server side request forgery, or even remote code execution. XXE attacks are most commonly used against web applications, but can also be used against other types of applications that process XML input.

To execute an XXE attack, an attacker needs to send specially crafted XML input to the application. The XML input contains a reference to an external entity that the attacker controls. When the application processes the XML input, it will try to resolve the external entity, which can result in the attacker gaining access to sensitive data or executing arbitrary code on the server.

Business value: An attacker can use an XXE attack to gain access to sensitive data, such as passwords or customer information, or to execute arbitrary code on the server. This can result in financial loss, reputational damage, and legal liability for the organization.

## Requirements

1. Access to the application that processes XML input

1. Knowledge of the XML parser used by the application

1. Ability to send specially crafted XML input to the application

## Defense

1. Implement input validation and sanitization to prevent external entities from being processed by the XML parser

1. Disable external entity processing in the XML parser configuration

1. Use a secure XML parser that does not support external entities by default

## Objectives

1. To gain access to sensitive data

1. To execute arbitrary code on the server

# Instructions

1. Define an entity with a given name and value.

**Code**: [[&lt;!ENTITY entity_name &quot;entity_value&quot;&g]]

> This command is used to define an entity in an XML document. The entity name is given as 'entity_name' and the entity value is given as 'entity_value'. The entity value can be any valid XML content, including other entities, text, or markup. Once defined, the entity can be referenced using its name in the XML document.

**Command** ([[Define ENTITY]]):

```bash
&lt;!ENTITY entity_name &quot;entity_value&quot;&gt;
```

2. To declare an external entity, use the following syntax:

<!ENTITY entity_name SYSTEM "file_path">

**Code**: [[SYSTEM]]

> Here, entity_name is the name of the entity, SYSTEM is the type of the entity, and file_path is the path to the file containing the entity's content. This command is used to create an entity that can be referenced within an XML document but is defined outside of it.

3. To define an XML entity, use the ENTITY keyword followed by the entity name and its value. The SYSTEM keyword is used to specify the location of the entity value file.

**Code**: [[&lt;!ENTITY entity_name SYSTEM &quot;entity_value&]]

> The ENTITY keyword is used in Document Type Definition (DTD) files to define an entity. An entity is a piece of text that can be referenced within an XML document. The value of an entity can be a string of characters or a reference to an external file. The SYSTEM keyword is used to specify the location of the external file that contains the entity value.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Define ENTITY]]

## Tags

- [[XML External Entity]]
