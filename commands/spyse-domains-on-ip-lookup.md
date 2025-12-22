---
type: command
executor: bash
data: spyse -target $_TARGET_IP --domains-on-ip
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - reconnaissance
  - spyse
verified: true
validated: true
---

# spyse-domains-on-ip-lookup

## Command

```bash
spyse -target $_TARGET_IP --domains-on-ip
```

## Description

This command uses the Spyse CLI to perform a reverse IP lookup, retrieving all domains and subdomains hosted on the specified IP address. It is used during network reconnaissance to discover co-hosted sites that may provide additional attack vectors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | The target IP address to query for associated domains (e.g., 52.14.144.171) | Yes |
| -target | Flag to specify the IP target | Yes |
| --domains-on-ip | Flag to retrieve domains hosted on the target IP | Yes |

## Examples

### Basic Usage

```bash
spyse -target 52.14.144.171 --domains-on-ip
```

### Advanced Usage

Pipe output to a file for analysis:

```bash
spyse -target 52.14.144.171 --domains-on-ip > discovered_domains.txt
```

## Expected Output

The command outputs a list of domains in a structured format, such as JSON or plain text, including domain names, subdomains, and metadata like hosting info. Example:

```
Domain: example1.com
Subdomains: www.example1.com, api.example1.com
Hosting Provider: AWS
SSL Info: Valid certificate

Domain: example2.com
...
```

Success is indicated by a non-empty list of domains. If no results, check API key or IP validity.

## Related

- [[procedures/Spyse-Reverse-IP-Lookup-for-Domain-Discovery]]
- [[tools/Spyse]]
