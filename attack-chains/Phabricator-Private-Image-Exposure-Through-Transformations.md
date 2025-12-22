---
tags:
  - phabricator
  - access-control
  - file-upload
  - privacy-leak
  - image-transformation
type: attack_chain
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Upload-Private-Image-in-Phabricator]]'
  - '[[procedures/Access-View-Transformations-in-Phabricator]]'
  - '[[procedures/Generate-Image-Transformations-in-Phabricator]]'
  - '[[procedures/Verify-Public-Access-to-Transformed-Image]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Attack chain exploiting improper access control in Phabricator's file upload
  and transformation feature to expose private images publicly.
skill_level: intermediate
impact_level: high
id: 28ed469d-3815-4fda-89cd-a2c8d8da26e7
created_at: '2025-12-14T05:32:13.536Z'
updated_at: '2025-12-14T05:32:13.536Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Phabricator Private Image Exposure Through Transformations

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper access control in Mozilla's Phabricator instance.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Private Image] --> B[Access Transformations]
    B --> C[Generate Transformed Image]
    C --> D[Verify Public Exposure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox or Chrome)

### Target Environment

- Phabricator instance (e.g., https://phabricator.allizom.org)
- Authenticated user account with file upload permissions
- No special services or ports required beyond standard web access

### Initial Access Requirements

- Valid Phabricator user credentials
- Network access to the Phabricator web interface
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Upload Private Image
procedure: [[procedures/Upload-Private-Image-in-Phabricator]]

**Objective**: Upload an image file to Phabricator while ensuring it is set to private visibility to simulate sensitive data handling.

**Instructions**: Navigate to the Phabricator file upload page at https://phabricator.allizom.org/file/upload/. Select and upload an image file (e.g., a JPEG containing PII like a passport scan), and explicitly set the visibility to 'no one' or 'just you' during the upload process to restrict access.

**Expected Output**: Confirmation of successful upload with the file marked as private, visible only to the uploader.

**Success Indicators**:
- File appears in the user's personal files section
- Visibility settings confirm private access only

### Step 2: Access View Transformations
procedure: [[procedures/Access-View-Transformations-in-Phabricator]]

**Objective**: Navigate to the transformations interface for the uploaded private image to prepare for regeneration.

**Instructions**: After upload, go to the file details page for the uploaded image. On the right side of the page, click on 'View Transformations' to open the interface showing available image transformation options.

**Expected Output**: Transformations interface loads, displaying options like profile crop or other image modifications for the private file.

**Success Indicators**:
- Interface accessible without errors
- Original private file details still show restricted visibility

### Step 3: Generate Image Transformations
procedure: [[procedures/Generate-Image-Transformations-in-Phabricator]]

**Objective**: Apply transformations to the private image, triggering the creation of a new publicly accessible version.

**Instructions**: In the transformations interface, select a transformation type (e.g., profile crop) and click 'regenerate' next to it. Preview the new transformed image to confirm generation.

**Expected Output**: A new transformed image version is created and previewed, but ownership and visibility are altered without user notification.

**Success Indicators**:
- Transformed image preview displays successfully
- New file entry appears in the transformations list

### Step 4: Verify Public Access to Transformed Image
procedure: [[procedures/Verify-Public-Access-to-Transformed-Image]]

**Objective**: Confirm that the transformed image is now publicly accessible and uncontrollable by the original owner.

**Instructions**: Return to the transforms page and locate the new link to the transformed file. Attempt to access it in an incognito browser or share the link with another user to verify public access. Check permissions to ensure the original uploader cannot edit or delete the new file.

**Expected Output**: The transformed image is viewable by anyone via the public link, with no edit/delete options available to the owner.

**Success Indicators**:
- Public link allows unauthenticated access
- Original owner lacks control over the new file

## Attack Chain Summary

### Key Achievements

1. Successful upload of private sensitive image
2. Generation of transformed version bypassing privacy controls
3. Confirmation of public exposure without remediation options

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Collection]]

---
*Last updated: 2023-10-01*
