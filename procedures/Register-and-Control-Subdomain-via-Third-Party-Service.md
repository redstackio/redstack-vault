---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - subdomain-takeover
  - registration
  - tumblr
  - impersonation
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
updated_at: '2025-12-14T04:51:10.686Z'
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
# Register and Control Subdomain via Third-Party Service

## Summary

This procedure registers an unused subdomain on a third-party service like Tumblr to gain control, enabling hosting of malicious content or phishing under the target's domain.

## Description

Exploiting the dangling CNAME, an attacker creates a Tumblr blog at the subdomain (e.g., ux.shopify.com), password-protecting it as proof-of-concept. This grants full control, allowing brand impersonation or malicious redirects. In the Shopify report, a password-protected blog was created, demonstrating impact despite being out-of-scope for bounty.

## Requirements

1. Confirmed unused subdomain from prior verification
2. Tumblr account or ability to register one
3. Web browser for manual signup

## Defense

Defensive measures and detection strategies:

- Automate DNS cleanup post-migration
- Monitor for new content on subdomains via certificate transparency logs
- Block third-party subdomain claims through service policies

## Objectives

1. Claim control over the subdomain
2. Host proof-of-concept content
3. Demonstrate potential for phishing or impersonation

## Instructions

### Step 1: Create Tumblr Account

**Context**: Sign up for a Tumblr account if not already available.

No command; navigate to tumblr.com and register with email.

> Expected: Valid account for blog creation.

### Step 2: Register Subdomain Blog

**Context**: Initiate blog creation specifying the subdomain (ux.shopify.com) and set password protection.

No command; use Tumblr's dashboard to create a new blog at the custom domain, entering the CNAME details.

> Expected: Blog live at http://ux.shopify.com with password (e.g., c7gBX6gELPFLhYOeYxQD). Verify by accessing and entering password.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[subdomain-takeover]]
- [[registration]]
