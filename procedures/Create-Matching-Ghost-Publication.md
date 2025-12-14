---
tags:
  - publication-setup
  - ghost.io
  - subdomain-takeover
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
  - '[[Email Accounts]]'
updated_at: '2025-12-14T04:51:26.545Z'
sub_techniques: []
id: 80822b91-59cd-4fca-8443-dbdea6138760
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Email Accounts]]'
---
# Create-Matching-Ghost-Publication

## Summary

This procedure creates a new Ghost publication with a name matching the inactive subdomain alias, setting the stage for DNS-based claiming in a takeover scenario.

## Description

Once a Ghost Pro account is active, users can create publications—essentially sites or blogs—that can be linked to custom domains. For subdomain takeover, the publication name must exactly match the abandoned Ghost.io subdomain (e.g., 'udemy-engineering-blog') to hijack the CNAME. This step occurs in the Ghost dashboard and prepares for validation without altering the target's DNS.

## Requirements

1. Active Ghost Pro account
2. Exact name of the inactive subdomain from DNS recon
3. Web browser access to dashboard

## Defense

Defensive measures and detection strategies:

- Periodically scan for and remove unused CNAME records
- Use DNS security extensions (DNSSEC) to prevent unauthorized claims
- Monitor for new content on engineering subdomains

## Objectives

1. Establish a publication aligned with the target alias
2. Enable subsequent DNS configuration
3. Facilitate content serving post-takeover

## Instructions

### Step 1: Log In to Dashboard

**Context**: Access the Ghost Pro interface to start publication creation.

No command; log in at https://ghost.org/ with credentials.

> Navigate to 'Publications' section.

### Step 2: Create New Publication

**Context**: Name it to match the CNAME target for seamless claiming.

No command; click 'New Publication' and enter name 'udemy-engineering-blog' (or equivalent).

> Expected: Publication listed in dashboard, ready for customization.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Email Accounts]] Compromise Accounts: Third-party Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[publication-setup]]
- [[ghost.io]]
- [[subdomain-takeover]]
