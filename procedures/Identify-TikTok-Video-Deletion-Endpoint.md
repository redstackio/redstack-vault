---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
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
updated_at: '2025-12-14T17:27:36.175Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-TikTok-Video-Deletion-Endpoint

## Summary

This procedure involves inspecting TikTok's web application to identify the video deletion endpoint, enabling the crafting of forged CSRF requests for unauthorized deletions.

## Description

In the context of TikTok's CSRF vulnerability, attackers first need to understand the request structure for video deletion. By simulating a legitimate deletion while monitoring network traffic, the endpoint URL, method (typically POST), and parameters (e.g., video_id) are revealed. This step is crucial as the vulnerability stems from missing CSRF tokens, allowing forged requests from external sites. Prerequisites include access to a TikTok account with videos and tools for traffic inspection.

## Requirements

1. Authenticated TikTok session with uploadable videos
2. Browser with developer tools or a proxy like Burp Suite
3. Basic knowledge of HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for anomalous deletion requests from unusual referers
- Rate-limit video management actions per user

## Objectives

1. Locate the exact deletion endpoint and parameters
2. Confirm absence of CSRF protection
3. Prepare for forging requests

## Instructions

### Step 1: Simulate Legitimate Deletion

**Context**: Perform a video deletion in the browser to capture the request.

Log in to TikTok, upload a test video, then attempt to delete it. Open browser dev tools (F12), go to Network tab, and filter for POST requests.

**Expected Output**: Captured request showing URL like `https://www.tiktok.com/aweme/v1/aweme/delete/` and form data with `aweme_id` or similar.

### Step 2: Analyze Request Structure

**Context**: Extract key elements for replication.

Inspect the request headers, body, and cookies. Note that session cookies will be sent automatically in CSRF scenarios.

**Expected Output**: Documented endpoint, method, and required parameters (e.g., video ID from URL).

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
- [[recon]]
