---
id: proc-001
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:42.387Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Create-Chaturbate-Photo-Set-and-Obtain-ID

## Summary

This procedure sets up a target photo set on a Chaturbate account by uploading an initial image, allowing the attacker to obtain the public set ID needed for subsequent CSRF targeting.

## Description

In the context of exploiting Chaturbate's CSRF-vulnerable image upload, this step requires authentication as the victim to create a photo set. The upload process exposes a unique set ID in the URL, which is public and can be used to direct forged requests. This is a prerequisite for any targeted CSRF attack, as the endpoint `/photo_videos/photoset/detail/[username]/[set_id]/` relies on this ID without additional protections.

## Requirements

1. Valid Chaturbate account credentials (victim's)
2. Web browser with internet access
3. A sample image file for initial upload

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for unusual image uploads from automated or cross-origin sources
- Rate-limit uploads per account to detect anomalies

## Objectives

1. Create a new photo set to establish a target
2. Extract the set ID for CSRF payload customization
3. Ensure the set is public for verification

## Instructions

### Step 1: Authenticate to Chaturbate

**Context**: Gain access to the victim's account to perform uploads.

Log in via the Chaturbate login page using the victim's credentials.

**Expected Output**: Successful login, redirect to dashboard.

### Step 2: Navigate to Photo Upload Section

**Context**: Access the profile page where photo sets are managed.

Browse to the user's profile and select the photo upload feature.

**Expected Output**: Upload interface visible.

### Step 3: Upload Initial Image and Capture ID

**Context**: Create the set and note the ID from the success URL.

Select and upload a test image; upon success, copy the set ID from the URL `https://chaturbate.com/photo_videos/photoset/detail/[username]/[set_id]/`.

**Expected Output**: Photo set created with ID recorded (e.g., 4771110).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
