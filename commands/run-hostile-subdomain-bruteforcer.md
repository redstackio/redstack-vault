---
id: f1820543-f86e-4096-ba54-243db83f74a7
name: run-hostile-subdomain-bruteforcer
type: command
executor: bash
data: ./sub_brute.rb -d $_DOMAIN -w $_WORDLIST -t $_THREADS
output: null
created_at: '2023-04-06T03:56:25.800850+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - recon
  - enumeration
verified: true
validated: true
---

# run-hostile-subdomain-bruteforcer

## Command

```bash
./sub_brute.rb -d $_DOMAIN -w $_WORDLIST -t $_THREADS
```

## Description

This command executes the Hostile Subdomain Bruteforcer Ruby script to bruteforce subdomains of a target domain and check for takeover vulnerabilities. It resolves potential subdomains via DNS and fingerprints responses for dangling records pointing to claimable services like AWS S3 or GitHub Pages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d $_DOMAIN | Target domain (e.g., example.com) | Yes |
| -w $_WORDLIST | Path to wordlist file (default: wordlist.txt in repo) | No |
| -t $_THREADS | Number of threads for parallel DNS queries (default: 25) | No |

## Examples

### Basic Usage

```bash
./sub_brute.rb -d example.com
```

### With Custom Wordlist and Threads

```bash
./sub_brute.rb -d example.com -w /path/to/custom_wordlist.txt -t 100
```

## Expected Output

[*] Checking for subdomains of example.com

admin.example.com - 192.0.2.1 (Possible takeover: AWS S3 bucket)
api.example.com - 198.51.100.1 (Live, no takeover)

[+] TAKEOVER POSSIBLE: test.example.com points to unused Heroku app

## Related

- [[procedures/Subdomain-Enumeration-and-Takeover-using-Hostile-Subdomain-Bruteforcer]]
- [[tools/Hostile-Subdomain-Bruteforcer]]
