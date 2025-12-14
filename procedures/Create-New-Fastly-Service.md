---
id: p-create-fastly-service
tags:
  - domain-takeover
  - service-creation
type: procedure
tools:
  - '[[tools/Fastly-Management-Dashboard]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.677Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Fastly-Service

## Summary

This procedure covers initiating a new service in the Fastly dashboard, which serves as the container for domain configurations in a takeover attack.

## Description

Fastly services act as edge configurations for CDN delivery. Creating one allows attachment of custom domains, including vulnerable subdomains from the free TLS pool. In this attack, a new service is created with minimal details (e.g., name and description) to host the takeover. This step leverages Fastly's open provisioning, enabling any user to set up infrastructure that can hijack whitelisted domains like gl-canary.freetls.fastly.net. Expected outcome: A blank service ready for domain addition.

## Requirements

1. Logged-in Fastly session
2. Access to services management page
3. Basic service naming convention

## Defense

Defensive measures and detection strategies:

- Scan for unused or dangling subdomains in CDN whitelists
- Implement approval workflows for new service creations in enterprise accounts
- Monitor for services attaching to sensitive domain patterns

## Objectives

1. Establish a new CDN service instance
2. Provide groundwork for domain attachment
3. Enable subsequent configuration for malicious control

## Instructions

### Step 1: Initiate Creation

**Context**: Start the service setup process.

On the services page, click 'Create Service' and enter a name like 'test-takeover' and optional description.

### Step 2: Confirm and Save

**Context**: Finalize the service to make it active.

Review settings and click 'Create' to generate the service.

**Expected Output**: Service ID displayed, with options to edit domains and hosts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Fastly-Management-Dashboard]]

## Tags

- [[domain-takeover]]
- [[service-creation]]
