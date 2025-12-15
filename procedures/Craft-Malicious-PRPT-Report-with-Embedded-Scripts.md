---
tags:
  - rce
  - prpt
  - bsh
  - javascript
  - java
type: procedure
tools:
  - '[[tools/Pentaho-Report-Designer]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:54.330Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 13ca2764-f59f-430e-acc7-5e89cae3871d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-PRPT-Report-with-Embedded-Scripts

## Summary

This procedure uses Pentaho Report Designer to create a PRPT report file embedding malicious BeanShell, JavaScript, or Java scripts, which can execute arbitrary code when the report is rendered on the server.

## Description

PRPT files are report archives in Pentaho that support scripting languages without proper validation. By embedding code like BeanShell for server-side execution (e.g., Runtime.exec()), attackers can achieve RCE. This targets the report designer's flexibility, assuming access to the tool and knowledge of Pentaho's scripting integration.

## Requirements

1. Pentaho Report Designer installed
2. Basic knowledge of BeanShell, JavaScript, or Java scripting
3. Target Pentaho BI Server version vulnerable to script execution

## Defense

Defensive measures and detection strategies:

- Disable scripting in report rendering or enforce sandboxing
- Validate uploaded reports for embedded code before execution
- Scan PRPT files for suspicious script patterns using antivirus or custom tools
- Restrict report upload to trusted users only

## Objectives

1. Embed executable scripts in a PRPT file
2. Ensure compatibility with Pentaho's report engine
3. Prepare for upload to trigger RCE

## Instructions

### Step 1: Launch Pentaho Report Designer

**Context**: Open the tool to start creating a new report.

Install and launch Pentaho Report Designer from its official download.

### Step 2: Design Report with Embedded Scripts

**Context**: Add elements that incorporate malicious scripts for code execution.

Create a new report, add a formula or attribute field, and embed script such as BeanShell: import java.lang.Runtime; Runtime.getRuntime().exec('malicious_command'). Save as .prpt.

> Preview the report to verify script integration without errors. The file is now ready for upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Pentaho-Report-Designer]]

## Tags

- [[rce]]
- [[prpt]]
- [[bsh]]
- [[JavaScript]]
- [[java]]
