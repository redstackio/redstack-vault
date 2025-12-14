---
id: proc-injection-execute-001
tags:
  - xpc-connection
  - injection
  - av-control
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Dynamic-link Library Injection]]'
  - '[[Component Object Model]]'
updated_at: '2025-12-14T17:29:10.010Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Dynamic-link Library Injection]]'
  - '[[Component Object Model]]'
---
# Execute-Dylib-Injection-and-XPC-Connection

## Summary

Run the modified Kaspersky installer to load the custom dylib proxy, triggering code injection that establishes an unauthorized XPC connection to the AV system extension and invokes methods to disable protections.

## Description

Copy the modified Kaspersky Downloader.app to /Users/Shared for execution. Launching it loads the proxy dylib due to disabled validation, executing the constructor to create an NSXPCConnection to '2Y8XE5CQ94.com.kaspersky.kav.sysext' with options 4096, set IPCServiceProtocol interface, call getEndpointForProtocol:@"FileMonitorProtocol", create a new connection with FileMonitorProtocol, and invoke DisableReadonlyVolumeScan:1. This grants control over AV functions without privileges.

## Requirements

1. Modified app bundle ready
2. Write access to /Users/Shared
3. Running KIS system extension

## Defense

Defensive measures and detection strategies:

- Audit XPC connections with os_log or Console.app for anomalies
- Block execution of old installers via version pinning
- Enable SIP and monitor process injections with EndpointSecurity

## Objectives

1. Load proxy dylib successfully
2. Establish XPC connection bypassing auth
3. Invoke AV disable method

## Instructions

### Step 1: Place and Execute Modified App

**Context**: Position the app for safe execution and trigger loading.

Copy to /Users/Shared:

```bash
cp -R /Volumes/Kaspersky\ Internet\ Security/Kaspersky\ Downloader.app /Users/Shared/
```

Launch: open /Users/Shared/Kaspersky\ Downloader.app

> Expected output: App runs, dylib loads, constructor executes without errors.

### Step 2: Perform XPC Invocation in Proxy

**Context**: The injected code handles connection; no manual command needed post-launch.

In dylib constructor (as coded in prior procedure):

> Expected output: Successful connection and method call; no exceptions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Dynamic-link Library Injection]] Dynamic-link Library Injection
- [[Component Object Model]] Inter-Process Communication (XPC)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xpc
- injection
- execution
