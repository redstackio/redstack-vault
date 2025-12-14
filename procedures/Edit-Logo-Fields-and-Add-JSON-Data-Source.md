---
id: proc-infogram-edit-logo-001
tags:
  - ssrf
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:18.599Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Edit-Logo-Fields-and-Add-JSON-Data-Source

## Summary

This procedure details entering the editing mode for logo fields in an Infogram project and initiating the addition of a JSON data source, setting up the SSRF exploitation vector.

## Description

The Infogram editing interface lacks validation on JSON inputs, allowing SSRF. This step prepares the input field for URLs that trigger server-side requests. Expected outcomes include access to the URL entry prompt, enabling port scanning tests.

## Requirements

1. Access to loaded project page
2. Edit permissions on the project
3. Web browser

## Defense

Defensive measures and detection strategies:

- Validate user permissions before edit access
- Log JSON source additions for anomaly detection
- Restrict edit interfaces to authenticated sessions

## Objectives

1. Activate project editing
2. Expose JSON input field
3. Prepare for SSRF payload injection

## Instructions

### Step 1: Initiate Edit Mode

**Context**: Click the edit option to enter the project customization interface.

No command; browser interaction:

```plaintext
Click 'Edit' button on project page
```

> The interface expands with customization options, including logo fields.

### Step 2: Select Logo and Add JSON

**Context**: Navigate to logo fields and choose to add a data source.

```plaintext
Select 'Logo Fields' > 'Add JSON Data Source'
```

> Input prompt for JSON URL appears, ready for exploitation.

**Expected Output**: JSON URL input field visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[web-exploit]]
