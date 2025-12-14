---
tags:
  - xss
  - stored-xss
  - svg-upload
  - cookie-theft
  - session-hijacking
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
procedures:
  - '[[procedures/Upload-Malicious-SVG-for-Stored-XSS]]'
  - '[[procedures/Trigger-Stored-XSS-via-Shared-Image-Link]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in the Ubiquiti
  community forum's media gallery by uploading a malicious SVG file containing
  JavaScript, leading to cookie theft upon victim viewing.
skill_level: intermediate
impact_level: high
id: ef13ecac-380f-4652-8c97-69eeb7b4ecdb
created_at: '2025-12-14T03:16:37.366Z'
updated_at: '2025-12-14T03:16:37.366Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Stored XSS via Malicious SVG Upload in Ubiquiti Forum Media Gallery

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored XSS vulnerability in the Ubiquiti community forum's media gallery upload feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Malicious SVG] --> B[Share Image Link]
    B --> C[Victim Views and XSS Executes]
    C --> D[Cookie Theft and Session Hijack]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual upload via web interface)

### Target Environment

- Web platform: Ubiquiti community forum (https://community.ubnt.com)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to the forum

### Initial Access Requirements

- Forum account (user registration required)
- Network position: External attacker
- Prior access needed: None, but authenticated upload

## Detailed Attack Procedures

### Step 1: Upload Malicious SVG
procedure: [[procedures/Upload-Malicious-SVG-for-Stored-XSS]]

**Objective**: Upload an SVG file containing an embedded JavaScript payload to the media gallery, exploiting the lack of content sanitization to store the XSS payload.

**Instructions**: Create an SVG file with a malicious script, such as one that exfiltrates cookies to an attacker-controlled server. Navigate to the media gallery upload endpoint and submit the file, which will be accepted despite any parsing errors.

**Expected Output**: The SVG file is uploaded successfully to https://community.ubnt.com/t5/media/gallerypage/user-id/559584, generating a unique image ID.

**Success Indicators**:
- Upload confirmation in the gallery
- File accessible via the generated URL

### Step 2: Share Image Link and Trigger XSS
procedure: [[procedures/Trigger-Stored-XSS-via-Shared-Image-Link]]

**Objective**: Distribute the link to the uploaded malicious image to a victim, causing the XSS payload to execute when the image is viewed, stealing session cookies.

**Instructions**: Obtain the preview link for the uploaded image and share it with the target victim via email, chat, or forum post. When the victim accesses the link, the SVG renders, executing the JavaScript to capture and exfiltrate cookies.

**Expected Output**: Victim's browser executes the script, sending cookies to the attacker's server; attacker receives stolen data.

**Success Indicators**:
- Victim reports viewing the image
- Attacker receives cookie data from exfiltration endpoint

## Attack Chain Summary

### Key Achievements

1. Successful upload of unsanitized SVG with XSS payload to a public forum gallery.
2. Execution of stored XSS upon victim interaction, leading to cookie theft.
3. Potential session hijacking using stolen authentication tokens.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
