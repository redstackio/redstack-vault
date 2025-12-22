---
type: command
executor: command_prompt
data: netsh firewall set opmode DISABLE
output: Ok.
platforms:
  - Windows
tags:
  - firewall-bypass
verified: true
validated: true
---

# netsh-disable-legacy-firewall

## Command

```command_prompt
netsh firewall set opmode DISABLE
```

## Description

This command uses the legacy netsh 'firewall' context to completely disable the Windows Firewall on Windows Server 2008 and earlier versions (or systems using the deprecated interface). It sets the operational mode to disabled, allowing all inbound and outbound traffic without filtering. Useful in post-exploitation for evading network defenses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `firewall` | Specifies the legacy firewall context | Yes |
| `set` | Command to modify settings | Yes |
| `opmode` | Operational mode parameter | Yes |
| `DISABLE` | Disables the firewall entirely | Yes |

## Examples

### Basic Usage

```command_prompt
netsh firewall set opmode DISABLE
```

### Advanced Usage

To re-enable the firewall:

```command_prompt
netsh firewall set opmode ENABLE
```

Verify the change:

```command_prompt
netsh firewall show opmode
```

## Expected Output

```
Ok.
```

Returns 'Ok.' on success. Verify with `netsh firewall show opmode` which should display 'Operational mode: Disable'. On failure, it may return an error like 'The requested operation requires elevation' if not run as administrator.

## Related

- [[procedures/Disable-Windows-Firewall]]
- [[commands/netsh-show-legacy-firewall-state]]
