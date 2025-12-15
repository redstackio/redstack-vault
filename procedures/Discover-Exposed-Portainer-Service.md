---
id: proc-discover-portainer
tags:
  - reconnaissance
  - exposed-service
  - portainer
type: procedure
tools:
  - '[[tools/Portainer]]'
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
updated_at: '2025-12-14T17:23:28.065Z'
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
# Discover Exposed Portainer Service

## Summary

This procedure involves identifying a publicly accessible Portainer instance, a web-based Docker management tool, which is often misconfigured in demo or development environments like Nextcloud, allowing attackers to probe for vulnerabilities without specialized tools.

## Description

In the context of a Nextcloud demo, Portainer was running on a subdomain without authentication restrictions or configuration changes, exposing it to direct access. This step focuses on verifying the service's availability via HTTP, confirming it's a potential entry point for further exploitation. Prerequisites include basic knowledge of target URLs and ports; no credentials are needed at this stage. Expected outcomes include confirmation of the login interface, setting the stage for credential testing.

## Requirements

1. Web browser or HTTP client for accessing the target URL
2. Knowledge of the target's subdomain and port (e.g., :9000)
3. Public internet access to the service

## Defense

Defensive measures and detection strategies:

- Restrict Portainer access to internal networks via firewalls or VPN
- Monitor for anomalous HTTP requests to management ports like 9000
- Use web application firewalls (WAF) to block unauthorized probes

## Objectives

1. Confirm exposure of the Portainer service
2. Verify lack of access controls
3. Identify the login interface for next steps

## Instructions

### Step 1: Access the Target URL

**Context**: Directly navigate to the Portainer endpoint to check for public exposure.

No specific command required; use a browser to visit http://spreed-demo.nextcloud.com:9000/.

> The page should load the Portainer login screen, indicating the service is running and accessible.

### Step 2: Verify Service Response

**Context**: Ensure the response confirms Portainer without errors or redirects.

Inspect the page source or network tab for Portainer.io branding.

> Successful verification shows the UI elements for login, confirming unconfigured exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Portainer]]

## Tags

- [[Reconnaissance]]
- [[exposed-service]]
