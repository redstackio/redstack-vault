---
tags:
  - ssrf
  - gitlab
  - email-injection
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - GitLab
techniques:
  - '[[Unsecured Credentials]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 59f179ef-9157-4c9a-a7a9-74e486753bbb
created_at: '2025-12-14T00:11:16.688Z'
updated_at: '2025-12-14T00:11:16.688Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Chain XSS to SSRF Attack

## Summary

This procedure uses injected stylesheet links to perform SSRF via premailer-rails, accessing internal services like Google metadata.

## Description

The network strategy in premailer-rails loads arbitrary URLs, enabling SSRF to internal endpoints when processing emails.

## Requirements

1. Active XSS in an issue
2. Email notification setup
3. Target internal URLs known

## Defense

Defensive measures and detection strategies:

- Block external URL loading in premailer-rails
- Monitor for anomalous network requests from email processor

## Objectives

1. Inject links targeting internal URLs
2. Access and leak internal data
3. Achieve SSRF impact

## Instructions

### Step 1: Inject SSRF Links

**Context**: Post comment with SSRF payloads.

Inject: <link rel='stylesheet' href='http://metadata.google.internal/computeMetadata/v1beta1'>.

> This requests internal metadata.

### Step 2: Capture Response in Email

**Context**: Trigger email and extract data.

Send notification and check inlined content for SSRF response.

> Expected: Internal data leaked in email.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- ssrf
- gitlab
- email-injection
