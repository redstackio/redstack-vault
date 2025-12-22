---
data: >-
  # Configured in Turbo Intruder: Use wordlist for subdomains under
  bountypay.h1ctf.com
tags:
  - recon
type: command
output: List of live subdomains
executor: bash
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.945Z'
id: eb90b6af-afe6-40f5-81dd-5b8bfdf86f79
verified: false
validated: true
submitted: true
---
# turbo-intruder-subdomain-enum

## Command

```bash
# Run in Burp Suite Turbo Intruder with wordlist
```

## Description

High-speed subdomain enumeration using Turbo Intruder extension in Burp Suite, fuzzing Host header with common domain names.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| wordlist | Common subdomains list | Yes |
| target | Base domain like bountypay.h1ctf.com | Yes |

## Examples

### Basic Usage

```bash
# Payload: §s.bountypay.h1ctf.com in Host
```

### Advanced Usage

```bash
# With custom rate limits in Turbo Intruder
```

## Expected Output

HTTP responses indicating live subdomains, e.g., app.bountypay.h1ctf.com: 200 OK.

## Related

- [[Related Procedure: Enumerate-Subdomains-of-Target-Domain]]
