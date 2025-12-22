---
type: command
executor: bash
data: |
  echo "$_IP" | hakrevdns -r $_RESOLVER
output: null
platforms:
  - Linux
tags:
  - reconnaissance
  - dns
verified: true
validated: true
---

# hakrevdns-lookup-subdomain-with-custom-resolver

## Command

```bash
echo "$_IP" | hakrevdns -r $_RESOLVER
```

## Description

This command performs a reverse DNS lookup on a single IP using a specified custom resolver to avoid default OS DNS settings. It is ideal for targeted queries or when default resolvers are unreliable/blocked.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_IP | Single IP address to resolve (e.g., 173.0.84.110) | Yes |
| -r | Flag to specify custom DNS resolver | No |
| $_RESOLVER | IP of the DNS resolver (e.g., 1.1.1.1 for Cloudflare) | No (uses default if omitted) |

## Examples

### Basic Usage

```bash
echo "173.0.84.110" | hakrevdns -r 1.1.1.1
```

### Advanced Usage

For Google DNS:

```bash
echo "8.8.8.8" | hakrevdns -r 8.8.8.8
```

## Expected Output

Outputs the IP and resolved domain if found, or just the IP. Example:

```
173.0.84.110 mail.example.com
```

## Related

- [[procedures/Reverse-DNS-Lookup-for-Subdomains-Using-Hakrevdns]]
- [[tools/hakrevdns]]
