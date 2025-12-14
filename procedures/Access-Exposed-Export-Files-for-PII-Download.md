---
tags:
  - information-disclosure
  - pii-leak
  - export-files
  - download
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Client Configurations]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:56.479Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c127045c-4481-45a3-bc31-a70046d03908
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Client Configurations]]'
  - '[[Exploit Public-Facing Application]]'
---
# Access-Exposed-Export-Files-for-PII-Download

## Summary

This procedure targets discovered export endpoints from WordPress enumeration, directly accessing and downloading CSV files that contain personally identifiable information (PII) such as names, emails, phones, roles, and organizations, without any authentication checks.

## Description

Following post ID enumeration, attackers access paths like /do_action-export-{timestamp}/, which serve raw CSV files due to missing access controls. These files often aggregate user data from events like hackathons, exposing bulk PII. The technique relies on the predictability of export naming (e.g., timestamps) and the site's failure to restrict direct file access, leading to unauthorized data exfiltration in a web environment.

## Requirements

1. List of enumerated paths from prior reconnaissance
2. HTTP client capable of downloading files (e.g., curl or wget)
3. Target site with exposed export directories

## Defense

Defensive measures and detection strategies:

- Enforce authentication and authorization on all export endpoints
- Store export files in private directories or use temporary signed URLs
- Implement file access logging and anomaly detection for bulk downloads
- Use .htaccess or server configs to deny direct access to export paths

## Objectives

1. Download sensitive CSV files containing PII
2. Extract and analyze user data for further exploitation
3. Demonstrate the scope of data leakage (e.g., nearly 1000 participants)

## Instructions

### Step 1: Identify Export Paths

**Context**: From the enumerated list, select paths matching export patterns.

Review paths for formats like /do_action-export- followed by numbers (timestamps), e.g., https://doaction.org/do_action-export-1498557984/.

**Expected Output**: Curated list of candidate URLs for direct access.

### Step 2: Download CSV Files

**Context**: Attempt direct retrieval of files to confirm exposure and capture data.

Use curl to download the file:

```bash
curl -O "https://doaction.org/do_action-export-1498557984/do_action_export.csv"
```

> This fetches the CSV directly. Expected output: A file named do_action_export.csv containing columns for names, emails, phones, etc. Verify by opening in a spreadsheet tool; look for rows with hackathon participant data.

### Step 3: Validate PII Content

**Context**: Ensure the downloaded data includes sensitive information.

Inspect the CSV for unique entries (e.g., grep for emails or phones) to assess impact.

```bash
grep -E "@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" do_action_export.csv | wc -l
```

> Counts email addresses. Expected output: High count (e.g., 1000+) indicating successful PII leak.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Client Configurations]] Gather Victim Identity Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[pii-leak]]
- [[export-files]]
