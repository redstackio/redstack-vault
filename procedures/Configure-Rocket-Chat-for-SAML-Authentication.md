---
tags:
  - saml
  - configuration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a347a1dc-6433-4ad6-a0cc-7472190fc4fb
created_at: '2025-12-13T09:01:26.319Z'
updated_at: '2025-12-13T09:01:26.319Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure Rocket.Chat for SAML Authentication

## Summary

This procedure sets up SAML authentication in Rocket.Chat to enable the vulnerable login process, which is a prerequisite for exploiting the authentication bypass vulnerability.

## Description

By configuring SAML in the Rocket.Chat settings, the application begins processing SAML responses via saml_utils.js, where the improper validation occurs. This step is necessary to trigger the SAML login flow in a test environment.

## Requirements

1. Administrative access to Rocket.Chat
2. SAML provider details (e.g., IdP metadata)
3. Web browser for configuration

## Defense

Defensive measures and detection strategies:

- Regularly audit SAML configurations for security settings
- Monitor for unexpected SAML provider integrations

## Objectives

1. Enable SAML authentication
2. Prepare the environment for SAML response exploitation
3. Verify SAML login redirection

## Instructions

### Step 1: Access Configuration Panel

**Context**: Log in as admin and navigate to SAML settings.

Access the administration panel and locate the SAML configuration section.

> This enables the SAML login option.

### Step 2: Enable and Save SAML Settings

**Context**: Input SAML provider details and save.

Enter the required SAML metadata and enable the feature.

> Configuration is now active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- saml
- configuration
