---
id: 858192fb-90ed-4978-9490-3645f2e0a611
name: amass dns enum subdomains with validated dns servers list
type: command
executor: ''
data: amass enum -rf $_RESOLVERS_FILE -src -ip -d $_TARGET_DOMAIN -max-dns-queries
  $_MAX_QUERIES_NUM
output: "root@kali ~# amass enum -rf 25.txt -src -ip -d owasp.org -max-dns-queries\
  \ 20000\nQuerying DNSDumpster for owasp.org subdomains\nQuerying GoogleCT for owasp.org\
  \ subdomains\nQuerying Entrust for owasp.org subdomains\nQuerying DNSTable for owasp.org\
  \ subdomains\nQuerying HackerTarget for owasp.org subdomains\nQuerying HackerOne\
  \ for owasp.org subdomains\nQuerying SiteDossier for owasp.org subdomains\nQuerying\
  \ Shodan for owasp.org subdomains\nQuerying UKGovArchive for owasp.org subdomains\n\
  Querying Mnemonic for owasp.org subdomains\nQuerying Pastebin for owasp.org subdomains\n\
  Querying URLScan for owasp.org subdomains\nQuerying Sublist3rAPI for owasp.org subdomains\n\
  Querying Wayback for owasp.org subdomains\nQuerying Spyse for owasp.org subdomains\n\
  Querying Yahoo for owasp.org subdomains\nQuerying VirusTotal for owasp.org subdomains\n\
  Querying ThreatCrowd for owasp.org subdomains\nQuerying LoCArchive for owasp.org\
  \ subdomains\nQuerying ViewDNS for owasp.org subdomains\nQuerying Riddler for owasp.org\
  \ subdomains\nQuerying SecurityTrails for owasp.org subdomains\nQuerying Robtex\
  \ for owasp.org subdomains\nQuerying RapidDNS for owasp.org subdomains\nQuerying\
  \ Chaos for owasp.org subdomains\nQuerying Baidu for owasp.org subdomains\nQuerying\
  \ BufferOver for owasp.org subdomains\nQuerying AlienVault for owasp.org subdomains\n\
  Querying BinaryEdge for owasp.org subdomains\nQuerying Ask for owasp.org subdomains\n\
  Querying Bing for owasp.org subdomains\nQuerying CIRCL for owasp.org subdomains\n\
  Querying CertSpotter for owasp.org subdomains\nQuerying CommonCrawl for owasp.org\
  \ subdomains\nQuerying ArchiveIt for owasp.org subdomains\nQuerying Censys for owasp.org\
  \ subdomains\nQuerying Crtsh for owasp.org subdomains\n[Crtsh]           cheatsheetseries.owasp.org\
  \ 104.22.26.77,104.22.27.77,172.67.10.39\n[Crtsh]           lists.owasp.org 172.67.10.39,104.22.26.77,104.22.27.77\n\
  [Crtsh]           name-virt-host.owasp.org 172.67.10.39,104.22.27.77,104.22.26.77\n\
  [Crtsh]           www2.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77\n[Crtsh]\
  \           owasp.org 104.22.27.77,104.22.26.77,172.67.10.39\n[Crtsh]          \
  \ contact.owasp.org 172.67.10.39,104.22.26.77,104.22.27.77\n[Crtsh]           austin.owasp.org\
  \ 104.22.27.77,172.67.10.39,104.22.26.77\n[Crtsh]           ocms.owasp.org 172.67.10.39,104.22.27.77,104.22.26.77\n\
  [Crtsh]           www.owasp.org 172.67.10.39,104.22.27.77,104.22.26.77\n[VirusTotal]\
  \      groups.owasp.org 2606:4700:10::6816:1a4d,104.22.27.77,172.67.10.39,2606:4700:10::6816:1b4d,2606:4700:10::ac43:a27,104.22.26.77\n\
  [ThreatCrowd]     mail.owasp.org 2606:4700:10::ac43:a27,2606:4700:10::6816:1a4d,2606:4700:10::6816:1b4d\n\
  [VirusTotal]      calendar.owasp.org 172.67.10.39,104.22.26.77,104.22.27.77,2606:4700:10::6816:1a4d,2606:4700:10::6816:1b4d,2606:4700:10::ac43:a27\n\
  [ThreatCrowd]     sl.owasp.org 2606:4700:10::6816:1b4d,104.22.27.77,104.22.26.77,172.67.10.39,2606:4700:10::ac43:a27,2606:4700:10::6816:1a4d\n\
  [HackerTarget]    gapps.owasp.org 104.22.26.77,104.22.27.77,172.67.10.39\n[HackerTarget]\
  \    wiki.owasp.org 2606:4700:10::ac43:a27,104.22.26.77,2606:4700:10::6816:1b4d,172.67.10.39,2606:4700:10::6816:1a4d,104.22.27.77\n\
  [HackerTarget]    dev.owasp.org 2606:4700:10::6816:1b4d,104.22.27.77,104.22.26.77,2606:4700:10::ac43:a27,172.67.10.39,2606:4700:10::6816:1a4d\n\
  [HackerTarget]    videos.owasp.org 2606:4700:10::ac43:a27,104.22.27.77,2606:4700:10::6816:1a4d,2606:4700:10::6816:1b4d,172.67.10.39,104.22.26.77\n\
  Average DNS queries performed: 355/sec, Average retries required: 9.58%\nAverage\
  \ DNS queries performed: 110/sec, Average retries required: 9.09%\n[Alterations]\
  \     6ntact.owasp.org 180.122.78.238,180.122.78.239,180.122.78.240,180.122.78.243,180.122.78.242,180.122.78.248,180.122.78.244,180.122.78.241\n\
  [Alterations]     gvirt-host.owasp.org 163.171.139.156\n\nOWASP Amass v3.7.2   \
  \                             https://github.com/OWASP/Amass\n--------------------------------------------------------------------------------\n\
  19 names discovered - cert: 9, api: 8, alt: 2\n--------------------------------------------------------------------------------\n\
  ASN: 13335 - CLOUDFLARENET, US\n\t104.22.16.0/20    \t32   Subdomain Name(s)\n\t\
  172.67.0.0/20     \t16   Subdomain Name(s)\n\t2606:4700::/32    \t21   Subdomain\
  \ Name(s)\nASN: 4134 - CHINANET-BACKBONE No.31,Jin-rong Street, CN\n\t180.96.0.0/11\
  \     \t8    Subdomain Name(s)\nASN: 54994 - QUANTILNETWORKS, US\n\t163.171.139.0/24\
  \  \t1    Subdomain Name(s)\n\nThe enumeration has finished\nDiscoveries are being\
  \ migrated into the Cayley Graph database"
