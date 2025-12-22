---
id: proc-938683-step2
tags:
  - setup
  - template-selection
  - editor-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.671Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Fill Campaign Fields and Select Blank Template

## Summary

This procedure completes the basic configuration of a lemlist email campaign by filling required fields and selecting a blank template, unlocking the Froala editor for payload injection in the next steps.

## Description

As part of the DOM-based XSS attack chain, this step ensures the email body editor is accessible without errors. It involves inputting minimal data to proceed to the composition area, where the blank template provides a clean slate for HTML manipulation. Prerequisites include an active campaign session.

## Requirements

1. Active lemlist campaign creation session from prior step
2. Test recipient list or dummy data for fields
3. Web browser session maintained

## Defense

Defensive measures and detection strategies:

- Validate input fields with client-side checks to prevent incomplete setups
- Log template selections for anomaly detection in campaign patterns

## Objectives

1. Configure campaign basics to access the editor
2. Load blank template without content restrictions
3. Prepare for code view injection

## Instructions

### Step 1: Input Campaign Details

**Context**: Fill mandatory fields to advance the workflow.

Enter a campaign name, select or create a recipient list, and configure any other required options like send schedule.

> Form validates and proceeds to email composition.

### Step 2: Choose Blank Template

**Context**: Select template to initialize the Froala editor.

In the email body section, choose the "Blank" template option to open the WYSIWYG editor in visual mode.

> Editor loads empty, ready for view switching.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- template-selection
