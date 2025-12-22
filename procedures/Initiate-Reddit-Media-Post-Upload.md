---
tags:
  - file-upload
  - reddit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:59.817Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0cc1473e-9c18-44c4-ac8b-460e1ccd6aa5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Reddit-Media-Post-Upload

## Summary

This procedure sets up a media post on Reddit with a legitimate PNG upload to create an interceptable second upload slot, preparing for exploitation of file validation weaknesses.

## Description

In the context of exploiting Reddit's image upload, this step involves navigating the web interface to initiate a post, add a title, and upload a normal PNG image. A second PNG is selected to generate the target HTTP request. This bypasses initial UI checks and positions the attack for MIME and content manipulation. Prerequisites include a logged-in Reddit account and browser proxy setup for Burp Suite. Expected outcome: A pending post with two image slots, ready for request interception.

## Requirements

1. Valid Reddit user account with posting permissions
2. Modern web browser (e.g., Chrome or Firefox) configured to proxy through Burp Suite
3. Access to a legitimate PNG image file for upload
4. Network connectivity to reddit.com

## Defense

Defensive measures and detection strategies:

- Implement client-side file type previews and server-side MIME sniffing before processing
- Rate-limit media uploads per user to detect anomalous patterns
- Monitor for multiple image uploads in quick succession via proxy logs

## Objectives

1. Establish a valid media post context to avoid UI errors
2. Create an HTTP request for the second image that can be intercepted
3. Position for subsequent modification without triggering early failures

## Instructions

### Step 1: Access Media Post Creation

**Context**: Begin the post creation to load the upload interface.

No command; perform via UI:

- Navigate to reddit.com and log in.
- Click 'Create Post' and select 'Media' or 'Create Media Post'.

> This opens the post editor with title and upload fields.

### Step 2: Upload First Normal PNG

**Context**: Add a legitimate image to stabilize the session and bypass loading checks.

No command; UI action:

- Enter a post title (e.g., "Test Post").
- Click upload and select a valid PNG file (e.g., test.png).
- Wait for upload confirmation.

> Expected: Image thumbnail appears; no errors.

### Step 3: Add Second Image Slot

**Context**: Prepare the interceptable request by selecting another PNG.

No command; UI action:

- Click the '+' icon next to the first image.
- Select another PNG file to trigger the upload request.

> Expected: Second upload initiates, request sent to proxy.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- file-upload
- reddit
- web-ui
