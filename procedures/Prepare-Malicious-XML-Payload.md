---
tags:
  - xxe
  - payload-crafting
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Java
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: cd413307-5e4f-4275-85bc-9a7e734099d0
created_at: '2025-12-13T09:00:27.236Z'
updated_at: '2025-12-13T09:00:27.236Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare Malicious XML Payload

## Summary

This procedure involves crafting a malicious XML payload with recursive entity definitions to exploit XML entity expansion vulnerabilities, specifically the Billion Laughs Attack, in systems like Pippo JAXB engine.

## Description

The attack targets XML parsers that allow DTD processing, causing exponential memory usage through nested entity references. This is applicable in Java environments where user-provided XML is parsed without disabling DTD support.

## Requirements

1. Text editor to create XML file
2. Knowledge of XML DTD entity syntax
3. Access to the target Java application for testing

## Defense

Defensive measures and detection strategies:

- Disable DTD support in XML parsers (e.g., set XMLInputFactory.SUPPORT_DTD to false)
- Monitor for unusual memory spikes in JVM processes

## Objectives

1. Create a payload that triggers recursive expansion
2. Ensure compatibility with the target parser
3. Achieve DoS potential

## Instructions

### Step 1: Define Recursive Entities

**Context**: Build entities that reference each other exponentially, such as PERSON1 referencing itself multiple times.

Create the XML with DTD like: <!ENTITY person1 "lol"><!ENTITY person2 "&person1;&person1;"> up to person9.

> This sets up the billion laughs expansion.

### Step 2: Save as Resource File

**Context**: Prepare the file for loading in the Java client.

Save the XML content to a file named malicious.xml.

> Ensure it's accessible as a classpath resource.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[payload-crafting]]
