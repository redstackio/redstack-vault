---
tags:
  - redirect
  - phishing
  - impact
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:26.735Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: d378eda3-dc45-439e-87c0-1b6233b94b33
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Trigger-Open-Redirect-via-Download

## Summary

This procedure demonstrates the impact of the open redirect by simulating a hiring manager accessing the submitted application and clicking download links, resulting in redirection to the tampered external URL.

## Description

After submission, the tampered application appears in the Greenhouse dashboard for recruiters. When a user clicks 'Download' on the resume or cover letter, the backend serves the stored URL, which is now an arbitrary external site (e.g., google.com), causing a redirect instead of file delivery. This can lead to phishing, malware, or CSRF. In testing, this was verified by accessing the application (assuming access) or notifying a tester; the vulnerability stems from unvalidated storage and serving of URLs.

## Requirements

1. Submitted application with tampered URLs
2. Access to the hiring manager dashboard (simulated in testing)
3. Browser for observing redirect behavior

## Defense

Defensive measures and detection strategies:

- Validate URLs on download serving, restricting to S3
- Implement redirect confirmation prompts
- Monitor redirect logs for external domains

## Objectives

1. Confirm redirect to malicious site on download
2. Highlight phishing potential for hiring managers
3. Validate full exploit chain

## Instructions

### Step 1: Access Application in Dashboard

**Context**: Simulate hiring manager viewing the submitted application.

No command required; log into Greenhouse admin (or use test account) and navigate to the new application under scout24 jobs.

> Expected: Application details show attachments with disguised filenames.

### Step 2: Click Download and Observe Redirect

**Context**: Trigger the vulnerable download to see the redirect.

No command required; click 'Download' on resume or cover letter; browser should redirect to the tampered URL (e.g., google.com) instead of downloading a file.

> Expected: HTTP redirect (302) to external site; no file served from S3.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[redirect]]
- [[Phishing]]
- [[Impact]]
