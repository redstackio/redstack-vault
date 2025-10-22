---
id: 4cd57084-ad1f-4e97-be7f-fdb450e1d9cf
name: Subdomain Enumeration and Takeover using Hostile Subdomain Bruteforcer
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.807525+00:00'
updated_at: '2023-04-10T20:25:35.905060+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
- '[[Remote Service Session Hijacking|T1563 - Remote Service Session Hijacking]]'
sub_techniques:
- '[[RDP Hijacking|T1563.002 - RDP Hijacking]]'
tags:
- '[[Subdomains Enumeration]]'
- '[[Subdomain take over]]'
- '[[Using HostileSubBruteForcer]]'
commands:
- '[[Clone HostileSubBruteforcer repository]]'
- '[[Make sub_brute.rb executable]]'
- '[[Run sub_brute.rb]]'
---

# Subdomain Enumeration and Takeover using Hostile Subdomain Bruteforcer

## Summary

Subdomain enumeration is the process of discovering subdomains of a domain. It is a critical step in reconnaissance for an attacker as it can provide valuable information about the target's infrastructure. Hostile Subdomain Bruteforcer is a tool that automates the process of subdomain enumeration a

## Description

# Description

Subdomain enumeration is the process of discovering subdomains of a domain. It is a critical step in reconnaissance for an attacker as it can provide valuable information about the target's infrastructure. Hostile Subdomain Bruteforcer is a tool that automates the process of subdomain enumeration and can help an attacker identify subdomains that may be vulnerable to takeover. Subdomain takeover is a type of attack where an attacker takes control of a subdomain by pointing it to their own server. This can result in various types of attacks including phishing, malware distribution or sensitive data theft. The tool works by bruteforcing subdomains using a wordlist and then checking for known vulnerabilities that can be exploited to take over the subdomain. Hostile Subdomain Bruteforcer can be used by both Red and Blue teams for reconnaissance and vulnerability identification.

## Requirements

1. Access to the internet

1. Target domain name

1. Hostile Subdomain Bruteforcer tool

## Defense

1. Ensure that all subdomains are registered and under your control

1. Monitor DNS records for any unauthorized changes

1. Implement DNSSEC to prevent DNS spoofing attacks

## Objectives

1. Identify subdomains of a given domain

1. Check if any of the subdomains are vulnerable to takeover

1. Take control of the subdomain if it is vulnerable

# Instructions

1. To use the Hostile Subdomain Bruteforcer, follow these steps:
1. Clone the HostileSubBruteforcer repository using the command 'git clone https://github.com/nahamsec/HostileSubBruteforcer'
2. Navigate to the sub_brute.rb file using the command 'cd HostileSubBruteforcer'
3. Make the sub_brute.rb file executable using the command 'chmod +x sub_brute.rb'
4. Run the sub_brute.rb file using the command './sub_brute.rb'

**Code**: [[git clone https://github.com/nahamsec/HostileSubBr]]

> The Hostile Subdomain Bruteforcer is a tool used to discover subdomains of a target domain. The tool works by brute forcing subdomains using a wordlist. The user can provide their own wordlist or use the default wordlist provided with the tool. The tool also allows the user to specify the number of threads to use for the brute forcing process. The Hostile Subdomain Bruteforcer can be used for security testing purposes to identify potential attack vectors on a target domain.

**Command** ([[Clone HostileSubBruteforcer repository]]):

```bash
git clone https://github.com/nahamsec/HostileSubBruteforcer
```

**Command** ([[Make sub_brute.rb executable]]):

```bash
chmod +x sub_brute.rb
```

**Command** ([[Run sub_brute.rb]]):

```bash
./sub_brute.rb
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]
- [[Remote Service Session Hijacking|T1563 - Remote Service Session Hijacking]]

### Sub-Techniques

- [[RDP Hijacking|T1563.002 - RDP Hijacking]]

## Commands Used

- [[Clone HostileSubBruteforcer repository]]
- [[Make sub_brute.rb executable]]
- [[Run sub_brute.rb]]

## Tags

- [[Subdomains Enumeration]]
- [[Subdomain take over]]
- [[Using HostileSubBruteForcer]]
