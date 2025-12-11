---
tags:
  - sso
  - saml
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d3e79287-fefa-4963-a2b2-15b1e5e39594
created_at: '2025-12-11T03:47:39.572Z'
updated_at: '2025-12-11T03:47:39.572Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Configure and Verify Grammarly SSO

## Summary

This procedure sets up and verifies SSO for a Grammarly business account, establishing a baseline for legitimate authentication before exploiting vulnerabilities.

## Description

In this procedure, you configure SSO using SAML for a Grammarly business account, define the entityId, and test login functionality. This is a prerequisite for demonstrating conflicts in entityId handling. The target environment is Grammarly's web-based SSO integration, and success results in confirmed access without errors.

## Requirements

1. Access to Grammarly business account creation.
2. SAML Identity Provider setup capabilities.
3. Web browser for configuration and testing.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual SSO configuration changes.
- Implement strict entityId validation without trimming.

## Objectives

1. Establish legitimate SSO setup.
2. Verify authentication works.
3. Prepare for entityId conflict exploitation.

## Instructions

### Step 1: Configure SSO

**Context**: Set up SSO in the Grammarly business account dashboard, including defining the entityId and keypair.

Navigate to Grammarly's SSO configuration page and input the necessary SAML details.

> This step involves web interface interactions; no command-line tools are used.

### Step 2: Verify Login

**Context**: Test the SSO login to ensure it functions correctly.

Attempt to log in using the configured SSO; confirm access to the account.

> Expect no errors and full account access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #sso
- #saml
