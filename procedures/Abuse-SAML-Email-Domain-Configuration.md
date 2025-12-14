---
id: proc-abuse-saml-domain-config-171398
tags:
  - configuration-issue
  - typosquatting
  - saml
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
  - '[[T1583.001]]'
updated_at: '2025-12-13T23:52:39.382Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1583.001]]'
---
# Abuse-SAML-Email-Domain-Configuration

## Summary

This procedure exploits the SAML email domain configuration in HackerOne to add invalid domains with extra dots, enabling typosquatting to hijack login flows via user typing errors.

## Description

The config dialog allows domains like 'hackerone..com', 'hackerone.com.', or '.hackerone.com' without validation, permitting registration of similar domains (e.g., hackerone-com.com) that victims might mistype into. This redirects logins to attacker-controlled flows. Prerequisites: Access to SAML config (admin or vuln). Outcome: Long-term hijacking potential for phishing or intercepts.

## Requirements

1. Access to SAML email domain config
2. Ability to register similar domains
3. Knowledge of target domains

## Defense

Defensive measures and detection strategies:

- Validate domain formats strictly (no extra dots)
- Use exact domain matching without wildcards
- Monitor registered domains for anomalies

## Objectives

1. Insert invalid domain configs
2. Register typosquatted domains
3. Intercept victim logins via errors

## Instructions

### Step 1: Access Config Dialog

**Context**: Navigate to SAML settings.

In HackerOne admin, go to email domain config.

> Ensure privileged access.

### Step 2: Add Malformed Domains

**Context**: Input extra-dot variants.

Enter: 'hackerone..com', 'gmail..com', etc., and save.

> System accepts without validation.

### Step 3: Register and Hijack

**Context**: Use for typosquatting.

Register 'hackerone-com.com' and set up fake login to capture creds.

> Victims typing errors lead to your site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1583.001]] Acquire Infrastructure: Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[typosquatting]]
- [[configuration]]
