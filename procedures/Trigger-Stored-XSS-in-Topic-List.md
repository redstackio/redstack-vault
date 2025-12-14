---
id: proc-uuid-2
tags:
  - xss
  - stored-xss
  - execution
  - concrete-cms
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
created_at: '2024-10-01'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.553Z'
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
# Trigger-Stored-XSS-in-Topic-List

## Summary

This procedure triggers the execution of a previously injected stored XSS payload by rendering the vulnerable topic list page, leading to arbitrary JavaScript execution in the victim's browser.

## Description

Once the payload is stored in the Concrete CMS database via the title field, accessing the topic list causes the CMS to output the unsanitized title directly into the HTML, executing the injected script. This affects any user viewing the list, enabling attacks like cookie theft or keylogging. The procedure assumes the injection step has succeeded and focuses on delivery to victims.

## Requirements

1. Access to the topic list page (may require authentication depending on CMS permissions)
2. Web browser to load and execute the page
3. Prior successful injection of payload

## Defense

Defensive measures and detection strategies:

- Enforce output encoding for all user-controlled data in HTML contexts
- Use strict CSP headers to prevent script execution from inline sources
- Implement web application firewall (WAF) rules to detect XSS patterns in rendered output
- Log and alert on unexpected JavaScript errors or alerts in user sessions

## Objectives

1. Render the stored payload to execute JavaScript in browser context
2. Demonstrate impact such as alert popups or data exfiltration
3. Affect multiple users viewing the topic list

## Instructions

### Step 1: Navigate to Topic List

**Context**: Access the page that displays the list of topics, where titles are rendered without escaping.

In Concrete CMS, go to the topic list view (e.g., Dashboard > Topics or public topic page). Ensure the injected topic is visible in the list.

### Step 2: Observe Execution

**Context**: Load the page to trigger rendering of the malicious title, executing the onerror handler or script.

The payload `'><img src=x onerror=alert(1)>` will cause an alert(1) to pop up immediately upon page load.

> In production, this could be escalated to steal session cookies via a beacon to an attacker-controlled server. Check browser console for any errors or confirm execution via the alert.

**Expected Output**: JavaScript executes, showing an alert box or performing the intended action (e.g., network request).

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
- [[stored-xss]]
- [[concrete-cms]]
