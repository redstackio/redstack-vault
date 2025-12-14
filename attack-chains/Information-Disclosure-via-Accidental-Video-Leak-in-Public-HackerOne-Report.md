---
id: 3859e3eb-434a-48af-b7f9-0bfa6e760ea0
name: Information Disclosure via Accidental Video Leak in Public HackerOne Report
type: attack_chain
description: >-
  A multi-stage discovery of sensitive private bug report details exposed
  through a video attachment in a public HackerOne disclosure report, enabling
  potential exploitation of unfixed vulnerabilities.
verified: false
submitted: true
step_count: 4
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.255Z'
procedures:
  - '[[procedures/Access-Public-HackerOne-Report-Video]]'
  - '[[procedures/Extract-Sensitive-Information-from-Video]]'
  - '[[procedures/Verify-and-Capture-Disclosure-Evidence]]'
  - '[[procedures/Report-Information-Disclosure-to-HackerOne]]'
techniques:
  - '[[Data from Information Repositories]]'
  - '[[Gather Victim Host Information]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Collection]]'
tags:
  - information-disclosure
  - hackerone
  - bug-bounty
  - video-leak
  - privacy-violation
platforms:
  - Web
tools: []
complexity: low
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
  - '[[Gather Victim Host Information]]'
---

# Information Disclosure via Accidental Video Leak in Public HackerOne Report

Multi-stage attack chain demonstrating a complete attack workflow for discovering and exploiting an information disclosure vulnerability in a public bug bounty report.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Public Report] --> B[View and Analyze Video]
    B --> C[Capture Evidence]
    C --> D[Report and Verify Resolution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Web platform
- Public access to HackerOne reports
- No special services or ports required

### Initial Access Requirements

- Internet access
- No credentials needed
- Publicly accessible HackerOne platform

## Detailed Attack Procedures

### Step 1: Access Public Report
procedure: [[procedures/Access-Public-HackerOne-Report-Video]]

**Objective**: Gain access to the public HackerOne report containing the vulnerable video attachment to initiate the disclosure discovery.

**Instructions**: Open a web browser and navigate to the public report URL. Locate and play the attached video file identified as {F2131973}.

**Expected Output**: The video loads and plays, revealing embedded content.

**Success Indicators**:
- Report page loads successfully
- Video attachment is visible and playable

### Step 2: Extract Sensitive Information
procedure: [[procedures/Extract-Sensitive-Information-from-Video]]

**Objective**: Analyze the video content to identify and document accidentally disclosed private information from other bug reports.

**Instructions**: Play the video and pause at relevant sections to note down visible details such as redacted company names (e.g., █████), bug types, subdomains, report IDs (e.g., #1841996, #1838699), titles (e.g., "Deleted Admin still can invite admins and delete owner of the portal"), severities (e.g., High, Low), and target companies (e.g., ██████████, ██████).

**Expected Output**: List of sensitive details including bug summaries and private program information.

**Success Indicators**:
- Private report details are visible in the video
- Specific vulnerabilities from other companies are identifiable

### Step 3: Verify and Capture Evidence
procedure: [[procedures/Verify-and-Capture-Disclosure-Evidence]]

**Objective**: Confirm the persistence of the disclosure and preserve evidence for reporting, including checks for re-uploads or related incidents.

**Instructions**: Download or screenshot the video for proof. Check if the video persists after initial viewing. Cross-reference with similar reports (e.g., https://hackerone.com/reports/1826141). Monitor for re-uploads, such as on YouTube at https://www.youtube.com/@bugbountypocs.

**Expected Output**: Saved video file or screenshots; confirmation of re-upload if applicable.

**Success Indicators**:
- Evidence captured successfully
- Disclosure confirmed as violating HackerOne's Code of Conduct
- Links to related incidents noted

### Step 4: Report Vulnerability
procedure: [[procedures/Report-Information-Disclosure-to-HackerOne]]

**Objective**: Submit the discovered disclosure to HackerOne for remediation, leading to video removal and platform review.

**Instructions**: Use HackerOne's reporting platform to submit details of the finding, including evidence from the video. Await internal review and resolution.

**Expected Output**: Acknowledgment from HackerOne, video deletion, and potential bounty award.

**Success Indicators**:
- Report submitted and accepted
- Video removed from the original report
- Bounty issued (low severity in this case)

## Attack Chain Summary

### Key Achievements

1. Discovered accidental exposure of private bug reports in a public video.
2. Identified high-impact details like unfixed vulnerabilities and subdomains.
3. Captured persistent evidence despite deletion attempts.
4. Facilitated platform remediation through responsible reporting.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Data from Information Repositories]] Data from Information Repositories
- [[Gather Victim Host Information]] Gather Victim Host Information

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
