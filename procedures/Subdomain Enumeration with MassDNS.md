---
id: ebf675c2-b334-4ebe-b27d-c74afd47e196
name: Subdomain Enumeration with MassDNS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.697945+00:00'
updated_at: '2023-04-10T20:25:38.447590+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Search Open Technical Databases|T1596 - Search Open Technical Databases]]'
sub_techniques:
- '[[Digital Certificates|T1596.003 - Digital Certificates]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using MassDNS]]'
---

# Subdomain Enumeration with MassDNS

## Summary

Subdomain enumeration is a crucial step in reconnaissance for an attacker. By identifying subdomains, an attacker can gather information on the target's infrastructure and potentially find vulnerabilities to exploit. MassDNS is a tool that can be used to enumerate subdomains by performing DNS resol

## Description

# Description

Subdomain enumeration is a crucial step in reconnaissance for an attacker. By identifying subdomains, an attacker can gather information on the target's infrastructure and potentially find vulnerabilities to exploit. MassDNS is a tool that can be used to enumerate subdomains by performing DNS resolutions. It can be useful when other tools fail to resolve subdomains. By using MassDNS, an attacker can gather a comprehensive list of subdomains for a target domain.

Technical Explanation: MassDNS performs DNS resolutions by sending multiple queries in parallel using a user-provided list of subdomains. It can be used to resolve both A and AAAA records. MassDNS is designed to be fast and efficient, making it a valuable tool for subdomain enumeration.

Business Value: Subdomain enumeration with MassDNS can help businesses identify potential security risks in their infrastructure. By identifying subdomains, businesses can take steps to secure them and prevent attacks that target these subdomains.

## Requirements

1. Access to the target domain's DNS server

1. A list of subdomains to resolve

1. MassDNS tool installed on the attacker's system

## Defense

1. Regularly monitor DNS queries and look for unusual patterns

1. Implement DNS security measures such as DNSSEC and DNS filtering

1. Use subdomain takeover services to identify and secure unused subdomains

## Objectives

1. Identify all subdomains for a target domain

1. Gather information on the target's infrastructure

1. Identify potential security risks in the target's infrastructure

# Instructions

1. This command resolves the subdomains found by Subfinder using MassDNS. The command reads the subdomains from a file called `results_subfinder.txt` and writes the resolved IP addresses to a file called `results_subfinder_resolved.txt`. The `-r` flag specifies the path to a file containing a list of DNS resolvers. The `-t A` flag specifies to resolve A records. The `-o S` flag specifies to write the output in a sorted format. The `-w` flag specifies the path to the output file.

**Code**: [[DNS_RESOLVERS="./resolvers.txt"
cat /tmp/results_s]]

> The `DNS_RESOLVERS` variable can be set to the path of a file containing a list of DNS resolvers. The `cat` command reads the contents of the `results_subfinder.txt` file and pipes it as input to the `massdns` command. The `-r` flag specifies the path to a file containing a list of DNS resolvers. The `-t A` flag specifies to resolve A records. The `-o S` flag specifies to write the output in a sorted format. The `-w` flag specifies the path to the output file. The `goaltdns` tool is an alternative to MassDNS that can also be used to resolve subdomains.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

### Sub-Techniques

- [[Digital Certificates|T1596.003 - Digital Certificates]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using MassDNS]]
