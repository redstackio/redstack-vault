---
type: command
executor: bash
data: altdns -i $_INPUT_FILE -o $_OUTPUT_DIR -w $_WORDS_FILE -r -s $_RESULTS_FILE
output: null
tags:
  - reconnaissance
  - dns
platforms:
  - Linux
verified: true
validated: true
---

# altdns-generate-and-resolve-subdomains

## Command

```bash
altdns -i $_INPUT_FILE -o $_OUTPUT_DIR -w $_WORDS_FILE -r -s $_RESULTS_FILE
```

## Description

This command uses altdns to generate subdomain permutations from a base list and a wordlist, then resolves them via DNS to identify active hosts. It is used during reconnaissance to expand known subdomains into potential hidden ones like development or staging environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_INPUT_FILE | Path to input file with base subdomains (one per line) | Yes |
| -o $_OUTPUT_DIR | Directory for intermediate permutation output | Yes |
| -w $_WORDS_FILE | Path to wordlist for mutations (e.g., prefixes/suffixes) | Yes |
| -r | Enable DNS resolution for generated permutations | Yes (for this use case) |
| -s $_RESULTS_FILE | Path to output file for resolved subdomains only | Yes |

## Examples

### Basic Usage

```bash
altdns -i subdomains.txt -o output -w words.txt -r -s results.txt
```

### Advanced Usage

```bash
altdns -i subdomains.txt -o output -w words.txt -r -s results.txt -t 4
```

> Adds -t 4 for 4 threads to speed up resolution on large lists.

## Expected Output

The $_RESULTS_FILE will list only subdomains that resolved successfully, e.g.:

dev.target.com
api-staging.target.com

Intermediate files in $_OUTPUT_DIR will contain all permutations before resolution.

## Related

- [[procedures/Mutate-Subdomain-Wordlist-for-DNS-Enumeration-Using-Altdns]]
- [[tools/Altdns]]
