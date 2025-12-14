---
id: proc-uuid-001
tags:
  - ssrf
  - misconfiguration
  - sentry
  - recon
type: procedure
tools:
  - '[[tools/Sentry]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.151Z'
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
# Identify-Sentry-Source-Code-Scraping-Misconfiguration

## Summary

This procedure involves probing Cloudflare's Sentry deployment on platform.dash.cloudflare.com to detect if the source code scraping feature is enabled, which can lead to blind SSRF vulnerabilities by allowing arbitrary request forwarding through the infrastructure.

## Description

In Cloudflare's application monitoring setup, Sentry is used for error tracking. A misconfiguration occurs when the source code scraping feature is enabled, permitting the system to fetch code from specified URLs. Attackers can test this by submitting requests that trigger the feature, observing if internal or arbitrary endpoints are accessible. This step is crucial for reconnaissance in SSRF attacks, as it confirms the vulnerability without direct exploitation. The target environment is a web-based platform with cloud infrastructure, and success relies on public access to the dashboard.

## Requirements

1. Access to platform.dash.cloudflare.com via web browser or HTTP client.
2. Basic understanding of Sentry's integration with Cloudflare.
3. No special credentials needed for initial probing.

## Defense

Defensive measures and detection strategies:

- Disable source code fetching in Sentry configurations.
- Implement request whitelisting to restrict endpoint access.
- Monitor Sentry logs for unusual scraping attempts.

## Objectives

1. Confirm the presence of the misconfigured source code scraping feature.
2. Gather evidence of potential SSRF vectors.
3. Prepare for exploitation by identifying reachable endpoints.

## Instructions

### Step 1: Probe Sentry Integration

**Context**: Access the Cloudflare dashboard and interact with the application monitoring section to trigger Sentry's source code features.

No specific command required; use a web interface to submit a test error report or monitoring query that invokes source code scraping.

> Observe the response for indications that scraping is enabled, such as attempts to fetch from user-supplied URLs.

### Step 2: Verify Arbitrary Request Capability

**Context**: Test if the feature allows requests to non-standard endpoints by crafting a payload in the monitoring setup.

Use browser developer tools to inspect network requests and confirm if internal-like fetches are initiated.

> Expected output includes successful initiation of blind requests without client-side blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Sentry]]

## Tags

- [[ssrf]]
- [[misconfiguration]]
- [[tools/Sentry]]
- [[recon]]
