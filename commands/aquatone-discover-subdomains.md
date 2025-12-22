---
id: 22099ef5-ae7a-4bb6-9cd4-362425183031
name: aquatone-discover-subdomains
type: command
executor: bash
data: aquatone-discover --domain $_DOMAIN
output: null
created_at: '2023-04-06T03:56:25.578136+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
verified: true
validated: true
---

# aquatone-discover-subdomains

## Command

```bash
aquatone-discover --domain $_DOMAIN
```

## Description

Discovers subdomains for the specified domain using passive intelligence sources. Generates hosts.txt in ~/.aquatone/$_DOMAIN/ with enumerated subdomains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --domain | Target domain to enumerate (e.g., example.com) | Yes |
| --threads | Number of concurrent threads (default: 10) | No |
| --sleep | Base delay between requests in seconds | No |
| --jitter | Random jitter added to sleep (0-100%) | No |
| --set-key shodan | Sets Shodan API key for enhanced queries (run separately) | No |

## Examples

### Basic Usage

```bash
aquatone-discover --domain example.com
```

### With Threads and Delays

```bash
aquatone-discover --domain example.com --threads 25 --sleep 5 --jitter 30
```

### Set Shodan Key (Separate Command)

```bash
aquatone-discover --set-key shodan o1hyw8pv59vSVjrZU3Qaz6ZQqgM91ihQ
```

## Expected Output

[INFO] Starting subdomain discovery for example.com
[INFO] Found 150 subdomains
[INFO] Results saved to /root/.aquatone/example.com/hosts.txt

The hosts.txt file will list subdomains like:
www.example.com
mail.example.com
...

## Related

- [[procedures/Subdomain-Enumeration-with-Aquatone]]
- [[tools/Aquatone]]
