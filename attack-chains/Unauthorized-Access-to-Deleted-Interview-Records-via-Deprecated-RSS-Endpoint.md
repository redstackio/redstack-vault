---
id: ac-unauthorized-deleted-interviews-glassdoor
tags:
  - idor
  - unauthorized-access
  - web
  - rss-endpoint
  - glassdoor
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Deleted-Employer-Profiles]]'
  - '[[procedures/Access-Deleted-Interview-Records-via-RSS-Endpoint]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:07.532Z'
description: >-
  Multi-stage attack exploiting IDOR in Glassdoor's RSS endpoint to access
  deleted interview records after employer profile deletion.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Access to Deleted Interview Records via Deprecated RSS Endpoint

Multi-stage attack chain demonstrating unauthorized access to sensitive deleted interview data on Glassdoor through a deprecated RSS endpoint, exploiting insecure direct object references after employer profile deletion.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Deleted Profiles] --> B[Access via RSS Endpoint]
    B --> C[View Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[commands/curl-access-rss-endpoint]]

### Target Environment

- Glassdoor web platform
- Access to public employer profiles and RSS feeds
- No authentication required for public endpoints

### Initial Access Requirements

- Public internet access
- Knowledge of target employer profile IDs
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Identify Deleted Employer Profiles
procedure: [[procedures/Identify-Deleted-Employer-Profiles]]

**Objective**: Locate employer profiles that have been deleted to target associated interview records.

**Instructions**: Manually search for employer profiles on Glassdoor and note their IDs. Verify deletion by attempting to access the profile URL directly, observing 404 or removal indicators. Use browser developer tools to inspect network requests for profile IDs.

**Expected Output**: List of deleted employer profile IDs (e.g., employer_id=12345).

**Success Indicators**:
- Profile page returns deletion confirmation or error
- Profile ID extracted from URLs or API calls

### Step 2: Access Deleted Interview Records via RSS Endpoint
procedure: [[procedures/Access-Deleted-Interview-Records-via-RSS-Endpoint]]

**Objective**: Exploit the deprecated RSS endpoint to retrieve interview data linked to deleted profiles.

**Instructions**: Construct the RSS URL using the deleted employer ID, such as `https://www.glassdoor.com/rss/interviews?employer_id=DELETED_ID`. Use [[commands/curl-access-rss-endpoint]] to fetch the feed:

```bash
curl "https://www.glassdoor.com/rss/interviews?employer_id=12345" -o interviews.xml
```

Parse the XML output to view interview details like questions, experiences, and dates.

**Expected Output**: XML feed containing interview records, including sensitive details from deleted profiles.

**Success Indicators**:
- RSS feed returns data without errors
- Interview records visible despite profile deletion

## Attack Chain Summary

### Key Achievements

1. Identified deleted employer profiles and extracted IDs
2. Bypassed access controls via deprecated RSS endpoint
3. Viewed unauthorized sensitive interview data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
