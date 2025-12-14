---
id: proc-insightly-xss-trigger-001
tags:
  - xss-execution
  - cookie-theft
  - session-hijack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Pass the Hash]]'
updated_at: '2025-12-13T23:55:20.889Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Pass the Hash]]'
---
# Trigger-XSS-via-Notification-View

## Summary

This procedure simulates a victim viewing the notification list, causing the stored XSS payload to execute and steal session cookies for hijacking.

## Description

Accessing the email notification list renders the unsanitized subject, loading the <img> tag which fails (src="X") and triggers onerror. The JavaScript then exfiltrates cookies, potentially to an attacker server, allowing session takeover.

## Requirements

1. Victim account in the shared group
2. Malicious email already injected
3. Browser with JS enabled (standard for CRM users)

## Defense

Defensive measures and detection strategies:

- Escape HTML in notification renders
- Monitor for anomalous JS execution in browser consoles
- Implement session cookie HttpOnly and Secure flags

## Objectives

1. Execute payload in victim's context
2. Capture and exfiltrate authentication cookies
3. Achieve unauthorized access via hijacked session

## Instructions

### Step 1: Log In as Victim

**Context**: Switch to the secondary account.

Log in to Insightly with the invited account credentials.

### Step 2: Access Notification List

**Context**: Load the page containing the stored payload.

Navigate to https://crm.na1.insightly.com/list/Email/.

### Step 3: Trigger Execution

**Context**: Force render of the malicious subject.

Refresh the page or scroll to load notifications. Observe JS execution in developer tools (F12 > Console) for cookie transmission.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Pass the Hash]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[Collection]]

