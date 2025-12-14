---
id: proc-nextcloud-endpoint-identify
tags:
  - ssrf
  - nextcloud
  - recon
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/add-trusted-server-normal]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:48.735Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Nextcloud-Trusted-Servers-Endpoint

## Summary

This procedure involves analyzing the Nextcloud federation feature's trusted-servers endpoint to identify the SSRF vulnerability, where user-supplied URLs trigger unauthenticated server-side cURL requests without validation.

## Description

In Nextcloud, the federation feature allows adding trusted servers via a POST request to `/nextcloud/index.php/apps/federation/trusted-servers` with a 'url' parameter. The server performs a cURL request to this URL to fetch `/status.php`, enabling SSRF if no URL validation exists. This step sets up reconnaissance by confirming the endpoint's behavior, allowing subsequent internal probing.

## Requirements

1. Access to Nextcloud instance documentation or source code
2. Ability to send HTTP POST requests (e.g., via cURL)
3. Network connectivity to the target server

## Defense

Defensive measures and detection strategies:

- Implement URL allowlisting to restrict requests to external domains only
- Monitor server logs for unusual cURL errors or internal IP connections
- Use web application firewalls (WAF) to block localhost or internal URL patterns

## Objectives

1. Confirm the endpoint accepts arbitrary URLs
2. Understand response patterns for open vs. closed connections
3. Prepare for port scanning exploitation

## Instructions

### Step 1: Examine Endpoint Functionality

**Context**: Review the endpoint to understand normal usage and identify the 'url' parameter vulnerability.

**Command** ([[commands/add-trusted-server-normal]]):
```bash
curl -X POST -d "url=http://nextcloud.remote.server.com/" https://target-nextcloud/index.php/apps/federation/trusted-servers
```

> This simulates adding a legitimate trusted server, revealing the cURL initiation to the supplied URL + /status.php. Expected output includes a 400 Bad Request with details on the client error response.

### Step 2: Analyze Response for SSRF Indicators

**Context**: Observe how responses differ based on URL reachability to confirm SSRF potential.

**Command** ([[commands/add-trusted-server-normal]]):
```bash
curl -X POST -d "url=http://example.com/" https://target-nextcloud/index.php/apps/federation/trusted-servers
```

> Look for JSON messages indicating cURL attempts, such as status codes or connection errors, which expose internal behaviors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/add-trusted-server-normal]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- nextcloud
- endpoint-analysis
