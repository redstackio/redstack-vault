---
id: c4391d16-b30e-4054-b465-70efbad8c528
name: sublist3r-enumerate-subdomains
type: command
executor: bash
data: sublist3r -d $_DOMAIN -o $_OUTPUT_FILE
output: |-
  root@kali:/opt/Sublist3r# ./sublist3r.py -d cisco.com           
                                                                  
                   ____        _     _ _     _   _____            
                  / ___| _   _| |__ | (_)___| |_|___ / _ __       
                  \___ \| | | | '_ \| | / __| __| |_ \| '__|      
                   ___) | |_| | |_) | | \__ \ |_ ___) | |         
                  |____/ \__,_|_.__/|_|_|___/\__|____/|_|         

                  # Coded By Ahmed Aboul-Ela - @aboul3la
      
  [-] Enumerating subdomains now for cisco.com
  [-] Searching now in Baidu..
  [-] Searching now in Yahoo..
  [-] Searching now in Google..
  [-] Searching now in Bing..
  [-] Searching now in Ask..
  [-] Searching now in Netcraft..
  [-] Searching now in DNSdumpster..
  [-] Searching now in Virustotal..
  [-] Searching now in ThreatCrowd..
  [-] Searching now in SSL Certificates..
  [-] Searching now in PassiveDNS..
  [-] Total Unique Subdomains Found: 1255
  www.cisco.com
  173-39-226-40.cisco.com
  173-39-227-1.cisco.com
  173-39-234-141.cisco.com
  6lab.cisco.com
created_at: '2019-09-12T17:55:35.975030+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - osint
  - subdomain-enumeration
verified: true
validated: true
---

# sublist3r-enumerate-subdomains

## Command

```bash
sublist3r -d $_DOMAIN -o $_OUTPUT_FILE
```

## Description

Enumerates subdomains for the specified domain using various OSINT sources such as search engines, DNS databases, and certificate transparency logs. Outputs unique subdomains to a file for further analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d, --domain $_DOMAIN` | Target domain to enumerate (e.g., cisco.com) | Yes |
| `-o, --output $_OUTPUT_FILE` | File to save the list of discovered subdomains (e.g., subdomains.txt) | No (defaults to stdout) |
| `-v, --verbose` | Enable verbose output for detailed progress | No |
| `-t, --threads <num>` | Number of threads for faster querying (default: 10) | No |

## Examples

### Basic Usage

```bash
sublist3r -d example.com -o subdomains.txt
```

### Advanced Usage

```bash
sublist3r -d example.com -o subdomains.txt -v -t 20
```

## Expected Output

```
root@kali:/opt/Sublist3r# ./sublist3r.py -d cisco.com           
                                                                
                 ____        _     _ _     _   _____            
                / ___| _   _| |__ | (_)___| |_|___ / _ __       
                \___ \| | | | '_ \| | / __| __| |_ \| '__|      
                 ___) | |_| | |_) | | \__ \ |_ ___) | |         
                |____/ \__,_|_.__/|_|_|___/\__|____/|_|         

                # Coded By Ahmed Aboul-Ela - @aboul3la
    
[-] Enumerating subdomains now for cisco.com
[-] Searching now in Baidu..
[-] Searching now in Yahoo..
[-] Searching now in Google..
[-] Searching now in Bing..
[-] Searching now in Ask..
[-] Searching now in Netcraft..
[-] Searching now in DNSdumpster..
[-] Searching now in Virustotal..
[-] Searching now in ThreatCrowd..
[-] Searching now in SSL Certificates..
[-] Searching now in PassiveDNS..
[-] Total Unique Subdomains Found: 1255
www.cisco.com
173-39-226-40.cisco.com
173-39-227-1.cisco.com
173-39-234-141.cisco.com
6lab.cisco.com
```

The output file ($_OUTPUT_FILE) will contain the full list of unique subdomains.

## Related

- [[commands/sublist3r-show-help]]
- [[procedures/Enumerate-Domain-Subdomains-using-OSINT]]
