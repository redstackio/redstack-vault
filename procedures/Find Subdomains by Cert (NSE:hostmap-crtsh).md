---
id: 1df850c8-2298-4ac6-af8e-8502e1b8962d
name: Find Subdomains by Cert (NSE:hostmap-crtsh)
type: procedure
verified: false
submitted: false
created_at: '2020-06-30T01:33:49.208576+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[NSE hostmap-crtsh find subdomains by cert]]'
---

# Find Subdomains by Cert (NSE:hostmap-crtsh)

## Summary

Nmap script hostmap-crtsh queries Google's Certificate Transparency Logs database https://crt.sh . You can use this to find certificate's issued to sub domains by an organization or domain. 

## Description

# Description

Nmap script hostmap-crtsh queries Google's Certificate Transparency Logs database [https://crt.sh](https://crt.sh) .

You can use this to find certificate's issued to sub domains by an organization or domain.

**Command** ([[NSE hostmap-crtsh find subdomains by cert]]):

```bash
nmap -sn --script hostmap-crtsh $_TARGET_DOMAIN
```

## Commands Used

- [[NSE hostmap-crtsh find subdomains by cert]]
