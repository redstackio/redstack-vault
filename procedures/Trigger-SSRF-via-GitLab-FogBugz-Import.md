---
id: proc-trigger-gitlab-import-ssrf
tags:
  - ssrf
  - gitlab
  - import
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.232Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger SSRF via GitLab FogBugz Import

## Summary

This procedure triggers SSRF by importing a FogBugz repository into GitLab over HTTP, causing the attachment download to fetch from localhost due to Kernel.open in app/services/projects/download_service.rb.

## Description

GitLab's valid_url? and valid_domain? methods whitelist fogbugz.com and http/https, but CarrierWave's download! uses Kernel.open, which allows resolution to 127.0.0.1. The import from http://poc.fogbugz.com pulls the malicious attachment, downloading internal content (e.g., from port 9090) and storing it in the issue.

## Requirements

1. GitLab instance with project import permissions
2. Configured subdomain redirect and malicious response
3. HTTP access (not HTTPS) to poc.fogbugz.com

## Defense

Defensive measures and detection strategies:

- Patch Kernel.open to block localhost resolutions in import code
- Enforce URL validation against redirects and IP resolutions
- Audit imported attachments for sensitive data

## Objectives

1. Initiate import to validate and download attachments
2. Exploit SSRF to access internal APIs
3. Exfiltrate data via stored issue content

## Instructions

### Step 1: Access GitLab Import UI

**Context**: Navigate to project creation and select FogBugz import.

**Instructions**: Log in to GitLab, go to New Project > Import Project > FogBugz, enter URL http://poc.fogbugz.com and repository name 'SSRF Repository'.

### Step 2: Start Import

**Context**: Trigger the import process.

**Instructions**: Click Import; GitLab fetches from poc.fogbugz.com, downloads attachments via download_service.rb.

**Expected Output**: Import succeeds, issue created with attachment content from localhost API.

### Step 3: Verify SSRF

**Context**: Check the imported issue for exfiltrated data.

**Instructions**: View the imported project/issues; the attachment or description should contain internal service response (e.g., JSON from /api/v1/targets).

**Success Indicators**:
- No validation errors
- Sensitive internal data visible in GitLab

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- gitlab
- import
