---
tags:
  - account-merging
  - shopify
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Modify Authentication Process]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 633a41a7-e5b8-4582-8ab5-dd0bac2519f1
created_at: '2025-12-13T09:01:26.819Z'
updated_at: '2025-12-13T09:01:26.819Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Initiate Shopify Account Review

## Summary

This procedure starts the account review process in Shopify after bypassing email confirmation, enabling the merging of attacker and victim accounts.

## Description

Within the Shopify interface of the attacker-created store, clicking 'Review accounts' initiates the merging workflow. This targets SSO-enabled accounts and requires prior email association. The outcome is progression to authentication steps for merging.

## Requirements

1. Access to attacker-controlled store dashboard
2. Prior email confirmation bypass completed

## Defense

Defensive measures and detection strategies:

- Add rate limiting on account review initiations
- Log and alert on frequent merging attempts

## Objectives

1. Begin account merging process
2. Prepare for authentication and bypass

## Instructions

### Step 1: Access Review Button

**Context**: Locate and click the review option.

In the shop interface, click the 'Review accounts' button.

> This triggers the merging interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[account-merging]]
- [[shopify]]
