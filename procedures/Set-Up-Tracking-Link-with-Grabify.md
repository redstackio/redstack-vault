---
id: proc-setup-grabify-001
tags:
  - ssrf
  - tracking
  - reconnaissance
type: procedure
tools:
  - '[[tools/Grabify]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.054Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Set-Up-Tracking-Link-with-Grabify

## Summary

This procedure sets up a URL tracking service using Grabify to monitor incoming HTTP requests, capturing IP addresses and headers to verify SSRF exploitation where the target server fetches the attacker's controlled URL.

## Description

In SSRF attacks, attackers need to observe if the vulnerable server initiates requests to internal or external resources. Grabify provides a simple, no-setup-required service for creating shortened links that log visitor details. This is used here to confirm the WordPress server fetches the pingback validation URL, revealing the server's IP for reconnaissance. The procedure assumes public internet access and targets web-based SSRF scenarios in WordPress environments.

## Requirements

1. Internet access to https://grabify.link/
2. No special credentials or tools beyond a web browser
3. Basic understanding of URL redirection for evasion

## Defense

Defensive measures and detection strategies:

- Monitor outbound HTTP requests from web servers for unusual domains or IPs
- Block or filter requests to known tracking services like Grabify in firewall rules
- Use web application firewalls (WAF) to detect anomalous pingback URL patterns

## Objectives

1. Generate a trackable URL for SSRF payload delivery
2. Configure logging to capture server IPs without bot filtering
3. Prepare for verification of forced requests in subsequent steps

## Instructions

### Step 1: Access Grabify and Create Link

**Context**: Navigate to the Grabify service and input a target redirect URL to create a tracking shortened link.

No command required; use web interface:

1. Visit https://grabify.link/
2. Enter a benign redirect URL, e.g., http://youtube.com, in the 'Enter URL to shorten' field
3. Click 'Create URL' to generate the tracking link (e.g., https://grabify.link/XXXXXX)
4. Copy the tracking code or URL for use in PoC scripts

> This step creates a link that redirects to YouTube but logs the requester's IP, user-agent, and timestamp before redirection.

### Step 2: Configure Tracking Settings

**Context**: Adjust settings to ensure accurate logging of server requests without false positives from bots.

No command required; use dashboard:

1. Go to the tracking page using the generated code
2. Disable the 'Bot Toggle' to include all hits, as servers may appear as bots
3. Optionally, set up domain fronting if needed for evasion, but keep default for simplicity

> Expected output: Dashboard showing '0 hits' initially, ready for monitoring.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Grabify]]

## Tags

- [[ssrf]]
- [[tracking]]
- [[Reconnaissance]]
