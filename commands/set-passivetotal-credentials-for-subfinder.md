---
id: b5e7cfd1-9895-44bc-a406-9b1d4db18c71
name: set-passivetotal-credentials-for-subfinder
type: command
executor: bash
data: >-
  subfinder -update-config -set-config
  PassivetotalUsername='$_USERNAME',PassivetotalKey='$_API_KEY'
output: null
created_at: '2023-04-06T03:56:25.499351+00:00'
updated_at: '2023-04-10T20:25:39.525193+00:00'
platforms:
  - Linux
tags:
  - configuration
  - recon
verified: true
validated: true
---

# set-passivetotal-credentials-for-subfinder

## Command

```bash
subfinder -update-config -set-config PassivetotalUsername='$_USERNAME',PassivetotalKey='$_API_KEY'
```

## Description

This command sets PassiveTotal API credentials in Subfinder's config, allowing queries to their passive DNS and WHOIS data for subdomain enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -update-config | Updates the YAML config file | Yes |
| -set-config | Specifies config keys and values | Yes |
| PassivetotalUsername='$_USERNAME' | PassiveTotal username | Yes |
| PassivetotalKey='$_API_KEY' | PassiveTotal API key | Yes |

## Examples

### Basic Usage

```bash
subfinder -update-config -set-config PassivetotalUsername='user',PassivetotalKey='key123'
```

## Expected Output

Configuration updated successfully.

## Related

- [[procedures/Subdomain-Enumeration-with-Subfinder]]
- [[tools/Subfinder]]
