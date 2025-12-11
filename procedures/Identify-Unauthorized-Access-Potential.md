---
id: cc909b60-65f0-4c5b-bd1b-e7504c4796eb
name: Identify Unauthorized Access Potential
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:22.677Z'
updated_at: '2025-12-11T06:10:22.677Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - oauth
  - authentication-bypass
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---

# Identify Unauthorized Access Potential

## Summary

This procedure involves testing and observing whether a user without the required 'Apps' permission can access the Shopify Stocky app, highlighting potential authentication flaws.

## Description

In this procedure, a staff member or tester attempts to access the Stocky app using an account lacking proper permissions. The goal is to identify if the app allows entry, which indicates a vulnerability in the authentication process. This is typically done in a web environment targeting OAuth-integrated services.

## Requirements

1. Access to a Shopify account without 'Apps' permission
2. Web browser for initiating app access
3. Network connectivity to Shopify services

## Defense

Defensive measures and detection strategies:

- Implement strict permission checks at the end of OAuth flows
- Monitor access logs for unauthorized attempts

## Objectives

1. Confirm unauthorized access is possible
2. Document the observation for further analysis
3. Identify initial signs of OAuth misconfiguration

## Instructions

### Step 1: Attempt App Access

**Context**: Use a browser to navigate to the Stocky app URL and attempt login with an unauthorized account.

> Navigate to the app and observe if access is granted without errors.

### Step 2: Verify Access

**Context**: Check if app features are accessible despite lacking permissions.

> Interact with the app interface to confirm full or partial access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- oauth
- authentication-bypass
