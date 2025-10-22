---
id: a2d502ed-daab-4944-9821-c8a0b6573ee6
name: amass active dns brute force enumeration w/ DB
type: command
executor: bash
data: amass enum -active -d $_TARGET_DOMAIN -brute -w $_WORDLIST -src -ip -dir $_OUTPUT_DIR
  -o $_OUTPUT_RESULTS_FILE
output: "root@kali ~# amass enum -active -d owasp.org -brute -w /usr/share/amass/wordlists/deepmagic.com_top500prefixes.txt\
  \ -src -ip -dir owasp.org -o owasp_results.txt\nQuerying Spyse for owasp.org subdomains\n\
  Querying ThreatCrowd for owasp.org subdomains\nQuerying Shodan for owasp.org subdomains\n\
  Querying SiteDossier for owasp.org subdomains\nQuerying Sublist3rAPI for owasp.org\
  \ subdomains\nQuerying UKGovArchive for owasp.org subdomains\nQuerying VirusTotal\
  \ for owasp.org subdomains\nQuerying ViewDNS for owasp.org subdomains\nQuerying\
  \ Wayback for owasp.org subdomains\nQuerying URLScan for owasp.org subdomains\n\
  Querying Yahoo for owasp.org subdomains\nQuerying AlienVault for owasp.org subdomains\n\
  Querying BinaryEdge for owasp.org subdomains\nQuerying Chaos for owasp.org subdomains\n\
  Querying BufferOver for owasp.org subdomains\nQuerying CommonCrawl for owasp.org\
  \ subdomains\nQuerying Censys for owasp.org subdomains\nQuerying Ask for owasp.org\
  \ subdomains\nQuerying Crtsh for owasp.org subdomains\nQuerying CertSpotter for\
  \ owasp.org subdomains\nQuerying Bing for owasp.org subdomains\nQuerying ArchiveIt\
  \ for owasp.org subdomains\nQuerying Baidu for owasp.org subdomains\nQuerying CIRCL\
  \ for owasp.org subdomains\nQuerying Entrust for owasp.org subdomains\nQuerying\
  \ DNSTable for owasp.org subdomains\nQuerying DNSDumpster for owasp.org subdomains\n\
  Querying Mnemonic for owasp.org subdomains\nQuerying Pastebin for owasp.org subdomains\n\
  Querying HackerTarget for owasp.org subdomains\nQuerying LoCArchive for owasp.org\
  \ subdomains\nQuerying GoogleCT for owasp.org subdomains\nQuerying HackerOne for\
  \ owasp.org subdomains\nQuerying Riddler for owasp.org subdomains\nQuerying SecurityTrails\
  \ for owasp.org subdomains\nQuerying RapidDNS for owasp.org subdomains\nQuerying\
  \ Robtex for owasp.org subdomains\n[Crtsh]           ocms.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77\n\
  [DNS]             owasp.org 104.22.27.77,104.22.26.77,172.67.10.39\n[Crtsh]    \
  \       cheatsheetseries.owasp.org 104.22.26.77,104.22.27.77,172.67.10.39\n[Crtsh]\
  \           www.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77\n[Crtsh]      \
  \     name-virt-host.owasp.org 172.67.10.39,104.22.27.77,104.22.26.77\n[Crtsh] \
  \          austin.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77\n[Crtsh]    \
  \       kerala.owasp.org 104.22.26.77,172.67.10.39,104.22.27.77\n[Crtsh]       \
  \    lists.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77\n[Crtsh]           www2.owasp.org\
  \ 104.22.26.77,104.22.27.77,172.67.10.39\n[Crtsh]           contact.owasp.org 172.67.10.39,104.22.26.77,104.22.27.77\n\
  [ThreatCrowd]     sl.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77\n[HackerTarget]\
  \    dev.owasp.org 172.67.10.39,104.22.27.77,104.22.26.77\n[HackerTarget]    wiki.owasp.org\
  \ 104.22.27.77,104.22.26.77,172.67.10.39\n[HackerTarget]    videos.owasp.org 104.22.27.77,104.22.26.77,172.67.10.39\n\
  [VirusTotal]      groups.owasp.org 104.22.26.77,172.67.10.39,104.22.27.77\n[ThreatCrowd]\
  \     mail.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77\n[HackerTarget]    gapps.owasp.org\
  \ 172.67.10.39,2606:4700:10::6816:1a4d,104.22.26.77,104.22.27.77,2606:4700:10::ac43:a27,2606:4700:10::6816:1b4d\n\
  [VirusTotal]      calendar.owasp.org 2606:4700:10::ac43:a27,172.67.10.39,104.22.27.77,104.22.26.77,2606:4700:10::6816:1b4d,2606:4700:10::6816:1a4d\n\
  Average DNS queries performed: 507/sec, Average retries required: 7.30%\nAverage\
  \ DNS queries performed: 100/sec, Average retries required: 1.00%\nAverage DNS queries\
  \ performed: 272/sec, Average retries required: 8.09%\n\nOWASP Amass v3.7.2    \
  \                            https://github.com/OWASP/Amass\n--------------------------------------------------------------------------------\n\
  18 names discovered - dns: 1, api: 8, cert: 9\n--------------------------------------------------------------------------------\n\
  ASN: 13335 - CLOUDFLARENET, US\n\t2606:4700:10::/44 \t6    Subdomain Name(s)\n\t\
  104.22.16.0/20    \t36   Subdomain Name(s)\n\t172.67.0.0/20     \t18   Subdomain\
  \ Name(s)\n\nThe enumeration has finished\nDiscoveries are being migrated into the\
  \ Cayley Graph database"
