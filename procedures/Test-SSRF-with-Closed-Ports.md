---
id: proc-uuid-1
tags:
  - ssrf
  - testing
  - validation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-submit-url-to-validator]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.564Z'
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
# Test-SSRF-with-Closed-Ports

## Summary

This procedure tests for SSRF vulnerabilities by submitting localhost URLs targeting closed ports to a public-facing validator, observing error responses that confirm internal network access without proper URL sanitization.

## Description

In the context of the Twitter Cards validator, lack of URL validation (with a prior fix reverted) allows fetching arbitrary internal resources. This step focuses on closed ports like 123 to elicit distinct errors (e.g., connection refused) versus external URLs, proving the server processes internal requests. Prerequisites include public access to the validator; no tools beyond a browser or curl are needed. Expected outcomes: confirmation of SSRF via error patterns indicating localhost resolution.

## Requirements

1. Access to https://cards-dev.twitter.com/validator
2. Knowledge of non-responsive ports (e.g., 123)
3. Ability to submit POST requests with URL parameter

## Defense

Defensive measures and detection strategies:

- Implement strict URL whitelisting or blacklisting for internal IPs/localhost
- Monitor server logs for anomalous fetch attempts to 0.0.0.0 or 127.0.0.1
- Use WAF rules to block SSRF payloads in URL parameters

## Objectives

1. Verify SSRF by confirming internal request processing
2. Distinguish internal error responses from external ones
3. Establish baseline for further probing

## Instructions

### Step 1: Submit Closed Port URL

**Context**: Target a closed localhost port to trigger an internal connection attempt, revealing SSRF through error handling.

**Command** ([[commands/curl-submit-url-to-validator]]):
```bash
curl -X POST https://cards-dev.twitter.com/validator -d 'url=http://0.0.0.0:123'
```

> This sends the URL to the validator's form endpoint. Expected output: An error like "Connection refused" or timeout specific to internal fetches, differing from blocked external URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-submit-url-to-validator]]

## Tools Used


## Tags

- ssrf
- testing
