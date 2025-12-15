---
id: whoami-all-append
data: 'whoami /all >> c:\attacker\who.txt'
tags:
  - privilege-check
  - validation
type: command
output: >-
  Detailed user, group, and privilege information confirming elevated privileges
  in the who.txt file
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.847Z'
verified: false
validated: true
submitted: true
---
# whoami-validate-privileges

## Command

```cmd
whoami /all >> c:\attacker\who.txt
```

## Description

This command outputs comprehensive information about the current user context, including groups and privileges, and appends it to a file for post-exploitation validation, particularly to confirm elevated execution in privilege escalation scenarios like DLL hijacking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/all` | Displays all user, group, and privilege information for the current user | Yes |
| `>> c:\attacker\who.txt` | Appends the output to the specified file instead of printing to console | Yes |

## Examples

### Basic Usage

```cmd
whoami /all >> c:\attacker\who.txt
```

### Advanced Usage

In a batch file for chained validation:

```cmd
whoami /all >> c:\attacker\who.txt
echo Elevated execution confirmed > c:\attacker\success.txt
```

## Expected Output

The who.txt file will contain lines like:

`USER INFORMATION
----------------

User Name                SID
========================-============================
nt authority\system      S-1-5-18

GROUP INFORMATION
-----------------

Group Name                                 Type             SID          Attributes
=========================================== ================ ================================== ==================================================
Everyone                                   Well-known group S-1-1-0                              Enabled by default, Enabled group
BUILTIN\Administrators                     Alias            S-1-5-32-544                         Enabled by default, Enabled group
...

PRIVILEGES INFORMATION
---------------------

Privilege Name                Description                    State
=============================== ============================== =======
SeAssignPrimaryTokenPrivilege  Replace a process level token  Enabled
SeAuditPrivilege               Generate security audits       Enabled
...`

This confirms high-privilege context (e.g., SYSTEM) if executed elevated.

## Related

- [[Related Procedure: Trigger-DLL-Hijacking-for-Escalation]]
