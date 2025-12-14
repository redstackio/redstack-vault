---
id: proc-setup-enable-gitlab-bulkimport
tags:
  - gitlab
  - feature-flag
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/gitlab-rails-console]]'
  - '[[commands/feature-enable-bulk-import]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:14.630Z'
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
# Setup-and-Enable-GitLab-Bulk-Import-Feature

## Summary

This procedure sets up a GitLab instance for testing the BulkImports vulnerability and enables the required feature flag, allowing access to the DecompressedArchiveSizeValidator for command injection exploitation.

## Description

In a controlled environment, deploy GitLab v15.1.0-ee, create necessary groups and projects, generate an API token, and use the Rails console to enable the bulk_import_projects feature flag. This prepares the instance for importing from a malicious source, where the import_source parameter can be controlled to inject shell commands into the gzip validation command executed via Open3.popen3.

## Requirements

1. Access to a Linux server or VM for GitLab installation
2. Admin privileges on the GitLab instance
3. GitLab Omnibus package or Docker setup

## Defense

Defensive measures and detection strategies:

- Disable unused feature flags like bulk_import_projects
- Monitor Rails console access and feature changes via audit logs
- Restrict admin access to trusted users only

## Objectives

1. Prepare GitLab for BulkImports exploitation
2. Enable vulnerable feature without production impact
3. Generate credentials for API interactions

## Instructions

### Step 1: Spin Up GitLab Instance

**Context**: Deploy a local GitLab environment for safe testing.

**Command** ([[commands/gitlab-install]]):
No specific command; use GitLab Omnibus installer or Docker: `curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash && sudo EXTERNAL_URL="http://gitlab.example.com" apt-get install gitlab-ee`.

> Installs GitLab EE; configure via /etc/gitlab/gitlab.rb and run `sudo gitlab-ctl reconfigure`.

### Step 2: Create Group, Project, and API Token

**Context**: Set up resources needed for import simulation.

**Instructions**: Log in as admin, create a new group (e.g., 'test-group'), a project inside it, and generate a personal access token with api scope.

> UI-based; no CLI command.

### Step 3: Enable Feature Flag

**Context**: Activate BulkImports to trigger the validator.

**Command** ([[commands/gitlab-rails-console]]):
```bash
sudo gitlab-rails console
```

> Opens interactive Rails console.

**Command** ([[commands/feature-enable-bulk-import]]):
```ruby
::Feature.enable(:bulk_import_projects)
```

> Enables the flag; exit console with `exit`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/gitlab-rails-console]]
- [[commands/feature-enable-bulk-import]]

## Tools Used


## Tags

- gitlab
- feature-flag
