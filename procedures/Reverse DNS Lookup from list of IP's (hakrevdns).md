---
id: 31411ee6-cc77-4bc4-b23a-04e3ea54b90f
name: Reverse DNS Lookup from list of IP's (hakrevdns)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:12:16.661646+00:00'
updated_at: '2023-05-26T00:46:30.155093+00:00'
commands:
- '[[hakrevdns lookup subdomains from list of IP''s]]'
- '[[hakrevdns lookup subdomains with specific resolver]]'
---

# Reverse DNS Lookup from list of IP's (hakrevdns)

**Status**: ✓ Verified

## Summary

Find sub domains belonging to a company from their IP Addresses Can use prips tool to pipe a list of IP addresses to hakrevdns hakrevdns 

## Description

# Description

Find sub domains belonging to a company from their IP Addresses

Can use prips tool to pipe a list of IP addresses to hakrevdns

[hakrevdns](https://github.com/hakluke/hakrevdns)

##  Instructions

1. Pass in a list of IP addresses, here we use prips, but you can cat a text file in as well.

This will print a list of ip's and subdomains to stdout.

**Command** ([[hakrevdns lookup subdomains from list of IP's]]):

```bash
prips 173.0.84.0/24 | hakrevdns 

```

2. (Optional) You can specify your own resolver, works to avoid the one the OS specifies

**Command** ([[hakrevdns lookup subdomains with specific resolver]]):

```bash
echo "173.0.84.110" | hakrevdns -r 1.1.1.1

```

## Commands Used

- [[hakrevdns lookup subdomains from list of IP's]]
- [[hakrevdns lookup subdomains with specific resolver]]
