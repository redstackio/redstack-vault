---
tags:
  - subdomain-takeover
  - webflow
  - account-creation
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
updated_at: '2025-12-14T05:32:23.972Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c7b6aaa4-e150-40ff-8a62-63a852e5b6a1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-Webflow-Account-for-Takeover

## Summary

This procedure outlines the creation of a Webflow account to enable claiming and hosting on dangling subdomains configured with CNAME records pointing to Webflow's proxy services, facilitating subdomain takeover attacks.

## Description

In a subdomain takeover scenario, the target's DNS includes a CNAME record for a subdomain (e.g., learnstormindia.khanacademy.org) pointing to an unused Webflow proxy (proxy-ssl.webflow.com). Since the resource is abandoned, registering a Webflow account allows the attacker to associate the subdomain with their own site. This step is the prerequisite for hosting malicious content, leading to phishing, malware, or other exploits targeting users who visit the subdomain expecting legitimate Khan Academy content. The process requires only basic web access and takes minutes, but custom domain support necessitates a paid Webflow plan.

## Requirements

1. Internet access and a web browser (e.g., Chrome, Firefox).
2. An email address for account verification.
3. Approximately $15 for a Webflow paid plan to enable custom domains (free tier insufficient).

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or subfinder.
- Monitor third-party services for unused resources and remove associated DNS entries.
- Implement domain verification workflows before adding CNAMEs to external providers.

## Objectives

1. Establish control over Webflow hosting to claim the target subdomain.
2. Prepare for content deployment to exploit user trust in the subdomain.
3. Enable rapid propagation of malicious payloads to visitors.

## Instructions

### Step 1: Access Webflow Registration

**Context**: Begin the account creation process to gain platform access.

Navigate to https://webflow.io and click 'Sign up'.

> Fill in email, password, and other details. No command execution required; this is a web form submission.

### Step 2: Verify Account

**Context**: Confirm ownership to activate the account.

Check your email for the verification link from Webflow and click it to activate.

> Upon success, you'll be redirected to the Webflow dashboard. If no email arrives, check spam or resend from the login page.

### Step 3: Upgrade for Custom Domains

**Context**: Enable features needed for subdomain claiming.

In the dashboard, go to Account Settings and upgrade to a Site plan (starting at ~$15/month) to unlock custom domain support.

> Paid plans allow adding external domains like the target's CNAME; free plans are limited to Webflow subdomains.

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
- [[webflow]]
- [[account-creation]]
