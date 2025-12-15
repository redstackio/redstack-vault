---
id: proc-uuid-2
tags:
  - host-header
  - modification
  - open-redirect
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.686Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Host-Header-for-Redirect

## Summary

This procedure modifies the Host header in an intercepted HTTP request to an attacker-controlled domain, exploiting unvalidated redirects in the web application.

## Description

By changing the Host header, the server constructs a redirect URL based on the fake host, leading to an open redirect. This targets apps like www.localizestaging.com that do not validate or allowlist hosts. The attacker must control a domain with malicious content, such as an index.html embedding JavaScript.

## Requirements

1. Intercepted request from previous step
2. Attacker-owned domain (e.g., evil.com) with hosted malicious page
3. Burp Suite for editing

## Defense

Defensive measures and detection strategies:

- Validate and allowlist Host headers against known domains
- Log and alert on unexpected Host values in requests

## Objectives

1. Tamper with Host to enable arbitrary redirect
2. Set up for phishing or further chaining
3. Ensure modification doesn't break request syntax

## Instructions

### Step 1: Edit Header in Burp

**Context**: Locate and alter the Host header in the intercepted request.

In Burp's Intercept tab, find the line 'Host: www.localizestaging.com' and change it to 'Host: evil.com' (attacker domain).

**Expected Output**: Updated request header visible; no syntax errors.

### Step 2: Verify Payload Hosting

**Context**: Ensure the target domain hosts the redirect payload.

Confirm that http://evil.com/ serves an index.html with <script>alert(document.cookie)</script> or similar.

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

- [[host-header]]
- [[modification]]
- [[open-redirect]]
