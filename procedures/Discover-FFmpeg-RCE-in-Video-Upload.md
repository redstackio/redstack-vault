---
id: proc-uuid-1
name: Discover FFmpeg RCE in Video Upload
tags:
  - rce
  - ffmpeg
  - discovery
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:14.653Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover FFmpeg RCE in Video Upload

## Summary

This procedure involves identifying a remote code execution vulnerability in the video upload process of a web application, specifically through a misconfiguration in FFmpeg used for video processing, as seen in the TikTok Ads portal.

## Description

In the attack scenario, the target is a web-based advertising portal like TikTok Ads that processes uploaded videos using FFmpeg. A misconfiguration allows attackers to inject shell commands via filenames, metadata, or parameters passed to FFmpeg, leading to arbitrary code execution on the server. Prerequisites include access to the upload endpoint and basic knowledge of shell injection techniques. Expected outcomes include confirmation of the vulnerability through test injections that reveal server-side execution.

## Requirements

1. Valid user account with upload permissions in the target portal
2. Network access to the video upload endpoint
3. Tools for crafting and sending HTTP requests (e.g., browser or curl, though not strictly required)

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs to FFmpeg, including filenames and parameters, to prevent shell injection
- Run FFmpeg in a sandboxed environment with restricted privileges
- Monitor logs for anomalous FFmpeg executions or command outputs in error responses

## Objectives

1. Confirm the presence of command injection in video processing
2. Map the injection points in the upload workflow
3. Prepare for exploitation by validating injection success

## Instructions

### Step 1: Analyze Upload Endpoint

**Context**: Examine the video creation/upload process to identify how FFmpeg is invoked.

No specific command; use browser developer tools or intercept requests to observe parameters sent to the server.

> Inspect network traffic during a normal upload to note FFmpeg-related processing steps.

### Step 2: Test for Injection

**Context**: Attempt basic command injection via filename or parameters to detect misconfiguration.

Craft an upload with a filename like `test$(id).mp4` and submit. Check response or subsequent processing for signs of execution, such as embedded command output.

> Successful injection may return partial output like user ID in an error message, indicating RCE potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- ffmpeg
- video-upload
