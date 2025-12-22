---
tags:
  - shopify
  - store-access
  - persistent-session
type: procedure
tools:
  - '[[tools/Chrome-Beta]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:58.525Z'
sub_techniques: []
id: 495e5b81-c74f-40c6-a2ad-c43f3f2364e3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Shopify-Store-with-Old-Session

## Summary

This procedure navigates to a Shopify store admin using the session from old credentials, showcasing unauthorized persistent access despite the email change.

## Description

Once logged in with old credentials, the session allows full management of stores (e.g., https://store.myshopify.com/admin), including data viewing and modifications. This exploits the two-hour session expiration window, enabling attacks like data exfiltration or alterations by unauthorized parties.

## Requirements

1. Active session from old email login
2. Store URL under the account
3. [[tools/Chrome-Beta]] session

## Defense

Defensive measures and detection strategies:

- Force session timeout on profile changes
- Audit admin access logs for old credential usage
- Require re-authentication for sensitive store actions

## Objectives

1. Load store admin panel
2. Perform unauthorized actions
3. Demonstrate impact of persistent sessions

## Instructions

### Step 1: Navigate to Store

**Context**: Direct the browser to the target store's admin URL.

In [[tools/Chrome-Beta]], enter the store URL (e.g., https://150hy.myshopify.com/admin) and confirm automatic login.

### Step 2: Verify Access

**Context**: Test administrative functions to validate full control.

Browse products, orders, or settings to ensure complete access without prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Beta]]

## Tags

- shopify
- store-access
