---
tags:
  - ssrf
  - redirect
  - metadata
type: procedure
tools:
  - '[[tools/maliciousHttpsServer.py]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Linux
  - GCP
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: critical
detection_risk: medium
sub_techniques: []
id: a001a32f-eb8b-47fb-b8b5-467cce619541
created_at: '2025-12-14T04:08:48.098Z'
updated_at: '2025-12-14T04:08:48.098Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Redirect Docker Requests to Internal Targets

## Summary

This procedure triggers SSRF by having the GitLab Runner's Docker client send requests to the hijacked daemon, which the malicious server redirects to internal endpoints like Google Cloud metadata for blind data access.

## Description

With traffic forwarded, any Docker API call (e.g., images/create for GET/POST) from the Runner hits the external server. The server responds with 302/301 redirects to targets like http://metadata.google.internal/computeMetadata/v1beta1/... , exploiting the client's lack of redirect policy to reach localhost/link-local networks.

## Requirements

1. Hijacked port 2376 forwarding active
2. Malicious server running with redirect logic
3. CI job configured to invoke Docker API

## Defense

Defensive measures and detection strategies:

- Set http.Client.CheckRedirect in Docker client code
- Block redirects to internal IPs in proxy configs
- Log all Docker API calls and monitor for anomalies
- Isolate metadata services with network ACLs

## Objectives

1. Execute SSRF to internal services
2. Support GET/POST/DELETE methods
3. Enable resource exhaustion if needed

## Instructions

### Step 1: Configure Server Redirects

**Context**: Ensure malicious server maps API paths to internal URLs.

Update [[tools/maliciousHttpsServer.py]] to redirect, e.g., /v1.41/images/create to http://metadata.google.internal:80/computeMetadata/v1beta1/instance/service-accounts/default/token?alt=text for GET; similar for POST/DELETE.

### Step 2: Trigger Docker API Call

**Context**: Run CI job to invoke client.

In .gitlab-ci.yml, add a Docker command like `docker pull alpine` to force API interaction.

**Expected Output**: Job hangs or errors due to invalid redirect responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/maliciousHttpsServer.py]]

## Tags

- ssrf
- redirect
- metadata
