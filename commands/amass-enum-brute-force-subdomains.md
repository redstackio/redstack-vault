---
id: 17452678-8b72-416e-8303-edb60041f5aa
name: amass-enum-brute-force-subdomains
type: command
executor: bash
data: amass enum -ip -brute -d $_TARGET_DOMAIN
output: "root@kali ~# amass enum -ip -brute -d redstack.io\nQuerying Riddler for redstack.io subdomains\nQuerying Crtsh for redstack.io subdomains\nQuerying Ask for redstack.io subdomains\nQuerying Robtex for redstack.io subdomains\nQuerying AlienVault for redstack.io subdomains\nQuerying SecurityTrails for redstack.io subdomains\nQuerying CertSpotter for redstack.io subdomains\nQuerying ViewDNS for redstack.io subdomains\nQuerying CommonCrawl for redstack.io subdomains\nQuerying Spyse for redstack.io subdomains\nQuerying Chaos for redstack.io subdomains\nQuerying Sublist3rAPI for redstack.io subdomains\nQuerying BinaryEdge for redstack.io subdomains\nQuerying URLScan for redstack.io subdomains\nQuerying CIRCL for redstack.io subdomains\nQuerying UKGovArchive for redstack.io subdomains\nQuerying Bing for redstack.io subdomains\nQuerying ThreatCrowd for redstack.io subdomains\nQuerying BufferOver for redstack.io subdomains\nQuerying Wayback for redstack.io subdomains\nQuerying Censys for redstack.io subdomains\nQuerying VirusTotal for redstack.io subdomains\nQuerying Baidu for redstack.io subdomains\nQuerying Yahoo for redstack.io subdomains\nQuerying ArchiveIt for redstack.io subdomains\nQuerying SiteDossier for redstack.io subdomains\nQuerying RapidDNS for redstack.io subdomains\nQuerying Shodan for redstack.io subdomains\nQuerying Mnemonic for redstack.io subdomains\nQuerying GoogleCT for redstack.io subdomains\nQuerying Pastebin for redstack.io subdomains\nQuerying DNSTable for redstack.io subdomains\nQuerying HackerOne for redstack.io subdomains\nQuerying HackerTarget for redstack.io subdomains\nQuerying DNSDumpster for redstack.io subdomains\nQuerying Entrust for redstack.io subdomains\nQuerying LoCArchive for redstack.io subdomains\nredstack.io 13.224.13.104,13.224.13.117,13.224.13.8,13.224.13.96\nwww.redstack.io 13.249.138.105,13.249.138.17,13.249.138.4,13.249.138.86\nsystem.redstack.io 15.223.15.46,3.96.15.73\nAverage DNS queries performed: 384/sec, Average retries required: 22.14%\n\nOWASP Amass v3.7.2                                https://github.com/OWASP/Amass\n--------------------------------------------------------------------------------\n3 names discovered - dns: 1, scrape: 1, brute: 1\n--------------------------------------------------------------------------------\nASN: 16509 - AMAZON-02 - Amazon.com, Inc.\n\t13.249.136.0/21   \t4    Subdomain Name(s)\n\t15.222.0.0/15     \t1    Subdomain Name(s)\n\t3.96.0.0/15       \t1    Subdomain Name(s)\n\t13.224.8.0/21     \t4    Subdomain Name(s)\n\nThe enumeration has finished\nDiscoveries are being migrated into the Cayley Graph database"
created_at: '2020-06-29T16:22:08.332954+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - dns
  - amass
verified: true
validated: true
---

# amass-enum-brute-force-subdomains

## Command

```bash
amass enum -ip -brute -d $_TARGET_DOMAIN
```

## Description

This command performs subdomain enumeration using Amass, combining passive intelligence gathering from various sources with active brute-force DNS querying using the tool's built-in wordlist. The -ip flag resolves and displays IP addresses for discovered subdomains, aiding in infrastructure mapping. Use this for initial reconnaissance on a target domain to uncover subdomains quickly without needing external files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ip | Resolve IP addresses for discovered subdomains | Yes |
| -brute | Enable brute-force subdomain enumeration | Yes |
| -d $_TARGET_DOMAIN | Specify the target domain to enumerate (e.g., example.com) | Yes |

## Examples

### Basic Usage

```bash
amass enum -ip -brute -d example.com
```

### Advanced Usage

```bash
amass enum -ip -brute -d example.com -timeout 10
```

(Adds a 10-second timeout per query for faster execution in constrained environments.)

## Expected Output

Description of what output to expect when the command runs successfully.

The output begins with passive source queries, followed by brute-force results showing resolved subdomains with IPs. It ends with a summary of discoveries by source and ASN details. For example:

```
root@kali ~# amass enum -ip -brute -d redstack.io
Querying Riddler for redstack.io subdomains
... (list of sources queried) ...
redstack.io 13.224.13.104,13.224.13.117,13.224.13.8,13.224.13.96
www.redstack.io 13.249.138.105,13.249.138.17,13.249.138.4,13.249.138.86
system.redstack.io 15.223.15.46,3.96.15.73
Average DNS queries performed: 384/sec, Average retries required: 22.14%

OWASP Amass v3.7.2                                https://github.com/OWASP/Amass
--------------------------------------------------------------------------------
3 names discovered - dns: 1, scrape: 1, brute: 1
--------------------------------------------------------------------------------
ASN: 16509 - AMAZON-02 - Amazon.com, Inc.
	13.249.136.0/21   	4    Subdomain Name(s)
	15.222.0.0/15     	1    Subdomain Name(s)
	3.96.0.0/15       	1    Subdomain Name(s)
	13.224.8.0/21     	4    Subdomain Name(s)

The enumeration has finished
Discoveries are being migrated into the Cayley Graph database
```

Success is confirmed by the discovery count and listed subdomains.

## Related

- [[procedures/DNS-Brute-Force-Subdomain-Enumeration-with-Amass]]
- [[commands/amass-enum-active-brute-force-with-database]]
