---
id: proc-slack-upload-svg-104087
tags:
  - xss
  - svg
  - file-upload
  - slack
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
updated_at: '2025-12-14T17:24:26.101Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload-Malicious-SVG-to-Slack

## Summary

This procedure involves creating and uploading an SVG file with embedded JavaScript in an onload attribute to a Slack workspace, allowing the script to execute when the file is loaded in a browser, facilitating redirects or other client-side actions.

## Description

In the context of exploiting Slack's open redirect vulnerability, the attacker uploads an SVG file to Slack's file storage. The SVG contains an onload event that executes JavaScript to redirect the browser to an external site. Since the file is hosted on files.slack.com, it bypasses domain checks in the /checkcookie endpoint. Prerequisites include a Slack account with upload permissions in a workspace.

## Requirements

1. Valid Slack account with file upload access to a channel.
2. Text editor to create the SVG file.
3. Web browser to interact with Slack.

## Defense

Defensive measures and detection strategies:

- Disable or restrict file uploads to non-SVG formats in Slack workspaces.
- Implement content security policies (CSP) to block inline JavaScript execution in SVGs.
- Monitor for unusual file uploads containing script tags or onload attributes.

## Objectives

1. Host malicious JavaScript on a trusted Slack domain.
2. Prepare for redirect bypass in subsequent steps.
3. Enable client-side execution without direct XSS.

## Instructions

### Step 1: Create the Malicious SVG File

**Context**: Craft an SVG with an onload attribute that redirects to an external phishing site.

Create a file named `redirect.svg` with the following content:

```xml
<svg onload="window.location='http://www.example.com'" xmlns="http://www.w3.org/2000/svg"></svg>
```

> This SVG is minimal and triggers the JavaScript redirect upon loading.

### Step 2: Upload to Slack

**Context**: Upload the SVG to a Slack channel to obtain Slack-hosted storage.

In Slack, navigate to a channel, click the upload icon, and select the `redirect.svg` file.

> Upload confirmation appears in the channel; the file is now stored on files.slack.com.

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
- [[svg]]
- [[file-upload]]
- [[slack]]
