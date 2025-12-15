---
tags:
  - csp-misconfig
  - template-creation
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
updated_at: '2025-12-14T17:24:31.378Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 90e6b70e-c6d0-490e-9fa6-69a901c50fb6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Email-Template-in-Stripo-Editor

## Summary

This procedure initiates the attack by accessing Stripo's template editor to create a new HTML-based email template, setting the stage for iframe injection without triggering immediate sanitization.

## Description

In the context of exploiting Stripo's CSP misconfiguration, this step involves logging into the Stripo dashboard and starting a new template. The editor at https://my.stripo.email/cabinet/#/template-editor/... allows direct HTML editing, which is key for inserting malicious iframes. No special privileges are needed beyond a standard user account, and the process is straightforward for intermediate users familiar with web interfaces.

## Requirements

1. Valid Stripo account with access to the template editor
2. Web browser (e.g., Google Chrome)
3. Internet access to my.stripo.email

## Defense

Defensive measures and detection strategies:

- Implement strict HTML sanitization in editors to block iframe tags
- Monitor for unusual template creations with external embeds
- Educate users on risks of previewing untrusted templates

## Objectives

1. Access editable HTML content in the template
2. Prepare for payload insertion
3. Avoid detection during creation

## Instructions

### Step 1: Access Template Editor

**Context**: Log in and navigate to create a new template to open the HTML editor.

No specific command; use the web interface:

- Navigate to https://my.stripo.email/cabinet/#/template-editor/...
- Select 'New Template' and choose HTML mode

> This loads the editor where HTML can be directly edited.

### Step 2: Verify Editor Access

**Context**: Confirm the HTML input is available and CSP allows frame-src *.firebaseapp.com.

Inspect the page headers using browser dev tools (F12 > Network > Headers) to check CSP.

> Expected: frame-src includes *.firebaseapp.com, enabling later iframe loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csp-misconfig]]
- [[template-creation]]
