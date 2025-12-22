---
id: proc-fanfootage-access-upload
tags:
  - xss
  - file-upload
  - profile-edit
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:25.318Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Edit-Profile-and-Upload-Image

## Summary

This procedure outlines accessing the FanFootage application's profile edit page and initiating an image upload, setting the stage for exploiting the reflected XSS vulnerability in the filename handling.

## Description

In the FanFootage Ruby on Rails app using Paperclip, the profile edit feature allows users to upload images without sanitizing filenames. This step involves authentication and navigation to the upload form, where the vulnerability originates from direct reflection of user-controlled filenames into HTML on the profile view page. Expected outcomes include successful access to the upload interface, enabling subsequent payload injection. Prerequisites include a valid user session.

## Requirements

1. Valid authenticated session in FanFootage
2. Web browser with developer tools for inspection
3. Direct network access to the application

## Defense

Defensive measures and detection strategies:

- Implement user authentication checks and rate limiting on profile edits
- Monitor upload logs for suspicious filenames containing script tags or SVG elements
- Use Content Security Policy (CSP) to block inline JavaScript execution

## Objectives

1. Gain access to the profile edit functionality
2. Locate and interact with the image upload form
3. Prepare for filename manipulation without triggering client-side validation

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to establish a session and reach the profile management area.

Browse to the FanFootage login page, enter credentials, and submit. Upon success, navigate to the user's profile edit page (typically /profile/edit or similar).

> Expected: Redirect to edit page with upload form visible.

### Step 2: Locate Upload Feature

**Context**: Identify the profile image upload input to select a file.

Inspect the form for the file input field (e.g., <input type="file" name="profile_image">). Click to browse for a local image file.

> Expected: File dialog opens, ready for selection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[file-upload]]
