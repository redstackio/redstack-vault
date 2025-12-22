---
id: proc-cloudflare-login-001
tags:
  - authentication
  - cloudflare
  - web
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.503Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Cloudflare-Dashboards

## Summary

This procedure establishes active sessions in both the Cloudflare Dashboard and Zero Trust Dashboard using their shared login mechanism, setting the stage for exploiting session independence.

## Description

In the context of testing Cloudflare's authentication, this involves using valid credentials to authenticate into the unified login system that powers both dashboards. The shared mechanism creates parallel sessions without additional prompts, which is normal but becomes vulnerable when combined with improper logout synchronization. Prerequisites include a Cloudflare account with Zero Trust enabled. Expected outcome is dual access for further session manipulation testing.

## Requirements

1. Valid Cloudflare email and password
2. Web browser with cookies enabled
3. Internet access to Cloudflare domains

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to add layers beyond session tokens
- Monitor for anomalous login patterns from the same IP or device
- Use session binding to IP or user-agent for added validation

## Objectives

1. Gain initial access to both dashboards
2. Verify shared authentication propagation
3. Prepare for session isolation testing

## Instructions

### Step 1: Access Cloudflare Dashboard Login

**Context**: Initiate authentication to create the primary session.

Navigate to https://dash.cloudflare.com/login in your web browser. Enter your Cloudflare email and password, then submit the form.

> Upon success, you will be redirected to the Dashboard homepage, confirming session establishment.

### Step 2: Access Zero Trust Dashboard

**Context**: Leverage the shared session to access the secondary interface without re-authentication.

From the Dashboard, click on the Zero Trust icon or navigate directly to https://dash.teams.cloudflare.com. The session should carry over seamlessly.

> Expected output: Zero Trust Dashboard loads with your account's configurations visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[cloudflare]]
