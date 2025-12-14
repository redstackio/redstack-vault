---
id: p-open-redirect-discover
tags:
  - open-redirect
  - vendor
  - testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.505Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover Stored Open Redirect in Vendor Endpoint

## Summary

This procedure tests a third-party vendor's web endpoint for stored open redirect vulnerabilities by injecting arbitrary URLs into parameters like destination_url, confirming if the system stores and redirects without validation.

## Description

Open redirects occur when a web application fails to validate redirect parameters, allowing attackers to specify arbitrary destinations. In this case, the vendor's /widgets/experience endpoint accepts destination_url without sanitization, storing the redirect. This is tested post-CNAME identification, targeting inherited setups like those on Twitter subdomains, with outcomes including potential phishing vectors.

## Requirements

1. Identified vendor domain from prior DNS reconnaissance
2. Tool for sending HTTP requests (e.g., curl or browser)
3. Attacker-controlled domain for testing (e.g., evil.com)

## Defense

Defensive measures and detection strategies:

- Implement URL validation whitelisting only trusted domains
- Log and monitor redirect parameters for anomalies
- Use Content Security Policy (CSP) to restrict redirects

## Objectives

1. Validate lack of parameter sanitization
2. Confirm stored redirect behavior
3. Assess exploitability for downstream impacts

## Instructions

### Step 1: Test Parameter Injection

**Context**: Send a request to the endpoint with an arbitrary destination_url to check acceptance.

**Command** ([[commands/curl-test-url]]):
```bash
curl "https://vendor.example.com/widgets/experience?destination_url=https://evil.com" -v
```

> The -v flag provides verbose output showing headers and any redirect. Expected output: Response incorporating the arbitrary URL, indicating no validation.

### Step 2: Verify Stored Redirect

**Context**: Follow up by accessing the generated page to observe if the redirect persists.

**Command** ([[commands/curl-test-url]]):
```bash
curl -L "https://vendor.example.com/widgets/experience?destination_url=https://evil.com"
```

> The -L flag follows redirects. Success: Redirects to evil.com, confirming stored open redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-test-url]]

## Tools Used

- None

## Tags

- [[open-redirect]]
- [[vendor]]
- [[testing]]
