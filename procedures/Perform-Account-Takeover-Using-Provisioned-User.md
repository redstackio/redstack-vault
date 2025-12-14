---
tags:
  - sso
  - saml
  - takeover
  - provisioning
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
  - SAML SSO
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.313Z'
sub_techniques: []
id: a529b257-c837-4ccc-aca7-6330cde68ee9
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Perform-Account-Takeover-Using-Provisioned-User

## Summary

This procedure completes the attack by modifying the attacker's entityId post-provisioning and using the keypair to impersonate the victim user, achieving full account takeover including access to documents.

## Description

Once the user is in the attacker's org, changing the entityId breaks the collision without affecting the provisioned state. The attacker then crafts SAML assertions with their keypair for the user's credentials, bypassing normal auth to access victim data, especially if it's a converted personal account.

## Requirements

1. User provisioned in attacker's organization
2. Access to attacker's SSO keypair
3. SAML assertion crafting capability (manual or via IdP)

## Defense

Defensive measures and detection strategies:

- Bind users to specific organizations via additional attributes
- Rotate keypairs and validate signatures strictly
- Monitor for entityId changes correlating with access anomalies

## Objectives

1. Secure persistent access to provisioned victim user
2. Impersonate and control the victim's account
3. Exfiltrate or manipulate sensitive documents

## Instructions

### Step 1: Modify Attacker's EntityId

**Context**: Update the attacker's org to a new entityId to stabilize access.

No command; in attacker admin panel, change entityId to a unique value (e.g., 'attacker_new').

> Change propagates; provisioned user remains intact.

### Step 2: Impersonate with Keypair

**Context**: Use the attacker's keypair to sign a SAML assertion for the provisioned user's login.

No command; generate assertion via IdP or tool, submit to Grammarly SSO endpoint.

> Login succeeds, granting access to victim's documents and settings.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[sso]]
- [[saml]]
- [[takeover]]
- [[provisioning]]
