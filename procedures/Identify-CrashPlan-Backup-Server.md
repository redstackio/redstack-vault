---
tags:
  - recon
  - crashplan
  - backup
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d2d4f5e8-8b46-4092-8dca-6a22a613d640
created_at: '2025-12-14T17:26:30.462Z'
updated_at: '2025-12-14T17:26:30.462Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-CrashPlan-Backup-Server

## Summary

This procedure involves reconnaissance to locate and verify a CrashPlan backup server, such as Uber's at backup.uber.com:443, confirming its configuration for inbound backups using friend codes.

## Description

CrashPlan is a cloud backup service that allows peer-to-peer and server-based backups. In this scenario, the target is a publicly hosted instance (backup.uber.com) running on HTTPS port 443. The procedure checks for the presence of a friend code authentication mechanism, which enables external machines to join the backup network. No special privileges are needed, but basic web reconnaissance skills are required. Expected outcome: Confirmation of the server's role and authentication method, setting the stage for further exploitation.

## Requirements

1. Internet access to the target domain (backup.uber.com)
2. Web browser or HTTP client for probing
3. Knowledge of CrashPlan's default port and interface

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) to log anomalous probes to backup endpoints
- Restrict public access to backup servers via IP whitelisting or VPN
- Monitor access logs for unusual traffic patterns to port 443

## Objectives

1. Confirm the target hosts a CrashPlan server
2. Identify the friend code input mechanism
3. Verify inbound backup support without prior authentication

## Instructions

### Step 1: Probe Target Domain

**Context**: Access the target URL to observe the service interface and confirm CrashPlan deployment.

Use a web browser or HTTP client to visit https://backup.uber.com:443. Look for CrashPlan branding, login prompts, or friend code entry fields.

> Expected output: Page loads with CrashPlan interface, indicating the service is active on port 443.

### Step 2: Inspect for Friend Code Feature

**Context**: Verify the server's support for external backups via friend codes.

Examine the page source or use developer tools to identify forms or API endpoints related to friend code validation (e.g., /auth or similar). Test entering a dummy code to see response behavior.

> Expected output: Interface accepts 6-digit alphanumeric input without immediate rejection, confirming the feature.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[crashplan]]
