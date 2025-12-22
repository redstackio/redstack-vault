---
tags:
  - subdomain-takeover
  - webflow
  - impersonation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-verify-takeover]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.885Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 42cf006e-7577-440e-beee-da52685c7a42
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim Unused Webflow Site for Takeover

## Summary

This procedure exploits a dangling DNS record by claiming the associated unused Webflow site, allowing control over the subdomain to host phishing or malicious content under the target's domain.

## Description

Once a dangling record is identified (e.g., sales.mixmax.com to Webflow IP), the attacker registers on Webflow and claims the unused site linked to the proxy. This takes over the subdomain without altering the target's DNS. The target is web-hosted services using third-party site builders. Prerequisites: Webflow account. Outcomes: Full subdomain control, enabling brand impersonation or phishing attacks.

## Requirements

1. Free Webflow account for site claiming
2. Knowledge of the dangling IP and service
3. Browser access to Webflow dashboard

## Defense

Defensive measures and detection strategies:

- Promptly delete unused sites in third-party dashboards
- Monitor DNS for external resolutions and audit integrations
- Use subdomain takeover detection tools like dnsrecon or subjack

## Objectives

1. Gain unauthorized control of the subdomain
2. Host malicious content for phishing
3. Impersonate the brand to steal credentials or data

## Instructions

### Step 1: Access Webflow and Search for Site

**Context**: Log into Webflow and check for available/unused sites matching the dangling record.

**Command**: No CLI; use web interface to create/claim site.

> In Webflow dashboard, create a new site and configure it to the proxy endpoint. If dangling, it becomes active under the subdomain.

### Step 2: Verify Takeover

**Context**: Test the subdomain to confirm attacker content loads.

**Command** ([[commands/curl-verify-takeover]]):
```bash
curl https://sales.mixmax.com
```

> Output should now show custom HTML or attacker page instead of 404, confirming successful takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-takeover]]

## Tools Used

- Webflow (web interface)

## Tags

- [[webflow-takeover]]
- [[Phishing]]
