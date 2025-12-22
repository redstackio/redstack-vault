---
tags:
  - ssrf
  - ghost-cms
  - testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.714Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 9b8bcd2e-7cae-4fa1-ae20-a87fd4a7f9c2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Direct-SSRF-Attempt-on-oEmbed

## Summary

This procedure tests a direct SSRF attempt by sending an internal URL to the oEmbed endpoint, confirming the presence of validation that blocks straightforward exploitation.

## Description

Directly inputting internal URLs like cloud metadata endpoints (e.g., http://169.254.169.254/metadata/v1.json) to the oEmbed endpoint results in a validation error, as the query function expects content from fetchOembedData but receives none due to blocked fetches.

## Requirements

1. Authenticated session to oEmbed endpoint
2. HTTP client like curl or browser dev tools
3. Knowledge of target internal URLs (e.g., DigitalOcean metadata)

## Defense

Defensive measures and detection strategies:

- Log and alert on requests to internal IPs in oEmbed parameters
- Validate all user-supplied URLs against allowlists
- Rate-limit admin API endpoints

## Objectives

1. Verify SSRF protection on direct inputs
2. Identify error responses for bypass planning
3. Confirm endpoint behavior

## Instructions

### Step 1: Craft Direct Request

**Context**: Send a GET request with an internal URL to test blocking.

Use curl to issue: curl -H "Cookie: ghost-admin-api-session=YOUR_SESSION" "https://your-ghost-instance/ghost/api/v3/admin/oembed/?url=http://169.254.169.254/metadata/v1.json&type=embed"

> Expect a validation error, such as no content returned from fetch.

### Step 2: Observe Response

**Context**: Analyze the failure to understand limitations.

Check the response for errors indicating blocked fetches or missing oEmbed data.

> Error confirms direct SSRF is prevented, guiding toward bypass methods.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- ghost-cms
- testing
