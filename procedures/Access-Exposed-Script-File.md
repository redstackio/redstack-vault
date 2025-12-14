---
id: proc-uuid-001
name: Access Exposed Script File
tags:
  - unauthorized-access
  - exposed-file
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-exposed-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:20.285Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Exposed Script File

## Summary

This procedure demonstrates how to access a publicly exposed script file on a web server without authentication, exploiting misconfigured access controls to retrieve server-side code.

## Description

In scenarios like the Unikrn CRM server, script files may be placed in publicly accessible directories without proper authorization checks. Directly navigating to the URL allows any unauthenticated user to download and execute the script's contents, potentially triggering unintended server actions or revealing internal logic. This targets web-based CRM applications like Mautic running on PHP and Symfony, where configuration errors lead to such exposures.

## Requirements

1. Internet connectivity to reach the target URL
2. Web browser or curl tool for HTTP requests
3. No credentials required due to lack of auth

## Defense

Defensive measures and detection strategies:

- Implement access controls (e.g., .htaccess or server config) to restrict script directories
- Use web application firewalls (WAF) to block direct file access attempts
- Regularly scan for exposed files using tools like dirbuster or automated crawlers

## Objectives

1. Retrieve the exposed script content without authentication
2. Confirm lack of access controls on the endpoint
3. Identify potential for server-side execution or data exposure

## Instructions

### Step 1: Fetch the Exposed Script

**Context**: Use curl to directly request the script file, bypassing any potential client-side checks.

**Command** ([[commands/curl-access-exposed-url]]):
```bash
curl -k https://crm.unikrn.com/███████
```

> This command sends an HTTP GET request to the exposed URL, ignoring SSL certificate issues with -k if needed. Expected output is the raw script content served by the server.

### Step 2: Verify Accessibility

**Context**: Confirm the response indicates successful access without auth prompts.

**Command** ([[commands/curl-access-exposed-url]]):
```bash
curl -I -k https://crm.unikrn.com/███████
```

> The -I flag fetches only headers. Look for 200 OK status and Content-Type indicating script delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-exposed-url]]

## Tools Used


## Tags

- [[unauthorized-access]]
- [[exposed-file]]
