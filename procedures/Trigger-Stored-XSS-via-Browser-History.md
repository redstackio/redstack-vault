---
tags:
  - xss-trigger
  - browser-history
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.138Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b28a65f9-5f0d-404b-b3ba-6f596ddbbd4b
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Browser-History

## Summary

This procedure triggers the stored XSS by inducing the victim to navigate to the VK.com developer page through browser history, causing the malicious app name to load and execute JavaScript in their browser context.

## Description

Once the victim is main admin, accessing https://vk.com/dev/Login via direct link or back button from another site will render the unsanitized app name, injecting and executing the JavaScript payload. This relies on natural browsing behavior for stealthy delivery, leading to arbitrary code execution like cookie theft.

## Requirements

1. Victim promoted to main admin
2. Victim's browser session active on VK.com
3. Social engineering to prompt navigation (e.g., link to another page)

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected content from stored fields
- Implement browser history isolation or referrer checks
- Monitor for JS errors or anomalous script executions in logs

## Objectives

1. Execute the stored payload in victim context
2. Achieve client-side compromise
3. Steal session data or perform actions

## Instructions

### Step 1: Direct Victim to External Site

**Context**: Lure victim to visit a non-VK site while logged into VK.

Send a link or instruct via social engineering to browse elsewhere.

### Step 2: Induce Back Navigation

**Context**: Prompt use of browser back button to reach dev page.

Encourage hitting back to return to VK.com/dev/Login.

### Step 3: Observe Execution

**Context**: Payload runs on page load.

The app name injects JS, e.g., alert(1) or document.cookie exfil.

**Expected Output**: JS executes silently or visibly in victim's browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[browser-history]]
