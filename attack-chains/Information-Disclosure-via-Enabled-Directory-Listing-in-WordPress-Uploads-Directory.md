---
tags:
  - directory-listing
  - information-disclosure
  - wordpress
  - misconfiguration
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Browse-WordPress-Uploads-for-Directory-Listing-Enumeration]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T05:32:10.206Z'
description: >-
  A simple reconnaissance attack exploiting misconfigured directory listing on a
  WordPress site's uploads folder to enumerate and access potentially sensitive
  files without authentication.
skill_level: beginner
impact_level: medium
id: 2556a44a-e296-4cfa-a0f2-f538fcdfc00d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Information Disclosure via Enabled Directory Listing in WordPress Uploads Directory

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Discovery]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- WordPress-based website
- Web server (Apache or nginx) with uploads directory exposed
- No specific ports required beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Public internet access to the target website
- No credentials or prior access needed

## Detailed Attack Procedures

### Step 1: Enumerate Uploads Directory
procedure: [[procedures/Browse-WordPress-Uploads-for-Directory-Listing-Enumeration]]

**Objective**: Gain unauthorized access to the file structure and contents of the WordPress uploads directory by exploiting enabled directory listing, potentially exposing sensitive media or documents.

**Instructions**: Open a web browser and directly navigate to the target's WordPress uploads endpoint. For example, for the target mtn.ci, enter the URL `https://www.mtn.ci/wp-content/uploads/` in the address bar. The server will respond by listing available folders (e.g., by year/month) and files due to the misconfiguration allowing directory indexing.

**Expected Output**: An HTML page displaying a directory tree with hyperlinks to folders and files, such as `2023/01/`, `image.jpg`, or other uploaded assets.

**Success Indicators**:
- Directory listing page loads without errors or authentication prompts
- Files and subfolders are visible and clickable
- Potential exposure of sensitive files like PDFs or private images

## Attack Chain Summary

### Key Achievements

1. Unauthorized enumeration of the uploads directory structure
2. Potential access to confidential webmaster-uploaded files
3. Identification of misconfiguration for further reporting or exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
