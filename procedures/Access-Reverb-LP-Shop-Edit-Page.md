---
tags:
  - xss
  - web
  - access
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
updated_at: '2025-12-14T03:46:31.368Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 38f9f6cc-211e-44ab-8034-79d10f2cb4bf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Reverb LP Shop Edit Page

## Summary

This procedure outlines navigating to the Reverb LP shop edit interface, a prerequisite for injecting payloads into the vulnerable shop name field.

## Description

In the context of exploiting a stored XSS vulnerability on Reverb.com, this step involves logging into an account with shop privileges and accessing the dedicated edit page. The page allows modification of shop details, including the name, which is not properly sanitized. Expected outcome is reaching the editable form without authentication barriers beyond standard login.

## Requirements

1. Valid Reverb.com account with LP shop setup
2. Web browser with cookies enabled
3. Internet access to reverb.com

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit shop editing to verified owners
- Monitor for unusual login patterns from shop edit endpoints

## Objectives

1. Gain access to the shop name input interface
2. Verify edit permissions
3. Prepare for payload injection

## Instructions

### Step 1: Log In and Navigate

**Context**: Authenticate and directly access the edit URL to load the form.

No specific command; use browser navigation:

Visit `https://reverb.com/my/lp_shop/edit` after logging in.

> This loads the shop editing interface. Expected output: Form with shop name field displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[access]]
