---
type: command
executor: command_prompt
data: sc config WinDefend start= disabled
output: '[SC] ChangeServiceConfig SUCCESS'
platforms:
  - Windows
tags:
  - defender
  - service-disable
  - defense-evasion
verified: true
validated: true
---

# SC Config WinDefend Start Disabled

## Command

```command_prompt
sc config WinDefend start= disabled
```

## Description

This command modifies the startup type of the WinDefend service (Windows Defender Antivirus) to 'disabled', preventing it from starting automatically on boot. It requires administrative privileges and is useful in scenarios where antivirus interference needs to be minimized during testing or evasion. Note that on modern Windows versions with Tamper Protection enabled, this may fail without additional bypasses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `WinDefend` | The internal name of the Windows Defender service. | Yes |
| `start=` | Specifies the startup type; 'disabled' prevents automatic or manual starts. | Yes |
| `disabled` | Sets the service to not start under any condition. | Yes |

## Examples

### Basic Usage

```command_prompt
sc config WinDefend start= disabled
```

### Verification

After running, verify the change:

```command_prompt
sc qc WinDefend
```

Expected to show START_TYPE : 4 DISABLED.

### Advanced Usage

To apply to multiple services, chain with other sc commands or use a batch script.

## Expected Output

```
C:\>sc config WinDefend start= disabled
[SC] ChangeServiceConfig SUCCESS
```

If successful, no errors are returned. On failure (e.g., insufficient privileges), you may see '[SC] OpenService FAILED 5: Access is denied.'

## Related

- [[tools/service-control-sc]] (parent tool)
- [[commands/sc-stop-windefend]] (complementary command to stop the service immediately)
