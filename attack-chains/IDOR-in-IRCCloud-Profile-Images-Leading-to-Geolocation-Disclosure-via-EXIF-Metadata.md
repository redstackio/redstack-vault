---
tags:
  - idor
  - exif
  - metadata
  - geolocation
  - information-disclosure
  - web
type: attack_chain
tools:
  - '[[tools/exiftool]]'
  - '[[tools/exif-regex-info]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-Images-with-EXIF-Data]]'
  - '[[procedures/Upload-Profile-Image-and-Extract-URL]]'
  - '[[procedures/Exploit-IDOR-to-Access-Other-Users-Image]]'
  - '[[procedures/Extract-EXIF-Metadata-from-Image]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:34.421Z'
description: >-
  A multi-stage attack exploiting Insecure Direct Object Reference (IDOR) in
  IRCCloud's profile image upload to access other users' images and extract
  sensitive EXIF metadata including GPS coordinates for location tracking.
skill_level: intermediate
impact_level: high
id: 84ec7126-cbd4-4a4f-b8b9-5a499be66db3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
  - '[[Data from Information Repositories]]'
---
# IDOR in IRCCloud Profile Images Leading to Geolocation Disclosure via EXIF Metadata

Multi-stage attack chain demonstrating exploitation of IDOR in IRCCloud's image upload feature combined with unstripped EXIF metadata to retrieve users' geolocation data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Images] --> B[Upload and Extract URLs]
    B --> C[Exploit IDOR]
    C --> D[Extract Metadata]
    D --> E[Location Tracking]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/exiftool]]
- [[tools/exif-regex-info]]

### Target Environment

- Web platform
- IRCCloud service with image upload feature
- No specific ports required (web-based)

### Initial Access Requirements

- Two separate IRCCloud user accounts with upload permissions
- Network access to IRCCloud web interface
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Prepare Test Images
procedure: [[procedures/Prepare-Images-with-EXIF-Data]]

**Objective**: Create or obtain images embedded with GPS EXIF metadata to test for disclosure.

**Instructions**: Download sample JPEG images containing GPS coordinates from a public repository like GitHub. Use [[tools/exiftool]] to verify or add EXIF data if needed.

**Expected Output**: Images ready for upload with confirmed GPS metadata (latitude/longitude).

**Success Indicators**:
- EXIF data verifiable via tool output showing GPS tags
- Images in JPEG format

### Step 2: Upload Images and Extract URLs
procedure: [[procedures/Upload-Profile-Image-and-Extract-URL]]

**Objective**: Upload images to two accounts and capture the direct image URLs for IDOR manipulation.

**Instructions**: Log into the first IRCCloud account via web interface, upload the prepared image as profile picture, and open the image in a new tab to copy the URL (format: https://www.irccloud.com/image/██████████). Repeat for the second account to get its URL (format: https://www.irccloud.com/image/█████).

**Expected Output**: Two distinct image URLs, each tied to a user-specific parameter.

**Success Indicators**:
- Upload successful without errors
- URLs accessible and display the image

### Step 3: Exploit IDOR
procedure: [[procedures/Exploit-IDOR-to-Access-Other-Users-Image]]

**Objective**: Manipulate URL parameters to bypass access controls and view another user's image.

**Instructions**: In the first account's image URL, replace the user-specific parameter value with the one from the second account's URL. Load the modified URL in the browser to access the unauthorized image.

**Expected Output**: The second user's profile image loads without authentication checks.

**Success Indicators**:
- Image from second account visible
- No access denied errors

### Step 4: Extract Metadata
procedure: [[procedures/Extract-EXIF-Metadata-from-Image]]

**Objective**: Analyze the accessed image to retrieve sensitive EXIF data including geolocation.

**Instructions**: Copy the URL of the accessed image and paste it into an online EXIF viewer like [[tools/exif-regex-info]]. Alternatively, download the image and use [[tools/exiftool]] locally to dump metadata.

**Expected Output**: EXIF output revealing GPS coordinates, timestamps, and device info.

**Success Indicators**:
- GPS latitude/longitude extracted
- Metadata confirms sensitive data exposure

## Attack Chain Summary

### Key Achievements

1. Bypassed access controls via IDOR to access unauthorized profile images
2. Exposed unstripped EXIF metadata leading to geolocation tracking
3. Demonstrated potential for user surveillance without direct authentication

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]
- [[Data from Information Repositories]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
