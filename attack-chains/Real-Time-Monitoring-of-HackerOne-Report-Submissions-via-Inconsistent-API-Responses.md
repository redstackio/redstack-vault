---
id: ac-hackerone-report-monitoring-001
tags:
  - information-disclosure
  - api-enumeration
  - polling
  - hackerone
  - reconnaissance
type: attack_chain
tools:
  - '[[tools/python-requests]]'
  - '[[tools/h1-py2-script]]'
  - '[[tools/h1-py3-script]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Endpoint-Response-Differences]]'
  - '[[procedures/Determine-Last-Known-Report-ID]]'
  - '[[procedures/Poll-for-New-Report-Submissions]]'
  - '[[procedures/Log-and-Monitor-Submission-Activity]]'
step_count: 4
techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:29:28.125Z'
description: >-
  An attack chain exploiting inconsistent JSON response lengths from HackerOne's
  report endpoint to detect and monitor new private report submissions in
  real-time, disclosing platform activity metadata.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Network Service Scanning]]'
---
# Real-Time Monitoring of HackerOne Report Submissions via Inconsistent API Responses

Multi-stage attack chain demonstrating exploitation of inconsistent server responses on HackerOne's platform to monitor private report submissions in real-time.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~Continuous (polling-based) |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Response Differences] --> B[Determine Last Known ID]
    B --> C[Poll Sequential IDs]
    C --> D[Log New Submissions]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/python-requests]]
- [[tools/h1-py2-script]] or [[tools/h1-py3-script]]

### Target Environment

- Web platform: HackerOne's public API endpoint (/reports/[report_id].json)
- No specific services/ports beyond standard HTTPS (443)
- Network access: Public internet connectivity to hackerone.com

### Initial Access Requirements

- No credentials required
- Public network position (no internal access needed)
- Basic knowledge of Python scripting

## Detailed Attack Procedures

### Step 1: Identify Endpoint Response Differences
procedure: [[procedures/Identify-Endpoint-Response-Differences]]

**Objective**: Understand the vulnerability by observing distinct response patterns for existent vs. non-existent report IDs.

**Instructions**: Manually query the endpoint using a tool like curl or Python requests to compare responses. For a known submitted private report (e.g., ID 159874), expect an empty JSON response (length 0). For a non-existent ID (e.g., 999999), expect a 404 JSON object {"status":"404","error":"Not Found"} (length 36).

**Expected Output**: Confirmation of response length discrepancy enabling report existence detection.

**Success Indicators**:
- Empty response (length 0) for valid private reports
- 404 response (length 36) for non-existent IDs

### Step 2: Determine Last Known Report ID
procedure: [[procedures/Determine-Last-Known-Report-ID]]

**Objective**: Establish a baseline by finding the highest known submitted report ID to start polling from.

**Instructions**: Use Python with requests to iterate from a starting ID (e.g., 159874) upwards, checking response lengths until an empty response is found, then set that as the last known ID.

**Expected Output**: The highest ID with length 0 response, e.g., 159890.

**Success Indicators**:
- Identified sequential IDs up to the latest submission
- Script outputs the last valid ID

### Step 3: Poll for New Report Submissions
procedure: [[procedures/Poll-for-New-Report-Submissions]]

**Objective**: Continuously scan sequential IDs to detect new submissions by identifying shifts from length 36 to length 0.

**Instructions**: From the last known ID +1, loop with requests.get(), checking lengths. If length 36, sleep 30 seconds and retry; if length 0, log and advance.

**Expected Output**: Detection of new IDs transitioning to length 0, indicating submissions.

**Success Indicators**:
- New report IDs detected in real-time
- Polling loop continues without rate-limiting interruptions

### Step 4: Log and Monitor Activity
procedure: [[procedures/Log-and-Monitor-Submission-Activity]]

**Objective**: Record timestamps of detections to analyze submission patterns and platform activity.

**Instructions**: Upon detecting a new submission, use datetime.now() to timestamp and output to console or file for pattern analysis.

**Expected Output**: Log entries like "New report submitted at 2023-10-01 12:00:00 for ID 159891".

**Success Indicators**:
- Timestamps logged for each new submission
- Ability to derive frequency and timing insights

## Attack Chain Summary

### Key Achievements

1. Exploited response inconsistency for passive reconnaissance of private data.
2. Enabled real-time monitoring without authentication.
3. Disclosed metadata on submission rates and hacker engagement.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning
- [[Network Service Scanning]] Network Service Scanning

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
