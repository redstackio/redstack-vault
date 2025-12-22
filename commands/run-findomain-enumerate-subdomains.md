---
id: d419967a-3d2a-48f1-8746-bc364515c6ea
name: run-findomain-enumerate-subdomains
type: command
executor: bash
data: ./findomain-linux -t $_TARGET_DOMAIN -o $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:25.542112+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - subdomain
verified: true
validated: true
---

# run-findomain-enumerate-subdomains

## Command

```bash
./findomain-linux -t $_TARGET_DOMAIN -o $_OUTPUT_FILE
```

## Description

This command runs Findomain to enumerate subdomains of a target domain, using brute-force and passive sources, and saves results to a specified output file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t $_TARGET_DOMAIN | Target domain to enumerate (e.g., example.com) | Yes |
| -o $_OUTPUT_FILE | Output file for results (e.g., results.txt) | Yes |
| -r | Enable recursive enumeration | No |
| --format json | Output in JSON format | No |

## Examples

### Basic Usage

```bash
./findomain-linux -t example.com -o subdomains.txt
```

### With JSON Output

```bash
./findomain-linux -t example.com -o subdomains.json --format json
```

## Expected Output

Console output:

[+] Enumerating subdomains for example.com
[+] 150 subdomains found

Subdomains printed to console and saved to file:

mail.example.com
www.example.com
api.example.com

File '$_OUTPUT_FILE' contains one subdomain per line.

## Related

- [[procedures/Subdomain-Enumeration-with-Findomain]]
- [[commands/set-findomain-api-tokens]]
