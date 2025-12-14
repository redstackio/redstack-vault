---
id: proc-53098-step1
name: Access-Twitter-Unsafe-Link-with-Nested-Payload
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:15:53.446Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - xss
  - payload-delivery
  - url-injection
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---

# Access-Twitter-Unsafe-Link-with-Nested-Payload

## Summary

This procedure delivers a crafted nested URL payload to Twitter's unsafe link warning page, exploiting insufficient sanitization of the 'unsafe_link' parameter to reflect malicious JavaScript attributes like onmouseover into the page DOM.

## Description

In the context of a reflected XSS attack on Twitter's safety warning feature, this step involves navigating to a specially crafted URL in Internet Explorer. The payload uses double URL encoding to nest a malicious link (e.g., http://example.com onmouseover=alert(1) style=font-size:100pt) within the 'unsafe_link' parameter, bypassing basic validation. Upon loading, the parameter is reflected unsanitized, embedding the attributes in the page's HTML. This sets up the vulnerability for subsequent interaction. Prerequisites include access to Internet Explorer and the ability to direct a victim to the URL via social engineering.

## Requirements

1. Internet Explorer browser (version vulnerable to this payload, e.g., IE 11)
2. Network access to https://twitter.com
3. Crafted URL with nested payload

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and HTML attribute encoding for reflected parameters
- Deploy Content Security Policy (CSP) to block inline JavaScript execution
- Monitor for anomalous URL patterns in access logs, such as double-encoded payloads

## Objectives

1. Inject malicious attributes into the reflected 'unsafe_link' parameter
2. Load the warning page without triggering sanitization errors
3. Prepare the DOM for XSS trigger

## Instructions

### Step 1: Craft and Navigate to Payload URL

**Context**: Construct the nested URL to evade checks and reflect the payload, then access it in the vulnerable browser.

No specific command required; use browser navigation.

Navigate to: https://twitter.com/safety/unsafe_link_warning?unsafe_link=https%3A%2F%2Ftwitter.com%2Fsafety%2Funsafe_link_warning%3Funsafe_link%3Dhttp%3A%2F%2Fexample.com%2520onmouseover%3Dalert%281%29%2520style=font-size:100pt%2520

> This URL injects the onmouseover=alert(1) and style attributes. Expected output: Warning page loads with reflected link in source.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-delivery]]
- [[url-injection]]
