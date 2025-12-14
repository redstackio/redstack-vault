---
tags:
  - subdomain-takeover
  - custom-domain
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.262Z'
sub_techniques: []
id: 5bccdd33-6615-4325-b9ab-980c07f16e9f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add Dangling Custom Domain to GitLab Pages

## Summary

This procedure adds a dangling custom domain to a GitLab Pages project, exploiting the lack of immediate verification to claim and serve content on the victim's subdomain.

## Description

GitLab Pages allows custom domains if DNS points to their infrastructure, but without upfront checks, attackers can add any dangling domain (CNAME to gitlab-com.gitlab.io). This triggers proxying of attacker content. Scenario: Post-setup in takeover chain; targets GitLab SaaS/self-hosted. Prerequisites: Disabled HTTPS, verified DNS. Impacts: Phishing, cookie stealing, 7-day grace period.

## Requirements

1. GitLab Pages project with HTTPS disabled
2. Known dangling domain with correct CNAME
3. Project access for configuration

## Defense

Defensive measures and detection strategies:

- Implement real-time domain ownership verification (e.g., TXT records)
- Monitor DNS changes and Pages domain additions
- Periodically scan for dangling subdomains using automated tools

## Objectives

1. Bind attacker site to victim domain
2. Initiate content serving without ownership proof
3. Exploit 7-day verification window

## Instructions

### Step 1: Enter Custom Domain

**Context**: Input the dangling domain in Pages settings.

**Command** (UI Action):

> In Settings > Pages, add 'docs-dev.gitlab.com' under Custom domains and save.

### Step 2: Confirm Addition

**Context**: Verify the domain is accepted and active.

**Command** (UI Check):

> Save; expected: Domain listed without errors. GitLab begins serving content immediately.

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
- [[custom-domain]]
- [[gitlab]]
