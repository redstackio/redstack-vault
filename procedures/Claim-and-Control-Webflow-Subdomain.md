---
id: proc-uuid-claim
tags:
  - subdomain-takeover
  - webflow
  - domain-claim
  - hosting-control
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Resource Development]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1583.003]]'
updated_at: '2025-12-14T04:51:26.343Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Resource Development]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1583.003]]'
---
---
id: proc-uuid-claim
name: Claim-and-Control-Webflow-Subdomain
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Initial Access]], [[Resource Development]]
techniques: [[Exploit Public-Facing Application]], [[T1583.003]]
sub_techniques: []
tags: subdomain-takeover, webflow, domain-claim, hosting-control
platforms: Web
commands: []
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
---

# Claim-and-Control-Webflow-Subdomain

## Summary

This procedure details the steps to create a Webflow account, upgrade it, set up a site, and claim an unclaimed custom domain like jet.acronis.com, granting full control for hosting malicious content or redirects.

## Description

Subdomain takeover exploitation involves registering with the third-party service (Webflow) and associating the dangling domain with an attacker-controlled site. This targets web hosting platforms where DNS misconfigurations allow external claims. The process requires a paid Webflow plan for custom domains and results in complete subdomain ownership, including SSL issuance. Prerequisites: Confirmed unclaimed status from detection. Expected outcomes: Attacker site live on the subdomain, enabling phishing, malware hosting, or traffic redirection.

## Requirements

1. Valid email for Webflow signup
2. Payment method for Webflow upgrade (basic plan ~$12/month)
3. Confirmed unclaimed domain from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Delete or redirect dangling DNS records promptly after service decommissioning
- Monitor for unexpected SSL certificates on subdomains using tools like crt.sh
- Implement automated alerts for changes in third-party service claims

## Objectives

1. Gain ownership of the subdomain through Webflow
2. Deploy custom content to demonstrate control
3. Enable advanced attacks like phishing or credential theft

## Instructions

### Step 1: Create Webflow Account

**Context**: Establish presence on the platform to access domain claiming features.

Visit https://webflow.com and complete the signup form with email and password.

> Receive and verify email; log in to dashboard.

### Step 2: Upgrade Account Plan

**Context**: Enable custom domain functionality, unavailable on free tiers.

In dashboard, go to Account Settings > Plans and upgrade to Site Plan (Basic).

> Complete payment; confirm upgrade in settings.

### Step 3: Create New Site

**Context**: Prepare a project to link the custom domain.

Click "New Blank Site" in the dashboard and name it appropriately.

> Site editor opens; save initial blank page.

### Step 4: Add and Claim Custom Domain

**Context**: Associate the unclaimed domain with the site to take ownership.

Go to Project Settings > Hosting > Custom Domains > Add Domain, enter jet.acronis.com, and follow verification (Webflow handles CNAME check).

> Domain status updates to connected; propagation may take minutes.

### Step 5: Publish and Validate Control

**Context**: Deploy content and confirm subdomain resolution to attacker site.

Edit site with PoC content (e.g., <h1>Takeover Successful</h1>), publish, and revisit https://jet.acronis.com.

> Custom content loads; check source for Webflow embeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Resource Development]] Resource Development

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[T1583.003]] Virtual Private Server

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[webflow]]
- [[domain-claim]]
- [[hosting-control]]
