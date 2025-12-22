---
id: f2ff86aa-a2fa-4dee-9d8e-be43998b3bbe
name: netdom-trust-enable-pam-options
type: command
executor: cmd
data: |-
  netdom trust $_TRUSTING_DOMAIN /domain:$_TRUSTED_DOMAIN /EnableSIDHistory:Yes 
  netdom trust $_TRUSTING_DOMAIN /domain:$_TRUSTED_DOMAIN /EnablePIMTrust:Yes 
  netdom trust $_TRUSTING_DOMAIN /domain:$_TRUSTED_DOMAIN /Quarantine:No
output: null
created_at: '2023-04-06T03:56:07.394107+00:00'
updated_at: '2023-04-10T20:26:01.511941+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - trust
  - pam
verified: true
validated: true
---

# netdom-trust-enable-pam-options

## Command

```cmd
netdom trust $_TRUSTING_DOMAIN /domain:$_TRUSTED_DOMAIN /EnableSIDHistory:Yes
netdom trust $_TRUSTING_DOMAIN /domain:$_TRUSTED_DOMAIN /EnablePIMTrust:Yes
netdom trust $_TRUSTING_DOMAIN /domain:$_TRUSTED_DOMAIN /Quarantine:No
```

## Description

This multi-line command sequence enhances an existing trust by enabling SID history (for preserving user permissions), PIM trust (for privileged access management), and disabling quarantine (removing SID filtering). Run after creating the base transitive trust.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TRUSTING_DOMAIN | The local domain (e.g., lab.local) | Yes |
| $_TRUSTED_DOMAIN | The remote domain (e.g., bastion.local) | Yes |
| /EnableSIDHistory:Yes | Allows SID migration for access continuity | Built-in |
| /EnablePIMTrust:Yes | Activates PIM for cross-domain admin management | Built-in |
| /Quarantine:No | Disables SID filtering for full access | Built-in |

## Examples

### Basic Usage

```cmd
netdom trust lab.local /domain:bastion.local /EnableSIDHistory:Yes
netdom trust lab.local /domain:bastion.local /EnablePIMTrust:Yes
netdom trust lab.local /domain:bastion.local /Quarantine:No
```

## Expected Output

For each line:

The trust attribute has been successfully modified.

The command completed successfully.

## Related

- [[procedures/Establish-and-Enumerate-PAM-Trust-Between-Domains]]
- [[commands/netdom-trust-create-transitive]]
