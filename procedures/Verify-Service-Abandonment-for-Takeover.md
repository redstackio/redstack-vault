---
id: proc-verify-abandonment
tags:
  - service-verification
  - abandonment-check
  - zendesk
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-check-status]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T05:32:24.082Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify Service Abandonment for Takeover

## Summary

This procedure checks if an external service pointed to by a DNS CNAME, such as a Zendesk instance, is abandoned and available for claiming, confirming the feasibility of a subdomain takeover.

## Description

Following DNS enumeration, this step involves probing the service endpoint for the subdomain (e.g., support.easycontactnow.com) to determine if it's unclaimed. An abandoned Zendesk instance would redirect to a signup page, allowing an attacker to register and control the subdomain content.

## Requirements

1. Identified CNAME target from prior enumeration
2. Web access to the service URL
3. Browser or HTTP client for verification

## Defense

Defensive measures and detection strategies:

- Maintain active monitoring of third-party service accounts
- Use DNS security extensions (DNSSEC) to prevent unauthorized claims
- Conduct periodic audits of integrated services

## Objectives

1. Confirm the service is no longer controlled by the organization
2. Validate availability for takeover
3. Assess potential impact of hijacking

## Instructions

### Step 1: Probe Service Endpoint

**Context**: Send an HTTP request to the subdomain's service URL to check for abandonment indicators.

**Command** ([[commands/curl-check-status]]):
```bash
curl -I https://support.easycontactnow.com
```

> This fetches the HTTP headers. Expected output: A 200 OK with a redirect to Zendesk signup or a 404, indicating unclaimed status.

### Step 2: Attempt Claim Simulation

**Context**: Manually visit the service's dashboard creation page to verify claimability without actual registration.

**Command** (No CLI; use browser):
```bash
# Navigate to https://subdomain.zendesk.com/signup in a browser
```

> Look for prompts to create a new account. Expected output: Option to claim the subdomain.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-check-status]]

## Tools Used

- [[tools/curl]]

## Tags

- [[service-probing]]
- [[takeover-verification]]
