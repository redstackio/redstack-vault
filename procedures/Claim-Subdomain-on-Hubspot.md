---
id: proc-claim-subdomain-hubspot
tags:
  - subdomain-takeover
  - hubspot
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.573Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Subdomain-on-Hubspot

## Summary

This procedure claims control of a dangling subdomain by registering it on Hubspot after verifying an expired account, allowing hosting of arbitrary content on the victim's domain.

## Description

Exploiting the subdomain takeover, register the CNAME on a new Hubspot account to redirect traffic to your controlled infrastructure. For blog.greenhouse.io, this grants the ability to serve phishing pages or JavaScript on the greenhouse.io domain, leading to XSS risks. This applies to any expired SaaS integrations with DNS dependencies.

## Requirements

1. Free Hubspot account (signup required)
2. Verified dangling CNAME from prior steps
3. Basic web development knowledge for content upload

## Defense

Defensive measures and detection strategies:

- Monitor for unauthorized subdomain claims via service alerts and DNS change notifications
- Use domain shadowing prevention by locking DNS records and requiring multi-factor for changes
- Regularly scan for takeover risks with tools like Subjack or Takeover

## Objectives

1. Gain administrative control over the subdomain
2. Enable hosting of malicious payloads
3. Simulate impact for proof-of-concept

## Instructions

### Step 1: Register Hubspot Account

**Context**: Create a new account to access domain management features.

**Command** (Web signup):

> Visit hubspot.com, complete free signup, and verify email.

### Step 2: Add and Verify Subdomain

**Context**: Connect the dangling subdomain to your account.

**Command** (Hubspot UI):

> In Settings > Domains & URLs, add blog.greenhouse.io as a connected domain using the existing CNAME. Hubspot will verify via DNS propagation (may take minutes).

### Step 3: Upload Test Content

**Context**: Confirm control by hosting a simple page.

**Command** (Hubspot CMS):

> Use Hubspot's page builder or CMS to create and publish a test HTML page to the subdomain root.

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
- [[initial-access]]
