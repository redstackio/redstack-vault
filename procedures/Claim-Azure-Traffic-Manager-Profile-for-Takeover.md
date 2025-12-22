---
id: p3c4d5e6-f7g8-9012-cdef-345678901234
tags:
  - azure
  - takeover
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Cloud (Microsoft Azure)
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[T1583.001]]'
updated_at: '2025-12-14T04:38:49.551Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1583.001]]'
---
# Claim-Azure-Traffic-Manager-Profile-for-Takeover

## Summary

This procedure registers an unclaimed Azure Traffic Manager profile to hijack the associated subdomain's traffic routing.

## Description

By creating the profile s00149tmppcrpt.trafficmanager.net in Azure, the attacker inherits control over wfmnarptpc.starbucks.com's DNS resolution, allowing traffic redirection to malicious endpoints. This exploits misconfigurations where cloud resources are deleted but DNS remains.

## Requirements

1. Valid Azure subscription and account
2. Access to Azure portal
3. Endpoint name from DNS reconnaissance

## Defense

Defensive measures and detection strategies:

- Remove DNS records immediately upon resource deletion
- Monitor for unauthorized profile creations via Azure activity logs
- Implement just-in-time resource provisioning

## Objectives

1. Acquire control over the Traffic Manager
2. Redirect subdomain traffic
3. Enable malicious hosting

## Instructions

### Step 1: Create Profile in Azure Portal

**Context**: Navigate to Traffic Manager and register the exact name to claim it.

In portal.azure.com, go to Traffic Manager profiles > Create, enter name "s00149tmppcrpt", routing method (e.g., Performance), and domain suffix ".trafficmanager.net".

> Azure allows creation if unregistered, granting immediate control.

### Step 2: Configure Endpoints

**Context**: Add endpoints to route traffic to attacker-controlled servers.

Add external endpoints pointing to a hosted server IP or domain.

> Save changes; DNS propagation takes minutes to hours.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1583.001]] Acquire Infrastructure: Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[azure]]
- [[takeover]]
- [[initial-access]]
