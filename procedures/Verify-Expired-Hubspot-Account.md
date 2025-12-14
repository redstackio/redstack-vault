---
id: proc-verify-expired-hubspot
tags:
  - hubspot
  - dns
  - vulnerability-discovery
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.574Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify-Expired-Hubspot-Account

## Summary

This procedure verifies if a DNS CNAME pointing to Hubspot infrastructure corresponds to an expired or cancelled account, enabling subdomain takeover by checking for inactive service associations.

## Description

Following a DNS lookup revealing a Hubspot alias, this step involves manual verification that the account linked to the subdomain is no longer active. In the Greenhouse.io case, the blog subdomain's pointer to san.secure001.hubspot.com.edgekey.net was claimable because the original integration expired, leaving the DNS record dangling. This targets SaaS integrations in web environments and requires understanding third-party service behaviors.

## Requirements

1. Access to a web browser for Hubspot signup and dashboard checks
2. Knowledge of the target CNAME from prior DNS lookup
3. Public access to the subdomain for content verification

## Defense

Defensive measures and detection strategies:

- Automate expiry checks for third-party accounts and remove DNS records immediately upon cancellation
- Use certificate transparency logs or subdomain monitoring tools to detect dangling records
- Implement webhook notifications from services like Hubspot for account status changes

## Objectives

1. Confirm account inactivity for the pointed service
2. Assess takeover feasibility without exploitation
3. Document evidence for responsible disclosure

## Instructions

### Step 1: Check Subdomain Content

**Context**: Attempt to access the subdomain to see if it serves active Hubspot content or defaults to errors, indicating expiry.

**Command** (Browser access):

> Navigate to http://blog.greenhouse.io/. If it shows a blank, error, or Akamai default page instead of Hubspot-hosted content, the account is likely expired.

### Step 2: Test Hubspot Claiming Process

**Context**: Sign up for Hubspot and attempt to add the subdomain to verify availability.

**Command** (No CLI; web UI):

> In Hubspot dashboard, go to Settings > Domains & URLs > Connect a domain, and enter the CNAME. If accepted without conflict, the original account is inactive.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[hubspot]]
- [[DNS]]
