---
id: proc-uuid-3
name: Search-GitHub-for-Leaked-Credentials
tags:
  - credential-access
  - github-search
  - leak-discovery
type: procedure
tools:
  - '[[tools/GitHub]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:28:44.326Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Search GitHub for Leaked Credentials

## Summary

This procedure uses GitHub's search functionality to query for a specific hostname extracted from a TLS certificate, uncovering exposed admin credentials in public repository commits that can be reused for GitLab access.

## Description

Public code repositories like GitHub often contain accidental leaks of credentials due to poor redaction in commits. By searching for unique identifiers like internal hostnames, attackers can find credentials intended for services like Jenkins but applicable to default GitLab root accounts. This targets web-based GitHub with no special access required.

## Requirements

1. GitHub account (optional for basic search)
2. Target hostname from TLS cert
3. Web browser access to github.com

## Defense

Defensive measures and detection strategies:

- Scan commits for secrets using tools like TruffleHog before pushing
- Use GitHub's secret scanning feature
- Implement branch protection and require PR reviews to catch leaks

## Objectives

1. Locate public commits with credential exposure
2. Extract usable username/password pairs
3. Confirm applicability to target service

## Instructions

### Step 1: Perform GitHub Search

**Context**: Query GitHub using the exact hostname to find relevant commits.

In GitHub search bar, enter:

[target-hostname]

> Results show repositories and commits; filter to code for credential snippets.

### Step 2: Review Commit for Credentials

**Context**: Inspect the found commit for leaked values.

Navigate to the repository commit, e.g., titled '[redacted] ([redacted])', and locate lines like JENKINS_OC_USER=root and JENKINS_OC_PASSWD=[password].

> Note the default 'root' username for GitLab compatibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files]]

## Commands Used


## Tools Used

- [[tools/GitHub]]

## Tags

- [[credential-access]]
- [[github-search]]
- [[leak-discovery]]
