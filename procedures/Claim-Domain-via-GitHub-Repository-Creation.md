---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - domain-takeover
  - github
  - hijacking
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
updated_at: '2025-12-14T04:51:26.472Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim-Domain-via-GitHub-Repository-Creation

## Summary

This procedure achieves domain takeover by creating a GitHub repository matching the target domain name and configuring it for Pages, hijacking the existing DNS CNAME.

## Description

For domains like obviousengine.com pointing to GitHub Pages, an attacker creates a repo named obviousengine.com, enables Pages, adds a CNAME file, and deploys content. This leverages GitHub's policy allowing public repo claims for unowned Pages pointers, granting full hosting control for phishing or malware. Requires a free GitHub account; immediate effect due to existing DNS.

## Requirements

1. GitHub account with repository creation permissions
2. Confirmed dangling DNS from prior step
3. Basic Git knowledge for pushing files

## Defense

Defensive measures and detection strategies:

- Proactively claim GitHub repos for all domains pointing to Pages
- Use GitHub's domain verification features
- Monitor certificate transparency logs for unauthorized certs on owned domains

## Objectives

1. Hijack the domain's web presence
2. Host arbitrary content under the domain
3. Demonstrate control for phishing or reputation damage

## Instructions

### Step 1: Create Repository

**Context**: Match the exact domain name to claim the pointer.

Log in to GitHub, create a new public repository named "obviousengine.com".

### Step 2: Configure GitHub Pages

**Context**: Enable hosting and set up DNS alias.

In repo settings, go to Pages and select the main branch. Create a CNAME file in the repo root with content "obviousengine.com", then commit and push.

### Step 3: Deploy and Verify Content

**Context**: Confirm takeover by customizing the site.

Add an index.html file with custom content (e.g., "Domain Taken Over"), commit, and wait ~1-2 minutes for Pages deployment. Revisit the domain to see the new page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[domain-takeover]]
- [[github]]
- [[hijacking]]
