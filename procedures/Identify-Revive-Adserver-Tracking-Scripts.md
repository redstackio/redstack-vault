---
tags:
  - recon
  - web
  - revive-adserver
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 81fb86e2-22f0-4bfb-8794-94233ef6030a
created_at: '2025-12-14T17:24:23.033Z'
updated_at: '2025-12-14T17:24:23.033Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Revive Adserver Tracking Scripts

## Summary

This procedure locates the ck.php and lg.php scripts in Revive Adserver, which are responsible for ad impression and click tracking and serve as entry points for the open redirect vulnerability.

## Description

Revive Adserver uses ck.php for click tracking and lg.php for logging impressions. These scripts, part of the core delivery mechanism since early versions, accept parameters intended for third-party redirects but lack validation, making them prone to open redirects. This step involves reconnaissance to confirm their presence on the target ad server, typically by accessing standard paths or inspecting ad banners on hosted sites.

## Requirements

1. Access to the public Revive Adserver URL
2. Web browser or HTTP client for probing
3. Knowledge of common ad server paths

## Defense

Defensive measures and detection strategies:

- Implement URL allowlisting in tracking scripts
- Monitor for unusual redirect patterns in server logs
- Use web application firewalls (WAF) to block unvalidated redirects

## Objectives

1. Confirm presence of vulnerable endpoints
2. Understand parameter handling for further exploitation
3. Map the attack surface

## Instructions

### Step 1: Probe for ck.php and lg.php

**Context**: Directly access the scripts to verify they exist and respond.

Visit or request http://target-adserver.com/ck.php or http://target-adserver.com/lg.php. Look for responses indicating tracking functionality, such as pixel loads or redirects.

**Expected Output**: HTTP 200 or 302 response with tracking headers.

### Step 2: Inspect Parameters

**Context**: Check accepted parameters by reviewing documentation or trial requests.

Send a basic request like http://target.com/ck.php?dest= to observe behavior.

**Expected Output**: Script processes the parameter without error.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
