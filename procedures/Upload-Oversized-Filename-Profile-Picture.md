---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - dos
  - upload-vulnerability
  - filename-injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.811Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Oversized-Filename-Profile-Picture

## Summary

This procedure exploits the lack of input validation and length restrictions on the filename parameter in HackerOne's profile picture upload feature, allowing the injection of extremely large payloads (up to 3MB) that lead to denial of service when propagated into GraphQL responses.

## Description

The attack targets the profile picture upload endpoint at https://hackerone.com/settings/profile/edit, where filenames are not sanitized for length. By appending massive text payloads to filenames, the oversized strings are stored (e.g., in S3) and later included in GraphQL queries fetching user profile data. This causes uncontrolled resource consumption, resulting in slow loading, timeouts, browser crashes, and potential DDoS effects on pages like reports, participant lists, program pages, and thank you pages. The procedure requires an authenticated HackerOne account and focuses on individual user profiles but extends similarly to organization profiles.

## Requirements

1. Authenticated HackerOne user account with upload permissions
2. Browser configured with a proxy like Burp Suite for request interception
3. A large text payload file (e.g., 3MB of repeated characters) prepared in advance
4. Access to a small image file (e.g., PNG) for the upload

## Defense

Defensive measures and detection strategies:

- Implement strict length limits (e.g., 255 characters) and sanitization on filename parameters during uploads
- Validate and strip oversized inputs before storage in backend services like S3
- Monitor GraphQL query response sizes and throttle or reject queries exceeding thresholds
- Use rate limiting on profile-related endpoints to prevent abuse

## Objectives

1. Successfully upload a profile picture with an oversized filename payload
2. Ensure the payload propagates to downstream GraphQL responses
3. Cause denial of service on pages displaying affected user profiles

## Instructions

### Step 1: Navigate to Profile Edit

**Context**: Access the upload interface to prepare for file submission.

Log in to HackerOne and go to https://hackerone.com/settings/profile/edit. Click to select a new profile picture.

### Step 2: Prepare and Intercept Upload

**Context**: Select a small image file and intercept the submission to modify the filename.

Choose a benign PNG file and submit the upload. With Burp Suite proxy active, the POST request to the upload endpoint will be captured.

### Step 3: Modify and Forward Request

**Context**: Inject the large payload into the filename to exploit the validation gap.

In Burp Suite, locate the filename in the multipart form data (e.g., Content-Disposition: form-data; name="file"; filename="original.png"). Prepend the contents of your 3MB payload.txt to it, e.g., filename="<3MB_payload>original.png". Forward the request.

**Expected Output**: The server processes the upload, storing the file with the oversized name, and returns a success response.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- dos
- upload-vulnerability
- filename-injection
- graphql
