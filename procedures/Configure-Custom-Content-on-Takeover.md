---
tags:
  - content-injection
  - redirect
type: procedure
tools:
  - '[[tools/Feed-Press]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T04:51:10.706Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b4959451-2944-47d8-9833-36813afc60ff
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Configure-Custom-Content-on-Takeover

## Summary

This procedure sets up arbitrary content, such as redirects, on a taken-over subdomain using the third-party service dashboard.

## Description

After claiming podcasts.slack-core.com on Feed.Press, configure redirects or hosted material. In this case, a root path redirect to https://hackerone.com demonstrates control, potentially enabling phishing on port 80 via nginx.

## Requirements

1. Control of the Feed.Press account
2. Propagated DNS
3. Knowledge of service configuration options

## Defense

Defensive measures and detection strategies:

- Scan for unexpected redirects on subdomains
- Implement content security policies (CSP)
- Alert on changes to subdomain content

## Objectives

1. Serve custom HTTP responses
2. Demonstrate impact (e.g., redirects)
3. Enable further attacks like phishing

## Instructions

### Step 1: Access Dashboard Configuration

**Context**: Navigate to domain settings.

Log in to Feed.Press and select the custom domain.

> Expected: Configuration panel open.

### Step 2: Set Redirect Rule

**Context**: Define custom behavior for paths.

Configure / to redirect to https://hackerone.com (301).

> Expected: Rule saved; immediate effect post-propagation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell (adapted for web config)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Feed-Press]]

## Tags

- [[content-injection]]
- [[redirect]]
