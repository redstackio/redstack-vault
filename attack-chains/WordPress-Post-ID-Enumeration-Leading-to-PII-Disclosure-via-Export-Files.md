---
tags:
  - information-disclosure
  - pii-leak
  - wordpress
  - enumeration
  - export-files
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enumerate-WordPress-Post-IDs-via-Parameter]]'
  - '[[procedures/Access-Exposed-Export-Files-for-PII-Download]]'
step_count: 2
techniques:
  - '[[Client Configurations]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:56.486Z'
description: >-
  Multi-stage attack exploiting WordPress post enumeration to discover and
  access unauthenticated CSV export files containing PII of hackathon
  participants.
skill_level: intermediate
impact_level: high
id: 4f460f57-fc15-4694-a294-61b90915849c
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Client Configurations]]'
  - '[[Exploit Public-Facing Application]]'
---
# WordPress Post ID Enumeration Leading to PII Disclosure via Export Files

Multi-stage attack chain demonstrating a complete attack workflow exploiting a WordPress site's lack of access controls on hidden export pages.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enumerate Post IDs] --> B[Discover Export Endpoints]
    B --> C[Download PII Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[tools/curl]]
- Scripting tool for automation (e.g., Python with requests library)

### Target Environment

- WordPress-based website
- Publicly accessible web application
- No specific ports required beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Internet access to the target site
- No credentials needed due to lack of authentication
- Basic knowledge of HTTP requests and enumeration techniques

## Detailed Attack Procedures

### Step 1: Enumerate Post IDs
procedure: [[procedures/Enumerate-WordPress-Post-IDs-via-Parameter]]

**Objective**: Discover hidden pages and endpoints by enumerating the 'p' GET parameter to reveal redirect paths.

**Instructions**: Use a web browser, curl, or a scripting tool to send requests to the target site with sequential post IDs. For example, iterate from ID 1 to 10000:

```bash
for id in {1..10000}; do
  curl -I "https://doaction.org/?p=$id" | grep Location
 done
```

Focus on 301 redirect responses, which expose full paths in the Location header (e.g., /event/ijebu-2019/ or /non-profit/test/).

**Expected Output**: List of valid post IDs with their corresponding redirect paths, identifying nearly 1000 unique endpoints.

**Success Indicators**:
- 301 status codes with Location headers revealing hidden paths
- Discovery of patterns indicating export-related pages

### Step 2: Access Exposed Export Files
procedure: [[procedures/Access-Exposed-Export-Files-for-PII-Download]]

**Objective**: Identify and download CSV files containing PII from the enumerated endpoints without authentication.

**Instructions**: Follow the discovered paths to check for export directories, such as /do_action-export-{timestamp}/. Directly access URLs like https://doaction.org/do_action-export-1498557984/ to download the CSV files.

```bash
curl -O "https://doaction.org/do_action-export-1498557984/"
```

Inspect the downloaded files for PII data including names, emails, phones, roles, and organizations.

**Expected Output**: CSV files with structured PII data from hackathon participants.

**Success Indicators**:
- Successful HTTP 200 responses serving CSV content
- Files containing sensitive user information without login prompts

## Attack Chain Summary

### Key Achievements

1. Enumerated over 10000 post IDs to uncover hidden WordPress pages
2. Identified nearly 1000 export endpoints exposing PII
3. Enabled unauthorized bulk download of participant data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Client Configurations]] Gather Victim Identity Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
