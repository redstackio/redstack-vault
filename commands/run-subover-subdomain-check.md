---
id: a1b78fbc-7c9e-4031-8437-9d70e62165ca
name: run-subover-subdomain-check
type: command
executor: bash
data: ./SubOver -l subdomains.txt
output: null
created_at: '2023-04-06T03:56:25.834042+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - subdomain-takeover
verified: true
validated: true
---

# run-subover-subdomain-check

## Command

```bash
./SubOver -l subdomains.txt
```

## Description

This command runs the SubOver tool to scan a list of subdomains for takeover vulnerabilities by checking DNS records against a fingerprint database of services like AWS, GitHub, and Heroku. It is a key step in reconnaissance to identify claimable subdomains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Path to the input file containing subdomains (one per line) | Yes |
| `subdomains.txt` | Example file name; replace with actual path | Yes |
| `./SubOver` | Path to the SubOver binary | Yes |

## Examples

### Basic Usage

```bash
./SubOver -l subdomains.txt
```

### Advanced Usage

Run with verbose output if supported (check -h for options):
```bash
./SubOver -l subdomains.txt -v
```

## Expected Output

Console output categorizing subdomains:
```
[INFO] Loading fingerprints...
[INFO] Checking 10 subdomains...
sub1.example.com: SAFE (points to active service)
sub2.example.com: VULNERABLE -> github (CNAME: sub2.github.io - repo deleted)
sub3.example.com: UNKNOWN
Takeover Summary: 1 vulnerable
```
Vulnerable entries include service details for manual claiming.

## Related

- [[procedures/Subdomain-Enumeration-and-Takeover-Detection-using-SubOver]]
- [[commands/install-subover-via-go]]
