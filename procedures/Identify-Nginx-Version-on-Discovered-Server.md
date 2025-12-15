---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - version-identification
  - nginx
  - web-server
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:23:32.727Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-Nginx-Version-on-Discovered-Server

## Summary

This procedure involves accessing a discovered server IP via HTTPS to inspect response headers and confirm the nginx version, revealing an outdated 1.4.6 installation vulnerable to known exploits.

## Description

Following certificate-based reconnaissance, this step passively fingerprints the web server by connecting to the exposed endpoint. For the IRCCloud target at 54.153.101.52, accessing the HTTPS URL exposes the nginx server banner, allowing assessment of patch levels without authentication. This is crucial for chaining to vulnerability research.

## Requirements

1. Discovered IP address from prior recon (e.g., 54.153.101.52)
2. Web browser or curl for header inspection
3. No credentials or special access needed

## Defense

Defensive measures and detection strategies:

- Hide server banners by customizing nginx error pages and headers
- Regularly scan for exposed services using tools like Nmap
- Update server software to latest versions

## Objectives

1. Confirm web server type and version
2. Screenshot or log evidence for reporting
3. Identify outdated software for exploitation potential

## Instructions

### Step 1: Access Server Endpoint

**Context**: Connect to the HTTPS URL to trigger server response.

Use browser or command line:

```bash
curl -I https://54.153.101.52
```

> Look for "Server: nginx/1.4.6" in headers; alternatively, browser dev tools show the same.

### Step 2: Capture and Verify Version

**Context**: Document the version for CVE correlation.

Take a screenshot of the response or save headers to file.

> Expected output: Confirmation of nginx 1.4.6, indicating end-of-life status.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Hardware

### Sub-Techniques

- None

## Commands Used

- None (uses curl implicitly, but not formalized)

## Tools Used

- None

## Tags

- [[version-identification]]
- [[web-server]]
