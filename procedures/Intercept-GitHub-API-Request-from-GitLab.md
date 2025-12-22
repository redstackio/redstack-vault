---
id: proc-intercept-github-request
tags:
  - intercept
  - api-request
  - github
type: procedure
tools:
  - '[[tools/Octokit-Ruby-Gem]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T04:08:46.076Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Intercept-GitHub-API-Request-from-GitLab

## Summary

This procedure captures the outgoing POST request from GitLab to the attacker-controlled GitHub API endpoint, revealing headers and payload for manipulation.

## Description

Upon testing the integration, GitLab uses Octokit to POST pipeline status to the fake endpoint. The attacker intercepts this to inspect details like Authorization token and target_url. Target: Attacker's server logs. Prerequisites: Configured integration. Outcome: Full request details for crafting redirect response.

## Requirements

1. Server listening on remote_ip (e.g., using netcat or HTTP server)
2. Network access to receive requests from GitLab
3. Logging capability on the server

## Defense

Defensive measures and detection strategies:

- Proxy and inspect outbound requests from applications
- Rate-limit API calls to external services
- Alert on unexpected tokens or URLs in requests

## Objectives

1. Capture GitLab's API interaction
2. Analyze request for sensitive data
3. Identify payload for SSRF exploitation

## Instructions

### Step 1: Monitor Server for Incoming Request

**Context**: Set up listener to log the POST request.

Use a tool like netcat: nc -l -p 80 on remote_ip.

> Expected output: Request logged, e.g., POST /api/v3/repos/1/2/statuses/5509244fe4919b85f5c1e0e1a2340805055c32d9 HTTP/1.1 with headers (Accept: application/vnd.github.v3+json, User-Agent: Octokit Ruby Gem 4.9.0, Authorization: token 1) and body {"context":"ci/gitlab/master","description":"Pipeline passed on GitLab","target_url":"https://gitlab.com/jobertabma/123/pipelines/36992118","state":"success"}.

### Step 2: Verify Request Details

**Context**: Confirm the request matches expected GitHub API format.

Inspect logs for body and headers.

> Expected output: Pipeline status payload confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Octokit-Ruby-Gem]]

## Tags

- [[intercept]]
- [[api-request]]
- [[github]]
