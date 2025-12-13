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
  - '[[Modify Authentication Process]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f9e8e010-e4b6-431d-97e4-b2d4e50ee938
created_at: '2025-12-13T09:01:26.872Z'
updated_at: '2025-12-13T09:01:26.872Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Setup SSO for Legitimate Organization

## Summary

This procedure involves configuring and verifying SSO for a legitimate organization in Grammarly Business to establish a baseline for subsequent exploitation.

## Description

In this setup, an attacker or tester configures SSO using a specific entityId and confirms functionality. This step is crucial for understanding how Grammarly handles entityIds before introducing duplicates. The target environment is Grammarly's web-based SSO integration using SAML, with expected outcomes including successful authentication.

## Requirements

1. Access to Grammarly Business account creation
2. Control over an SSO provider for entityId configuration
3. Network access to Grammarly services

## Defense

Defensive measures and detection strategies:

- Monitor for unusual SSO configurations or duplicate entityIds
- Implement strict validation on entityId inputs to prevent trailing spaces

## Objectives

1. Establish functional SSO baseline
2. Verify authentication process
3. Prepare for entityId manipulation

## Instructions

### Step 1: Configure SSO

**Context**: Set up SSO with the desired entityId.

Configure SSO through the Grammarly Business dashboard by entering the Identity Provider Issuer (entityId) and saving the settings.

> This establishes the legitimate organization's SSO.

### Step 2: Verify Login

**Context**: Test the SSO functionality.

Attempt to log in using legitimate credentials to confirm successful authentication.

> Expect no errors and full access to the account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[sso]]
- [[saml]]
