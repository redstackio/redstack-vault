---
id: dc8f713c-81bb-4b9d-bf7d-9b7e1ab9bda5
name: Upload Payload Snippet in GitLab
type: procedure
verified: false
submitted: true
created_at: '2025-12-09T00:20:45.052Z'
updated_at: '2025-12-09T00:20:45.052Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - gitlab
  - payload-upload
commands: []
platforms:
  - Web
  - Linux
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Upload Payload Snippet in GitLab

## Summary

This procedure involves creating a new snippet in GitLab and attaching a Ruby payload file, which will be used later for loading via directory traversal in the exploitation chain.

## Description

In GitLab, snippets allow file uploads that are stored on the server. By uploading a malicious Ruby file, an attacker can reference it in Wiki pages to achieve code execution when combined with Kramdown vulnerabilities. This targets the rendering pipeline for .rmd files.

## Requirements

1. GitLab user account with snippet creation permissions
2. Ruby payload file prepared (e.g., containing code like `puts "hello from ruby"` or shell commands)
3. Access to GitLab web interface

## Defense

Defensive measures and detection strategies:

- Monitor snippet uploads for suspicious file types like .rb
- Restrict Wiki push access and audit rendering logs for errors

## Objectives

1. Upload payload to GitLab server
2. Obtain upload path for reference
3. Prepare for Wiki-based exploitation

## Instructions

### Step 1: Create Snippet and Attach File

**Context**: Create a new snippet and upload the payload.

In the snippet description, click 'Attach a file' and upload the Ruby payload file. Note the upload path like /uploads/-/system/user/1/c4119c5b144037f708ead7295cea4dd0/payload.rb.

> This stores the file on the server for later exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #gitlab
- #payload-upload
