---
id: proc-analyze-disclosure
tags:
  - ssrf
  - information-disclosure
  - error-analysis
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:39:02.168Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-Responses-for-Information-Disclosure

## Summary

This procedure examines SSRF responses, including cURL errors and fetched content, to disclose server details, open services, and internal data.

## Description

Responses may include cURL codes (e.g., CURLE_RECV_ERROR for open ports), HTTP status errors (e.g., 500 with stack traces), or direct content from internal apps. Non-HTML files can be saved, while HTML may prompt further actions, revealing tech stack and configurations.

## Requirements

1. Captured responses from prior SSRF tests
2. Tools for viewing saved files (e.g., text editor)
3. Understanding of cURL error codes

## Defense

Defensive measures and detection strategies:

- Suppress detailed error messages in production
- Parse and filter responses before returning to users
- Implement content security policies for fetched resources

## Objectives

1. Identify open ports and services
2. Extract server or application details
3. Assess potential for further exploitation

## Instructions

### Step 1: Review Error Codes

**Context**: Interpret cURL responses for port status.

Look for codes like CURLE_COULDNT_CONNECT (closed port) or CURLE_RECV_ERROR (open but failed).

> Map codes to services: e.g., port 22 open indicates SSH.

### Step 2: Examine Fetched Content

**Context**: Analyze HTTP responses or errors.

If internal content is returned (e.g., 500 error page), note details like server versions. Save non-HTML outputs for inspection.

> For HTML, the form may treat it as an image upload prompt, but errors often leak info.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[error-analysis]]
