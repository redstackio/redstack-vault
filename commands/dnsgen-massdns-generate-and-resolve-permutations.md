---
id: bbf0de6b-746f-4496-9e2d-3a9c7e3e03a7
name: dnsgen-massdns-generate-and-resolve-permutations
type: command
executor: bash
data: >
  cat domains.txt | dnsgen - | massdns -r /path/to/resolvers.txt -t A -o J
  --flush 2>/dev/null
output: null
created_at: '2020-07-24T17:11:30.890757+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - dns
verified: true
validated: true
---

# dnsgen-massdns-generate-and-resolve-permutations

## Command

```bash
cat domains.txt | dnsgen - | massdns -r /path/to/resolvers.txt -t A -o J --flush 2>/dev/null
```

## Description

This command generates domain name permutations from an input file using dnsgen and resolves them via massdns to discover valid DNS A records, useful for subdomain brute-forcing during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domains.txt | Path to input file with base domains/keywords, one per line | Yes |
| /path/to/resolvers.txt | Path to file containing DNS resolvers (format: ip:port) | Yes |
| -t A | Query type: A records (IPv4 addresses) | Yes |
| -o J | Output format: JSON lines | Yes |
| --flush | Flush output immediately without buffering | No |
| 2>/dev/null | Suppress stderr for clean output | No |

## Examples

### Basic Usage

```bash
cat domains.txt | dnsgen - | massdns -r resolvers.txt -t A -o J --flush 2>/dev/null > results.json
```

### Advanced Usage

For verbose output, remove 2>/dev/null and add massdns -v flag if supported:

```bash
cat domains.txt | dnsgen - | massdns -r resolvers.txt -t A -o J --flush -v
```

## Expected Output

JSON lines for each resolved domain, e.g.:

```json
{"timestamp":"2023-01-01T00:00:00Z","resolver":"8.8.8.8:53","query":"api.example.com","answer":{"A":["192.0.2.1"]}}
{"timestamp":"2023-01-01T00:00:01Z","resolver":"8.8.4.4:53","query":"admin.example.com","answer":{"A":["192.0.2.2"]}}
```

Unresolved queries are not outputted. Parse with jq or grep for analysis.

## Related

- [[procedures/Generate-and-Resolve-Domain-Name-Permutations]]
- [[tools/dnsgen]]
- [[tools/massdns]]
