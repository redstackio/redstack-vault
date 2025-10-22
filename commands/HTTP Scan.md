---
id: 43fe541f-92ad-4d24-8152-9105721acf1d
name: HTTP Scan
type: command
executor: bash
data: 'nmap -vv -sS -Pn-n -p80,443,8080 --script=http-vhosts,http-userdir-enum,http-apache-negotiation,http-backup-finder,http-config-backup,http-default-accounts,http-email-harvest,http-methods,http-method-tamper,http-passwd,http-robots.txt
  -oA

  '
output: null
created_at: '2020-07-14T18:21:14.335914+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# HTTP Scan

```bash
nmap -vv -sS -Pn-n -p80,443,8080 --script=http-vhosts,http-userdir-enum,http-apache-negotiation,http-backup-finder,http-config-backup,http-default-accounts,http-email-harvest,http-methods,http-method-tamper,http-passwd,http-robots.txt -oA

```
