---
id: 1ac0bdef-5a93-4c47-945b-59835ae161b8
name: set-securitytrails-credentials-for-subfinder
type: command
executor: bash
data: subfinder -update-config -set-config SecurityTrailsKey='$_API_KEY'
output: null
created_at: '2023-04-06T03:56:25.499539+00:00'
updated_at: '2023-04-10T20:25:39.525193+00:00'
platforms:
  - Linux
tags:
  - configuration
  - recon
verified: true
validated: true
---

# set-securitytrails-credentials-for-subfinder

## Command

```bash
subfinder -update-config -set-config SecurityTrailsKey='$_API_KEY'
```

## Description

Sets the SecurityTrails API key in Subfinder's configuration to enable historical DNS record queries for subdomain discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -update-config | Updates the config file | Yes |
| -set-config | Specifies the API key | Yes |
| SecurityTrailsKey='$_API_KEY' | SecurityTrails API key | Yes |

## Examples

### Basic Usage

```bash
subfinder -update-config -set-config SecurityTrailsKey='st_key_abc123'
```

## Expected Output

Configuration updated successfully.

## Related

- [[procedures/Subdomain-Enumeration-with-Subfinder]]
- [[tools/Subfinder]]
