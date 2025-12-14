---
id: proc-setup-attacker-store
tags:
  - shopify
  - store-creation
  - app-installation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:44.428Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Attacker's Independent Shopify Store

## Summary

This procedure creates a separate Shopify store under the attacker's account and installs the Digital Downloads app, providing a clean session for accessing victim endpoints without interference.

## Description

The attacker logs in with their secondary account to create an independent store (e.g., test100.myshopify.com) and installs the Digital Downloads app. No products are needed, as the goal is to establish app authentication context. This allows the attacker to browse external app URLs while logged in, bypassing some session isolation. Upon completion, the app dashboard is accessible, confirming installation.

## Requirements

1. Separate Shopify account for attacker
2. Access to create new stores (trial or paid plan)
3. Web browser session management

## Defense

Defensive measures and detection strategies:

- Monitor for rapid store creations tied to single accounts
- Restrict app installations to verified stores
- Log cross-app session accesses

## Objectives

1. Isolate attacker session from victim store
2. Enable app-authenticated access to shared endpoints
3. Prepare for disclosure testing

## Instructions

### Step 1: Create Independent Store

**Context**: Establish the attacker's base store.

Log in as attacker, navigate to Shopify dashboard, and create test100.myshopify.com via UI.

> Manual store setup process.

### Step 2: Install App

**Context**: Add the app to the new store for session context.

In the new store's admin, go to Apps > Shopify App Store, search and install Digital Downloads.

> One-click installation; no configuration needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[store-creation]]
