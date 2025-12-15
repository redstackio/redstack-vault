---
data: 'whoami /all >> c:\attacker\who.txt'
tags:
  - privilege-check
  - validation
type: command
output: 'Detailed user privileges and groups appended to c:\attacker\who.txt'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.433Z'
id: 47874660-9231-45d9-991e-ab8b11645ec9
verified: false
validated: true
submitted: true
---
# whoami-privilege-check

## Command

```cmd
whoami /all >> c:\attacker\who.txt
```

## Description

This command queries the current user's identity, privileges, and group memberships, appending the output to a file for post-exploitation validation of privilege escalation in a DLL hijacking scenario.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/all` | Displays comprehensive user information including privileges, groups, and SIDs | Yes |
| `>> c:\\attacker\\who.txt` | Appends output to the specified log file without overwriting | Yes |

## Examples

### Basic Usage

```cmd
whoami /all >> c:\attacker\who.txt
```

### Advanced Usage

```cmd
whoami /all /fo csv >> c:\attacker\who.csv
```

## Expected Output

Detailed textual output listing the user SID, privileges (e.g., SeDebugPrivilege), and group memberships (e.g., Administrators), appended to the file. Successful escalation shows high-privilege groups like SYSTEM or Administrators.

## Related

- [[Related Procedure: Trigger-DLL-Hijacking-and-Validate-Escalation]]
