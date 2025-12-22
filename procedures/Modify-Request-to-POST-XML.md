---
tags:
  - xxe
  - request-modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f1ae4b74-331b-4d03-96d0-aadca020b010
created_at: '2025-12-13T09:00:28.042Z'
updated_at: '2025-12-13T09:00:28.042Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify Request to POST XML

## Summary

This procedure modifies an intercepted GET request to a POST request with XML content type, enabling the injection of XML payloads for testing vulnerabilities like XXE.

## Description

Converting requests to POST with application/xml allows testers to submit custom XML data, exploiting parsers that process external entities insecurely. This is key in blind XXE scenarios where responses are not directly observable.

## Requirements

1. Intercepted request in Burp Suite
2. Knowledge of HTTP methods and headers
3. Target endpoint supporting POST

## Defense

Defensive measures and detection strategies:

- Validate and restrict HTTP methods on endpoints
- Use WAF to block unexpected content types

## Objectives

1. Change request method to POST
2. Set appropriate headers for XML
3. Prepare for payload injection

## Instructions

### Step 1: Send to Repeater and Change Method

**Context**: Use Repeater to modify the request.

In Burp Suite, send the intercepted request to Repeater and change the method to POST. Adjust headers including Content-Length: 173.

> Expected: Request updated in Repeater.

### Step 2: Add Content-Type Header

**Context**: Specify the body as XML.

Set Content-Type: application/xml in the request headers.

> Expected: Headers reflect XML content type.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xxe
- request-modification
