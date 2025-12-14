---
tags:
  - gitlab
  - setup
  - environment
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/gitlab-rake-env-info]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:34.065Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 324ee7da-bd2f-4a50-8cbf-2c4f5bf02888
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Self-Managed-GitLab-Instance

## Summary

This procedure sets up a local or self-hosted GitLab instance to replicate and test the stored XSS vulnerability in a controlled environment, ensuring the version matches the vulnerable one (e.g., 14.4.2-ee).

## Description

The attack requires a self-managed GitLab setup to initially discover and exploit the sanitization bypasses without affecting production. This involves installing GitLab CE/EE, configuring dependencies like PostgreSQL and Redis, and verifying the environment. The procedure targets web-based GitLab deployments and assumes basic server administration knowledge. Expected outcomes include a running instance on localhost:80 or a specified port, ready for issue creation and payload testing.

## Requirements

1. Linux server or VM with at least 4GB RAM and Ubuntu/Debian OS
2. Docker or Omnibus package for GitLab installation
3. Access to install services: PostgreSQL 12+, Redis 6+
4. Network access to download GitLab packages

## Defense

Defensive measures and detection strategies:

- Use official GitLab installation guides and apply security patches promptly
- Monitor server logs for unusual installation patterns or version mismatches
- Implement network segmentation to isolate test environments from production

## Objectives

1. Deploy a vulnerable GitLab instance for safe exploitation testing
2. Verify environment details to confirm exploitability
3. Prepare for subsequent attack stages like payload injection

## Instructions

### Step 1: Install GitLab Omnibus Package

**Context**: Download and install the GitLab package to set up the core application and dependencies.

**Command** (no specific command; use package manager):

Follow official docs: curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash, then sudo EXTERNAL_URL="http://gitlab.example.com" apt-get install gitlab-ee.

> This installs GitLab with default configs; adjust EXTERNAL_URL for your domain/IP.

### Step 2: Configure and Start Services

**Context**: Ensure PostgreSQL, Redis, and GitLab services are running.

**Command** (systemd):
```bash
sudo gitlab-ctl reconfigure
sudo gitlab-ctl start
```

> Reconfigures and starts all components; check status with gitlab-ctl status.

### Step 3: Verify Environment

**Context**: Confirm the GitLab version and dependencies match the vulnerable setup.

**Command** ([[commands/gitlab-rake-env-info]]):
```bash
gitlab-rake gitlab:env:info
```

> Outputs system info; look for GitLab Version: 14.4.2-ee, Ruby 2.7.4, etc. Access the instance at http://localhost to complete initial setup (create admin user).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/gitlab-rake-env-info]]

## Tools Used


## Tags

- gitlab
- setup
- environment
