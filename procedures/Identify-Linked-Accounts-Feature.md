---
id: proc-identify-linked-dashlane
tags:
  - reconnaissance
  - feature-discovery
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:29:36.704Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Linked-Accounts-Feature

## Summary

This procedure involves exploring the Dashlane application to locate the linked accounts functionality, identifying forms or APIs that allow email-based queries for account associations.

## Description

As part of reconnaissance in web application testing, this step uncovers features vulnerable to IDOR by navigating the UI and inspecting network traffic. In Dashlane, it targets sections for entering emails to retrieve tokens or codes, revealing the /1/account/getLinkedAccounts endpoint. Prerequisites include an authenticated session.

## Requirements

1. Authenticated Dashlane session
2. Browser with network inspection (e.g., dev tools)
3. Basic understanding of web forms

## Defense

Defensive measures and detection strategies:

- Obfuscate or hide internal API endpoints from client-side code
- Log and monitor unusual navigation patterns in the application
- Implement client-side restrictions on feature access

## Objectives

1. Locate email input forms related to account linking
2. Infer API endpoints for linked accounts queries
3. Prepare for targeted exploitation

## Instructions

### Step 1: Explore Application UI

**Context**: Navigate authenticated areas to find relevant features.

After login, search for sections like 'Account Settings' or 'Linked Devices/Accounts'.

### Step 2: Inspect Form Elements

**Context**: Identify input fields for emails and monitor network requests.

Interact with any email entry form (e.g., for token retrieval) and use dev tools (Network tab) to capture requests to /1/account/getLinkedAccounts.

> Successful identification shows a form posting to the vulnerable endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- reconnaissance
- feature-discovery
