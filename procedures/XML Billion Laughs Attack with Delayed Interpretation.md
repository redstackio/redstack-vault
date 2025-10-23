---
id: e16fcd59-6c09-464c-8664-18bfa5f43dee
name: XML Billion Laughs Attack with Delayed Interpretation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.315383+00:00'
updated_at: '2023-04-10T20:24:38.336947+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[Endpoint Denial of Service|T1499 - Endpoint Denial of Service]]'
tags:
- '[[Exploiting XXE to perform a deny of service]]'
- '[[Parameters Laugh attack]]'
- '[[XML External Entity]]'
---

# XML Billion Laughs Attack with Delayed Interpretation

## Summary

The XML Billion Laughs Attack with Delayed Interpretation is a Denial of Service (DoS) attack that abuses the XML external entity expansion feature. An attacker can craft a malicious XML file that includes multiple levels of nested entities that expand to a large number of characters, overwhelming 

## Description

# Description

The XML Billion Laughs Attack with Delayed Interpretation is a Denial of Service (DoS) attack that abuses the XML external entity expansion feature. An attacker can craft a malicious XML file that includes multiple levels of nested entities that expand to a large number of characters, overwhelming the parser and causing it to crash. This attack can be used to disrupt the availability of a targeted system or service. The attack can be performed with a single request, but it can also be performed over multiple requests to evade rate limiting or other defenses. The attack can be executed remotely, without the need for authentication or network access.

From a technical perspective, the attack works by exploiting the XML external entity expansion feature, which allows an XML document to include external entities that are parsed and expanded by the XML parser. By including a malicious external entity that expands to a large number of characters, the attacker can cause the parser to consume excessive amounts of memory and CPU resources, eventually leading to a crash or DoS condition. The attack can be performed using a variety of XML parsing libraries and tools, including those used in web applications and web services.

From a business perspective, the attack can be used to disrupt the availability of a targeted system or service, leading to loss of revenue, reputation damage, or other negative impacts. The attack can also be used as a distraction or cover for other malicious activities, such as data theft or network intrusion.

 

## Requirements

1. Ability to craft a malicious XML file

1. Knowledge of the target system or service that uses XML parsing

1. Access to a tool or library that can parse XML files

 

## Defense

1. Implement input validation and sanitization to prevent malicious XML files from being parsed

1. Use XML parsing libraries and tools that have built-in protection against XXE attacks

1. Apply rate limiting or other defenses to prevent excessive resource consumption by a single request

 

## Objectives

1. Overwhelm the parser of the targeted system or service

1. Disrupt the availability of the targeted system or service

 

# Instructions

1. This command is used to launch a variant of the Billion Laughs attack on an XML parser. The attack uses delayed interpretation of parameter entities to consume excessive resources of the parser, causing a denial-of-service condition. 

 



**Code**: [[<!DOCTYPE r [
  <!ENTITY % pe_1 "<!---->">
  <!ENT]]



> The XML parser processes the DOCTYPE declaration and expands the parameter entities in the DTD. The %pe_4; parameter entity is defined as a recursive sequence of %pe_3; entities, which themselves are defined as recursive sequences of %pe_2; entities, and so on. The final expansion of %pe_4; results in an exponentially growing number of DOCTYPE declarations, leading to resource exhaustion and denial-of-service. This attack can be mitigated by disabling the expansion of external entities and by limiting the depth of entity expansion.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact|TA0040 - Impact]]

### Techniques

- [[Endpoint Denial of Service|T1499 - Endpoint Denial of Service]]

## Tags

- [[Exploiting XXE to perform a deny of service]]
- [[Parameters Laugh attack]]
- [[XML External Entity]]


