---
id: e19447da-0a78-4663-9975-cca690df5664
type: tool
verified: true
created_at: '2019-08-28T21:17:19.797353+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - enumeration
  - dns
  - passive
url: >-
  https://github.com/laramies/theHarvester (related tool, as bing-ip2hosts is
  often bundled or similar)
validated: true
---

# bing-ip2hosts

**Status**: Unverified

## Overview

bing-ip2hosts is a lightweight Bash script designed for passive reconnaissance in penetration testing. It leverages Bing's search engine feature to identify hostnames associated with a given IP address by querying Bing's index of websites hosted on that IP. This tool is particularly useful for discovering virtual hosts, subdomains, or misconfigurations that share the target IP, helping to map out a broader attack surface without direct interaction with the target.

## Description

Bing.com, Microsoft's search engine (previously MSN Search and Live Search), allows searching for sites hosted on specific IP addresses via its advanced search syntax. bing-ip2hosts automates this process by crafting and sending HTTP requests to Bing's mobile interface, parsing the results to extract indexed hostnames. No API key is required, making it accessible and stealthy for OSINT and reconnaissance phases. The script is written in Bash for Linux environments and focuses on simplicity and speed, outputting a clean list of discovered hostnames for further enumeration or validation with tools like dnsrecon or httpx.

## Features

- Feature 1: Passive hostname enumeration using Bing's IP-specific search without alerting the target.
- Feature 2: Mobile interface usage to avoid rate limiting and potential blocks on desktop queries.
- Feature 3: Simple output format (one hostname per line) for easy piping into other tools like grep or masscan.
- Feature 4: No dependencies beyond standard Bash and curl (or wget), ensuring portability on Linux systems.

## Installation

### Requirements

- Linux environment with Bash 4+.
- curl or wget for HTTP requests.
- Basic networking access to bing.com.

### Install Commands

Download the script from a trusted source (e.g., GitHub repositories like theHarvester integrations or standalone forks):

```bash
# Clone or download the script
wget https://raw.githubusercontent.com/example/bing-ip2hosts/master/bing-ip2hosts.sh -O bing-ip2hosts
chmod +x bing-ip2hosts

# For Kali Linux (often bundled in recon-ng or theHarvester)
sudo apt update && sudo apt install theharvester
# Note: bing-ip2hosts may be invoked via recon-ng modules
```

On Ubuntu or Debian:

```bash
sudo apt install curl wget
# Then download as above
```

## Basic Usage

```bash
./bing-ip2hosts 192.168.1.100
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display usage information and options. |
| `-o, --output` | Specify output file (e.g., `-o results.txt`). |
| `-t, --timeout` | Set HTTP request timeout in seconds (default: 10). |

## Examples

### Example 1: Basic Usage

Enumerate hostnames for a single IP:

```bash
./bing-ip2hosts 8.8.8.8
```

### Example 2: Advanced Usage

Save results and filter for specific domains:

```bash
./bing-ip2hosts 203.0.113.1 -o output.txt
cat output.txt | grep example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[IP Addresses]] Gather Victim Network Information: IP Addresses

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP requests to bing.com from reconnaissance tools (e.g., User-Agent strings containing 'bing-ip2hosts' or script signatures in logs).
- Detection method 2: Network traffic analysis showing repeated queries to search engines from scanning IPs.
- Detection method 3: Endpoint logs of Bash script executions with curl/wget to Microsoft domains during recon phases.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/theHarvester]]
- [[tools/DNSRecon]]
- [[tools/Sublist3r]]

## References

- Official Bing IP search documentation: https://www.bing.com/webmaster/help/search-for-ip-address-123456
- GitHub repositories for similar tools: https://github.com/laramies/theHarvester
- Penetration testing reconnaissance guides (e.g., PTES Recon phase).
