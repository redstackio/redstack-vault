---
id: b10fc917-52ca-4954-a6ac-e2fad691fb08
type: command
executor: bash
data: sed 's/$/.$_TARGET_DOMAIN/' $_SECLISTS_WORDLIST > $_OUTPUT_FILE
output: >-
  root@hacker:~# sed 's/$/.owasp.org/'
  /opt/SecLists/Discovery/DNS/subdomains-top1million-20000.txt >
  hosts-wordlist.txt

  www.owasp.org

  mail.owasp.org

  ftp.owasp.org

  localhost.owasp.org

  webmail.owasp.org

  smtp.owasp.org

  webdisk.owasp.org

  pop.owasp.org

  cpanel.owasp.org

  whm.owasp.org

  ... CUT
created_at: '2020-06-30T04:41:15.217716+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - wordlist
  - sed
verified: true
validated: true
---

# build-subdomain-wordlist-with-sed

## Command

```bash
sed 's/$/.$_TARGET_DOMAIN/' $_SECLISTS_WORDLIST > $_OUTPUT_FILE
```

## Description

Appends target domain to each line in SecLists subdomain list.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 's/$/.$_TARGET_DOMAIN/' | Sed substitution | Built-in |
| $_SECLISTS_WORDLIST | Input wordlist | Yes |
| $_OUTPUT_FILE | Output file | Yes |

## Examples

### Basic Usage

```bash
sed 's/$/.example.com/' subdomains.txt > full-list.txt
```

## Expected Output

One subdomain per line, e.g., www.example.com.

## Related

- [[procedures/Generate-Subdomain-Wordlist-from-SecLists]]
