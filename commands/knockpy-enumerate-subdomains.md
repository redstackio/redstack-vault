---
id: cmd-uuid-001
data: knockpy gratipay.com
tags:
  - reconnaissance
  - dns
  - subdomain
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:22.983Z'
verified: false
validated: true
submitted: true
---
# knockpy-enumerate-subdomains

## Command

```bash
knockpy gratipay.com
```

## Description

This command uses knockpy to enumerate subdomains of the target domain 'gratipay.com' through brute-force guessing and permutation of common names, helping identify potential vulnerabilities like dangling records.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gratipay.com` | The target domain to scan for subdomains | Yes |

## Examples

### Basic Usage

```bash
knockpy example.com
```

### Advanced Usage

Knockpy supports additional options like output files, but basic usage is domain-only.

```bash
knockpy -w wordlist.txt example.com
```

## Expected Output

A console output listing discovered subdomains, IP addresses, and DNS types. For example:

Subdomains: www.gratipay.com.herokudns.com
IPs: [resolved IP]

Includes NXDOMAIN for non-existent ones and highlights valid resolutions.

## Related

- [[Related Procedure: Subdomain-Enumeration-with-Knockpy]]
