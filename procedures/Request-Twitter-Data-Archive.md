---
tags:
  - data-archive
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:30:35.699Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 939350c9-9953-447c-82f8-dcbbb18c7242
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Request-Twitter-Data-Archive

## Summary

This procedure requests and downloads a user's Twitter data archive, which includes details of all liked tweets, enabling extraction of unauthorized private content after exploitation.

## Description

Twitter provides a data archive feature at settings/download_your_data, compiling account data including likes into a ZIP file with JSON and HTML formats. After liking a private tweet via bypass, the archive captures the full tweet content. This step requires an authenticated session and involves waiting ~24 hours for preparation. Expected outcome: Downloadable archive with like.js file containing tweet data.

## Requirements

1. Authenticated Twitter account
2. Access to Twitter settings page
3. Patience for 24-hour processing time

## Defense

Defensive measures and detection strategies:

- Monitor archive requests for spikes post-exploitation events
- Sanitize archive contents to exclude private data from unauthorized likes
- Implement delays or CAPTCHAs on frequent archive requests

## Objectives

1. Compile account data including recent likes
2. Obtain exfiltrated private tweet details
3. Validate the unauthorized like persisted in account data

## Instructions

### Step 1: Submit Archive Request

**Context**: Navigate to the data download settings to initiate compilation.

No command; in browser, go to https://twitter.com/settings/download_your_data, enter password if prompted, and click "Request archive".

> Expected output: Page confirmation that the request is being processed; email notification sent.

### Step 2: Monitor and Download

**Context**: Wait for preparation and retrieve the file.

Check email for "Your Twitter archive is ready" notification, then visit the link to download the ZIP.

> Expected output: ZIP file containing folders like data/ with like.js.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- data-archive
- exfiltration
