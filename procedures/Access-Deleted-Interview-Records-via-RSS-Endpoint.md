---
id: proc-access-deleted-interviews-rss
tags:
  - idor
  - unauthorized-access
  - rss
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:07.528Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Deleted-Interview-Records-via-RSS-Endpoint

## Summary

This procedure exploits a lack of access controls in Glassdoor's deprecated RSS endpoint to retrieve interview records associated with deleted employer profiles, demonstrating IDOR vulnerability.

## Description

After profile deletion, interview data remains accessible via the RSS feed URL formatted as `https://www.glassdoor.com/rss/interviews?employer_id=ID`. This bypasses intended restrictions, allowing viewing of sensitive details like interview questions and candidate experiences. The attack requires only the profile ID and targets public web endpoints.

## Requirements

1. Deleted employer profile ID from prior reconnaissance
2. Tool for HTTP requests (e.g., curl or browser)
3. XML parsing capability to read feed content

## Defense

Defensive measures and detection strategies:

- Deprecate and fully remove unused endpoints with proper 403/404 responses
- Enforce ID validation and access checks on all data retrieval paths
- Log and alert on accesses to deleted entity IDs

## Objectives

1. Retrieve unauthorized interview data
2. Expose sensitive deleted records
3. Validate IDOR impact

## Instructions

### Step 1: Construct RSS URL

**Context**: Build the endpoint URL using the deleted employer ID.

No command; manually format: `https://www.glassdoor.com/rss/interviews?employer_id=12345`.

> Ensure ID matches a deleted profile to exploit the gap.

### Step 2: Fetch and Parse RSS Feed

**Context**: Download the feed to access interview records.

**Command** ([[commands/curl-access-rss-endpoint]]):
```bash
curl "https://www.glassdoor.com/rss/interviews?employer_id=12345" -o interviews.xml
```

> This retrieves the XML; open in a browser or parser to view entries. Successful output includes <item> tags with interview details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-rss-endpoint]]

## Tools Used


## Tags

- idor
- unauthorized-access
