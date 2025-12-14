---
id: proc-uuid-4
tags:
  - content-control
  - phishing-setup
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
updated_at: '2025-12-14T04:51:26.694Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Custom-Content-on-Taken-Over-Subdomain

## Summary

Set up arbitrary web content on the hijacked subdomain via the claimed service dashboard, enabling phishing or defacement.

## Description

Post-takeover, use Desk.com's interface to customize pages. For help.cloudup.com, a custom page was set, though SSL mismatches caused errors, limiting full exploitation but proving control.

## Requirements

1. Access to the claimed Desk.com dashboard
2. Basic web configuration knowledge
3. Target subdomain resolution

## Defense

Defensive measures and detection strategies:

- Enforce SSL certificate pinning or HSTS
- Monitor subdomain traffic for anomalies
- Alert on unexpected content changes via service logs

## Objectives

1. Deploy custom content
2. Verify subdomain control
3. Assess impact limitations (e.g., SSL)

## Instructions

### Step 1: Access Dashboard

**Context**: Log into the newly claimed Desk.com account.

Navigate to customization settings for cloudup.desk.com.

### Step 2: Set Custom Page

**Context**: Configure HTML or redirect content.

Upload or edit a page, then test by visiting help.cloudup.com.

### Step 3: Validate Control

**Context**: Check for display issues like SSL errors.

Note partial functionality due to certificate mismatches.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[content-control]]
- [[phishing-setup]]
