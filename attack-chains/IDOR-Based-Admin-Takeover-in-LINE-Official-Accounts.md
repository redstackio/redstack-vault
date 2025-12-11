---
tags:
  - idor
  - privilege-escalation
  - web-exploitation
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-extract-group-id]]'
  - '[[commands/curl-craft-admin-request]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Discover-and-Extract-Group-IDs-from-LINE-Accounts]]'
  - '[[procedures/Exploit-IDOR-to-Gain-Admin-Privileges]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
description: >-
  Exploitation of IDOR vulnerability to gain unauthorized admin access to LINE
  Official Accounts
skill_level: intermediate
impact_level: high
id: 32ed7bff-6f58-4603-acf8-14b06208b067
created_at: '2025-12-11T06:10:22.409Z'
updated_at: '2025-12-11T06:10:22.409Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1068]]'
---
# IDOR-Based Admin Takeover in LINE Official Accounts

## Overview

This attack chain demonstrates how an attacker can exploit an Insecure Direct Object Reference (IDOR) vulnerability in LINE Official Accounts to gain unauthorized administrative access. By extracting or guessing group IDs and crafting malicious requests due to insufficient authentication, attackers can elevate privileges and take over any account, leading to potential misuse such as data exfiltration or account manipulation.

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Privilege Escalation]
    B --> C[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Platform: Web
- Services: LINE Official Accounts
- Network access: Public internet access to LINE endpoints

### Initial Access Requirements

- No prior credentials needed
- Ability to interact with LINE Official Account APIs

## Detailed Attack Procedures

## Step 1: Group ID Discovery - [[procedures/Discover-and-Extract-Group-IDs-from-LINE-Accounts]]

### Objective

Identify and extract or guess group IDs associated with target LINE Official Accounts, which are easily obtainable due to poor obfuscation.

### Instructions

Use [[commands/curl-extract-group-id]] to query public or semi-public endpoints and extract group IDs:

```bash
curl -X GET 'https://example.line.endpoint/account/info' -H 'User-Agent: Mozilla/5.0'
```

Analyze the response for patterns in group IDs (e.g., sequential or predictable IDs). If guessing is viable, iterate through potential IDs based on observed patterns.

### Validation

- Successful extraction yields valid group IDs
- Confirm IDs correspond to real accounts via API responses

## Step 2: IDOR Exploitation - [[procedures/Exploit-IDOR-to-Gain-Admin-Privileges]]

### Objective

Craft and send requests to administration endpoints using the extracted group IDs to bypass authentication and gain admin rights.

### Instructions

Execute [[commands/curl-craft-admin-request]] to send a crafted request adding the attacker as admin:

```bash
curl -X POST 'https://example.line.endpoint/admin/add' -H 'Content-Type: application/json' -d '{"group_id": "extracted_id", "user_id": "attacker_id", "role": "admin"}'
```

Due to insufficient checks, the request processes without proper authorization, granting admin access.

### Validation

- Verify admin status by accessing restricted features
- Check for unauthorized control over the target account

## Attack Chain Summary

### Key Achievements

1. Successful extraction or guessing of group IDs
2. Unauthorized privilege escalation to admin role
3. Full account takeover potential

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]
