---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - subdomain-takeover
  - cloud
  - gcp
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Cloud (GCP)
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.731Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-Pointed-Service-for-Takeover

## Summary

This procedure claims ownership of an external service (e.g., a cloud endpoint) referenced by a dangling DNS record, thereby taking control of the subdomain resolution.

## Description

Following identification of a dangling CNAME under mozgcp.net pointing to an unregistered GCP service, the attacker registers the service using a free or paid account. This misconfiguration allows resolution of the subdomain to the attacker's controlled resource, enabling further exploitation like phishing. No technical barriers exist if the service is truly abandoned.

## Requirements

1. Account on the pointed service provider (e.g., Google Cloud)
2. Exact identifier from DNS record
3. Basic web access to registration portal

## Defense

Defensive measures and detection strategies:

- Monitor cloud service registrations for domains you own
- Remove unused DNS records promptly
- Use subdomain validation tools to detect takeovers

## Objectives

1. Gain control over the service
2. Redirect subdomain traffic to attacker resources
3. Enable content hosting

## Instructions

### Step 1: Access Service Provider

**Context**: Log in or create an account on the provider matching the DNS pointer.

Navigate to the GCP console if applicable and search for the resource name.

> No command; web-based registration. Expected: Account setup confirmation.

### Step 2: Claim the Resource

**Context**: Register the exact service alias to hijack resolution.

For a GCP example, create a load balancer or bucket with the matching name.

> Upon success, re-query DNS to confirm resolution to your service.

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
- [[cloud]]
