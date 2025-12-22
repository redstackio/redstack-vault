---
id: proc-trigger-xss-click
tags:
  - xss
  - execution
  - javascript
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
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
updated_at: '2025-12-13T23:56:03.331Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Link-Click

## Summary

This procedure triggers the stored XSS by clicking the auto-linked javascript: payload in the rendered comment, executing arbitrary JavaScript in the browser under the WordPress site's domain.

## Description

After submission, the payload renders as a link due to the plugin's regex. Clicking it navigates to javascript://%0dalert(document.cookie), executing the JS. This can steal cookies, session tokens, or perform other client-side attacks, all in the site's context without server-side detection.

## Requirements

1. The malicious comment must be visible on the page
2. Victim (or tester) interaction via mouse click
3. Browser that supports javascript: URLs

## Defense

Defensive measures and detection strategies:

- Disable javascript: protocol handling in browsers via policy
- Log and alert on JS execution from user-generated content
- Use XSS auditors or WAF rules to block suspicious links in comments

## Objectives

1. Execute the injected JavaScript payload
2. Demonstrate impact like cookie exfiltration
3. Simulate real victim compromise

## Instructions

### Step 1: Interact with Rendered Link

**Context**: Locate and click the malicious link in the highlighted code block to trigger execution.

No command required; perform a browser action:

Scroll to the comment, hover over the 'javascript://' link (it should be underlined/blue), and click it.

> This executes alert(document.cookie), popping an alert with session data. Expected output: Alert box shows cookies; in a real attack, data could be exfiltrated to an attacker-controlled server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[xss]]
- [[Execution]]
- [[JavaScript]]
