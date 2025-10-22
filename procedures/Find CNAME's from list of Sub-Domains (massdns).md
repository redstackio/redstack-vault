---
id: 3778319c-fbfe-47e3-9e2b-49e9a51f130d
name: Find CNAME's from list of Sub-Domains (massdns)
type: procedure
verified: false
submitted: false
created_at: '2020-07-24T17:11:26.663609+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[massdns find cnames for online subdomains]]'
---

# Find CNAME's from list of Sub-Domains (massdns)

## Summary

A Canonical Name (CNAME) always points to another domain name not to an IP address. Find the CNAMES associated with a sub-domain using masssdns 

## Description

# Description

A Canonical Name (CNAME) always points to another domain name not to an IP address.

Find the CNAMES associated with a sub-domain using masssdns

##  Instructions

1. Using a list of resolvers created with dnsvalidator to locate cnames. This requires a list of subdomains in a text file.

**Command** ([[massdns find cnames for online subdomains]]):

```bash
massdns -r massdns/lists/resolvers.txt -t CNAME -o S -w paypal.massdns.cnames paypal.subdomains

```

## Commands Used

- [[massdns find cnames for online subdomains]]
