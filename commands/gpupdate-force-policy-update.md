---
type: command
executor: cmd
data: gpupdate /force
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - gpo
verified: true
validated: true
---

# gpupdate-force-policy-update

## Command

```cmd
gpupdate /force
```

## Description

Refreshes local and Active Directory-based Group Policy settings, forcing reapplication of all policies including modified Scheduled Tasks. Use after editing GPOs to immediately deploy changes to the target machine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /force | Reapplies all settings, ignoring unchanged policies | Yes |

## Examples

### Basic Usage

Run in elevated Command Prompt:

```cmd
gpupdate /force
```

### Target Specific

Update only computer policies:

```cmd
gpupdate /target:computer /force
```

## Expected Output

Updating policy...

Computer Policy update has completed successfully.
User Policy update has completed successfully.

If errors occur (e.g., network issues), it will show: "User Policy update failed."

## Related

- [[procedures/Exploit-GPO-Scheduled-Tasks-Preferences]]
- [[commands/access-sysvol-gpo-folder]]
