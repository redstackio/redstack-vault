---
type: command
executor: bash
data: >-
  nmap --script shodan-hq.nse --script-args
  'apikey=$_SHODAN_API_KEY,target=$_TARGET_HOST' $_TARGET_HOST
output: null
platforms:
  - Linux
tags:
  - reconnaissance
  - passive-scan
verified: true
validated: true
---

# Nmap Shodan HQ Integration Scan

## Command

```bash
nmap --script shodan-hq.nse --script-args 'apikey=$_SHODAN_API_KEY,target=$_TARGET_HOST' $_TARGET_HOST
```

## Description

This command integrates Nmap with the shodan-hq NSE script to query Shodan's database for information on the target host, identifying similar devices, open ports, and services passively. Use it during initial reconnaissance to gather infrastructure details without aggressive scanning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SHODAN_API_KEY | Your Shodan API key for authentication | Yes |
| $_TARGET_HOST | IP address or hostname of the target | Yes |
| --script shodan-hq.nse | Loads the Shodan HQ script | Built-in |
| --script-args | Passes API key and target to the script | Yes |

## Examples

### Basic Usage

```bash
nmap --script shodan-hq.nse --script-args 'apikey=yourkey,target=example.com' example.com
```

### Advanced Usage

```bash
nmap -sV --script shodan-hq.nse --script-args 'apikey=yourkey,target=192.168.1.1' 192.168.1.1
```

## Expected Output

Nmap results with Shodan insights:

```
Nmap scan report for example.com
Host is up.
PORT   STATE SERVICE
80/tcp open  http
| shodan-hq: 
|   Similar devices: Apache httpd 2.4.41
|   Ports: 80,443
|_  Vulnerabilities: CVE-2021-41773
```

## Related

- [[procedures/passive-reconnaissance-information-gathering]]
- [[tools/Nmap]]
