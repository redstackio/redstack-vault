---
id: f2c4d829-9241-40c8-a117-30f5befb5e22
name: spyse-enumerate-subdomains
type: command
executor: bash
data: spyse -target $_TARGET_DOMAIN --subdomains
output: null
created_at: '2023-04-06T03:56:22.094897+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - reconnaissance
  - subdomain-enumeration
verified: true
validated: true
---

# spyse-enumerate-subdomains

## Command

```bash
spyse -target $_TARGET_DOMAIN --subdomains
```

## Description

This command uses the Spyse CLI to enumerate subdomains for a given target domain by querying Spyse's passive reconnaissance database. It is ideal for initial reconnaissance to map a target's attack surface without active DNS probing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DOMAIN | The target domain to enumerate (e.g., example.com) | Yes |
| --subdomains | Flag to specifically request subdomain enumeration | Yes |

## Examples

### Basic Usage

```bash
spyse -target example.com --subdomains
```

### Usage with Output Redirection

```bash
spyse -target example.com --subdomains > subdomains.txt
```

## Expected Output

A list of discovered subdomains in JSON or tabular format, for example:

[
  "sub1.example.com",
  "sub2.example.com",
  "api.example.com"
]

Each entry may include additional metadata like associated IP addresses or ports if available in Spyse's database.

## Related

- [[procedures/Spyse-Subdomain-Enumeration]]
- [[tools/Spyse]]
