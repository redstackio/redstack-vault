---
tags:
  - information-disclosure
  - web
  - hackerone
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: low
procedures:
  - >-
    [[procedures/Export-and-Extract-Internal-Attachments-from-HackerOne-Reports]]
step_count: 4
techniques:
  - '[[Data from Information Repositories]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploiting the 'Export as .zip' feature in HackerOne reports to access
  internal or removed attachments
skill_level: beginner
impact_level: medium
id: e57e16d9-df84-45a0-93b8-5ebaffbc557b
created_at: '2025-12-11T03:47:47.743Z'
updated_at: '2025-12-11T03:47:47.743Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1213]]'
  - '[[T1190]]'
---
# Information Disclosure via HackerOne Report Zip Export

Multi-stage attack chain demonstrating how to exploit a vulnerability in HackerOne's report export feature to gain unauthorized access to internal or removed attachments, leading to potential confidential information disclosure.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Report] --> B[Export as Zip]
    B --> C[Extract Zip]
    C --> D[Observe Attachments]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (standard web browser and file extraction utility)

### Target Environment

- Web platform
- HackerOne report management service
- Access to a disclosed report URL

### Initial Access Requirements

- Public access to the disclosed report page
- No credentials required beyond standard web access

## Detailed Attack Procedures

### Step 1: Navigate to the Target Report Page - [[procedures/Export-and-Extract-Internal-Attachments-from-HackerOne-Reports]]

**Procedure**: [[procedures/Export-and-Extract-Internal-Attachments-from-HackerOne-Reports]]

**Objective**: Access the disclosed report to initiate the export process.

**Expected Output**: Successful loading of the report page with export options available.

**Success Indicators**:
- Report page loads without errors
- Export button is visible

### Step 2: Export the Report as a Zip File - [[procedures/Export-and-Extract-Internal-Attachments-from-HackerOne-Reports]]

**Procedure**: [[procedures/Export-and-Extract-Internal-Attachments-from-HackerOne-Reports]]

**Objective**: Download the report contents including attachments using the export feature.

**Expected Output**: A zip file named something like HackerOne_Report-security#182358.zip is downloaded.

**Success Indicators**:
- Download completes successfully
- File is saved locally

### Step 3: Extract the Downloaded Zip File - [[procedures/Export-and-Extract-Internal-Attachments-from-HackerOne-Reports]]

**Procedure**: [[procedures/Export-and-Extract-Internal-Attachments-from-HackerOne-Reports]]

**Objective**: Unpack the zip file to view its contents.

**Expected Output**: Extracted files including internal or removed attachments.

**Success Indicators**:
- Extraction completes without errors
- Files are accessible in the extracted directory

### Step 4: Observe the Presence of Unauthorized Attachments - [[procedures/Export-and-Extract-Internal-Attachments-from-HackerOne-Reports]]

**Procedure**: [[procedures/Export-and-Extract-Internal-Attachments-from-HackerOne-Reports]]

**Objective**: Inspect the extracted files to confirm unauthorized access to internal attachments.

**Expected Output**: Visibility of attachments that were removed or marked as internal, such as those with identifiers like {F134909}.

**Success Indicators**:
- Internal attachments are present and viewable
- Confirmation of information disclosure

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to internal attachments via export feature
2. Potential for confidential information disclosure
3. Demonstration of vulnerability in report management system

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Data from Information Repositories]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Collection]]

*Last updated: 2023-10-01*
