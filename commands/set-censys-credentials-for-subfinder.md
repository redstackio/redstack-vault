---
id: 5b47688d-1a46-4db2-bfd4-183df4595dc1
name: set-censys-credentials-for-subfinder
type: command
executor: bash
data: >-
  subfinder -update-config -set-config
  CensysUsername='$_USERNAME',CensysSecret='$_SECRET'
output: null
created_at: '2023-04-06T03:56:25.499461+00:00'
updated_at: '2023-04-10T20:25:39.525193+00:00'
platforms:
  - Linux
tags:
  - configuration
  - recon
verified: true
validated: true
---

# set-censys-credentials-for-subfinder

## Command

```bash
subfinder -update-config -set-config CensysUsername='$_USERNAME',CensysSecret='$_SECRET'
```

## Description

This command configures Subfinder to use Censys API credentials, enabling access to internet-wide scan data for subdomain discovery from certificates and hosts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -update-config | Flag to update the configuration file | Yes |
| -set-config | Sets key-value pairs for config | Yes |
| CensysUsername='$_USERNAME' | Censys API username | Yes |
| CensysSecret='$_SECRET' | Censys API secret key | Yes |

## Examples

### Basic Usage

```bash
subfinder -update-config -set-config CensysUsername='myuser',CensysSecret='mysecret'
```

### Advanced Usage

Combined with other configs:

```bash
subfinder -update-config -set-config CensysUsername='myuser',CensysSecret='mysecret' PassivetotalKey='key'
```

## Expected Output

Configuration updated successfully.

If invalid, error: Failed to validate credentials.

## Related

- [[procedures/Subdomain-Enumeration-with-Subfinder]]
- [[tools/Subfinder]]
