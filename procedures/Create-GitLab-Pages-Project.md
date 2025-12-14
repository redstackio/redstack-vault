---
tags:
  - gitlab
  - pages
  - setup
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
updated_at: '2025-12-14T04:38:49.270Z'
sub_techniques: []
id: 9cd966d1-7a0e-4275-94e6-c8a5e8f58e47
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create GitLab Pages Project

## Summary

This procedure creates a new GitLab project configured for Pages to host attacker-controlled content, setting the stage for subdomain takeover by preparing a site that can be bound to a dangling domain.

## Description

GitLab Pages allows static site hosting from repositories. Attackers create a project, add malicious HTML/JS (e.g., for phishing), and enable Pages. This is used in takeover attacks to serve content on victim subdomains immediately upon domain addition, bypassing verification. The target environment is any GitLab instance (self-hosted or SaaS) with Pages enabled. Prerequisites include a GitLab account; outcomes enable arbitrary content serving, leading to cookie theft or CSP bypass.

## Requirements

1. Active GitLab account (free tier works)
2. Git client for pushing content (git clone, add files, commit, push)
3. Basic web development knowledge to create static malicious pages

## Defense

Defensive measures and detection strategies:

- Monitor for new Pages projects with suspicious custom domains
- Require approval workflows for Pages deployments
- Scan for unverified domains in GitLab audit logs

## Objectives

1. Establish attacker-controlled hosting infrastructure
2. Prepare content for takeover deployment
3. Enable Pages feature for domain binding

## Instructions

### Step 1: Create New Project

**Context**: Log in to GitLab and initiate a blank project to host the Pages site.

**Command** (GitLab UI; no CLI):

> Navigate to https://gitlab.com/projects/new, name it (e.g., pn1), set visibility to public/private, and create. Clone locally: `git clone https://gitlab.com/username/pn1.git`

### Step 2: Add Content and Enable Pages

**Context**: Push static files and configure Pages deployment.

**Command** (Git operations):
```bash
git add .
git commit -m "Add malicious content"
git push origin main
```

> After push, go to project Settings > Pages, deploy from main branch. Expected: Pages URL like username.gitlab.io/pn1 becomes active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[pages]]
- [[setup]]
