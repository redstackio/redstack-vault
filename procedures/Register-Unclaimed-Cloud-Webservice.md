---
id: proc-uuid-1
tags:
  - subdomain-takeover
  - cloud-service
  - registration
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
updated_at: '2025-12-14T05:32:23.563Z'
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
# Register-Unclaimed-Cloud-Webservice

## Summary

This procedure involves signing up for a cloud webservice platform and creating a new app instance using a specific service name that matches a dangling CNAME record, setting the stage for subdomain takeover.

## Description

In scenarios where a target's DNS records include a CNAME pointing to an unclaimed resource on a cloud platform like Heroku, an attacker can register that exact service name to hijack the subdomain. This step focuses on the initial registration and app creation, requiring no prior access to the target but knowledge of the dangling record (e.g., from DNS enumeration tools like dig or nslookup). The outcome is a controllable service ready for domain binding, potentially leading to full subdomain control for malicious activities.

## Requirements

1. Access to the internet and a web browser
2. Knowledge of the dangling CNAME target service name (e.g., from DNS lookup)
3. Free account on the cloud platform (no payment required for basic setup)

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated scanners like dnsdumpster or subjack
- Monitor cloud platform logs for unexpected registrations matching known subdomains
- Implement DNSSEC to prevent unauthorized CNAME manipulations

## Objectives

1. Establish a foothold by creating a matching service instance
2. Prepare for custom domain claiming
3. Enable subsequent steps toward subdomain control

## Instructions

### Step 1: Sign Up and Access Marketplace

**Context**: Create an account on the cloud platform to gain access to the webservice creation features.

Navigate to the platform's signup page and register a new account using any valid email.

### Step 2: Create New Web App Instance

**Context**: Instantiate a new app with the exact service name from the dangling CNAME to align with the target's DNS record.

After logging in, go to the dashboard, select 'New App' or 'Create Web App', and enter the service name (e.g., example-app) that matches the CNAME target. Confirm creation.

> Expected output: Dashboard shows the new app with the specified name, ready for configuration.

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
