---
tags:
  - verification
  - http
  - takeover
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-verbose-http-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T04:51:10.702Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6da65f57-77d0-4af2-9322-53c939dc6d79
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Verify-Subdomain-Takeover-Control

## Summary

This procedure tests the taken-over subdomain by sending HTTP requests to confirm custom content delivery, such as redirects.

## Description

Post-takeover, access http://podcasts.slack-core.com to verify the 301 redirect to https://hackerone.com, confirming control via Feed.Press's nginx server on 5.135.16.40.

## Requirements

1. Network access to the subdomain on port 80
2. HTTP client tools
3. Configured custom content

## Defense

Defensive measures and detection strategies:

- Monitor HTTP traffic for anomalous redirects
- Use web application firewalls (WAF) to block unexpected responses
- Log access to subdomains and alert on unusual patterns

## Objectives

1. Validate custom configuration
2. Collect evidence of control
3. Assess impact potential

## Instructions

### Step 1: Send Verbose HTTP Request

**Context**: Fetch the root path and inspect response headers.

Execute [[commands/curl-verbose-http-request]]:

```bash
curl -vv http://podcasts.slack-core.com
```

> Explanation: Verbose mode shows connection details, returning HTTP/1.1 301 with Location: https://hackerone.com, served by nginx.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Network Sniffing]] Network Sniffing (adapted for request testing)

### Sub-Techniques


## Commands Used

- [[commands/curl-verbose-http-request]]

## Tools Used

- [[tools/curl]]

## Tags

- [[verification]]
- [[http]]
