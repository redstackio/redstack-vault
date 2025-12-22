---
tags:
  - xss
  - dom-xss
  - twitter
type: procedure
tools:
  - '[[tools/Browser-Console]]'
  - '[[tools/Internet-Explorer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/unescape-and-rewrite-document]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 39e4507d-c8c4-413b-8eb0-0cf83e21b41c
created_at: '2025-12-13T23:56:20.416Z'
updated_at: '2025-12-13T23:56:20.416Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS via Twitter Card

## Summary

This procedure accesses a malicious Twitter card to reflect the injected payload in the DOM, triggering XSS execution.

## Description

Loading the card endpoint reflects the unsanitized text parameter, allowing HTML injection. Using console commands unescapes content to verify and execute the payload.

## Requirements

1. Browser with developer tools
2. Access to twitter.com cards
3. Vulnerable payload from prior step

## Defense

Defensive measures and detection strategies:

- Escape all HTML in reflected parameters
- Monitor console executions on production domains

## Objectives

1. Reflect payload in DOM
2. Execute injected code
3. Confirm vulnerability

## Instructions

### Step 1: Load Card URL

**Context**: Access the card to load the payload.

Navigate to 'https://twitter.com/i/cards/tfw/v1/988278372894740480'.

> This reflects the text parameter.

### Step 2: Execute Unescape Command

**Context**: Unescape and rewrite document to trigger XSS.

Execute [[commands/unescape-and-rewrite-document]] in [[tools/Browser-Console]]:

```javascript
document.write(document.body.innerHTML.replace(/\\\\//g,'/'));
```

> This renders unescaped content, executing tags like <svg onload=alert()>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/unescape-and-rewrite-document]]

## Tools Used

- [[tools/Browser-Console]]
- [[tools/Internet-Explorer]]

## Tags

- xss
- dom-xss
