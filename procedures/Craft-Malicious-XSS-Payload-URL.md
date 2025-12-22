---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - payload-crafting
  - url-injection
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
updated_at: '2025-12-14T17:26:06.107Z'
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
# Craft Malicious XSS Payload URL

## Summary

This procedure details constructing a reflected XSS payload by injecting a script tag into the URL path suffix, exploiting the lack of validation on smarthistory.khanacademy.org.

## Description

By appending a closing quote, script tag, and JavaScript code to a legitimate path, the payload breaks out of HTML contexts and executes in the browser. The example uses an alert for proof-of-concept, but can be adapted for data theft like cookie exfiltration. This targets the subdomain's handling of .html extensions and path parameters.

## Requirements

1. Knowledge of JavaScript and HTML injection techniques
2. Text editor or browser developer tools for payload testing
3. Access to the vulnerable subdomain

## Defense

Defensive measures and detection strategies:

- Sanitize all URL components server-side with libraries like DOMPurify
- Reject URLs containing script tags or common XSS patterns
- Log and alert on suspicious payloads in web server access logs

## Objectives

1. Create a functional PoC URL for XSS execution
2. Ensure payload evades basic filters
3. Prepare for delivery via phishing or direct access

## Instructions

### Step 1: Select Base Path

**Context**: Choose a valid resource to append the payload to.

Start with a legitimate URL like http://smarthistory.khanacademy.org/Campin.

> This provides context for the injection point.

### Step 2: Build and Encode Payload

**Context**: Construct the injection string to close tags and insert script.

Append "><script>alert(/BigBear/)</script>.html to the path, resulting in http://smarthistory.khanacademy.org/Campin"><script>alert(/BigBear/)</script>.html.

> Test in browser URL bar; the alert should not yet execute until accessed fully.

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
- [[payload]]

