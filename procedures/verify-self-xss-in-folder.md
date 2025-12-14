---
id: proc-imgur-verify-xss
tags:
  - xss
  - self-xss
  - verification
type: procedure
tools:
  - '[[tools/browser-based-exploitation]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/xss-payload-folder-name]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:57.799Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify Self-XSS in Folder

## Summary

This procedure manually tests the stored self-XSS vulnerability in Imgur's favorites folder naming by creating a folder with an XSS payload and triggering it via image addition.

## Description

Folder names are not sanitized, allowing HTML/JS injection. When a user adds an image to the folder, the name is rendered unsafely in the UI, executing the payload. This verifies the self-XSS before chaining with CSRF. Targets the web interface; API involvement is indirect.

## Requirements

1. Authenticated Imgur account for testing
2. Access to Imgur web interface
3. A test image to add to favorites

## Defense

Defensive measures and detection strategies:

- Output encode folder names in UI (e.g., HTML entity escaping)
- Content Security Policy to block inline scripts
- Audit logs for folder name patterns indicating payloads

## Objectives

1. Confirm payload storage without immediate execution
2. Validate trigger on folder interaction
3. Assess execution context for hijacking potential

## Instructions

### Step 1: Create Test Folder with Payload

**Context**: Manually input the XSS payload as the folder name to store it.

**Command** ([[commands/xss-payload-folder-name]]):
```html
1"'><img src=x onerror=prompt(1)>
```

> Navigate to Imgur favorites, click 'New Folder', enter the payload, set private if desired, and save. This closes a quote and injects an img tag with onerror JS. Expected output: Folder created with exact name preserved.

### Step 2: Trigger via Image Addition

**Context**: Interact with the folder to execute the stored payload.

**Instructions**: Visit any image page on Imgur, click the heart to favorite, then the plus icon, select the malicious folder, and add.

> Expected output: prompt(1) alert pops up in the browser, confirming XSS execution in the user's context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/xss-payload-folder-name]]

## Tools Used

- [[tools/browser-based-exploitation]]

## Tags

- [[xss]]
- [[stored-xss]]
- [[testing]]
