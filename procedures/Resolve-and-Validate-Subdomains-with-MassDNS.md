---
id: 1cf027c4-b186-45cb-8b43-0c0ba54c32be
type: procedure
verified: true
submitted: true
created_at: '2020-06-30T05:00:10.558306+00:00'
updated_at: '2023-05-26T00:49:41.356374+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Scanning IP Blocks]]'
sub_techniques: []
tags:
  - dns
  - resolution
  - validation
platforms:
  - Linux
commands:
  - '[[commands/massdns-resolve-subdomains-for-a-records]]'
  - '[[commands/extract-online-hosts-from-massdns-output]]'
  - '[[commands/extract-ips-from-massdns-output]]'
tools:
  - '[[tools/massdns]]'
validated: true
---

# Resolve-and-Validate-Subdomains-with-MassDNS

## Summary

This procedure uses MassDNS to perform high-speed parallel DNS resolutions on a subdomain wordlist, querying A records to identify live hosts and their IPs, then filtering for online/accessible ones.

## Description

MassDNS excels at brute-forcing large lists with custom resolvers, handling thousands of queries per second. Input a one-per-line subdomain list; output includes query results with status (OK/NXDOMAIN). Use with 25-100 resolvers for balance; post-process to extract valid hosts, revealing the target's live DNS footprint.

## Requirements

- Subdomain wordlist (from SecLists or Amass)
- Verified resolvers.txt
- MassDNS compiled (C-based, fast)

## Defense

- DNS rate limiting and response caching
- Block recursive queries from unknown sources
- Log anomalous high-volume A record queries

## Objectives

- Resolve 10,000+ subdomains quickly
- Identify 5+ live hosts
- Output clean lists of hosts and IPs

## Instructions

### Step 1: Resolve Subdomains

**Context**: Query A records using resolvers for the wordlist.

**Command** ([[commands/massdns-resolve-subdomains-for-a-records]]):

```bash
massdns -r $_DNS_RESOLVERS -t A -o S -w $_OUTPUT_FILE $_HOST_WORDLIST
```

-o S for simple output; processes in seconds for large lists.

### Step 2: Extract Online Hosts

**Context**: Filter successful resolutions to list live subdomains.

**Command** ([[commands/extract-online-hosts-from-massdns-output]]):

```bash
cat $_MASSDNS_OUTPUT | awk '{print $1}' | sed 's/.$//' | sort -u > $_ONLINE_HOSTS_FILE
```

Removes query ID and duplicates.

### Step 3: Extract IPs

**Context**: Pull unique IPv4 addresses from resolutions.

**Command** ([[commands/extract-ips-from-massdns-output]]):

```bash
cat $_MASSDNS_OUTPUT | awk '{print $3}' | sort -u | grep -oE "\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b" > $_IPS_FILE
```

Uses regex for IPv4 only.
