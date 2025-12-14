---
tags:
  - subdomain-takeover
  - dns-hijacking
  - cloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - DNS
  - Cloud
  - GCP
techniques:
  - '[[External Remote Services]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8c2f9f37-cc11-4813-a67f-edf19096a996
created_at: '2025-12-14T05:32:23.721Z'
updated_at: '2025-12-14T05:32:23.721Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Claim-Abandoned-Subdomain

## Summary

This procedure involves registering an abandoned subdomain on a cloud provider's platform after identifying a dangling DNS record, granting the attacker control over the domain. It was used to claim a subdomain under mozgcp.net by exploiting the unclaimed service pointer.

## Description

Dangling records occur when DNS entries point to deleted resources (e.g., GCP projects), leaving the subdomain available for third-party registration. The attacker accesses the provider's console, searches for the subdomain, and claims it, updating records to their own hosting. Prerequisites: A provider account and the vulnerable subdomain name. Outcomes: Full DNS control, enabling malicious use.

## Requirements

1. Account on the target DNS provider (e.g., Google Cloud)
2. Identified dangling subdomain from prior recon
3. Web browser for console access

## Defense

Defensive measures and detection strategies:

- Automate subdomain inventory and cleanup of unused records
- Monitor for unauthorized registrations on cloud platforms
- Use certificate transparency logs to detect hijacked subdomains

## Objectives

1. Secure ownership of the vulnerable subdomain
2. Redirect DNS to attacker-controlled resources
3. Establish persistence for further attacks

## Instructions

### Step 1: Access Provider Console

**Context**: Log into the cloud provider's management interface to check subdomain availability.

Navigate to the DNS or domain registration section (e.g., GCP Cloud DNS console) and search for the subdomain (e.g., vulnerable.mozgcp.net).

No command needed; use the web UI to verify the resource is unclaimed due to the dangling record.

### Step 2: Register and Update DNS

**Context**: Claim the subdomain and configure it to point to your service.

In the console, initiate registration, provide payment/details if required, and add DNS records (e.g., A record to your IP or CNAME to your hosting).

Wait for propagation (use dig to verify).

**Expected Output**: Dashboard confirmation of ownership and updated DNS resolution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[subdomain-takeover]]
- [[cloud-misconfig]]
