---
tags:
  - xss
  - dom-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:31.522Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 3b7afa33-9fc1-4a72-9e24-a2510c0ede07
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-XSS-Payload-into-VK-Server-Name

## Summary

This procedure injects a DOM-based XSS payload into the server name field during VK group server creation, exploiting lack of sanitization to embed executable JavaScript that persists until triggered.

## Description

In VK.com's group management, the server name field accepts user input with character limits but fails to sanitize HTML tags or JavaScript, allowing DOM-based XSS. The payload is stored and reflected unsafely during actions like deletion, executing in the viewer's browser context. This is ideal for targeting subsequent admins in ownership transfer scenarios, enabling session theft or unauthorized actions.

## Requirements

1. Valid VK account with group admin privileges
2. Access to group server creation feature
3. Web browser for input and testing

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input sanitization using libraries like DOMPurify
- Encode output in DOM contexts to prevent script execution
- Monitor for unusual server name content via admin audits

## Objectives

1. Persist malicious JavaScript in group server metadata
2. Bypass character limits with compact payloads
3. Set up for execution in admin browser sessions

## Instructions

### Step 1: Access Group Server Creation

**Context**: Log in and navigate to the vulnerable feature to prepare injection.

Log in to VK.com, go to your group's management page, and select the "Servers" section. Click to create a new server.

### Step 2: Enter XSS Payload

**Context**: Input a payload that evades basic checks but executes on reflection.

In the server name field, enter a payload like `<img src=x onerror=alert(document.domain)>` or `<svg onload=alert(document.cookie)>`. These are compact to fit limits and trigger on DOM parsing. Submit to create the server.

### Step 3: Verify Persistence

**Context**: Confirm the payload is stored without alteration.

View the server list; the name should display the tag intact. Use browser dev tools to inspect if it's reflected in HTML without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[dom-xss]]
