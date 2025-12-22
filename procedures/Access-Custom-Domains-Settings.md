---
id: proc-uuid-2
tags:
  - subdomain-takeover
  - cloud-service
  - configuration
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
updated_at: '2025-12-14T05:32:23.557Z'
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
# Access-Custom-Domains-Settings

## Summary

This procedure navigates the registered cloud webservice dashboard to locate and access the Custom Domains configuration, enabling the binding of external domains to the service.

## Description

Following service registration, the attacker must configure domain settings to claim the vulnerable subdomain. This involves interacting with the platform's UI to find the relevant settings panel. The process assumes the service is active and requires no advanced technical skills, but familiarity with cloud dashboards. Success here allows progression to domain claiming, ultimately leading to traffic redirection from the DoD subdomain to the attacker's content.

## Requirements

1. Active session on the cloud platform
2. Registered web app from prior step
3. Web browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Restrict custom domain additions to verified accounts via email/SMS
- Alert on domain claims involving sensitive TLDs like .gov
- Use certificate transparency logs to monitor subdomain bindings

## Objectives

1. Gain access to domain configuration tools
2. Prepare for subdomain claiming
3. Verify service readiness for takeover

## Instructions

### Step 1: Log Into Dashboard

**Context**: Ensure authenticated access to the service management interface.

Log in to the cloud platform using the created account credentials.

### Step 2: Navigate to Settings

**Context**: Locate the configuration area for the specific app.

Select the registered app from the dashboard, then click on 'Settings' or 'Domains' tab to reveal the Custom Domains feature.

> Expected output: Interface loads with options to manage domains.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[cloud-service]]
