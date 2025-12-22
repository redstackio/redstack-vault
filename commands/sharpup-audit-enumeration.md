---
type: command
executor: cmd
data: SharpUp.exe audit
output: |-
  C:\Temp>SharpUp.exe audit 

  === SharpUp: Running Privilege Escalation Checks ===


  === Modifiable Services ===

  Name             : UsoSVC
  DisplayName      : UsoSVC
  ...
platforms:
  - Windows
tags:
  - enumeration
  - privilege-escalation
verified: true
validated: true
---

# sharpup-audit-enumeration

## Command

```cmd
SharpUp.exe audit
```

## Description

This command executes SharpUp in audit mode to perform a full enumeration of privilege escalation vectors on a Windows system, including checks for modifiable services, weak file permissions, registry misconfigurations, and other common privesc opportunities. Use it from a shell on a compromised host to quickly identify escalation paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| audit | Triggers the comprehensive privilege escalation audit, running all built-in checks | Yes (positional argument) |

## Examples

### Basic Usage

```cmd
SharpUp.exe audit
```

This runs the default audit without additional flags.

### Advanced Usage

```cmd
SharpUp.exe audit > privesc_results.txt
```

Redirect output to a file for later analysis or exfiltration.

## Expected Output

The command produces a detailed console report categorized by check type. Successful execution shows sections like:

```
C:\Temp>SharpUp.exe audit 

=== SharpUp: Running Privilege Escalation Checks ===


=== Modifiable Services ===

Name             : UsoSVC
DisplayName      : UsoSVC
StartName        : LocalSystem
Executable       : C:\Windows\system32\svchost.exe -k netsvcs -p
...
```

Look for non-empty sections indicating exploitable issues, such as services with writable binaries or weak permissions.

## Related

- [[procedures/Enumerate-Windows-for-Privilege-Escalation-Using-SharpUp]]
- [[tools/SharpUp]]
