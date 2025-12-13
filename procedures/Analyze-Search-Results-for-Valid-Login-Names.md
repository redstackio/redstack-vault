---
tags:
  - information-disclosure
  - reconnaissance
  - analysis
type: procedure
tools:
  - '[[tools/Google-Search]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Search Open Websites-Domains]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: e0aff145-c691-40a0-a91f-49f1562d2178
created_at: '2025-12-13T09:01:26.437Z'
updated_at: '2025-12-13T09:01:26.437Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
---
# Analyze Search Results for Valid Login Names

## Summary

This procedure focuses on reviewing Google search results to extract and validate login names from indexed SSO URLs, enabling potential attacks like password guessing or social engineering.

## Description

After obtaining search results, this procedure involves manual or scripted analysis to parse usernames from URLs. The target environment is a web SSO system where usernames follow patterns like alice_brown, often corresponding to email addresses. Prerequisites include having the search results from a prior reconnaissance step. Expected outcomes are a curated list of valid login names.

## Requirements

1. Google search results from the target domain
2. Basic text processing tools (e.g., grep)
3. Knowledge of username patterns in the target system

## Defense

Defensive measures and detection strategies:

- Regularly audit and de-index sensitive URLs using Google Search Console
- Implement access controls to prevent public exposure of internal directories

## Objectives

1. Extract usernames from indexed URLs
2. Validate them as potential SSO logins
3. Prepare for targeted attacks

## Instructions

### Step 1: Review and Parse Search Results

**Context**: Manually or automatically extract usernames from the results.

```bash
grep -oE '[a-z_]+' results.html | sort -u > usernames.txt
```

> This extracts unique usernames like alice_brown from URL patterns, assuming results are saved in results.html.

### Step 2: Validate Extracted Names

**Context**: Cross-reference with known email formats or test for validity if possible.

> No command needed; manually review the list to confirm patterns matching SSO accounts.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Search Open Websites-Domains]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Google-Search]]

## Tags

- [[information-disclosure]]
- [[Reconnaissance]]
