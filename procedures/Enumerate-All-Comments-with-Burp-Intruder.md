---
id: proc-enumerate-comments-intruder
tags:
  - idor
  - enumeration
  - intruder
  - web
type: procedure
tools:
  - '[[tools/Burp-Intruder]]'
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:33.647Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Active Scanning]]'
---
# Enumerate-All-Comments-with-Burp-Intruder

## Summary

This procedure automates the discovery of all comment IDs and their contents by using Burp Intruder to fuzz sequential integer payloads against the /comments/ endpoint, exploiting the absence of rate limiting for mass information disclosure.

## Description

With sequential comment IDs and no protections against brute-force, attackers can iterate over a range (e.g., 1-10000) in requests, harvesting responses that reveal contents for valid IDs. This scales the IDOR to expose entire threads, enabling comprehensive data collection for analysis or abuse.

## Requirements

1. Burp Suite Professional with Intruder module
2. Captured base request to /comments/{id}
3. Estimated range of comment IDs (e.g., from app observation)
4. Authenticated proxy session

## Defense

Defensive measures and detection strategies:

- Introduce rate limiting and IP blocking for comment endpoints
- Use non-sequential, unpredictable IDs (e.g., UUIDs)
- Monitor for high-volume sequential requests
- Paginate and access-control comment listings

## Objectives

1. Harvest contents of all accessible comments
2. Map full comment structure across threads
3. Identify sensitive or targetable data

## Instructions

### Step 1: Capture and Position Base Request

**Context**: Select a request to fuzz, marking the ID parameter.

In Burp, right-click a /comments/ request > Send to Intruder. Clear positions, then highlight the ID (e.g., §123§).

> Expected: Positions tab shows §id§ ready.

### Step 2: Configure Payloads

**Context**: Load sequential integers for enumeration.

Payloads tab: Type 'Numbers', From 1, To 10000, Step 1. No encoding needed.

> Expected: Payload list generated.

### Step 3: Launch Attack and Analyze

**Context**: Run the fuzzing to collect responses.

Options: Default throttle (or none for speed). Click 'Start Attack'. Sort results by response length or grep for content.

> Expected: Valid IDs return longer responses with comment JSON; export for review.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Intruder]]

## Tags

- enumeration
- brute-force
