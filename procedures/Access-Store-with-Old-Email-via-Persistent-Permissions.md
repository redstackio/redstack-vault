---
tags:
  - shopify
  - unauthorized-access
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:28:58.546Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1078.004]]'
id: 3aa343a9-0f8f-420d-aced-8b57a54f9909
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Access-Store-with-Old-Email-via-Persistent-Permissions

## Summary

This procedure demonstrates unauthorized access to a Shopify store using the old business email after a partner account email change, due to unrevoked collaboration permissions, leading to privilege escalation.

## Description

After changing the partner email, the old email can still authenticate to accounts.shopify.com and access collaborated stores under the original partner identity. This targets Shopify's account and store systems. Prerequisites: Prior setup with collaboration. Expected outcome: Full store access without re-granting permissions.

## Requirements

1. Old business email from initial setup
2. Previously collaborated store
3. Web browser for login attempts

## Defense

Defensive measures and detection strategies:

- Enforce permission revocation on email changes with session invalidation
- Monitor logins from outdated emails and flag persistent access attempts

## Objectives

1. Bypass email change by accessing via old credentials
2. Escalate to store control, potentially enabling ownership takeover
3. Disclose store details through unauthorized visibility

## Instructions

### Step 1: Attempt Direct Store Login

**Context**: Test if old email can directly access the store (expect failure to highlight the bypass path).

Go to the target store's login page (e.g., admin.shopify.com/store-name) and attempt login with the old business email and any known password.

> Expect an error like "email not registered," confirming direct access is blocked but indirect persists.

### Step 2: Login to Shopify Accounts

**Context**: Use the old email to enter the central accounts system, leveraging persistent ties.

Navigate to https://accounts.shopify.com and log in with the old business email and partner credentials.

> Successful login grants access to the Shopify account dashboard.

### Step 3: Access the Collaborated Store

**Context**: From the dashboard, enter the target store to exploit unrevoked permissions.

In the accounts dashboard, locate the list of stores or collaborations, select the target store, and attempt entry.

> Entry succeeds, displaying the dashboard under the original partner account name.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### Sub-Techniques

- [[T1078.004]] Cloud Accounts

## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[persistent-access]]
- [[cloud-accounts]]
