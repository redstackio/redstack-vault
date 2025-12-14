---
id: proc-search-keywords-2380084
tags:
  - osint
  - keyword-search
  - sensitive-data
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/grep-search]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Search Open Websites-Domains]]'
updated_at: '2025-12-14T17:32:29.089Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
---
# Search Archived Content for Sensitive Keywords

## Summary

This procedure scans the output of archived URL lists for keywords indicative of sensitive data, such as 'clientId', to pinpoint entries likely containing API keys or configurations.

## Description

After querying the CDX index, this step involves text searching the results for common indicators of embedded secrets in JavaScript, like API client IDs. In the Mozilla vulnerability, searching for 'clientId' revealed an encoded JSON URL with PayPal and Stripe keys. This is a manual or scripted OSINT refinement step.

## Requirements

1. Archived URLs file from prior query
2. grep or text editor for searching
3. Knowledge of target keywords (e.g., 'clientId', 'apiKey')

## Defense

Defensive measures and detection strategies:

- Obfuscate or minify client-side code to hinder keyword searches
- Implement content security policies to limit archiving impact
- Regularly audit public archives for keyword matches

## Objectives

1. Filter archived URLs for sensitive content indicators
2. Isolate promising entries for decoding
3. Reduce noise in reconnaissance data

## Instructions

### Step 1: Perform Keyword Search

**Context**: Use grep to find lines containing sensitive keywords in the archived URLs file.

**Command** ([[commands/grep-search]]):
```bash
grep -i 'clientid' archived_urls.txt
```

> This case-insensitive search outputs matching URLs. In the example, it identifies a URL like https://subscriptions.firefox.com/{encoded JSON}. Expected output: List of URLs with keyword hits.

### Step 2: Review Matches

**Context**: Manually inspect the output to select the most relevant archived entry.

**Command** ([[commands/cat-display]]):
```bash
cat archived_urls.txt | grep -i 'clientid' | head -1
```

> Displays the top match for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Search Open Websites-Domains]] Search Open Technical Databases or Platforms

### Sub-Techniques

-

## Commands Used

- [[commands/grep-search]]
- [[commands/cat-display]]

## Tools Used

-

## Tags

- [[osint]]
- [[keyword-search]]
- [[sensitive-data]]
