---
id: p2b3c4d5-e6f7-8901-bcde-f23456789012
name: Configure-App-in-Settings
tags:
  - django
  - configuration
type: procedure
tools:
  - '[[tools/manage-py]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.989Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-App-in-Settings

## Summary

Registers the newly created app in Django's settings to make it available for models and commands.

## Description

Django requires apps to be listed in INSTALLED_APPS for proper recognition. This step integrates the 'webapp' into the project, allowing model migrations and custom commands to function, setting the stage for the vulnerable Q object usage.

## Requirements

1. Existing Django project from previous setup
2. Text editor for settings.py
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Review INSTALLED_APPS for unauthorized or vulnerable apps
- Use linters to validate settings syntax

## Objectives

1. Enable app functionality in the project
2. Prepare for model and command development
3. Avoid runtime errors during execution

## Instructions

### Step 1: Edit Settings File

**Context**: Manually add the app to the configuration.

**Command** (Manual Edit):
No command; edit sqli/settings.py.

> Locate INSTALLED_APPS = [...] and append 'webapp'. Expected output: Updated list like INSTALLED_APPS = ['django.contrib.admin', ..., 'webapp'].

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/manage-py]]

## Tags

- django
- configuration
