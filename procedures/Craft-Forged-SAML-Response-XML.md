---
tags:
  - saml
  - forgery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e02ca67f-ec97-47f6-8425-25df1d290e2a
created_at: '2025-12-11T03:47:39.238Z'
updated_at: '2025-12-11T03:47:39.238Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Craft Forged SAML Response XML

## Summary

This procedure involves crafting a forged SAML response XML by removing the signature tag and modifying attributes to bypass authentication in the OneLogin SAML-SSO plugin, enabling unauthorized user impersonation.

## Description

The attack targets the plugin's failure to validate SAML responses without a signature tag. By modifying a valid response, attackers can specify usernames, emails, names, and roles like 'Administrator' to gain access. This is typically done manually or with XML editing tools in a web-based WordPress environment.

## Requirements

1. Access to a valid SAML response template
2. Text editor for XML modification
3. Knowledge of target user roles

## Defense

Defensive measures and detection strategies:

- Enforce strict SAML signature validation in plugins
- Monitor for anomalous login attempts without signatures

## Objectives

1. Create a bypassable SAML response
2. Impersonate admin users
3. Gain unauthorized access

## Instructions

### Step 1: Modify XML Attributes

**Context**: Remove the <ds:Signature /> tag and adjust user attributes.

Modify the XML file to include desired username (e.g., 'admin'), email, name, and role ('Administrator').

> Ensure no signature tag is present to bypass validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

## Commands Used

## Tools Used

## Tags

- [[commands/curl-send-forged-saml]]
- #forgery
