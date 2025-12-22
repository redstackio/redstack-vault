---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
name: Enumerate Document IDs via IDOR
tags:
  - idor
  - enumeration
  - discovery
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-download-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.637Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enumerate Document IDs via IDOR

## Summary

This procedure involves manipulating the 'id' parameter in the Download.aspx endpoint to enumerate and access multiple documents, exploiting the lack of authorization checks to discover sensitive files.

## Description

The IDOR vulnerability allows attackers to guess or sequentially enumerate document IDs (e.g., integers around 4675), retrieving unauthorized files containing PII and contracts. No session or permission validation occurs, making brute-force enumeration straightforward.

## Requirements

1. Valid base URL and initial working ID
2. Curl or scripting tool for automation
3. Ability to handle multiple downloads

## Defense

Defensive measures and detection strategies:

- Enforce user-specific access controls on object references
- Implement ID obfuscation or hashing
- Rate-limit requests to download endpoints and alert on sequential ID access

## Objectives

1. Identify valid document IDs
2. Expand access to additional sensitive resources
3. Map the scope of exposed data

## Instructions

### Step 1: Test Incremental IDs

**Context**: Modify the ID parameter by incrementing/decrementing from a known value to find valid documents.

**Command** ([[commands/curl-download-file]]):
```bash
curl -o doc_4676.pdf "https://www.█████████/Download.aspx?id=4676"
for i in {4670..4680}; do curl -o doc_${i}.pdf "https://www.█████████/Download.aspx?id=${i}"; done
```

> The loop automates testing a range; successful requests download files, while invalid IDs may return 404s, but no auth errors.

### Step 2: Log Valid Responses

**Context**: Track which IDs yield files for further analysis.

Use output from curl to note successful downloads.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-download-file]]

## Tools Used

- [[tools/curl]]

## Tags

- idor
- enumeration
