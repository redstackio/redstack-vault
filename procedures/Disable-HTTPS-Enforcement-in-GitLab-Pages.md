---
tags:
  - gitlab
  - https
  - bypass
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
updated_at: '2025-12-14T04:38:49.266Z'
sub_techniques: []
id: c68bd8cc-76e1-4356-812c-f86fcf0171d3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Disable HTTPS Enforcement in GitLab Pages

## Summary

This procedure disables HTTPS enforcement in a GitLab Pages project to bypass certificate and domain verification, allowing unverified custom domains to be added and content served immediately.

## Description

By default, GitLab Pages requires valid TLS certificates for custom domains, but disabling this option skips verification. This misconfiguration exploit enables subdomain takeover on dangling domains. Used in attack scenarios where attackers add victim subdomains without proof of ownership. Target: GitLab Pages settings; prerequisites: Existing Pages project. Outcomes: 7-day window to serve malicious content before disablement.

## Requirements

1. Access to GitLab project with Pages enabled
2. Project maintainer or owner role
3. No additional tools; UI-based

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS globally in GitLab instance configs
- Audit Pages settings for disabled enforcement
- Alert on custom domain additions without verification

## Objectives

1. Bypass TLS validation for custom domains
2. Enable immediate content proxying
3. Facilitate unverified domain claiming

## Instructions

### Step 1: Access Pages Configuration

**Context**: Navigate to the project's Pages settings to modify security options.

**Command** (UI Navigation):

> Go to Project > Settings > Pages (under Deploy section).

### Step 2: Disable Enforcement

**Context**: Uncheck the HTTPS option to skip checks.

**Command** (UI Action):

> Uncheck 'Force HTTPS (requires valid certificates)' and save changes. Expected: Setting updated without errors, allowing HTTP-only domain additions.

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
- [[https]]
- [[bypass]]
