---
id: 4a191295-1803-482b-b7c8-b9544d705f02
name: Access-Wiki-Page-to-Add-Attachment
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.112Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - web-access
  - attachment-upload
  - setup
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Access-Wiki-Page-to-Add-Attachment

## Summary

This procedure involves navigating to a TopCoder wiki page and uploading a benign attachment to prepare for exploiting a reflected XSS vulnerability in the editing feature.

## Description

In the context of attacking the TopCoder wiki, this initial step requires accessing a specific wiki page and adding an attachment like an SVG file. This sets up the scenario for triggering the vulnerable edit endpoint. The target environment is the web-based wiki application, and success leads to the attachment being available for manipulation. Prerequisites include a valid user session on the platform.

## Requirements

1. Web browser with JavaScript enabled
2. Valid credentials for TopCoder wiki access
3. Network connectivity to https://apps.topcoder.com

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on attachment uploads
- Monitor for unusual file uploads on wiki pages
- Require authentication for all wiki interactions

## Objectives

1. Establish presence on the target wiki page
2. Create an attachment for subsequent exploitation
3. Validate access without triggering alerts

## Instructions

### Step 1: Navigate to Wiki Attachments Page

**Context**: Open the browser and go to the attachments section of the target page to initiate the upload process.

No specific command; use browser navigation to https://apps.topcoder.com/wiki/pages/viewpageattachments.action?pageId=165871793.

> This loads the page where attachments can be added. Expected output: Interface for uploading files.

### Step 2: Upload Benign Attachment

**Context**: Select and upload a simple file to create the target attachment named sss.svg.

No specific command; use the upload form in the browser.

> Upload completes successfully, adding sss.svg to the page's attachment list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-access]]
- [[attachment-upload]]
- [[setup]]
