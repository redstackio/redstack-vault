---
id: proc-intercept-modify-burp
tags:
  - proxy
  - intercept
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:46.015Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Request-with-Burp

## Summary

This procedure uses Burp Suite to intercept an HTTP request to the target endpoint, switch it from GET to POST, and prepare it for custom payload injection in the Repeater module.

## Description

Burp Suite acts as a proxy for manipulating web requests, essential for crafting exploits like SSRF payloads. This step captures the initial request to xmlrpc.php and modifies it, enabling POST-based XML submission without direct client changes. Targeted at web vulnerability testing.

## Requirements

1. Burp Suite installed and proxy configured (e.g., browser traffic routed through 127.0.0.1:8080)
2. Target endpoint accessible
3. Basic understanding of HTTP methods

## Defense

Defensive measures and detection strategies:

- Monitor for proxy-like traffic anomalies (e.g., repeated requests from single IP)
- Enforce TLS and certificate pinning to hinder interception
- Rate-limit endpoint requests

## Objectives

1. Capture and alter request method
2. Set up for payload delivery
3. Ensure compatibility with XML content

## Instructions

### Step 1: Intercept Initial Request

**Context**: Route traffic through Burp to capture the GET to xmlrpc.php.

No command; use Burp Proxy tab to intercept.

> Forward the intercepted request to Repeater for modification.

### Step 2: Change to POST in Repeater

**Context**: Modify the method and prepare body.

No command; in Repeater, edit the raw request to change GET to POST and clear body.

> Verify the updated request shows POST https://target/xmlrpc.php.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[burp]]
