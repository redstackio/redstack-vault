---
tags:
  - web-access
  - authentication
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
updated_at: '2025-12-14T03:46:26.687Z'
sub_techniques: []
id: c901f64d-3317-43f0-9c62-ce9cd6430c67
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-TopCoder-Wiki-Edit-Mode

## Summary

This procedure outlines how to authenticate and navigate to the edit mode of a TopCoder wiki page, setting the stage for content manipulation in an XSS attack.

## Description

In the context of exploiting a stored XSS vulnerability, accessing the wiki editor requires an authenticated session with edit permissions. This step ensures the attacker can modify page content, such as injecting payloads into macros. The target environment is the TopCoder wiki platform, where pages are editable via specific URLs. Expected outcomes include loading the rich text or source editor without restrictions.

## Requirements

1. Valid TopCoder account with wiki edit permissions
2. Web browser supporting rich text editing (e.g., Firefox)
3. Network access to https://apps.topcoder.com/wiki/

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit wiki editing to trusted users
- Monitor edit logs for unusual content patterns or rapid changes
- Use client-side sanitization previews to detect potential XSS before saving

## Objectives

1. Establish authenticated access to the wiki editor
2. Load the target page in editable state
3. Prepare for payload insertion without triggering alerts

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to TopCoder and directly access the edit endpoint to bypass read-only views.

No specific command; perform via browser:

Navigate to https://apps.topcoder.com/wiki/pages/editpage.action?pageId=165871793 (replace pageId with target).

> This loads the editor if authenticated. Expected output: Editable page interface appears.

### Step 2: Verify Edit Access

**Context**: Confirm permissions by attempting a minor edit.

No specific command; interact with the UI to ensure the editor is functional.

> Success if content can be modified without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[authentication]]
