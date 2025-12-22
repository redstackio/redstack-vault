---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - execution
  - trigger
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
updated_at: '2025-12-14T03:15:46.773Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: Trigger-Stored-XSS-Payload-Execution
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Execution]], [[Collection]]
techniques: [[JavaScript]]
sub_techniques: []
tags: xss, execution, trigger
platforms: Web
commands: []
tools: []
---

# Trigger-Stored-XSS-Payload-Execution

## Summary

This procedure demonstrates how to trigger the stored XSS payload in Concrete CMS 5.7.2.1 by having a victim access the file manager's delete or properties pages, leading to JavaScript execution in their browser.

## Description

Once payloads are stored via upload or properties, they execute automatically when rendered in the DOM on interactive pages like delete confirmations or properties views. This affects any user with access to the file manager, enabling attacks such as session hijacking through cookie exfiltration. The vulnerability stems from output rendering without proper escaping.

## Requirements

1. A victim user account or simulated access
2. The malicious file already present in the file manager
3. Standard web access to the CMS

## Defense

Defensive measures and detection strategies:

- Escape all user-generated content before rendering in HTML
- Log and alert on JavaScript errors or unexpected script executions
- Implement role-based access to limit file manager visibility

## Objectives

1. Execute the stored payload in a victim context
2. Verify JavaScript control for data collection
3. Assess impact on session security

## Instructions

### Step 1: Simulate Victim Access

**Context**: Log in as or direct a victim to the file manager to interact with the malicious file.

Navigate to File Manager and search for the affected file.

> Ensure the victim has no knowledge of the payload to simulate real-world execution.

### Step 2: Open Triggering Page

**Context**: Load a page that renders the unsanitized filename or title, such as properties or delete.

Click 'Properties' or 'Delete' on the file; the payload executes on page load.

> Observe the alert (e.g., confirm(document.cookie)) to confirm execution and potential exfiltration.

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
- [[trigger]]
