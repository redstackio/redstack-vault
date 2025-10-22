---
id: b6a43e9a-8be7-4902-b991-04c9fc2dcc12
name: DNS Enumeration & OSINT
type: attack_chain
description: osint, dns, service enumeration, scanning
verified: true
submitted: true
step_count: 6
created_at: '2020-07-01T17:15:47.643290+00:00'
updated_at: '2023-05-30T20:16:39.686195+00:00'
procedures:
- '[[Generate DNS Sub-Domain Wordlist (seclists)]]'
- '[[Scan Sub-Domains for Online Hosts (massdns)]]'
- '[[Scan list of IP''s (masscan)]]'
- '[[build list of verified dns resolvers (dnsvalidator)]]'
- '[[Basic Port Scan with Aggressive Service Enumeration]]'
- '[[Find Subdomains (amass)]]'
tags:
- osint
- dns
- service enumeration
- scanning
---

# DNS Enumeration & OSINT

**Status**: ✓ Verified

**Description**: osint, dns, service enumeration, scanning

## Overview

This attack chain consists of 6 steps.

## Attack Steps

### Step 1: build list of verified dns resolvers (dnsvalidator)

**Procedure**: [[build list of verified dns resolvers (dnsvalidator)]]

> You can use this tool to build a list of verified dns servers to be used in conjunction with other tools. This tool can take a while to run so, do it prior to your pentest and use lots of threads (20-200 should be good). This command will store the results in the output file. This file can be used 

---

### Step 2: Find Subdomains (amass)

**Procedure**: [[Find Subdomains (amass)]]

> Amass uses a GraphDB that can store details of every scan which can then later be visualized, or differentiated. This can be done by specifying an output directory to amass. This will also retain a log of the scan attempts. Identifying the targets subdomains is important to: Know what servers are a

---

### Step 3: Generate DNS Sub-Domain Wordlist (seclists)

**Procedure**: [[Generate DNS Sub-Domain Wordlist (seclists)]]

> You will find it useful to build your own subdomain wordlist to brute force with tools like massdns. Once you obtain SecLists wordlist from github and un-gzip / un-tar it, run this command against your target domain to build the wordlist into your local directory. 

---

### Step 4: Scan Sub-Domains for Online Hosts (massdns)

**Procedure**: [[Scan Sub-Domains for Online Hosts (massdns)]]

> You have a list of subdomains in a text file and want to connect to all of them to match their IP address, and verify which ones are online and accessible from the internet. Use massdns to quickly parse through your subdomain list. If you do not have a resolvers.txt file, look up dnsvalidator to bu

---

### Step 5: Scan list of IP's (masscan)

**Procedure**: [[Scan list of IP's (masscan)]]

> The heavyweight port scanner of the internet will scan a list of ip addresses very quickly. The ip input file has one ip address per line. the -p1-65535 are the ports that it will scan 

---

### Step 6: Basic Port Scan with Aggressive Service Enumeration

**Procedure**: [[Basic Port Scan with Aggressive Service Enumeration]]

> Launch a port scan, enumerating services, performing OS detection, and banner grabbing. 

---

## Chain Summary

- **Total Steps**: 6
- **Key Procedures**: 6 procedures
