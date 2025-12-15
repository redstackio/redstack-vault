---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - unrestricted-file-upload
  - nexus-repository
  - path-traversal
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:28.608Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Repository-with-Arbitrary-Storage-Path

## Summary

This procedure exploits the lack of validation on the overrideLocalStorageUrl parameter in Nexus Repository Manager 2 to create a hosted Maven2 repository with an arbitrary filesystem path, enabling subsequent file writes to sensitive locations like the Windows Startup folder.

## Description

In Nexus Repository Manager OSS 2.14.9-01, authenticated administrators can POST to the /nexus/service/local/repositories endpoint with a JSON payload that includes an unrestricted overrideLocalStorageUrl. By setting this to a path two levels above the target (e.g., file:/c:/Users/myuser/AppData/Roaming/Microsoft/Windows/Start Menu/Programs), attackers position the repository storage for traversal into subdirectories like Startup. This sets up arbitrary file creation on the server filesystem, where Nexus runs as SYSTEM on Windows, amplifying impact to RCE and escalation.

## Requirements

1. Valid Nexus administrator credentials
2. Network access to Nexus web interface (e.g., http://nexus-server:8081)
3. Target running on Windows with Nexus as SYSTEM privileges

## Defense

Defensive measures and detection strategies:

- Validate and sanitize overrideLocalStorageUrl to restrict paths within Nexus data directory
- Run Nexus with least privileges (non-SYSTEM user)
- Monitor repository creation logs for suspicious paths and audit filesystem changes in sensitive directories

## Objectives

1. Create a repository enabling arbitrary path writes
2. Bypass storage restrictions for persistence setup
3. Prepare for malicious payload deployment

## Instructions

### Step 1: Authenticate and Prepare Payload

**Context**: Log in as admin and construct the JSON payload targeting a path two levels below the desired write location, such as the Start Menu/Programs directory to reach Startup.

No specific command; use a tool like curl or Postman to send:

```bash
curl -u admin:admin123 -X POST http://nexus-server:8081/nexus/service/local/repositories -H "Content-Type: application/json" -d '{"repoType":"hosted","id":"5000","name":"MyTestRepo","provider":"maven2","overrideLocalStorageUrl":"file:/c:/Users/myuser/AppData/Roaming/Microsoft/Windows/Start Menu/Programs"}'
```

> This creates the repository with ID 5000. Expected output: 201 Created JSON response with repository details.

### Step 2: Verify Repository Creation

**Context**: Confirm the repository exists and the storage path is set without errors, indicating successful path override.

Access the Nexus admin panel or query /nexus/service/local/repositories to list repos and inspect the overrideLocalStorageUrl.

**Expected Output**: Repository listed with the custom storage URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unrestricted-file-upload]]
- [[nexus-repository]]
- [[path-traversal]]
