---
id: proc-004
tags:
  - csrf
  - verification
  - impact
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Resource Hijacking]]'
updated_at: '2025-12-14T17:27:42.379Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Resource Hijacking]]'
---
# Verify-Unauthorized-Image-Addition

## Summary

This procedure checks the targeted photo set post-attack to confirm the successful addition of the unauthorized blank image, validating the CSRF exploitation.

## Description

After the forged upload, the photo set page should display the new image. This step assesses impact, such as cluttering the set or potential moderation triggers, highlighting the integrity compromise.

## Requirements

1. Photo set URL with known ID
2. Access to view the set (public)
3. Web browser

## Defense

Defensive measures and detection strategies:

- Audit logs for unexpected uploads
- User notifications for set modifications
- Image content scanning for anomalies (e.g., blanks)

## Objectives

1. Inspect set for new content
2. Confirm unauthorized addition
3. Document impact for report

## Instructions

### Step 1: Navigate to Photo Set

**Context**: Access the targeted set page.

Enter the URL `https://chaturbate.com/photo_videos/photoset/detail/[username]/[set_id]/` in the browser.

**Expected Output**: Photo set loads with original images.

### Step 2: Refresh and Inspect

**Context**: Check for the injected image.

Refresh the page and scroll through thumbnails for the blank white image.

**Expected Output**: New blank image visible in the set.

### Step 3: Validate Impact

**Context**: Ensure no reversals or detections.

Note any errors or if the image persists; screenshot for evidence.

**Expected Output**: Confirmed addition without alerts.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Resource Hijacking]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[verification]]
- [[Impact]]
