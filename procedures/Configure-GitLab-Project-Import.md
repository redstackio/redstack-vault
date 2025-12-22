---
id: proc-gitlab-config-import-001
tags:
  - ssrf
  - gitlab
  - configuration
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
updated_at: '2025-12-14T04:08:47.809Z'
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
# Configure-GitLab-Project-Import

## Summary

This procedure sets up the GitLab project import feature using 'Repo by URL' to prepare for SSRF exploitation by ensuring arbitrary URLs can be submitted.

## Description

In a GitLab environment, the project import functionality allows users to pull repositories from external URLs. Due to lack of validation, this can be abused for SSRF. This step involves logging in and accessing the import interface, assuming the feature is enabled. If disabled, administrative access may be needed, but for standard exploitation, user-level access suffices. The target is a GitLab instance exposed on the web, with internal services running on localhost ports.

## Requirements

1. Authenticated GitLab user account with project creation permissions
2. Web browser access to the GitLab UI
3. GitLab version vulnerable to unvalidated URL imports (pre-patch for CVE-2017-9181 or similar)

## Defense

Defensive measures and detection strategies:

- Disable or restrict 'Repo by URL' imports to trusted domains only
- Implement URL whitelisting and block localhost/internal IPs in GitLab configuration
- Monitor import logs for suspicious URLs (e.g., 127.0.0.1, localhost)

## Objectives

1. Gain access to the project import interface
2. Verify no URL validation is enforced
3. Prepare for submission of internal-targeting URLs

## Instructions

### Step 1: Log In and Navigate to Project Creation

**Context**: Authenticate to the GitLab instance and locate the import option to confirm accessibility.

Log in via the web interface at `https://gitlab.example.com/users/sign_in`. After login, click 'New Project' and select 'Import project' > 'Repo by URL'.

> If the option is missing, check Admin Area settings under General > Visibility and access controls > Import sources, and enable if possible (requires admin).

### Step 2: Verify Import Functionality

**Context**: Test the interface with a benign URL to ensure it processes requests without validation errors.

Enter a test URL like `https://github.com/example/repo.git` and attempt import. Observe if GitLab fetches the URL.

> Successful test shows the import initiating, confirming the feature is active for exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- gitlab
- configuration
