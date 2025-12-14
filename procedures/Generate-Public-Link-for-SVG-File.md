---
id: proc-slack-public-link-104087
tags:
  - public-link
  - file-sharing
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
updated_at: '2025-12-14T17:24:26.097Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Generate-Public-Link-for-SVG-File

## Summary

This procedure generates a public shareable URL for an uploaded SVG file in Slack, making it accessible without authentication and hosted on a trusted slack.com subdomain.

## Description

After uploading the malicious SVG, set the file's sharing permissions to public. This results in a URL on files.slack.com, which can be used in the open redirect parameter since it's considered a valid Slack domain. This step is crucial for bypassing the redirect restrictions.

## Requirements

1. Uploaded SVG file in a Slack channel.
2. Slack account with permission to share files publicly.
3. Web browser access to Slack.

## Defense

Defensive measures and detection strategies:

- Restrict public file sharing in Slack workspace settings.
- Audit public links generated for sensitive files.
- Scan uploaded files for malicious content before allowing public access.

## Objectives

1. Obtain a trusted-domain URL for the SVG.
2. Enable unauthenticated access to the malicious file.
3. Prepare the URL for use in redirect crafting.

## Instructions

### Step 1: Access File in Slack

**Context**: Locate the uploaded SVG in the Slack channel.

Hover over the file message and click the three dots menu.

### Step 2: Set to Public and Copy Link

**Context**: Change sharing to public to generate the link.

Select "Copy link" after setting to "Anyone with the link" or public; the URL will include a pub_secret parameter.

> Example output: https://files.slack.com/files-pri/T0E7QLVLL-F0G41EG2W/redirect.svg?pub_secret=7a6caed489. Verify by opening in an incognito browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[public-link]]
- [[file-sharing]]
- [[slack]]
