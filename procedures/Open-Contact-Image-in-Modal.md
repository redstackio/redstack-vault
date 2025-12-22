---
tags:
  - xss
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:16.068Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 9c702e28-aecd-4f67-a405-63fc6ddfdb54
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Open-Contact-Image-in-Modal

## Summary

This procedure simulates victim interaction by clicking the contact image thumbnail in Nextcloud to open it in a modal, preparing for further exploitation steps.

## Description

In the victim phase, viewing the contact details and interacting with the thumbnail loads the image in a modal without immediate execution. This step is necessary to expose the image URL for the final trigger. It relies on the stored malicious SVG from prior upload.

## Requirements

1. Access to the Nextcloud Contacts interface as a victim user
2. Uploaded malicious contact image visible in the interface
3. Web browser (any modern browser)

## Defense

Defensive measures and detection strategies:

- Log and monitor image modal opens for anomaly detection
- Implement client-side rendering restrictions on images
- Educate users on verifying contact sources

## Objectives

1. Load the malicious image in a controlled modal view
2. Expose the direct image URL for next step
3. Avoid immediate execution to maintain stealth

## Instructions

### Step 1: Navigate to Contact Details

**Context**: Locate the contact with the malicious image in the Contacts app.

Log in to Nextcloud, go to Contacts, and open the target contact's details page.

> The thumbnail of the uploaded SVG appears in the contact card.

### Step 2: Click Thumbnail to Open Modal

**Context**: Interact with the thumbnail to trigger the modal popup.

Click the small image thumbnail in the contact view.

> Modal opens displaying the image; no execution yet as it's not rendered as raw SVG.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[nextcloud]]
