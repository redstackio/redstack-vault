---
id: ac-uuid-001
name: Information Disclosure via Accessible Debug Log on ExactHosting
tags:
  - information-disclosure
  - debug-log
  - web-vulnerability
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
  - '[[procedures/Access-Public-Debug-Log-for-Information-Disclosure]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
  - '[[T1083.002]]'
updated_at: '2025-12-14T17:24:56.394Z'
description: >-
  A reconnaissance-based information disclosure vulnerability where a publicly
  accessible debug.log file on ExactHosting exposes debugging information,
  discovered during target enumeration on Tucows services.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[T1083.002]]'
---
# Information Disclosure via Accessible Debug Log on ExactHosting

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance and Discovery] --> B[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- Web platform
- ExactHosting service
- Publicly accessible web server without file access controls

### Initial Access Requirements

- Internet access to the target domain
- No credentials required due to public exposure
- Prior reconnaissance to identify hosting services

## Detailed Attack Procedures

### Step 1: Reconnaissance and File Access
procedure: [[procedures/Access-Public-Debug-Log-for-Information-Disclosure]]

**Objective**: Identify and access the publicly exposed debug.log file to disclose debugging information during reconnaissance of Tucows services.

**Instructions**: During enumeration of Tucows-related services, identify ExactHosting endpoints. Attempt to access common debug files like debug.log via direct URL. Use [[commands/curl-fetch-debug-log]] to retrieve the file content:

```bash
curl -s https://exacthosting.example.com/debug.log -o debug.log
```

Review the downloaded file for any exposed information, such as error messages, paths, or configuration details.

**Expected Output**: A text file containing debug log entries, potentially including timestamps, requests, and non-sensitive debugging data.

**Success Indicators**:
- HTTP 200 response when accessing /debug.log
- File content retrieved without authentication
- Log entries visible, confirming exposure

## Attack Chain Summary

### Key Achievements

1. Discovered publicly accessible debug.log during Tucows service reconnaissance
2. Retrieved debugging information without authentication
3. Reported the misconfiguration via HackerOne, resulting in an informative rating

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]
- [[T1083.002]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
