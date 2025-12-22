---
id: 4766fd8f-cc5c-42b0-b094-53b653a0dc7e
name: aquatone-scan-subdomains
type: command
executor: bash
data: aquatone-scan --domain $_DOMAIN
output: null
created_at: '2023-04-06T03:56:25.578182+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - scanning
verified: true
validated: true
---

# aquatone-scan-subdomains

## Command

```bash
aquatone-scan --domain $_DOMAIN
```

## Description

Actively scans subdomains from hosts.txt for open ports and live URLs, defaulting to common web ports. Outputs responsive URLs to urls.txt in ~/.aquatone/$_DOMAIN/.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --domain | Target domain directory to scan | Yes |
| --ports | Comma-separated ports (default: 80,443) or 'large' for extended | No |
| --threads | Number of concurrent threads (default: 10) | No |

## Examples

### Basic Usage

```bash
aquatone-scan --domain example.com
```

### Custom Ports

```bash
aquatone-scan --domain example.com --ports 80,443,3000,8080
```

### Large Port Set with Threads

```bash
aquatone-scan --domain example.com --ports large --threads 25
```

## Expected Output

[INFO] Scanning 150 hosts for example.com
[INFO] 45 responsive URLs found
[INFO] Results saved to /root/.aquatone/example.com/urls.txt

urls.txt example:
http://www.example.com:80/
https://mail.example.com:443/
...

## Related

- [[procedures/Subdomain-Enumeration-with-Aquatone]]
- [[tools/Aquatone]]
