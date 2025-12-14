---
id: p-identify-concrete-upload
tags:
  - recon
  - concrete-cms
  - ssrf
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.527Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Upload Feature in Concrete CMS

## Summary

This procedure involves locating the 'upload from remote servers' feature in Concrete CMS, which allows fetching files from arbitrary URLs and is vulnerable to SSRF due to lax validation.

## Description

In Concrete CMS, a PHP-based content management system, the file upload functionality includes an option to pull files directly from remote HTTP URLs. This feature saves fetched content locally or to cloud storage like S3, making it a vector for SSRF attacks. The procedure requires authenticated access to the dashboard and focuses on verifying the feature's presence and basic functionality before exploitation. Expected outcomes include confirmation of the endpoint and initial testing with public URLs to understand response handling.

## Requirements

1. Authenticated session in Concrete CMS (e.g., via login as a user with file upload permissions)
2. Web browser or HTTP client for navigation and testing
3. Knowledge of the CMS version (vulnerable in versions prior to patches for this issue)

## Defense

Defensive measures and detection strategies:

- Disable or restrict remote URL uploads to whitelisted domains only
- Implement IP allowlisting to block private ranges (RFC 1918) in outbound requests
- Monitor server logs for unusual HTTP fetches to internal IPs

## Objectives

1. Confirm availability of the vulnerable upload feature
2. Test basic functionality with safe public URLs
3. Prepare for SSRF exploitation by understanding response requirements (e.g., HTTP 200)

## Instructions

### Step 1: Access CMS Dashboard

**Context**: Log in to the Concrete CMS administrative interface to reach file management sections.

Navigate to the dashboard and go to Files > File Manager or Media > Upload.

### Step 2: Locate Remote Upload Option

**Context**: Identify the specific feature for remote fetches.

Look for 'Upload from Remote Server' or similar option, which prompts for a URL input. Test with a public image URL like http://httpbin.org/image/png to verify it fetches and displays the file.

**Expected Output**: File successfully added to the library after fetching.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[concrete-cms]]
