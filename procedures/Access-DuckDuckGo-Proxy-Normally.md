---
tags:
  - ssrf
  - proxy
  - recon
type: procedure
tools: []
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
updated_at: '2025-12-14T04:08:48.532Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 117c001f-0814-45bf-8275-07780b0f666c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-DuckDuckGo-Proxy-Normally

## Summary

This procedure establishes baseline behavior of the DuckDuckGo proxy endpoint by accessing it with a legitimate external URL, confirming the image_host parameter processes requests normally before attempting exploitation.

## Description

The DuckDuckGo proxy at https://proxy.duckduckgo.com/iur/ is designed to fetch and render images or content from specified hosts. By testing with an external, public URL, attackers can verify the endpoint's functionality, including the ?f=1 parameter for formatting, without triggering any anomalies. This step is crucial for understanding normal responses and avoiding detection during subsequent SSRF tests. The target environment is any web browser with internet access, and no special privileges are needed.

## Requirements

1. Web browser with developer tools enabled
2. Internet access to the public proxy endpoint
3. No authentication or special network position required

## Defense

Defensive measures and detection strategies:

- Monitor proxy logs for unusual image_host patterns
- Implement rate limiting on the endpoint to detect rapid testing
- Use web application firewalls (WAF) to flag suspicious parameter values

## Objectives

1. Confirm proxy fetches external content without errors
2. Establish response patterns for comparison in exploitation
3. Validate endpoint accessibility

## Instructions

### Step 1: Visit Endpoint with External URL

**Context**: Load the proxy with a known external image host to observe normal processing and rendering.

No specific command; use browser navigation:

```url
https://proxy.duckduckgo.com/iur/?f=1&image_host=https://tudomanyok.hu/
```

> This URL fetches content from tudomanyok.hu, rendering it via the proxy. Expected output includes successful image or page load without security errors.

### Step 2: Verify Response

**Context**: Inspect the rendered page to ensure baseline functionality.

Right-click and view the page; confirm no blocks or anomalies.

> Look for clean rendering of external content, indicating the parameter is active and unfiltered for external hosts.

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
- proxy
- baseline-testing
