---
id: proc-slack-upload-file-url
tags:
  - ssrf
  - file-upload
  - slack
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
updated_at: '2025-12-14T17:30:46.900Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload File to Slack and Obtain Direct URL

## Summary

This procedure involves uploading a file to a Slack workspace and retrieving its direct URL from files.slack.com, which serves as the entry point for subsequent SSRF exploitation by providing a legitimate request path.

## Description

In the context of SSRF attacks on Slack's file hosting, attackers first need a valid file URL to manipulate requests. This step uses Slack's standard upload feature to generate a URL like https://files.slack.com/files-pri/TNXC4JD70-FPSL307RB/test.png. No special privileges are required beyond a standard Slack account. Expected outcomes include a functional URL that can be proxied for header modifications, setting up blind SSRF to internal AWS resources.

## Requirements

1. Valid Slack workspace access with upload permissions
2. Internet connectivity to files.slack.com
3. A test file (e.g., PNG image) for upload

## Defense

Defensive measures and detection strategies:

- Monitor file upload volumes for anomalies
- Rate-limit uploads per user to prevent abuse
- Log direct URL accesses and correlate with suspicious patterns

## Objectives

1. Obtain a citable request path for SSRF exploitation
2. Verify legitimate access to files.slack.com
3. Prepare for request interception

## Instructions

### Step 1: Upload Test File

**Context**: Use Slack's interface to upload a file, ensuring it's publicly accessible via direct link.

No command required; perform via web UI:

- Log in to Slack
- Select a channel, click the paperclip icon, and upload a file (e.g., test.png)

> Expected output: File appears in the channel with a preview.

### Step 2: Retrieve Direct URL

**Context**: Access the original file path for HTTP request manipulation.

No command required; use UI:

- Right-click the file or use 'Open original' to copy the direct URL

> Expected output: URL like https://files.slack.com/files-pri/TNXC4JD70-FPSL307RB/test.png, which returns 200 OK on access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[file-upload]]
- [[slack]]
