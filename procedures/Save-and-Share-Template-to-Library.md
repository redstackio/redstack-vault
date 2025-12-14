---
tags:
  - persistence
  - sharing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:07.924Z'
sub_techniques: []
id: 228358bf-98f4-471a-a321-fbc1e01fcbc0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-and-Share-Template-to-Library

## Summary

This procedure saves the malicious template containing the XSS payload and shares it publicly via Drchrono's library, making it accessible to victims for execution.

## Description

After injecting the payload, saving persists it in the backend without sanitization. Sharing to the library generates a public URL, exposing the form to anyone, where the field name renders the XSS. This step bridges storage to execution, amplifying impact through public access.

## Requirements

1. Malicious template configured in the builder
2. Permissions to save and publish templates
3. Valid session to perform the save/share actions

## Defense

Defensive measures and detection strategies:

- Sanitize outputs during rendering of shared templates
- Require approval workflows for public sharing
- Monitor for high-volume shares from single accounts

## Objectives

1. Persist the payload in Drchrono's database
2. Generate a public URL for victim access
3. Ensure the shared form renders the vulnerable field

## Instructions

### Step 1: Save the Template

**Context**: Commit the changes to store the payload backend.

Click the 'Save' button in the form builder.

> Watch for success message; no errors should indicate payload acceptance.

### Step 2: Share to Public Library

**Context**: Expose the template publicly to enable XSS trigger.

Select 'Share to Library' or 'Publish', confirming public access.

> Copy the generated URL, e.g., https://www.drchrono.com/medical-forms/1460752/aaabbbcccdddeee.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- template-sharing
- public-exposure
