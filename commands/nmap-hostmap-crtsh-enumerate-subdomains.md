---
id: ba1e442a-e4f8-46b8-b9b6-d1db825cab5d
name: nmap-hostmap-crtsh-enumerate-subdomains
type: command
executor: bash
data: nmap -sn --script hostmap-crtsh $_TARGET_DOMAIN
output: >
  root@kali ~/owasp.org=# nmap -sn --script hostmap-crtsh redstack.io

  Starting Nmap 7.70 ( https://nmap.org ) at 2020-06-29 21:32 EDT

  Nmap scan report for redstack.io (99.84.71.85)

  Host is up (0.00019s latency).

  Other addresses for redstack.io (not scanned): 99.84.71.69 99.84.71.60
  99.84.71.49

  rDNS record for 99.84.71.85: server-99-84-71-85.hio50.r.cloudfront.net


  Host script results:

  | hostmap-crtsh: 

  |   subdomains: 

  |_    *.redstack.io\nredstack.io


  Nmap done: 1 IP address (1 host up) scanned in 1.21 seconds
created_at: '2020-06-30T01:33:49.185132+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - nmap
  - subdomain-enumeration
verified: true
validated: true
---

# nmap-hostmap-crtsh-enumerate-subdomains

## Command

```bash
nmap -sn --script hostmap-crtsh $_TARGET_DOMAIN
```

## Description

This command uses Nmap in ping scan mode (-sn) to perform host discovery on the target domain while executing the hostmap-crtsh NSE script. The script queries crt.sh for certificate transparency log entries related to the domain, enumerating associated subdomains passively. Use this during initial reconnaissance to map the target's subdomain footprint without direct interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DOMAIN | The root domain to query for subdomains (e.g., example.com) | Yes |
| -sn | Disable port scanning, perform only host discovery | Built-in |
| --script hostmap-crtsh | Execute the specific NSE script for crt.sh subdomain enumeration | Built-in |

## Examples

### Basic Usage

```bash
nmap -sn --script hostmap-crtsh example.com
```

### Advanced Usage

```bash
nmap -sn --script hostmap-crtsh --script-args hostmap-crtsh.limit=100 example.com -oN output.txt
```

> Adds output to file and limits results to 100 subdomains if the script supports the limit argument.

## Expected Output

Description of what output to expect when the command runs successfully.

Nmap will resolve the domain, perform a basic host check, and display script results showing discovered subdomains in a table format. For example:

```
Starting Nmap 7.70 ( https://nmap.org ) at 2020-06-29 21:32 EDT
Nmap scan report for redstack.io (99.84.71.85)
Host is up (0.00019s latency).
Other addresses for redstack.io (not scanned): 99.84.71.69 99.84.71.60 99.84.71.49
rDNS record for 99.84.71.85: server-99-84-71-85.hio50.r.cloudfront.net

Host script results:
| hostmap-crtsh: 
|   subdomains: 
|_    *.redstack.io
    redstack.io

Nmap done: 1 IP address (1 host up) scanned in 1.21 seconds
```

Success is indicated by the presence of the 'subdomains' section listing entries.

## Related

- [[procedures/Enumerate-Subdomains-Using-Certificate-Transparency-Logs-with-Nmap]]
- [[tools/Nmap]]
