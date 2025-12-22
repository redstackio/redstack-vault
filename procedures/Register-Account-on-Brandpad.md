---
tags:
  - account-creation
  - external-service
  - initial-access
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T04:38:39.873Z'
sub_techniques: []
id: 89c71fd8-7076-4c13-a576-ceae2b4d46ca
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Register-Account-on-Brandpad

## Summary

This procedure involves creating an account on the external service (Brandpad.io) identified via DNS, enabling the attacker to claim dangling subdomains.

## Description

Once a dangling CNAME is found pointing to a service like Brandpad.io, registering an account provides the interface to add custom DNS records. This step assumes the service allows open registration and subdomain claiming without verification, common in legacy or abandoned integrations.

## Requirements

1. Web browser
2. Valid email for registration
3. No prior credentials on the service

## Defense

Defensive measures and detection strategies:

- Services should require domain ownership proof (e.g., TXT records) for claims
- Monitor for new registrations attempting known dangling domains
- Deprecate unused third-party services entirely

## Objectives

1. Obtain dashboard access for DNS management
2. Prepare for subdomain claiming
3. Establish persistence on the service

## Instructions

### Step 1: Create Account

**Context**: Visit the service site and complete registration to gain access.

No command required; go to https://brandpad.io and fill out the signup form with email and password.

> Upon success, log in to access the domain management dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[initial-access]]
- [[external-service]]
