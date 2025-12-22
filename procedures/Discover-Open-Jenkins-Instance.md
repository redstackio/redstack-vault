---
tags:
  - jenkins
  - discovery
  - oauth-misconfig
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Jenkins
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Default Accounts]]'
id: 1ed19ea3-e842-4b83-936b-2d6e87bcb8af
created_at: '2025-12-11T06:10:15.843Z'
updated_at: '2025-12-11T06:10:15.843Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Discover Open Jenkins Instance

## Summary

This procedure involves identifying publicly accessible Jenkins instances misconfigured to allow Google OAuth login without restrictions, serving as an entry point for further exploitation.

## Description

Jenkins servers exposed to the internet with improper OAuth configurations can be discovered through reconnaissance techniques. This misconfiguration bypasses authentication controls, allowing any valid Google account to log in. The procedure focuses on non-intrusive discovery methods to avoid detection.

## Requirements

1. Internet access and search tools like Shodan or Google dorks.
2. Knowledge of Jenkins default paths (e.g., /login).
3. Valid Google account for verification (not used in this procedure).

## Defense

Defensive measures and detection strategies:

- Implement IP whitelisting and domain restrictions on OAuth providers.
- Monitor for unusual login attempts to Jenkins instances.

## Objectives

1. Locate exposed Jenkins server.
2. Confirm Google OAuth is enabled without restrictions.
3. Prepare for authentication bypass.

## Instructions

### Step 1: Reconnaissance

**Context**: Use search engines to find potential Jenkins instances.

Search for keywords like "inurl:jenkins login" or use Shodan queries for Jenkins ports (default 8080).

> Expected: List of potential URLs.

### Step 2: Verify Accessibility

**Context**: Access the URL and check for Google login option.

Navigate to the discovered URL and observe the authentication page.

> Expected: Google OAuth prompt without domain restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used

None

## Tools Used

None

## Tags

- jenkins
- discovery
- oauth-misconfig
