---
tags:
  - csrf
  - recon
  - web
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
updated_at: '2025-12-14T17:27:23.533Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 76567bb8-a068-4338-a396-a7764c6b1922
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Analyze-HTTP-Requests-for-CSRF-Vulnerabilities

## Summary

This procedure uses Burp Suite to intercept and analyze HTTP requests on m.badoo.com, identifying missing CSRF tokens in POST endpoints for account deletion and contact erasure, along with a JSON content-type flaw.

## Description

In a web application like m.badoo.com, CSRF vulnerabilities arise when state-changing POST requests lack token validation. This procedure captures traffic during simulated actions, revealing no tokens and a JSON parsing issue where the server appends an '=' to the content, which can be bypassed with a dummy parameter. Prerequisites include a browser and Burp Suite configured as a proxy; the target must be accessible.

## Requirements

1. Burp Suite installed and running as a proxy (default port 8080)
2. Browser configured to route traffic through Burp proxy
3. Active session or ability to perform actions on m.badoo.com
4. Knowledge of target endpoints for account deletion and contact erasure

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing requests
- Validate Content-Type headers strictly for JSON endpoints
- Monitor for anomalous POST requests from user agents

## Objectives

1. Confirm absence of CSRF protection on vulnerable endpoints
2. Document JSON parsing bypass method
3. Prepare for exploitation by replicating requests

## Instructions

### Step 1: Configure Burp Suite Proxy

**Context**: Set up interception to capture all traffic to m.badoo.com.

Intercept traffic by configuring your browser's proxy settings to 127.0.0.1:8080 and enabling Burp's intercept feature.

### Step 2: Perform Target Actions

**Context**: Trigger the vulnerable requests to analyze them.

Log into m.badoo.com, then attempt account deletion or contact erasure. Forward requests in Burp to complete the action while inspecting details.

### Step 3: Inspect Requests and Responses

**Context**: Look for security gaps.

In Burp's Proxy or Repeater tab, examine POST requests for CSRF tokens (e.g., _token field). Note Content-Type: application/json and check if responses append '='; test bypass by adding 'ignore_me':' value='test' in the body.

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

- [[csrf]]
- [[web]]
- [[recon]]
