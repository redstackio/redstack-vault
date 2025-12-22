---
id: 51bbc53b-14be-4359-aa15-b845a0155bd5
type: command
executor: bash
data: >-
  cat $_MASSDNS_OUTPUT | awk '{print $1}' | sed 's/.$//' | sort -u >
  $_OUTPUT_FILE
output: >-
  root@hacker:~# cat massdns.out | awk '{print $1}' | sed 's/.$//' | sort -u >
  hosts-online.txt

  austin.owasp.org

  calendar.owasp.org

  contact.owasp.org

  dev.owasp.org

  docs.owasp.org

  gapps.owasp.org

  groups.owasp.org

  kerala.owasp.org

  lists.owasp.org

  mail.owasp.org

  sl.owasp.org

  videos.owasp.org

  wiki.owasp.org

  www2.owasp.org

  www.owasp.org
created_at: '2020-06-30T05:00:10.524170+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - parsing
  - hosts
verified: true
validated: true
---

# extract-online-hosts-from-massdns-output

## Command

```bash
cat $_MASSDNS_OUTPUT | awk '{print $1}' | sed 's/.$//' | sort -u > $_OUTPUT_FILE
```

## Description

Extracts unique successfully resolved hostnames from MassDNS output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MASSDNS_OUTPUT | Input file | Yes |
| $_OUTPUT_FILE | Output file | Yes |

## Examples

### Basic Usage

```bash
cat massdns.out | awk '{print $1}' | sed 's/.$//' | sort -u > online.txt
```

## Expected Output

Unique hostnames, one per line.

## Related

- [[procedures/Resolve-and-Validate-Subdomains-with-MassDNS]]
