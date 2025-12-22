---
id: ac-001-directory-listing-disclosure
name: Information Disclosure via Enabled Directory Listing on Web Server
tags:
  - directory-listing
  - information-disclosure
  - reconnaissance
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
  - '[[procedures/Exploit-Directory-Listing-for-Enumeration]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T03:46:31.552Z'
description: >-
  A reconnaissance attack exploiting web server misconfiguration to disclose
  directory structure and contents, enabling further enumeration of potential
  attack surfaces.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Information Disclosure via Enabled Directory Listing on Web Server

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-directory-listing]]

### Target Environment

- Web server (e.g., Apache) with directory listing enabled
- No authentication required
- Direct network access to the target URL

### Initial Access Requirements

- Publicly accessible web server
- No credentials needed
- Basic HTTP access

## Detailed Attack Procedures

### Step 1: Enumerate Directory Structure
procedure: [[procedures/Exploit-Directory-Listing-for-Enumeration]]

**Objective**: Access the root directory to disclose listed contents, including subdirectories, for reconnaissance.

**Instructions**: Use [[commands/curl-directory-listing]] to fetch the directory listing from the target root URL:

```bash
curl -s http://irc.parrotsec.org/ | grep -E '<a href="[^/]*?/?">'
```

This command retrieves the HTML response and extracts links to directories or files.

**Expected Output**: An auto-generated index page listing subdirectories such as caine/, direct/, and parrot/, along with last modified dates.

**Success Indicators**:
- Directory listing page returned (e.g., "Index of /")
- Subdirectories like caine/, direct/, and parrot/ enumerated
- No 403 or 404 errors indicating suppression

## Attack Chain Summary

### Key Achievements

1. Successful disclosure of root directory contents without authentication
2. Identification of subdirectories for potential further exploration
3. Mapping of web server structure for reconnaissance

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
