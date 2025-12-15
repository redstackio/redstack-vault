---
id: ac-nodejs-pathtraversal-uint8array
tags:
  - path-traversal
  - node-js
  - information-disclosure
  - uint8array
  - filesystem-bypass
type: attack_chain
tools:
  - '[[tools/Node-js]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Node-js-fs-Path-Traversal-via-Uint8Array]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:22.643Z'
description: >-
  Demonstrates exploitation of a path traversal vulnerability in Node.js 20's fs
  module by using Uint8Array paths from TextEncoder to bypass filesystem
  permission restrictions and read sensitive files.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Path Traversal in Node.js fs Module via Uint8Array to Bypass Permissions and Read Arbitrary Files

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in Node.js 20's node:fs module, where paths provided as Uint8Array (not Buffer) evade normalization, allowing reads outside permitted directories like /tmp to access /etc/passwd.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Restricted Environment] --> B[Exploit Path Traversal]
    B --> C[Read Sensitive File]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node-js]]

### Target Environment

- Node.js 20 runtime on Linux
- Experimental permission system enabled
- Filesystem read permissions restricted to /tmp/

### Initial Access Requirements

- Local access to Node.js environment
- No network access required
- Administrative privileges not needed, but vulnerable Node.js version

## Detailed Attack Procedures

### Step 1: Exploit Path Traversal
procedure: [[procedures/Exploit-Node-js-fs-Path-Traversal-via-Uint8Array]]

**Objective**: Bypass filesystem permissions by encoding a traversal path as Uint8Array and reading a restricted file like /etc/passwd.

**Instructions**: Enable experimental permissions restricting reads to /tmp/, then use TextEncoder to create a Uint8Array path that includes '../' to traverse to /etc/passwd. Execute the following using [[commands/node-fs-readfile-uint8array-traversal]]:

```bash
node --experimental-permission --allow-fs-read=/tmp/ -p 'fs.readFileSync(new TextEncoder().encode("/tmp/../etc/passwd"))'
```

**Expected Output**: Buffer contents of /etc/passwd, starting with root user entry, e.g., <Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a ...>.

**Success Indicators**:
- Command outputs file contents outside /tmp/
- Buffer shows sensitive data like user accounts from /etc/passwd

## Attack Chain Summary

### Key Achievements

1. Bypassed Node.js experimental permission model
2. Read arbitrary sensitive files via path traversal
3. Demonstrated impact equivalent to prior CVEs (CVE-2023-30584, CVE-2023-32004)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---

*Last updated: 2023-10-01T00:00:00Z*
