---
id: 8d067e9c-48f1-45c3-904c-c5a34904337a
type: command
executor: bash
data: >-
  cat $_RESULTS_FILE | cut -d']' -f2 | awk '{print $1}' | sort -u >
  $_OUTPUT_FILE
output: >
  root@kali ~# cat owasp_results.txt | cut -d']' -f2 | awk '{print $1}' | sort
  -u > company_domains.txt

  austin.owasp.org

  calendar.owasp.org

  cheatsheetseries.owasp.org

  contact.owasp.org

  dev.owasp.org

  gapps.owasp.org

  groups.owasp.org

  kerala.owasp.org

  lists.owasp.org

  mail.owasp.org

  name-virt-host.owasp.org

  ocms.owasp.org

  owasp.org

  sl.owasp.org

  videos.owasp.org

  wiki.owasp.org

  www2.owasp.org

  www.owasp.org
created_at: '2020-06-30T04:31:50.451664+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - parsing
  - extraction
verified: true
validated: true
---

# extract-domains-from-amass-output

## Command

```bash
cat $_RESULTS_FILE | cut -d']' -f2 | awk '{print $1}' | sort -u > $_OUTPUT_FILE
```

## Description

Parses Amass output to extract unique subdomain names.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_RESULTS_FILE | Amass output file | Yes |
| -d']' -f2 | Delimiter and field | Built-in |
| $_OUTPUT_FILE | Output file | Yes |

## Examples

### Basic Usage

```bash
cat amass.txt | cut -d']' -f2 | awk '{print $1}' | sort -u > domains.txt
```

## Expected Output

Unique subdomains, one per line.

## Related

- [[procedures/Enumerate-Subdomains-with-Amass]]
