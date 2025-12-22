---
id: p-trigger-xss-instacart-preview
tags:
  - xss-execution
  - session-theft
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
  - '[[Clipboard Data]]'
updated_at: '2025-12-14T03:47:23.470Z'
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
  - '[[Clipboard Data]]'
---
# Trigger-XSS-via-List-Preview

## Summary

This procedure triggers the execution of the stored XSS payload by accessing the preview URL of the injected shopping list, resulting in arbitrary JavaScript execution that alerts the document domain and demonstrates potential for stealing session cookies or performing user actions.

## Description

The preview endpoint at https://www.instacart.com/lists/{id}?preview=true renders the list name without escaping, executing the injected script in the context of the viewing user's session. This allows attackers to exfiltrate data like cookies (e.g., via additional payloads sending to external servers) or manipulate the DOM on behalf of the victim.

## Requirements

1. List ID from the injected list (e.g., izy0w6Q)
2. Authenticated session (for realistic testing)
3. Web browser to observe execution

## Defense

Defensive measures and detection strategies:

- Output encoding for all rendered user-generated content
- Monitor for JavaScript errors or unexpected alerts in client logs
- Deploy browser-based XSS auditors or extensions to detect injections

## Objectives

1. Execute the stored payload
2. Confirm JavaScript runs in victim context
3. Highlight risks like data exfiltration

## Instructions

### Step 1: Obtain Preview URL

**Context**: Identify the URL for the created list's preview.

From the lists page, note the list ID or construct the URL as https://www.instacart.com/lists/{list-id}?preview=true.

> Example: https://www.instacart.com/lists/izy0w6Q?preview=true. Expected output: URL ready for access.

### Step 2: Access Preview and Observe Execution

**Context**: Load the preview to trigger the script.

Navigate to the preview URL in the browser.

> The payload executes. Expected output: Alert box shows 'www.instacart.com'; inspect console for script details.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Clipboard Data]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
