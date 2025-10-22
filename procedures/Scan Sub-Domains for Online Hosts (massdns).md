---
id: 1cf027c4-b186-45cb-8b43-0c0ba54c32be
name: Scan Sub-Domains for Online Hosts (massdns)
type: procedure
verified: true
submitted: true
created_at: '2020-06-30T05:00:10.558306+00:00'
updated_at: '2023-05-26T00:49:41.356374+00:00'
commands:
- '[[massdns check for online subdomains]]'
- '[[sort massdns output for ips]]'
- '[[sort massdns output for online hosts]]'
---

# Scan Sub-Domains for Online Hosts (massdns)

**Status**: ✓ Verified

## Summary

You have a list of subdomains in a text file and want to connect to all of them to match their IP address, and verify which ones are online and accessible from the internet. Use massdns to quickly parse through your subdomain list. If you do not have a resolvers.txt file, look up dnsvalidator to bu

## Description

# Description

You have a list of subdomains in a text file and want to connect to all of them to match their IP address, and verify which ones are online and accessible from the internet. Use massdns to quickly parse through your subdomain list.

If you do not have a resolvers.txt file, look up dnsvalidator to build your own verified dns servers list, and tail 25 to 100 of them.

The hosts-wordlist.txt is a single line document with a  subdomain on each line. 

**Command** ([[massdns check for online subdomains]]):

```bash
massdns -r $_DNS_RESOLVERS -t A -o S -w $_OUTPUT_FILE $_HOST_WORDLIST
```

Sort the massdns output into a new textfile containing only the online or publicly accessible hosts.

**Command** ([[sort massdns output for online hosts]]):

```bash
cat $_MASSDNS_OUTPUT | awk '{print $1}' | sed 's/.$//' | sort -u > $_OUTPUT_FILE
```

Sort the massdns output into a new textfil containing accessible IP addresses

**Command** ([[sort massdns output for ips]]):

```bash
cat $_MASSDNS_OUTPUT | awk '{print $3}' | sort -u | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > $_OUTPUT_FILE
```

## Commands Used

- [[massdns check for online subdomains]]
- [[sort massdns output for ips]]
- [[sort massdns output for online hosts]]
