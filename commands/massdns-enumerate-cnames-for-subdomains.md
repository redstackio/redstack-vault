---
type: command
executor: bash
data: massdns -r $_RESOLVER_LIST -t CNAME -o S -w $_OUTPUT_FILE $_SUBDOMAINS_FILE
output: null
tags:
  - dns
  - reconnaissance
platforms:
  - Linux
verified: true
validated: true
---

# massdns-enumerate-cnames-for-subdomains

## Command

```bash
massdns -r $_RESOLVER_LIST -t CNAME -o S -w $_OUTPUT_FILE $_SUBDOMAINS_FILE
```

## Description

This command uses MassDNS to perform bulk CNAME record resolution against a list of subdomains, distributing queries across multiple DNS resolvers for speed and evasion. It outputs only successful resolutions in a simple, parseable format, ideal for reconnaissance to uncover domain aliases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r $_RESOLVER_LIST | Path to file containing DNS resolver IP addresses (one per line) | Yes |
| -t CNAME | Query type: Restrict to CNAME records only | Yes |
| -o S | Output format: Simple (subdomain. CNAME target) | Yes |
| -w $_OUTPUT_FILE | Path to output file for results | Yes |
| $_SUBDOMAINS_FILE | Path to input file with subdomains (one per line) | Yes |

## Examples

### Basic Usage

```bash
massdns -r resolvers.txt -t CNAME -o S -w cnames-output.txt subdomains.txt
```

### Advanced Usage

For verbose output and threading (add -T for TCP fallback):

```bash
massdns -r resolvers.txt -t CNAME -o S -T -w cnames-output.txt -t 100 subdomains.txt
```

## Expected Output

The output file will contain lines for successful resolutions, e.g.:

```
api.example.com. CNAME api.cloudfront.net.
mail.example.com. CNAME mx.google.com.
www.example.com. NXDOMAIN
```

Failures like NXDOMAIN or SERVFAIL are included but can be filtered post-run. Progress is shown on stderr during execution.

## Related

- [[procedures/Enumerate-CNAME-Records-for-Subdomains-Using-MassDNS]]
- [[tools/massdns]]
