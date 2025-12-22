---
tags:
  - subdomain-takeover
  - sendgrid
  - exploitation
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
updated_at: '2025-12-14T04:38:39.376Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5746996a-a672-44e5-b3c4-f442ae2a0dbd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-Subdomain-on-Third-Party-Service

## Summary

This procedure outlines registering a dangling subdomain on a third-party service like SendGrid to achieve takeover, allowing control over traffic or emails directed to it.

## Description

Once a dangling CNAME is confirmed, an attacker creates an account on the service (e.g., SendGrid) and adds the subdomain as a custom domain. Verification succeeds due to the matching DNS record, granting control. For email subdomains, this enables inbound routing manipulation. Assumes public access to the service's dashboard; ethical use requires permission.

## Requirements

1. Attacker-controlled account on the third-party service (e.g., SendGrid free tier)
2. Confirmed dangling CNAME
3. Web browser for dashboard access

## Defense

Defensive measures and detection strategies:

- Audit and remove unused third-party integrations promptly
- Monitor service logs for unauthorized domain additions
- Use subdomain monitoring tools to alert on takeovers

## Objectives

1. Claim the subdomain on the service
2. Verify ownership via DNS
3. Gain control for further exploitation

## Instructions

### Step 1: Create Service Account

**Context**: Set up an account if not existing.

Navigate to SendGrid signup and create a free account.

> No command; web-based process.

### Step 2: Add Custom Domain

**Context**: Input the dangling subdomain in the service dashboard.

In SendGrid settings, go to Sender Authentication > Custom Domains, enter "email.smule.com", and verify.

> The service queries DNS, matches the CNAME, and approves without additional steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[sendgrid]]
- [[exploitation]]
