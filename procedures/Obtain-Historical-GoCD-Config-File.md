---
id: proc-uuid-2
tags:
  - gocd
  - config
  - xml
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.754Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Obtain Historical GoCD Config File

## Summary

This procedure retrieves the initial or historical cruise-config.xml file from GoCD, which serves as a nearly-empty placeholder for use in overwriting the live configuration during a CSRF attack.

## Description

GoCD installations generate a default cruise-config.xml upon setup, containing minimal elements. Attackers obtain this to craft a payload that resets or modifies the config without breaking the server. This can be from official docs, a fresh install, or backups. The file is XML-based, and modifications allow injecting malicious pipelines or credentials. Prerequisites: Access to GoCD install resources; outcomes: A valid XML payload ready for embedding in HTML forms.

## Requirements

1. GoCD installation documentation or a test environment
2. Text editor for XML validation
3. Basic understanding of GoCD configuration schema

## Defense

Defensive measures and detection strategies:

- Regularly backup and version control config files
- Restrict access to config endpoints to authenticated sessions only
- Audit config changes via logging

## Objectives

1. Acquire the default empty config XML
2. Validate its structure for compatibility
3. Prepare it as a base for malicious modifications

## Instructions

### Step 1: Locate Default Config

**Context**: Find the initial config from GoCD resources.

Download from GoCD GitHub repo or install a fresh instance and extract /go-config/cruise-config.xml.

> Expected: XML file with basic <cruise> root and empty <pipelines> section.

### Step 2: Validate XML Syntax

**Context**: Ensure the file is well-formed for upload.

Use an XML validator tool or editor to check for errors.

> Expected: No syntax errors; file parses correctly.

### Step 3: Customize if Needed

**Context**: Modify to include attacker-desired elements, like new admin users.

Edit <server> or <security> sections to add persistence mechanisms.

> Expected: Updated XML that, when applied, grants control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gocd]]
- [[config-file]]
- [[xml-payload]]
