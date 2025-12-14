---
tags:
  - ssrf
  - localhost
  - url-injection
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.314Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a7d4bb4a-382f-4df5-87c6-760a0d8c94ea
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Submit-Localhost-URL-for-SSRF

## Summary

This procedure involves injecting localhost URLs (e.g., https://127.0.0.1:22) into the 'Download Link' field of the Nextcloud app release form to trigger SSRF and force the server to request internal resources.

## Description

The vulnerability stems from insufficient validation of user-supplied URLs in the download link field, allowing the server to fetch arbitrary addresses, including localhost and internal IPs. By submitting URLs targeting specific ports, attackers can probe for open services. This is performed manually via the web form, with the server responding based on connection success or failure.

## Requirements

1. Access to the release creation page (from prior procedure)
2. List of target ports (e.g., 22, 80, 21)
3. Web browser for form interaction

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed URL domains (e.g., block localhost, private IPs)
- Log and alert on requests to internal addresses in application logs
- Rate-limit form submissions to prevent scanning attempts

## Objectives

1. Trigger server-side requests to localhost ports
2. Bypass external firewall protections for internal enumeration
3. Collect initial response data for port status

## Instructions

### Step 1: Prepare Payload URL

**Context**: Craft a URL targeting a localhost port to test service availability.

Example payload: `https://127.0.0.1:22` for SSH.

### Step 2: Inject and Submit

**Context**: Enter the payload into the form and submit to initiate the SSRF request.

Fill the 'Download Link' field with the URL and click submit.

**Expected Output**: Server error or processing message indicating the fetch attempt.

> For port 22 (open SSH): May show connection successful or partial fetch.
> For port 21 (closed Telnet): Connection failed error.

### Step 3: Repeat for Multiple Ports

**Context**: Test various ports to map open services.

Submit additional URLs like `https://127.0.0.1:80` (HTTP) and `https://127.0.0.1:21` (Telnet).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- port-scan
- nextcloud
