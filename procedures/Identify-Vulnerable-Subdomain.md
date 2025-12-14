---
id: proc-uuid-1
tags:
  - reconnaissance
  - subdomain-enumeration
  - shopify
  - aws
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud (AWS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:31:19.054Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Vulnerable-Subdomain

## Summary

This procedure involves locating a vulnerable subdomain, such as vpnify-data.ec2.shopify.io, that hosts a monitoring or VPN server with integrated Google OAuth authentication, setting the stage for exploitation.

## Description

In the context of Shopify's infrastructure, attackers can identify subdomains through public exposure or follow-up on prior reports (e.g., #143482). The target is an AWS EC2 instance running a VPN/monitoring service. Successful identification reveals a login flow vulnerable to authentication bypass. Prerequisites include basic web reconnaissance skills and access to public internet. Expected outcome is confirmation of the subdomain's existence and its authentication mechanism.

## Requirements

1. Internet access to query public domains.
2. Knowledge of target organization (e.g., Shopify subdomains).
3. Web browser for manual verification.

## Defense

Defensive measures and detection strategies:

- Implement subdomain monitoring tools like DNS logs to detect unusual queries.
- Use certificate transparency logs to track new subdomains.
- Restrict public exposure of internal service subdomains via DNS policies.

## Objectives

1. Discover hidden or misconfigured subdomains.
2. Verify presence of authentication interfaces.
3. Prepare for targeted exploitation.

## Instructions

### Step 1: Search for Target Subdomains

**Context**: Use manual or automated methods to find AWS-hosted subdomains related to VPN or monitoring services.

Focus on patterns like *.ec2.shopify.io. For Shopify, identify vpnify-data.ec2.shopify.io based on prior similar issues.

### Step 2: Verify Login Interface

**Context**: Access the subdomain and inspect for Google OAuth integration.

Navigate to https://vpnify-data.ec2.shopify.io/ in a browser. Look for a login page with Google sign-in options, confirming the OAuth flow without domain restrictions.

**Expected Output**: Page loads with Google login button; no immediate errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[subdomain-enumeration]]
