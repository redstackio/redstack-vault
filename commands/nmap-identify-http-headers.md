---
id: fc804e2a-639c-4787-93cc-3e049415a9a4
name: nmap-identify-http-headers
type: command
executor: bash
data: nmap -sV --script=http-headers $_TARGET
output: >-
  Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 00:20 IST

  Nmap scan report for 192.168.1.11

  Host is up (0.00019s latency).

  Not shown: 500 closed ports, 497 filtered ports

  PORT     STATE SERVICE  VERSION

  80/tcp   open  http     Apache httpd 2.4.41 ((Unix) OpenSSL/1.1.1d PHP/7.1.32
  mod_perl/2.0.8-dev Perl/v5.16.3)

  | http-headers: 

  |   Date: Mon, 31 Aug 2020 18:51:07 GMT

  |   Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev
  Perl/v5.16.3

  |   Last-Modified: Sat, 26 Oct 2019 05:14:41 GMT

  |   ETag: "1d96-595c958015240"

  |   Accept-Ranges: bytes

  |   Content-Length: 7574

  |   Connection: close

  |   Content-Type: text/html

  |   

  |_  (Request type: HEAD)

  |_http-server-header: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32
  mod_perl/2.0.8-dev Perl/v5.16.3

  443/tcp  open  ssl/http Apache httpd 2.4.41 ((Unix) OpenSSL/1.1.1d PHP/7.1.32
  mod_perl/2.0.8-dev Perl/v5.16.3)

  | http-headers: 

  |   Date: Mon, 31 Aug 2020 18:51:07 GMT

  |   Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev
  Perl/v5.16.3

  |   Last-Modified: Sat, 26 Oct 2019 05:14:41 GMT

  |   ETag: "1d96-595c958015240"

  |   Accept-Ranges: bytes

  |   Content-Length: 7574

  |   Connection: close

  |   Content-Type: text/html

  |   

  |_  (Request type: HEAD)

  |_http-server-header: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32
  mod_perl/2.0.8-dev Perl/v5.16.3
created_at: '2020-08-31T19:08:46.847809+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Web
tags:
  - nmap
  - reconnaissance
  - http-headers
verified: true
validated: true
---

# nmap-identify-http-headers

## Command

```bash
nmap -sV --script=http-headers $_TARGET
```

## Description

This command performs service version detection (-sV) on the target and executes the http-headers Nmap script to retrieve and display HTTP response headers from open web ports. It is used during reconnaissance to fingerprint web servers without full page loads, focusing on header information for technology identification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | IP address, hostname, or range of the target (e.g., 192.168.1.11 or example.com) | Yes |
| -sV | Enable service version detection to identify software on open ports | Built-in |
| --script=http-headers | Run the specific NSE script to fetch HTTP headers via HEAD requests | Built-in |

## Examples

### Basic Usage

```bash
nmap -sV --script=http-headers 192.168.1.11
```

### Advanced Usage

```bash
nmap -sV --script=http-headers -p 80,443 $_TARGET -oN scan_results.txt
```

This variation limits ports to common web ones and saves output to a file.

## Expected Output

Description of what output to expect when the command runs successfully.

```
Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 00:20 IST
Nmap scan report for 192.168.1.11
Host is up (0.00019s latency).
Not shown: 500 closed ports, 497 filtered ports
PORT     STATE SERVICE  VERSION
80/tcp   open  http     Apache httpd 2.4.41 ((Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3)
| http-headers: 
|   Date: Mon, 31 Aug 2020 18:51:07 GMT
|   Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
|   Last-Modified: Sat, 26 Oct 2019 05:14:41 GMT
|   ETag: "1d96-595c958015240"
|   Accept-Ranges: bytes
|   Content-Length: 7574
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-server-header: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
443/tcp  open  ssl/http Apache httpd 2.4.41 ((Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3)
| http-headers: 
|   Date: Mon, 31 Aug 2020 18:51:07 GMT
|   Server: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
|   Last-Modified: Sat, 26 Oct 2019 05:14:41 GMT
|   ETag: "1d96-595c958015240"
|   Accept-Ranges: bytes
|   Content-Length: 7574
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-server-header: Apache/2.4.41 (Unix) OpenSSL/1.1.1d PHP/7.1.32 mod_perl/2.0.8-dev Perl/v5.16.3
```

Success is indicated by the presence of | http-headers: sections listing key-value pairs like Server and Content-Type.

## Related

- [[procedures/Nmap-Identify-Web-Response-Headers]]
- [[tools/Nmap]]
