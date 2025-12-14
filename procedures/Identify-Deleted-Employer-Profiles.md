---
id: proc-identify-deleted-profiles
tags:
  - recon
  - web
  - profile-discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-rss-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:30:07.530Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Deleted-Employer-Profiles

## Summary

This procedure involves reconnaissance to identify deleted employer profiles on Glassdoor, extracting profile IDs for use in subsequent unauthorized access attempts to associated data.

## Description

In the context of Glassdoor's platform, employer profiles can be deleted by administrators, but linked data like interview records may persist. This procedure uses public search and direct URL access to confirm deletions and harvest profile IDs, setting up IDOR exploitation. It targets web-based platforms without authentication, relying on observable behaviors like 404 errors.

## Requirements

1. Public internet access to Glassdoor
2. Web browser for manual inspection
3. Basic knowledge of URL structures and HTTP status codes

## Defense

Defensive measures and detection strategies:

- Implement proper data cascading deletion to remove associated records upon profile deletion
- Monitor for anomalous access patterns to deprecated endpoints
- Use rate limiting on public search and RSS feeds

## Objectives

1. Confirm employer profile deletion status
2. Extract unique profile identifiers
3. Prepare for data access exploitation

## Instructions

### Step 1: Search for Employer Profiles

**Context**: Use Glassdoor's search functionality to locate target employers and note their profile URLs.

**Command** ([[commands/curl-access-rss-endpoint]]):
```bash
curl -I "https://www.glassdoor.com/Overview/Working-at-Employer-EI_IE12345.11,20.htm"
```

> This HEAD request checks the profile status; a 200 OK indicates active, while 404 confirms deletion. Extract the employer_id (e.g., EI_IE12345) from the URL.

### Step 2: Verify Deletion and Log IDs

**Context**: Document deleted profiles for targeting.

No specific command; manually log IDs from failed accesses.

> Expected: List of deleted IDs ready for RSS exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-rss-endpoint]]

## Tools Used


## Tags

- recon
- web
