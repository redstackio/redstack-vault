---
id: proc-slack-generate-public-link
tags:
  - public-link
  - sharing
  - redirect
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
updated_at: '2025-12-14T17:24:27.338Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate-Public-Sharing-Link-for-File

## Summary

This procedure creates a public sharing link for an uploaded Slack file, enabling anonymous access and execution of the malicious HTML content.

## Description

After uploading, use Slack's interface or API to generate a public link in the format https://files.slack.com/files-pri/{team}/{file_id}/{filename}?pub_secret={secret}, which serves the file directly in the browser, triggering the embedded script.

## Requirements

1. File ID from successful upload
2. Access to Slack workspace UI or API

## Defense

- Disable public file sharing or require approval
- Scan shared links for malicious content

## Objectives

1. Obtain accessible URL for the file
2. Ensure anonymous execution

## Instructions

### Step 1: Access File in Slack

**Context**: Navigate to the uploaded file in the Slack channel.

Click the file and select "Create public link" or use API call to files.sharedPublicURL.

### Step 2: Retrieve Link

**Context**: Copy the generated public URL.

Example: https://files.slack.com/files-pri/T1ARLSGBS-F1AU0FTGR/pixel?pub_secret=094ca97aee

> Test by opening in browser; should redirect without login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- public-link
- slack
