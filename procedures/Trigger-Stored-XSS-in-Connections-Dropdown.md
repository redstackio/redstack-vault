---
id: 123e4567-e89b-12d3-a456-426614174004
name: Trigger-Stored-XSS-in-Connections-Dropdown
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.390Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - execution
  - web
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trigger-Stored-XSS-in-Connections-Dropdown

## Summary

This procedure executes the stored XSS payload by interacting with the vulnerable dropdown in KitCRM's connections page, leading to arbitrary JavaScript execution.

## Description

The dropdown renders the malicious Facebook page name without proper escaping, allowing the payload to break out of HTML attributes and execute when selected. This triggers the onerror event in the img tag, running alert(9). In a real attack, this could steal cookies or hijack sessions for any victim viewing the page.

## Requirements

1. Connected Facebook account with payload-reflected page
2. Visible dropdown with malicious option
3. Victim or test browser context

## Defense

Defensive measures and detection strategies:

- Enforce strict HTML escaping for all user/API-controlled data in UI
- Implement client-side validation and CSP to block unsafe scripts
- Monitor for unexpected JavaScript errors or alerts in browser logs

## Objectives

1. Execute injected JavaScript in the browser context
2. Demonstrate impact like alert or data exfiltration
3. Enable follow-on attacks such as session theft

## Instructions

### Step 1: Locate Malicious Option

**Context**: Identify the vulnerable dropdown element.

On the connections page, find the Facebook pages dropdown.

### Step 2: Interact to Execute

**Context**: Trigger the payload via user interaction.

Click the dropdown option for the malicious page name.

**Expected Output**: Alert(9) dialog appears, confirming XSS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[web]]
