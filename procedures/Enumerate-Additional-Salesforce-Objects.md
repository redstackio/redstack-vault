---
tags:
  - object-enumeration
  - sequential-ids
  - data-exfiltration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/Exploit-getItems-for-Contact-Records]]'
verified: false
platforms:
  - Web
  - Salesforce
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:18.148Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 83b49eb0-c3fa-46c1-ab7f-edceb7ea87cc
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-Additional-Salesforce-Objects

## Summary

This procedure extends the exploitation by replacing entityNameOrId in getItems requests to target other objects like Account and AccountContactRelation, leveraging sequential IDs for comprehensive PII enumeration.

## Description

Salesforce IDs are predictable and sequential, allowing brute-force enumeration. Changing entityNameOrId to 'Account' or 'AccountContactRelation' retrieves related sensitive data, amplifying the leak to include user relationships and additional PII without further authentication.

## Requirements

1. Working getItems template from Contact exploitation
2. Burp Suite for request replay and modification
3. List of target objects (Contact, Account, AccountContactRelation, User)

## Defense

Defensive measures and detection strategies:

- Randomize or obscure Salesforce record IDs to hinder enumeration
- Implement query limits per user session and alert on multi-object queries
- Use field-level security to mask PII in responses for unauthorized users

## Objectives

1. Query multiple object types to broaden data collection
2. Exploit ID sequencing for complete dataset coverage
3. Compile cross-object PII for potential phishing or identity theft

## Instructions

### Step 1: Modify for New Object

**Context**: Update entityNameOrId and replay to access Account records.

**Command** ([[commands/Exploit-getItems-for-Contact-Records]]):

Adapt the previous command by changing "entityNameOrId":"Account" in the message JSON.

> Replay in Burp; response includes Account details linked to PII. Repeat for 'AccountContactRelation' to get relations.

### Step 2: Enumerate via IDs

**Context**: Use sequential IDs from responses to fetch more pages or related records.

No command; manually increment currentPage or ID values in params.

> Increment pageSize or currentPage for pagination; success if additional records return without rate limits hit.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/Exploit-getItems-for-Contact-Records]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- object-enumeration
- sequential-ids
- data-exfiltration
