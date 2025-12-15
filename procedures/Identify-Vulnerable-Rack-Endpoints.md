---
id: proc-rack-identify-001
tags:
  - recon
  - dos
  - rack
  - ruby
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:26:37.202Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable Rack Endpoints

## Summary

This procedure scans and verifies Ruby on Rails applications for vulnerable Rack versions and multipart-handling POST endpoints, setting the stage for a DoS attack by identifying targets where the parser flaw can be exploited.

## Description

Rack's multipart MIME parser in affected versions processes requests without limiting total parts, only file parts. This procedure involves analyzing the target's tech stack and endpoints to confirm vulnerability. It targets web applications built on Ruby/Rack, discovered via HackerOne report #1954937. Expected outcomes include a list of exploitable endpoints, enabling subsequent crafting and sending of malicious requests.

## Requirements

1. Network access to the target web application
2. Knowledge of Ruby on Rails architecture
3. Access to server logs or version disclosure (e.g., via headers or errors)

## Defense

Defensive measures and detection strategies:

- Upgrade Rack to patched versions (3.0.4.2+, 2.2.6.3+, etc.)
- Implement request body size limits at proxy level (e.g., Nginx client_max_body_size)
- Monitor for unusual POST request patterns with high part counts

## Objectives

1. Confirm Rack version vulnerability
2. Enumerate POST endpoints accepting multipart/form-data
3. Prepare endpoint list for DoS payload delivery

## Instructions

### Step 1: Verify Rack Version

**Context**: Check if the target uses a vulnerable Rack version by inspecting response headers, error pages, or source code if accessible.

**Command** (Manual inspection):

Inspect headers using browser dev tools or curl:

```bash
curl -I https://target.com
```

> Look for Server: Rack or X-Rack-Version headers; cross-reference with known vulnerable ranges.

### Step 2: Enumerate POST Endpoints

**Context**: Identify endpoints that process multipart uploads, such as file upload forms, by reviewing application documentation or fuzzing.

**Command** (Fuzzing with tools like ffuf, if available):

```bash
ffuf -u https://target.com/FUZZ -w endpoints.txt -X POST -H "Content-Type: multipart/form-data"
```

> Expected output: 200/302 responses indicating active endpoints like /upload or /files.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- vulnerability-identification
