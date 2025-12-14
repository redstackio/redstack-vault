---
tags:
  - setup
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
updated_at: '2025-12-14T03:15:05.473Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: cb189cd0-5d08-4112-99a0-71e85cbec713
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-New-Site-on-IntenseDebate

## Summary

This procedure creates a new site within an authenticated IntenseDebate account, generating a unique site ID that serves as the injection point for SQL vulnerability exploitation.

## Description

After authentication, users can install new sites via a simple form. This assigns a numeric site ID used in API endpoints like comment history. The process is straightforward but essential for targeting the vulnerable parameter in subsequent injection steps. Expected outcome is a functional site ready for endpoint testing.

## Requirements

1. Active authenticated session on IntenseDebate
2. Web browser access
3. Basic site details (name, URL placeholder)

## Defense

Defensive measures and detection strategies:

- Rate-limit site creation to prevent abuse
- Validate site details server-side to avoid malicious inputs
- Log and monitor new site registrations for suspicious patterns

## Objectives

1. Generate a valid site ID for vulnerability testing
2. Simulate legitimate user behavior to avoid detection
3. Set up the environment for SQL injection

## Instructions

### Step 1: Navigate to Install Page

**Context**: Access the site creation interface from the dashboard.

From the dashboard, click on the install or add site option, directing to https://intensedebate.com/install.

> The form loads, ready for input.

### Step 2: Complete Site Creation Form

**Context**: Submit details to register the new site.

Fill in site name, description, and a placeholder URL, then submit the form.

> Success message appears, and the site is added to your dashboard list with an assigned ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[site-creation]]
- [[setup]]
