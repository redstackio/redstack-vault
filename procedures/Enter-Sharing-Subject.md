---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - web
  - social-engineering
  - adobe
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:53.010Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enter Sharing Subject

## Summary

This procedure adds a subject line to the file sharing request in Adobe Acrobat, making the malicious link appear legitimate to entice victims to click and trigger the XSS.

## Description

In the XSS exploitation chain, entering a subject like 'Shared Document' in the form at https://cloud.acrobat.com/send helps disguise the attack. This step occurs after file selection and anonymous setup. It ensures the shared email or link preview looks innocuous. Outcomes include the subject being stored with the payload for rendering.

## Requirements

1. File selected and anonymous option enabled
2. Active form session on the send page

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all form inputs, including subjects
- Monitor for suspicious subject patterns in logs

## Objectives

1. Add benign metadata to the sharing request
2. Enhance phishing realism for victim engagement
3. Complete form setup before payload injection

## Instructions

### Step 1: Locate Subject Field

**Context**: Find the input for the sharing title.

Look for the 'Subject' or 'Email Subject' field on the form.

> It is typically near the top of the sharing configuration.

### Step 2: Input Neutral Text

**Context**: Enter text that mimics normal sharing.

Type 'Shared Document for Review' into the subject field.

> The field updates to show the text, with no validation errors for benign input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- social-engineering
