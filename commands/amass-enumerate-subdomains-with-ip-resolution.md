---
id: f27b22c7-ff9d-425e-9088-acc160356342
type: command
executor: bash
data: amass enum -ip -d $_TARGET_DOMAIN
output: "root@kali ~# amass enum -ip -d redstack.io\nQuerying ThreatCrowd for redstack.io subdomains\n... [various sources] ...\nredstack.io 13.33.71.21,13.33.71.17,13.33.71.50,13.33.71.66\nwww.redstack.io 13.224.13.8,13.224.13.104,13.224.13.96,13.224.13.117\nAverage DNS queries performed: 174/sec, Average retries required: 10.92%\n\nOWASP Amass v3.7.2                                https://github.com/OWASP/Amass\n--------------------------------------------------------------------------------\n2 names discovered - dns: 1, scrape: 1\n--------------------------------------------------------------------------------\nASN: 16509 - AMAZON-02, US\n\t13.33.64.0/21     \t4    Subdomain Name(s)\n\t13.224.8.0/21     \t4    Subdomain Name(s)\n\nThe enumeration has finished\nDiscoveries are being migrated into the Cayley Graph database"
created_at: '2020-06-29T16:22:08.332675+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - subdomain
  - enum
verified: true
validated: true
---

# amass-enumerate-subdomains-with-ip-resolution

## Command

```bash
amass enum -ip -d $_TARGET_DOMAIN
```

## Description

Enumerates subdomains using passive and active sources, resolving IPs for each.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ip | Enable IP resolution | Yes |
| -d $_TARGET_DOMAIN | Target domain | Yes |

## Examples

### Basic Usage

```bash
amass enum -ip -d example.com
```

## Expected Output

Logs of queried sources, discovered subdomains with IPs, and summary stats.

## Related

- [[procedures/Enumerate-Subdomains-with-Amass]]
- [[tools/amass]]
