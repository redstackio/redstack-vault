---
id: proc-uuid-005
name: Fuzz-User-IDs-to-Enumerate-Gold-Members
tags:
  - fuzzing
  - enumeration
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-fuzz-user-ids]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.691Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Fuzz-User-IDs-to-Enumerate-Gold-Members

## Summary

This procedure fuzzes the user_id parameter using Burp Suite Intruder to enumerate all Zomato Gold members by identifying 301 redirects that indicate membership.

## Description

By sending multiple requests with varying user_id values (e.g., sequential from 1 to N), valid Gold members are detected via redirects exposing subscription_ids. Invalid users return no redirect, allowing full enumeration of the subscriber base.

## Requirements

1. Burp Suite with Intruder configured
2. List of potential user_ids (e.g., 1-100000)
3. Proxy setup for traffic interception

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or delays on repeated probes
- Block rapid sequential requests
- Monitor for high-volume user_id variations

## Objectives

1. Identify all Gold member user_ids
2. Collect associated subscription_ids
3. Map the entire subscriber list

## Instructions

### Step 1: Configure Fuzzing in Burp

**Context**: Set up Intruder to payload on user_id and check for 301 responses.

**Command** ([[commands/curl-fuzz-user-ids]]):
```bash
# Simulated fuzz loop; use Burp for efficiency
for uid in {1000..2000}; do curl -X GET "https://www.zomato.com/gold/payment-success?user_id=$uid" -i -L -w "%{http_code} %{redirect_url}\n" | grep -E "301|subscription_id"; done > enumerated_members.txt
```

> Expected output: Lines with 301 and subscription_id for valid members.

### Step 2: Analyze Results

**Context**: Parse logs for redirects to build enumeration list.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fuzz-user-ids]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- fuzzing
- enumeration
