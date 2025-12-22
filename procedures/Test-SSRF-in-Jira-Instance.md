---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - ssrf
  - testing
  - jira
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ssrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.446Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-SSRF-in-Jira-Instance

## Summary

This procedure tests for Server-Side Request Forgery (SSRF) vulnerabilities in Atlassian Jira instances by crafting requests to URL-processing endpoints and monitoring for unintended server-side outbound connections.

## Description

In the context of the reported vulnerability on jira.mariadb.org, SSRF allows attackers to make the server request internal or external resources on their behalf. This procedure uses a controlled external endpoint (e.g., Burp Collaborator) to detect if Jira processes and fetches the supplied URL, confirming the vulnerability without exploiting it further. Prerequisites include access to a web proxy tool for monitoring.

## Requirements

1. Public access to the Jira instance URL
2. Burp Suite or similar for Collaborator payloads
3. curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Upgrade to latest Atlassian Jira version to patch known SSRF issues
- Implement URL whitelisting and validation in request handlers
- Monitor outbound traffic from application servers for anomalous requests

## Objectives

1. Confirm SSRF vulnerability presence
2. Identify exploitable endpoints in Jira
3. Gather evidence for reporting without causing harm

## Instructions

### Step 1: Setup Monitoring Endpoint

**Context**: Prepare an external endpoint to detect server-side requests.

Launch Burp Collaborator and generate a unique payload URL, e.g., http://abc123.burpcollaborator.net/test.

### Step 2: Craft and Send Test Request

**Context**: Target a Jira REST endpoint that may process URLs, such as search or plugin interfaces.

**Command** ([[commands/curl-ssrf-test]]):
```bash
curl -X POST 'https://jira.mariadb.org/rest/api/2/search' -H 'Content-Type: application/json' -d '{"jql":"url=http://abc123.burpcollaborator.net/test"}'
```

> This sends a JSON payload with a Collaborator URL embedded. If SSRF exists, the Jira server will request the URL, visible in Collaborator polls.

### Step 3: Verify Detection

**Context**: Check for incoming requests to confirm SSRF.

Poll Burp Collaborator for DNS/HTTP interactions from the target's IP.

**Expected Output**: Collaborator shows request from jira.mariadb.org IP to the payload URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ssrf-test]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[jira]]
- [[vulnerability-testing]]
