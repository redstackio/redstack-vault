---
tags:
  - access
  - persistence
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a003432a-1164-4cc7-bbb8-3da559043c18
created_at: '2025-12-14T17:25:52.935Z'
updated_at: '2025-12-14T17:25:52.935Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Target-Account-via-Added-Secondary-User

## Summary

This procedure uses the credentials of a newly added unauthorized secondary user to log in and access the target PayPal business account's functions and privileges, achieving account takeover.

## Description

Following the IDOR exploitation, the added secondary user provides a valid login path to the target account without ownership verification. Attackers log in with the secondary user's credentials (e.g., email/password from the original account) to perform actions like managing users, viewing sensitive data, or initiating transactions. This establishes persistence in the compromised account.

## Requirements

1. Credentials of the added secondary user (email and password)
2. Valid session or direct login capability to PayPal
3. Knowledge of assigned privileges from the addition step

## Defense

Defensive measures and detection strategies:

- Notify account owners of new secondary user additions via email/SMS
- Require multi-factor authentication for all logins
- Audit login events for anomalous IP locations or devices

## Objectives

1. Authenticate as the secondary user to gain target account access
2. Validate privileges and perform restricted actions
3. Maintain access for potential further exploitation

## Instructions

### Step 1: Obtain Secondary User Credentials

**Context**: Retrieve login details for the added user from the original account or social engineering.

If the target user ID corresponds to a known account, use its email and password. Otherwise, reset or guess based on prior intel.

### Step 2: Log In to PayPal

**Context**: Use the secondary credentials to access the business portal.

Navigate to login.paypal.com, enter the secondary user's email and password, and authenticate. Select the associated business account upon login.

**Expected Output**: Dashboard access with business functions available, such as user management or reports.

### Step 3: Validate Access

**Context**: Test privileges to confirm unauthorized access.

Attempt actions like editing user roles or viewing transaction history. Monitor for any restrictions.

**Expected Output**: Successful execution of privileged actions without errors.

**Success Indicators**:
- Access to target account confirmed
- Privileges match those assigned in exploitation step

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access]]
- [[Persistence]]
- [[account-takeover]]