created_at: '2020-06-30T03:02:02.411205+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# amass dns enum subdomains with validated dns servers list

```bash
amass enum -rf $_RESOLVERS_FILE -src -ip -d $_TARGET_DOMAIN -max-dns-queries $_MAX_QUERIES_NUM
```

## Expected Output

```
root@kali ~# amass enum -rf 25.txt -src -ip -d owasp.org -max-dns-queries 20000
Querying DNSDumpster for owasp.org subdomains
Querying GoogleCT for owasp.org subdomains
Querying Entrust for owasp.org subdomains
Querying DNSTable for owasp.org subdomains
Querying HackerTarget for owasp.org subdomains
Querying HackerOne for owasp.org subdomains
Querying SiteDossier for owasp.org subdomains
Querying Shodan for owasp.org subdomains
Querying UKGovArchive for owasp.org subdomains
Querying Mnemonic for owasp.org subdomains
Querying Pastebin for owasp.org subdomains
Querying URLScan for owasp.org subdomains
Querying Sublist3rAPI for owasp.org subdomains
Querying Wayback for owasp.org subdomains
Querying Spyse for owasp.org subdomains
Querying Yahoo for owasp.org subdomains
Querying VirusTotal for owasp.org subdomains
Querying ThreatCrowd for owasp.org subdomains
Querying LoCArchive for owasp.org subdomains
Querying ViewDNS for owasp.org subdomains
Querying Riddler for owasp.org subdomains
Querying SecurityTrails for owasp.org subdomains
Querying Robtex for owasp.org subdomains
Querying RapidDNS for owasp.org subdomains
Querying Chaos for owasp.org subdomains
Querying Baidu for owasp.org subdomains
Querying BufferOver for owasp.org subdomains
Querying AlienVault for owasp.org subdomains
Querying BinaryEdge for owasp.org subdomains
Querying Ask for owasp.org subdomains
Querying Bing for owasp.org subdomains
Querying CIRCL for owasp.org subdomains
Querying CertSpotter for owasp.org subdomains
Querying CommonCrawl for owasp.org subdomains
Querying ArchiveIt for owasp.org subdomains
Querying Censys for owasp.org subdomains
Querying Crtsh for owasp.org subdomains
[Crtsh]           cheatsheetseries.owasp.org 104.22.26.77,104.22.27.77,172.67.10.39
[Crtsh]           lists.owasp.org 172.67.10.39,104.22.26.77,104.22.27.77
[Crtsh]           name-virt-host.owasp.org 172.67.10.39,104.22.27.77,104.22.26.77
[Crtsh]           www2.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77
[Crtsh]           owasp.org 104.22.27.77,104.22.26.77,172.67.10.39
[Crtsh]           contact.owasp.org 172.67.10.39,104.22.26.77,104.22.27.77
[Crtsh]           austin.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77
[Crtsh]           ocms.owasp.org 172.67.10.39,104.22.27.77,104.22.26.77
[Crtsh]           www.owasp.org 172.67.10.39,104.22.27.77,104.22.26.77
[VirusTotal]      groups.owasp.org 2606:4700:10::6816:1a4d,104.22.27.77,172.67.10.39,2606:4700:10::6816:1b4d,2606:4700:10::ac43:a27,104.22.26.77
[ThreatCrowd]     mail.owasp.org 2606:4700:10::ac43:a27,2606:4700:10::6816:1a4d,2606:4700:10::6816:1b4d
[VirusTotal]      calendar.owasp.org 172.67.10.39,104.22.26.77,104.22.27.77,2606:4700:10::6816:1a4d,2606:4700:10::6816:1b4d,2606:4700:10::ac43:a27
[ThreatCrowd]     sl.owasp.org 2606:4700:10::6816:1b4d,104.22.27.77,104.22.26.77,172.67.10.39,2606:4700:10::ac43:a27,2606:4700:10::6816:1a4d
[HackerTarget]    gapps.owasp.org 104.22.26.77,104.22.27.77,172.67.10.39
[HackerTarget]    wiki.owasp.org 2606:4700:10::ac43:a27,104.22.26.77,2606:4700:10::6816:1b4d,172.67.10.39,2606:4700:10::6816:1a4d,104.22.27.77
[HackerTarget]    dev.owasp.org 2606:4700:10::6816:1b4d,104.22.27.77,104.22.26.77,2606:4700:10::ac43:a27,172.67.10.39,2606:4700:10::6816:1a4d
[HackerTarget]    videos.owasp.org 2606:4700:10::ac43:a27,104.22.27.77,2606:4700:10::6816:1a4d,2606:4700:10::6816:1b4d,172.67.10.39,104.22.26.77
Average DNS queries performed: 355/sec, Average retries required: 9.58%
Average DNS queries performed: 110/sec, Average retries required: 9.09%
[Alterations]     6ntact.owasp.org 180.122.78.238,180.122.78.239,180.122.78.240,180.122.78.243,180.122.78.242,180.122.78.248,180.122.78.244,180.122.78.241
[Alterations]     gvirt-host.owasp.org 163.171.139.156

OWASP Amass v3.7.2                                https://github.com/OWASP/Amass
--------------------------------------------------------------------------------
19 names discovered - cert: 9, api: 8, alt: 2
--------------------------------------------------------------------------------
ASN: 13335 - CLOUDFLARENET, US
	104.22.16.0/20    	32   Subdomain Name(s)
	172.67.0.0/20     	16   Subdomain Name(s)
	2606:4700::/32    	21   Subdomain Name(s)
ASN: 4134 - CHINANET-BACKBONE No.31,Jin-rong Street, CN
	180.96.0.0/11     	8    Subdomain Name(s)
ASN: 54994 - QUANTILNETWORKS, US
	163.171.139.0/24  	1    Subdomain Name(s)

The enumeration has finished
Discoveries are being migrated into the Cayley Graph database
```
