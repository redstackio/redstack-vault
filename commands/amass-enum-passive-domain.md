---
id: 9dbc5701-85d0-4084-97e4-27ebb9db88bb
type: command
executor: bash
data: amass enum -passive -d $_TARGET_DOMAIN -src
output: |-
  root@kali ~# amass enum -passive -d redstack.io -src
  Querying UKGovArchive for redstack.io subdomains
  Querying Riddler for redstack.io subdomains
  Querying Robtex for redstack.io subdomains
  Querying RapidDNS for redstack.io subdomains
  Querying SecurityTrails for redstack.io subdomains
  Querying VirusTotal for redstack.io subdomains
  Querying ViewDNS for redstack.io subdomains
  Querying Sublist3rAPI for redstack.io subdomains
  Querying URLScan for redstack.io subdomains
  Querying Wayback for redstack.io subdomains
  Querying ThreatCrowd for redstack.io subdomains
  Querying Yahoo for redstack.io subdomains
  Querying SiteDossier for redstack.io subdomains
  Querying Shodan for redstack.io subdomains
  Querying Spyse for redstack.io subdomains
  Querying Crtsh for redstack.io subdomains
  Querying CertSpotter for redstack.io subdomains
  Querying ArchiveIt for redstack.io subdomains
  Querying BinaryEdge for redstack.io subdomains
  Querying CommonCrawl for redstack.io subdomains
  Querying BufferOver for redstack.io subdomains
  Querying Baidu for redstack.io subdomains
  Querying Bing for redstack.io subdomains
  Querying Censys for redstack.io subdomains
  Querying CIRCL for redstack.io subdomains
  Querying Ask for redstack.io subdomains
  Querying AlienVault for redstack.io subdomains
  Querying Chaos for redstack.io subdomains
  Querying DNSTable for redstack.io subdomains
  Querying GoogleCT for redstack.io subdomains
  Querying Mnemonic for redstack.io subdomains
  Querying DNSDumpster for redstack.io subdomains
  Querying Entrust for redstack.io subdomains
  Querying HackerTarget for redstack.io subdomains
  Querying LoCArchive for redstack.io subdomains
  Querying Pastebin for redstack.io subdomains
  Querying HackerOne for redstack.io subdomains
  [DNS]             redstack.io
  [Yahoo]           www.redstack.io
created_at: '2020-06-29T17:07:22.477341+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - amass
  - enumeration
  - passive
verified: true
validated: true
---

# amass-enum-passive-domain

## Command

```bash
amass enum -passive -d $_TARGET_DOMAIN -src
```

## Description

This command performs passive subdomain enumeration for a specified domain using Amass's enum subcommand. It queries multiple passive data sources (e.g., certificate logs, search engines, threat intelligence feeds) without sending active DNS queries to the target, reducing the risk of detection. The -src flag lists the sources being queried for transparency. Use this during initial reconnaissance to map an organization's attack surface stealthily.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DOMAIN | The target domain to enumerate (e.g., redstack.io) | Yes |
| -passive | Enables passive mode, avoiding active DNS resolution | Built-in |
| -d | Specifies the root domain for enumeration | Built-in |
| -src | Displays the data sources being queried | Built-in |

## Examples

### Basic Usage

```bash
amass enum -passive -d redstack.io -src
```

### Advanced Usage

```bash
amass enum -passive -d redstack.io -src -o subdomains.txt
```

This saves the results to a file for further processing.

## Expected Output

```
root@kali ~# amass enum -passive -d redstack.io -src
Querying UKGovArchive for redstack.io subdomains
Querying Riddler for redstack.io subdomains
Querying Robtex for redstack.io subdomains
Querying RapidDNS for redstack.io subdomains
Querying SecurityTrails for redstack.io subdomains
Querying VirusTotal for redstack.io subdomains
Querying ViewDNS for redstack.io subdomains
Querying Sublist3rAPI for redstack.io subdomains
Querying URLScan for redstack.io subdomains
Querying Wayback for redstack.io subdomains
Querying ThreatCrowd for redstack.io subdomains
Querying Yahoo for redstack.io subdomains
Querying SiteDossier for redstack.io subdomains
Querying Shodan for redstack.io subdomains
Querying Spyse for redstack.io subdomains
Querying Crtsh for redstack.io subdomains
Querying CertSpotter for redstack.io subdomains
Querying ArchiveIt for redstack.io subdomains
Querying BinaryEdge for redstack.io subdomains
Querying CommonCrawl for redstack.io subdomains
Querying BufferOver for redstack.io subdomains
Querying Baidu for redstack.io subdomains
Querying Bing for redstack.io subdomains
Querying Censys for redstack.io subdomains
Querying CIRCL for redstack.io subdomains
Querying Ask for redstack.io subdomains
Querying AlienVault for redstack.io subdomains
Querying Chaos for redstack.io subdomains
Querying DNSTable for redstack.io subdomains
Querying GoogleCT for redstack.io subdomains
Querying Mnemonic for redstack.io subdomains
Querying DNSDumpster for redstack.io subdomains
Querying Entrust for redstack.io subdomains
Querying HackerTarget for redstack.io subdomains
Querying LoCArchive for redstack.io subdomains
Querying Pastebin for redstack.io subdomains
Querying HackerOne for redstack.io subdomains
[DNS]             redstack.io
[Yahoo]           www.redstack.io
```

The output shows querying progress from each source, followed by discovered subdomains tagged by source (e.g., [Yahoo] www.redstack.io). Redirect to a file with -o for parsing.

## Related

- [[tools/amass]]
- [[commands/amass-intel-enum-domains-by-asn]]
