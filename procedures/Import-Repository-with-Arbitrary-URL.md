---
id: proc-gitlab-ssrf-import-001
name: Import-Repository-with-Arbitrary-URL
tags:
  - ssrf
  - gitlab
  - arbitrary-url
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.112Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Import-Repository-with-Arbitrary-URL

## Summary

This procedure exploits the SSRF in GitLab by submitting an arbitrary URL in the repository import field, causing the server to make an outbound request to the attacker's listener.

## Description

The vulnerability stems from no validation ensuring the URL is from GitHub; any URL works, leading GitLab to issue a Git protocol request (e.g., GET /info/refs?service=git-upload-pack) to the specified endpoint. This can be used for external DoS or internal scanning if pivoted. The procedure assumes the listener is running and focuses on the UI submission.

## Requirements

1. Active listener server on public IP:4444
2. Authenticated GitLab session with import URL field visible
3. Knowledge of attacker's public IP

## Defense

Defensive measures and detection strategies:

- Validate URLs against allowlist (e.g., github.com)
- Proxy outbound requests through a secure gateway
- Monitor for Git protocol requests to unexpected hosts

## Objectives

1. Trigger server-side fetch to arbitrary endpoint
2. Initiate GitLab's backend request without client-side blocks
3. Enable logging of the SSRF confirmation

## Instructions

### Step 1: Enter Attacker URL

**Context**: Input the listener URL to direct GitLab's fetch.

**Command**: No command; UI input.

> In the URL field, enter http://<attacker-public-ip>:4444. Provide a repository name and submit. Expected: Form validation passes, import starts.

### Step 2: Submit and Trigger

**Context**: Create the repository to execute the fetch.

**Command**: No command; click "Create project".

> Submission sends the URL to backend, triggering the SSRF request. Expected: Progress indicator or error if fetch fails, but request is sent regardless.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- url-injection
- git-fetch