created_at: '2020-06-29T17:38:12.269049+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# amass active dns brute force enumeration w/ DB

```bash
amass enum -active -d $_TARGET_DOMAIN -brute -w $_WORDLIST -src -ip -dir $_OUTPUT_DIR -o $_OUTPUT_RESULTS_FILE
```

## Expected Output

```
root@kali ~# amass enum -active -d owasp.org -brute -w /usr/share/amass/wordlists/deepmagic.com_top500prefixes.txt -src -ip -dir owasp.org -o owasp_results.txt
Querying Spyse for owasp.org subdomains
Querying ThreatCrowd for owasp.org subdomains
Querying Shodan for owasp.org subdomains
Querying SiteDossier for owasp.org subdomains
Querying Sublist3rAPI for owasp.org subdomains
Querying UKGovArchive for owasp.org subdomains
Querying VirusTotal for owasp.org subdomains
Querying ViewDNS for owasp.org subdomains
Querying Wayback for owasp.org subdomains
Querying URLScan for owasp.org subdomains
Querying Yahoo for owasp.org subdomains
Querying AlienVault for owasp.org subdomains
Querying BinaryEdge for owasp.org subdomains
Querying Chaos for owasp.org subdomains
Querying BufferOver for owasp.org subdomains
Querying CommonCrawl for owasp.org subdomains
Querying Censys for owasp.org subdomains
Querying Ask for owasp.org subdomains
Querying Crtsh for owasp.org subdomains
Querying CertSpotter for owasp.org subdomains
Querying Bing for owasp.org subdomains
Querying ArchiveIt for owasp.org subdomains
Querying Baidu for owasp.org subdomains
Querying CIRCL for owasp.org subdomains
Querying Entrust for owasp.org subdomains
Querying DNSTable for owasp.org subdomains
Querying DNSDumpster for owasp.org subdomains
Querying Mnemonic for owasp.org subdomains
Querying Pastebin for owasp.org subdomains
Querying HackerTarget for owasp.org subdomains
Querying LoCArchive for owasp.org subdomains
Querying GoogleCT for owasp.org subdomains
Querying HackerOne for owasp.org subdomains
Querying Riddler for owasp.org subdomains
Querying SecurityTrails for owasp.org subdomains
Querying RapidDNS for owasp.org subdomains
Querying Robtex for owasp.org subdomains
[Crtsh]           ocms.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77
[DNS]             owasp.org 104.22.27.77,104.22.26.77,172.67.10.39
[Crtsh]           cheatsheetseries.owasp.org 104.22.26.77,104.22.27.77,172.67.10.39
[Crtsh]           www.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77
[Crtsh]           name-virt-host.owasp.org 172.67.10.39,104.22.27.77,104.22.26.77
[Crtsh]           austin.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77
[Crtsh]           kerala.owasp.org 104.22.26.77,172.67.10.39,104.22.27.77
[Crtsh]           lists.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77
[Crtsh]           www2.owasp.org 104.22.26.77,104.22.27.77,172.67.10.39
[Crtsh]           contact.owasp.org 172.67.10.39,104.22.26.77,104.22.27.77
[ThreatCrowd]     sl.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77
[HackerTarget]    dev.owasp.org 172.67.10.39,104.22.27.77,104.22.26.77
[HackerTarget]    wiki.owasp.org 104.22.27.77,104.22.26.77,172.67.10.39
[HackerTarget]    videos.owasp.org 104.22.27.77,104.22.26.77,172.67.10.39
[VirusTotal]      groups.owasp.org 104.22.26.77,172.67.10.39,104.22.27.77
[ThreatCrowd]     mail.owasp.org 104.22.27.77,172.67.10.39,104.22.26.77
[HackerTarget]    gapps.owasp.org 172.67.10.39,2606:4700:10::6816:1a4d,104.22.26.77,104.22.27.77,2606:4700:10::ac43:a27,2606:4700:10::6816:1b4d
[VirusTotal]      calendar.owasp.org 2606:4700:10::ac43:a27,172.67.10.39,104.22.27.77,104.22.26.77,2606:4700:10::6816:1b4d,2606:4700:10::6816:1a4d
Average DNS queries performed: 507/sec, Average retries required: 7.30%
Average DNS queries performed: 100/sec, Average retries required: 1.00%
Average DNS queries performed: 272/sec, Average retries required: 8.09%

OWASP Amass v3.7.2                                https://github.com/OWASP/Amass
--------------------------------------------------------------------------------
18 names discovered - dns: 1, api: 8, cert: 9
--------------------------------------------------------------------------------
ASN: 13335 - CLOUDFLARENET, US
	2606:4700:10::/44 	6    Subdomain Name(s)
	104.22.16.0/20    	36   Subdomain Name(s)
	172.67.0.0/20     	18   Subdomain Name(s)

The enumeration has finished
Discoveries are being migrated into the Cayley Graph database
```
