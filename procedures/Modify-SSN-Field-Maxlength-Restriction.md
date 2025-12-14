---
tags:
  - input-bypass
  - client-side-manipulation
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.932Z'
sub_techniques: []
id: 16d2d479-b720-4c20-8d38-0ae719955c4d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-SSN-Field-Maxlength-Restriction

## Summary

This procedure uses browser developer tools to alter the client-side maxlength attribute on the SSN input field, enabling the entry of SQL injection payloads longer than the intended 9 characters.

## Description

The web form enforces a maxlength of 9 on the SSN field to limit input to standard Social Security Number format. By inspecting the HTML element and editing the attribute, attackers can inject payloads like ' OR '1'='1. This bypasses front-end validation, allowing backend SQL execution. Prerequisites include the page loaded in a browser with dev tools enabled.

## Requirements

1. Browser with developer tools (F12 key)
2. Target page loaded
3. Basic HTML knowledge

## Defense

Defensive measures and detection strategies:

- Server-side validation independent of client-side limits
- Monitor for tampered requests via integrity checks or CSP

## Objectives

1. Remove input length restrictions
2. Enable payload injection
3. Facilitate authentication bypass

## Instructions

### Step 1: Inspect SSN Field

**Context**: Right-click the SSN input and inspect to access the HTML element.

No command; browser action:

```plaintext
Right-click SSN field > Inspect Element
```

> Locate the <input> tag for SSN, e.g., <input type="text" maxlength="9" name="SSN">

### Step 2: Edit Maxlength Attribute

**Context**: Change the maxlength to a high value to accept longer inputs.

Browser dev tools edit:

```plaintext
Edit maxlength from "9" to "9999"
```

> Save changes; the field now accepts extended input. Test by typing a long string.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[input-bypass]]
- [[client-side-manipulation]]
