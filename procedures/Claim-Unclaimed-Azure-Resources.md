---
tags:
  - azure
  - cloud
  - takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Azure
  - Cloud
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: edc68c7e-7191-4ebf-87fa-f9d69c9209f5
created_at: '2025-12-14T04:51:26.613Z'
updated_at: '2025-12-14T04:51:26.613Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Unclaimed-Azure-Resources

## Summary

This procedure involves registering unclaimed Azure Traffic Manager endpoints referenced by dangling CNAME records, granting control over associated subdomains for potential exploitation.

## Description

Target unclaimed Azure Traffic Manager profiles like s00197tmp0crdfulload0.trafficmanager.net. Using an Azure subscription, create matching Traffic Manager resources to hijack DNS resolution for subdomains such as svcgatewayloadus.starbucks.com. This allows routing traffic to attacker-controlled infrastructure, setting up for phishing or content injection in a cloud-based attack scenario.

## Requirements

1. Active Azure subscription (free tier works for Traffic Manager)
2. Knowledge of unclaimed endpoint names from DNS recon
3. Azure portal access

## Defense

Defensive measures and detection strategies:

- Delete unused cloud resources promptly
- Use Azure Resource Manager locks on critical endpoints
- Monitor Azure activity logs for unauthorized profile creations

## Objectives

1. Gain ownership of unclaimed Traffic Manager endpoints
2. Redirect subdomain traffic to controlled servers
3. Prepare for content serving or further exploitation

## Instructions

### Step 1: Access Azure Portal

**Context**: Log in and navigate to create Traffic Manager resources.

**Instructions**: Sign in at portal.azure.com, search for "Traffic Manager profiles", and create a new profile with the exact name of the unclaimed endpoint (e.g., s00197tmp0crdfulload0).

### Step 2: Configure Endpoints

**Context**: Set up routing to point to your server.

**Instructions**: Add endpoints in the profile configuration to forward traffic to an IP or hostname under your control. Save and wait for DNS propagation (TTL typically 300 seconds).

### Step 3: Verify Claim

**Context**: Confirm control by resolving the subdomain.

**Instructions**: Re-run a dig query on the subdomain to ensure it now resolves to your configured endpoint without NXDOMAIN.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[azure]]
- [[cloud]]
- [[takeover]]
