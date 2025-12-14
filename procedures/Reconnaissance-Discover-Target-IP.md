---
id: uuid-recon-ip
tags:
  - reconnaissance
  - dod
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:37.356Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Reconnaissance Discover Target IP

## Summary

Initial reconnaissance step to identify target IP addresses linked to US government systems, such as those redirecting to .mil domains, setting the stage for further scanning and exploitation.

## Description

This procedure involves passive or active reconnaissance to uncover IP addresses associated with sensitive environments. In this scenario, an IP was found during recon that redirected to a DoD login page, indicating potential high-value targets. No specific tools are required beyond basic browsing or scanning, but it assumes network visibility to the target range.

## Requirements

1. Network access to scan or browse potential targets
2. Knowledge of government domain patterns (e.g., .mil redirects)
3. Basic web browser or reconnaissance toolkit

## Defense

Defensive measures and detection strategies:

- Implement IP whitelisting and geofencing to restrict access to reconnaissance tools
- Monitor for anomalous traffic patterns indicating broad IP discovery attempts

## Objectives

1. Identify IP with government affiliation
2. Confirm sensitivity via redirects or page content
3. Prepare for targeted port scanning

## Instructions

### Step 1: Browse Potential Targets

**Context**: Perform general reconnaissance to stumble upon target IPs, such as through search engines, Shodan, or manual probing.

No specific command; use a browser to access http://suspected-ip/ and observe redirects.

> Expected: Redirect to login page with URL parameter like login_url=https%3A%2F%2Fexample.mil, confirming DoD ownership.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[dod]]
