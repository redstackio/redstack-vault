---
id: d8e51d8b-47d6-4540-9e86-a29e74895e0f
name: Subdomain Enumeration using AltDNS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.669752+00:00'
updated_at: '2023-04-10T20:25:36.353704+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
tags:
- '[[Enumerate all subdomains (only if the scope is *.domain.ext)]]'
- '[[Subdomains Enumeration]]'
- '[[Using AltDNS]]'
commands:
- '[[Altdns permutation]]'
- '[[Generate permutations]]'
- '[[Install AltDNS]]'
---

# Subdomain Enumeration using AltDNS

## Summary

Subdomain enumeration is a technique used by attackers to discover subdomains in a target domain. Attackers can use these subdomains to identify new attack vectors and target specific services. AltDNS is a tool that can be used in subdomain enumeration to generate permutations and combinations of d

## Description

# Description

Subdomain enumeration is a technique used by attackers to discover subdomains in a target domain. Attackers can use these subdomains to identify new attack vectors and target specific services. AltDNS is a tool that can be used in subdomain enumeration to generate permutations and combinations of domain names based on user-defined input. This tool can help attackers identify subdomains that may not be easily discoverable through traditional enumeration techniques. From a technical perspective, AltDNS works by generating permutations of domain names based on a user-defined input file. These permutations are then resolved using DNS queries to identify valid subdomains. From a business value perspective, subdomain enumeration can help organizations identify potential attack vectors and secure their infrastructure against attacks.

## Requirements

1. Access to the target domain

1. AltDNS tool

## Defense

1. Implement proper access controls to limit access to sensitive information

1. Implement DNS monitoring and logging to detect potential attacks

1. Implement strong password policies to prevent password guessing attacks

## Objectives

1. Identify subdomains in a target domain

1. Discover potential attack vectors

1. Secure infrastructure against attacks

# Instructions

1. AltDNS is a DNS recon tool that allows you to discover subdomains that are not visible using traditional DNS enumeration techniques. To use AltDNS, you need to provide a domain name and a list of words that will be used to generate permutations of subdomains. The tool will then resolve the generated subdomains to IP addresses using the specified DNS server. You can use the '-o' option to save the results in a file.

**Code**: [[AltDNS]]

> AltDNS takes two arguments: 
1. '-i': The input file containing a list of words to generate permutations of subdomains.
2. '-w': The output file where the results will be saved.

**Command** ([[Install AltDNS]]):

```bash
git clone https://github.com/infosec-au/altdns.git
 cd altdns/
 pip install -r requirements.txt
```

**Command** ([[Generate permutations]]):

```bash
python altdns.py -i subdomains.txt -o data_output -w words.txt
```

2. Use Altdns to generate permutations of input domains.

**Code**: [[WORDLIST_PERMUTATION="./Altdns/words.txt"
python2.]]

> This command generates a list of domain names by permutating the input domains. The command uses Altdns, a Python-based tool, and requires a wordlist of possible domain name permutations. The input domains should be in a text file located at /tmp/inputdomains.txt, and the generated domain names will be saved to /tmp/out.txt. The path to the wordlist file should be set to $WORDLIST_PERMUTATION. The output file will contain all the generated domain names, which can be used for further reconnaissance and enumeration.

**Command** ([[Altdns permutation]]):

```bash
WORDLIST_PERMUTATION="./Altdns/words.txt"
python2.7 ./Altdns/altdns.py -i /tmp/inputdomains.txt -o /tmp/out.txt -w $WORDLIST_PERMUTATION
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]

## Commands Used

- [[Altdns permutation]]
- [[Generate permutations]]
- [[Install AltDNS]]

## Tags

- [[Enumerate all subdomains (only if the scope is *.domain.ext)]]
- [[Subdomains Enumeration]]
- [[Using AltDNS]]
