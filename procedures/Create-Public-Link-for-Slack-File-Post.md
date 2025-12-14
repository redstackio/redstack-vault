---
tags:
  - xss
  - public-exposure
  - link-generation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 47d7e32c-df41-4feb-8fc3-92d3d23f5a65
created_at: '2025-12-14T03:16:31.138Z'
updated_at: '2025-12-14T03:16:31.138Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Public-Link-for-Slack-File-Post

## Summary

This procedure generates a public URL for the malicious file post, hosting it on www.slack-files.com for unauthenticated access.

## Description

Slack allows users to create public links for file posts, which are served from a sandboxed domain without authentication. This exposes the stored XSS payload to any visitor, enabling drive-by execution when the page loads and renders the unsanitized content.

## Requirements

1. Saved malicious file post in Slack
2. Permission to generate public links
3. Web browser access to Slack interface

## Defense

Defensive measures and detection strategies:

- Disable or restrict public link creation for sensitive content
- Scan public links for malicious payloads before activation
- Use domain isolation with strict CSP on slack-files.com to block script execution

## Objectives

1. Produce a shareable URL that delivers the stored XSS
2. Bypass authentication to reach external victims
3. Amplify the attack surface beyond the workspace

## Instructions

### Step 1: Locate the Post

**Context**: Find the saved post in Slack's file management.

Navigate to your Slack files or posts and select the malicious post.

### Step 2: Generate Link

**Context**: Invoke the public sharing feature.

Click the 'Create public link' button associated with the post.

### Step 3: Copy the URL

**Context**: Obtain the exposed endpoint.

Copy the generated URL, which will resemble `https://slack-files.com/T025LLJ2X-F025N8W7W-3a5691`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[public-link]]
- [[slack]]
