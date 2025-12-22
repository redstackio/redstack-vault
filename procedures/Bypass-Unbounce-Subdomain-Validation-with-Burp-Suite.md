---
id: proc-unbounce-validation-bypass
tags:
  - subdomain-takeover
  - validation-bypass
  - web-exploit
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
updated_at: '2025-12-14T04:38:39.780Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Unbounce Subdomain Validation with Burp Suite

## Summary

This procedure exploits insufficient input validation on the page[url] parameter in Unbounce Pages' POST /<account-id>/pages/<page-id> endpoint, allowing attackers to inject and claim arbitrary subdomains like info.hacker.one. By intercepting and modifying the 'EDIT NAME' update request with a proxy like Burp Suite, previous fixes can be bypassed, granting control over the subdomain for phishing or data exfiltration.

## Description

The vulnerability stems from inadequate sanitization of the page[url] parameter during page name updates, enabling subdomain injection. This occurs in the Unbounce Pages web application, where authenticated users can create pages and edit metadata. The attack requires an Unbounce account and a proxy tool to tamper with requests. Expected outcomes include successful subdomain claiming, verifiable by DNS resolution and content hosting under the target domain. This can lead to high-impact scenarios like impersonating trusted brands to steal credentials or payment details from HackerOne users.

## Requirements

1. Valid Unbounce account credentials for authentication.
2. Burp Suite or similar proxy installed and configured (browser proxy set to 127.0.0.1:8080).
3. Target subdomain must be vulnerable (e.g., dangling DNS record pointing to Unbounce).

## Defense

Defensive measures and detection strategies:

- Implement strict allowlist validation for subdomains in page[url] parameter, rejecting external domains.
- Monitor for anomalous DNS changes or subdomain resolutions pointing to Unbounce IPs.
- Enable request logging and anomaly detection for POST requests to page endpoints, alerting on unexpected parameter values.

## Objectives

1. Bypass subdomain validation to claim arbitrary domains.
2. Gain control over branded subdomains for malicious content hosting.
3. Facilitate phishing attacks targeting user credentials or sensitive data.

## Instructions

### Step 1: Authenticate and Create Page

**Context**: Gain access and set up a page to trigger the vulnerable endpoint.

**Instructions**: Log in to Unbounce, create a new landing page under any domain, and navigate to 'EDIT NAME'. Enter arbitrary text to prepare the request.

### Step 2: Intercept and Modify Request

**Context**: Capture the POST request and inject the malicious page[url] to bypass validation.

**Instructions**: Use Burp Suite to intercept the request. In the body, add `&page[url]=<target-subdomain>/<path>`, e.g., `&page[url]=info.hacker.one/takeover-bypass-by-ak1t4`. Forward the request.

### Step 3: Verify Takeover

**Context**: Confirm the subdomain is now under attacker control.

**Instructions**: Refresh the page or visit the target URL. Deploy custom content (e.g., phishing form) and check DNS resolution.

**Expected Output**: Subdomain loads attacker-controlled Unbounce page.

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

- [[subdomain-takeover]]
- [[validation-bypass]]
