---
data: whoami
tags:
  - discovery
  - privileges
type: command
executor: cmd
platforms:
  - Windows
id: 0c41c784-bdfe-4e0e-9eb5-3c533189f171
created_at: '2025-12-14T17:29:44.265Z'
updated_at: '2025-12-14T17:29:44.265Z'
verified: false
validated: true
submitted: true
---
# whoami Check Privileges

## Command

```cmd
whoami
```

## Description

This command displays the current username and domain, used to verify privilege escalation by confirming execution as NT AUTHORITY\SYSTEM in an elevated context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters; outputs current user | No |

## Examples

### Basic Usage

```cmd
whoami
```

### Advanced Usage

```cmd
whoami /priv
```

> Shows privileges; useful post-escalation to list SYSTEM rights.

## Expected Output

Outputs the current user, e.g., 'nt authority\system' for successful escalation, or 'domain\user' for standard context.

## Related

- [[Related Procedure: Verify SYSTEM Privilege Escalation]]
