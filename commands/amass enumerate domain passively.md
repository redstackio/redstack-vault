---
id: 9dbc5701-85d0-4084-97e4-27ebb9db88bb
name: amass enumerate domain passively
type: command
executor: bash
data: amass enum -passive -d $_TARGET_DOMAIN -src
output: 'root@kali ~# amass enum -passive -d redstack.io -src

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

  [Yahoo]           www.redstack.io'
created_at: '2020-06-29T17:07:22.477341+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# amass enumerate domain passively

```bash
amass enum -passive -d $_TARGET_DOMAIN -src
```

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
