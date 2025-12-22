---
id: proc-uuid-001
tags:
  - setup
  - gitlab
  - test-env
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:58.410Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-GitLab-Test-Environment

## Summary

This procedure sets up a vulnerable GitLab EE instance to test the blind SSRF vulnerability in the Jira OAuth integration, allowing safe reproduction of the attack without risking production systems.

## Description

The vulnerability exists in GitLab EE 11.2.1-ee's Oauth::Jira::AuthorizationsController#access_token endpoint, where unvalidated Host headers lead to SSRF via Gitlab::HTTP.post with allow_local_requests:true. This setup deploys an isolated instance to demonstrate arbitrary internal requests, potential access to unauthenticated endpoints, and availability impacts from 60-second timeouts.

## Requirements

1. Access to a Linux server or cloud VM (e.g., Ubuntu 18.04)
2. Docker or Omnibus package installer for GitLab EE
3. Internet access for downloading GitLab packages
4. Basic knowledge of server administration

## Defense

Defensive measures and detection strategies:

- Validate and sanitize Host headers in Rails controllers
- Disable allow_local_requests in HTTP clients or implement IP whitelisting
- Monitor for unusual delays in request processing (e.g., 60s timeouts)
- Use web application firewalls (WAF) to block anomalous Host header manipulations

## Objectives

1. Deploy a functional GitLab EE instance with the vulnerable version
2. Verify the Jira OAuth endpoint is accessible
3. Prepare for SSRF testing without external dependencies

## Instructions

### Step 1: Install GitLab EE

**Context**: Download and install GitLab EE 11.2.1-ee using the Omnibus package for a quick setup.

**Command** (no specific command, use official docs):
Follow the installation guide at https://docs.gitlab.com/ee/install/ to run:

```bash
curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash
sudo EXTERNAL_URL="https://your-gitlab.example.com" apt-get install gitlab-ee=11.2.1-ee.0
```

> This installs the exact vulnerable version. Configure external_url and start services with sudo gitlab-ctl reconfigure.

### Step 2: Verify Endpoint Accessibility

**Context**: Confirm the vulnerable endpoint responds to ensure the setup is correct.

**Command** ([[commands/curl-trigger-gitlab-ssrf]] - basic probe):

```bash
curl -X POST 'https://your-gitlab.example.com/-/jira/login/oauth/access_token'
```

> Expect a 404 or auth error, but no connection refusal, indicating the controller is present.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- setup
- gitlab
- test-env
