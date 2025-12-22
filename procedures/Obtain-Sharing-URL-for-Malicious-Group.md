---
id: proc-002
tags:
  - xss
  - url-sharing
  - payload-delivery
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
updated_at: '2025-12-14T03:16:25.472Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Obtain-Sharing-URL-for-Malicious-Group

## Summary

This procedure generates and copies a public sharing URL for a group containing a stored XSS payload, enabling delivery to potential victims.

## Description

After creating a group with an XSS payload, wis.pr provides a sharing feature that generates a public URL embedding the group ID. This URL points to a page where the group name (including the payload) is rendered in the twitter:description meta tag. The procedure assumes the malicious group exists and focuses on extracting the URL for distribution.

## Requirements

1. Access to the malicious group in wis.pr
2. Sharing feature enabled in the application
3. Web browser

## Defense

Defensive measures and detection strategies:

- Restrict sharing URLs to authenticated users only
- Rate-limit URL generation to prevent abuse
- Log and monitor sharing URL creations for suspicious patterns
- Scan shared content for malicious scripts before rendering

## Objectives

1. Generate a victim-facing URL
2. Facilitate payload exposure without direct access
3. Amplify reach to arbitrary visitors

## Instructions

### Step 1: Navigate to Group Sharing

**Context**: Locate the sharing option for the malicious group.

In wis.pr, open the group details page and find the 'Share' or 'Public Link' button.

### Step 2: Copy URL

**Context**: Extract the full sharing URL.

Click to generate the URL (format: http://wis.pr/*****) and copy it to clipboard. Redact the group ID if documenting.

> The URL embeds the group ID, which loads the page reflecting the stored payload.

**Expected Output**: Copied URL ready for distribution.

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
- [[payload-delivery]]
