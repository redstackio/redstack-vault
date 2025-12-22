---
id: proc-rails-trigger-xss
tags:
  - xss
  - execution
  - javascript
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
updated_at: '2025-12-14T17:28:20.728Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Fallback-HTML

## Summary

This procedure demonstrates how a victim interacts with the fallback HTML response from a stripped redirect, clicking the link to execute the injected JavaScript payload for reflected XSS, such as cookie theft.

## Description

After header stripping, Rails serves a simple HTML page with an <a> tag whose href is the user-supplied URL (e.g., javascript:alert(document.cookie)). Clicking executes the JS in the browser context, enabling data exfiltration or other actions. Impact includes session hijacking; occurs in browsers expecting a redirect.

## Requirements

1. Fallback HTML response received from prior step
2. Victim browser access (simulated by manual click)
3. JS payload designed for the target (e.g., alert for PoC)

## Defense

Defensive measures and detection strategies:

- Escape user input in HTML responses
- Implement strict referrer policies
- Detect and block javascript: schemes in links

## Objectives

1. Execute arbitrary JS via link click
2. Steal sensitive data like cookies
3. Achieve reflected XSS impact

## Instructions

### Step 1: Load Response in Browser

**Context**: Visit the crafted URL in a browser to receive the fallback HTML.

Navigate to: http://localhost:3000/vuln?redirect_url=javascript:alert(document.cookie)%08

> Browser shows the "You are being redirected" message with link.

### Step 2: Click the Link

**Context**: Simulate victim interaction by clicking the href.

Click the "redirected" link in the HTML.

> Executes javascript:alert(document.cookie), popping an alert with cookies.

### Step 3: Validate Execution

**Context**: Confirm JS ran and potential impact.

Observe alert or network requests for exfiltration.

> Success if JS payload triggers; in real attacks, payload could send data to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
- javascript
