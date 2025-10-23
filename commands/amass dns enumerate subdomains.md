---
id: f27b22c7-ff9d-425e-9088-acc160356342
name: amass dns enumerate subdomains
type: command
executor: ''
data: amass enum -ip -d $_TARGET_DOMAIN
output: "root@kali ~# amass enum -ip -d redstack.io\nQuerying ThreatCrowd for redstack.io\
  \ subdomains\nQuerying Sublist3rAPI for redstack.io subdomains\nQuerying Wayback\
  \ for redstack.io subdomains\nQuerying UKGovArchive for redstack.io subdomains\n\
  Querying SecurityTrails for redstack.io subdomains\nQuerying Robtex for redstack.io\
  \ subdomains\nQuerying Spyse for redstack.io subdomains\nQuerying RapidDNS for redstack.io\
  \ subdomains\nQuerying VirusTotal for redstack.io subdomains\nQuerying URLScan for\
  \ redstack.io subdomains\nQuerying Riddler for redstack.io subdomains\nQuerying\
  \ SiteDossier for redstack.io subdomains\nQuerying Shodan for redstack.io subdomains\n\
  Querying Yahoo for redstack.io subdomains\nQuerying ViewDNS for redstack.io subdomains\n\
  Querying Crtsh for redstack.io subdomains\nQuerying BinaryEdge for redstack.io subdomains\n\
  Querying CIRCL for redstack.io subdomains\nQuerying Censys for redstack.io subdomains\n\
  Querying CommonCrawl for redstack.io subdomains\nQuerying Chaos for redstack.io\
  \ subdomains\nQuerying ArchiveIt for redstack.io subdomains\nQuerying Bing for redstack.io\
  \ subdomains\nQuerying AlienVault for redstack.io subdomains\nQuerying BufferOver\
  \ for redstack.io subdomains\nQuerying Ask for redstack.io subdomains\nQuerying\
  \ CertSpotter for redstack.io subdomains\nQuerying Baidu for redstack.io subdomains\n\
  Querying LoCArchive for redstack.io subdomains\nQuerying GoogleCT for redstack.io\
  \ subdomains\nQuerying Mnemonic for redstack.io subdomains\nQuerying HackerTarget\
  \ for redstack.io subdomains\nQuerying Entrust for redstack.io subdomains\nQuerying\
  \ DNSTable for redstack.io subdomains\nQuerying HackerOne for redstack.io subdomains\n\
  Querying DNSDumpster for redstack.io subdomains\nQuerying Pastebin for redstack.io\
  \ subdomains\nredstack.io 13.33.71.21,13.33.71.17,13.33.71.50,13.33.71.66\nwww.redstack.io\
  \ 13.224.13.8,13.224.13.104,13.224.13.96,13.224.13.117\nAverage DNS queries performed:\
  \ 174/sec, Average retries required: 10.92%\n\nOWASP Amass v3.7.2              \
  \                  https://github.com/OWASP/Amass\n--------------------------------------------------------------------------------\n\
  2 names discovered - dns: 1, scrape: 1\n--------------------------------------------------------------------------------\n\
  ASN: 16509 - AMAZON-02, US\n\t13.33.64.0/21     \t4    Subdomain Name(s)\n\t13.224.8.0/21\
  \     \t4    Subdomain Name(s)\n\nThe enumeration has finished\nDiscoveries are\
  \ being migrated into the Cayley Graph database"
created_at: '2020-06-29T16:22:08.332675+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# amass dns enumerate subdomains

```bash
amass enum -ip -d $_TARGET_DOMAIN
```

## Expected Output

```
root@kali ~# amass enum -ip -d redstack.io
Querying ThreatCrowd for redstack.io subdomains
Querying Sublist3rAPI for redstack.io subdomains
Querying Wayback for redstack.io subdomains
Querying UKGovArchive for redstack.io subdomains
Querying SecurityTrails for redstack.io subdomains
Querying Robtex for redstack.io subdomains
Querying Spyse for redstack.io subdomains
Querying RapidDNS for redstack.io subdomains
Querying VirusTotal for redstack.io subdomains
Querying URLScan for redstack.io subdomains
Querying Riddler for redstack.io subdomains
Querying SiteDossier for redstack.io subdomains
Querying Shodan for redstack.io subdomains
Querying Yahoo for redstack.io subdomains
Querying ViewDNS for redstack.io subdomains
Querying Crtsh for redstack.io subdomains
Querying BinaryEdge for redstack.io subdomains
Querying CIRCL for redstack.io subdomains
Querying Censys for redstack.io subdomains
Querying CommonCrawl for redstack.io subdomains
Querying Chaos for redstack.io subdomains
Querying ArchiveIt for redstack.io subdomains
Querying Bing for redstack.io subdomains
Querying AlienVault for redstack.io subdomains
Querying BufferOver for redstack.io subdomains
Querying Ask for redstack.io subdomains
Querying CertSpotter for redstack.io subdomains
Querying Baidu for redstack.io subdomains
Querying LoCArchive for redstack.io subdomains
Querying GoogleCT for redstack.io subdomains
Querying Mnemonic for redstack.io subdomains
Querying HackerTarget for redstack.io subdomains
Querying Entrust for redstack.io subdomains
Querying DNSTable for redstack.io subdomains
Querying HackerOne for redstack.io subdomains
Querying DNSDumpster for redstack.io subdomains
Querying Pastebin for redstack.io subdomains
redstack.io 13.33.71.21,13.33.71.17,13.33.71.50,13.33.71.66
www.redstack.io 13.224.13.8,13.224.13.104,13.224.13.96,13.224.13.117
Average DNS queries performed: 174/sec, Average retries required: 10.92%

OWASP Amass v3.7.2                                https://github.com/OWASP/Amass
--------------------------------------------------------------------------------
2 names discovered - dns: 1, scrape: 1
--------------------------------------------------------------------------------
ASN: 16509 - AMAZON-02, US
	13.33.64.0/21     	4    Subdomain Name(s)
	13.224.8.0/21     	4    Subdomain Name(s)

The enumeration has finished
Discoveries are being migrated into the Cayley Graph database
```


