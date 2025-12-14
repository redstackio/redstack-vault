---
tags:
  - pii-leak
  - information-disclosure
  - dod
  - health-records
  - powerpoint
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Public-PowerPoint-File]]'
  - '[[procedures/Examine-Slides-for-PII-Leakage]]'
  - '[[procedures/Edit-PPTX-to-Reveal-Redacted-SSNs]]'
step_count: 3
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:24:56.474Z'
description: >-
  Multi-stage information disclosure attack revealing soldiers' PII including
  names, IDs, SSNs, and health details through a publicly accessible PowerPoint
  file on a DoD website.
skill_level: low
impact_level: high
id: 04d1dcb3-32f9-459f-bbb0-bfb3adafa3fc
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# PII Disclosure via Public DoD PowerPoint Containing Health Records

Multi-stage attack chain demonstrating information disclosure of sensitive PII from a publicly accessible PowerPoint presentation on a DoD-related WordPress site. The chain exploits poor document security, allowing attackers to access and manipulate screenshots of soldiers' health records to reveal names, civilian numbers (CIV#), PAD DSN#, and full Social Security Numbers (SSNs).

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Public File] --> B[Examine for PII]
    B --> C[Edit to Reveal Redactions]
    C --> D[Exfiltrate Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)
- PowerPoint editor (e.g., Microsoft PowerPoint, LibreOffice)

### Target Environment

- Web platform with WordPress hosting
- Publicly accessible file upload directory
- No authentication required

### Initial Access Requirements

- Internet access
- Direct URL to the target file
- No credentials or prior access needed

## Detailed Attack Procedures

### Step 1: Access Public PowerPoint File
procedure: [[procedures/Access-Public-PowerPoint-File]]

**Objective**: Download or view the publicly available PPTX file containing sensitive screenshots.

**Instructions**: Navigate to the direct URL of the PowerPoint file hosted on the WordPress site and download it using a web browser.

```bash
# No command needed; use browser to access:
# https://███████/wp-content/uploads/2018/12/HR_TECH_WOBC_Perform_eMILPO_Functions_eMILPO_Brief.pptx
curl -O https://███████/wp-content/uploads/2018/12/HR_TECH_WOBC_Perform_eMILPO_Functions_eMILPO_Brief.pptx
```

**Expected Output**: Downloaded PPTX file ready for examination.

**Success Indicators**:
- File downloads without errors or authentication prompts
- File opens in PowerPoint without restrictions

### Step 2: Examine Slides for PII Leakage
procedure: [[procedures/Examine-Slides-for-PII-Leakage]]

**Objective**: Identify slides with screenshots leaking soldiers' PII such as names, CIV#, PAD DSN#, and health information.

**Instructions**: Open the PPTX file in a PowerPoint viewer and navigate to suspect slides, focusing on slide 13 and others with embedded screenshots of medical records.

```bash
# Open file manually in PowerPoint or use libreoffice for automation:
libreoffice --headless --invisible --convert-to pdf HR_TECH_WOBC_Perform_eMILPO_Functions_eMILPO_Brief.pptx
# Then inspect PDF or original slides for text extraction
```

**Expected Output**: Visible PII in screenshots, including unredacted names and IDs.

**Success Indicators**:
- Screenshots show clear health records with identifiable information
- No encryption or access controls on slide content

### Step 3: Edit PPTX to Reveal Redacted SSNs
procedure: [[procedures/Edit-PPTX-to-Reveal-Redacted-SSNs]]

**Objective**: Modify the file to uncover redacted SSNs by removing or editing blackouts in the screenshots.

**Instructions**: Open the PPTX in an editor, select redacted areas on relevant slides, and delete or adjust the redaction layers to expose underlying text.

```bash
# Use PowerPoint GUI or unzip PPTX for manual edit:
unzip HR_TECH_WOBC_Perform_eMILPO_Functions_eMILPO_Brief.pptx -d temp_dir
# Edit XML or image files in temp_dir/slides/slide13.xml or images
# Re-zip: cd temp_dir; zip -r ../edited.pptx *
```

**Expected Output**: Full SSNs visible after editing, confirming the ease of redaction bypass.

**Success Indicators**:
- Redacted text becomes readable
- Full PII dataset extractable for exploitation

## Attack Chain Summary

### Key Achievements

1. Accessed sensitive DoD health records without authentication
2. Identified multiple PII elements in embedded screenshots
3. Bypassed redactions to reveal complete SSNs, enabling identity theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2024-01-01T00:00:00Z*
