---
id: 2bfcab16-7609-49ae-8681-fba7de55e253
name: DNS Reconnaissance with ADIDNS Search Commands
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.469362+00:00'
updated_at: '2023-04-10T20:26:28.508838+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Gather Victim Network Information|T1590 - Gather Victim Network Information]]'
- '[[Network Boundary Bridging|T1599 - Network Boundary Bridging]]'
- '[[Search Open Technical Databases|T1596 - Search Open Technical Databases]]'
tags:
- '[[Active Directory Attacks]]'
- '[[DNS Reconnaissance]]'
commands:
- '[[StandIn DNS Lookup with Forest and Credentials]]'
- '[[StandIn DNS Lookup with Legacy and Credentials]]'
- '[[StandIn DNS Lookup with Limit of 20]]'
- '[[StandIn DNS Lookup with SQL Filter and Limit of 10]]'
---

# DNS Reconnaissance with ADIDNS Search Commands

## Summary

DNS reconnaissance is a critical step in Active Directory attacks. The ADIDNS Search Commands can be used to perform DNS reconnaissance on a target network. By querying the DNS server for information, an attacker can gather valuable information about the network topology and the services that are r

## Description

# Description

DNS reconnaissance is a critical step in Active Directory attacks. The ADIDNS Search Commands can be used to perform DNS reconnaissance on a target network. By querying the DNS server for information, an attacker can gather valuable information about the network topology and the services that are running. This information can then be used to identify potential attack vectors and to plan a targeted attack.

The ADIDNS Search Commands use LDAP queries to search the Active Directory for DNS records. This allows the attacker to gather information about the DNS zones, DNS servers, and other DNS-related information. The commands can be used to gather information about the domain name, the domain controllers, the DNS servers, and the DNS zones. This information can be used to identify potential attack vectors such as DNS cache poisoning, DNS spoofing, and zone transfer attacks.

By performing DNS reconnaissance with ADIDNS Search Commands, an attacker can gain a better understanding of the target network and plan a more effective attack.

## Requirements

1. Access to the target network

1. Authenticated access to the Active Directory

1. ADIDNS Search Commands

## Defense

1. Implement DNS security best practices such as DNSSEC and DNS filtering

1. Monitor DNS logs for suspicious activity

1. Restrict access to the ADIDNS Search Commands to authorized personnel only

## Objectives

1. Gather information about the target network

1. Identify potential attack vectors

1. Plan a targeted attack

# Instructions

1. To use these commands, open PowerShell and navigate to the directory containing StandIn.exe. Then, type in the desired command based on your search criteria and hit enter. The results will be displayed in the PowerShell window.

**Code**: [[StandIn.exe --dns --limit 20
StandIn.exe --dns --f]]

> These commands are used to perform ADIDNS searches. The '--dns' flag specifies that we want to search for DNS records. The '--limit' flag specifies the maximum number of results we want to display. The '--filter' flag filters the results based on a keyword or phrase. The '--forest' flag specifies that we want to search the entire forest. The '--domain' flag specifies the domain we want to search. The '--user' and '--pass' flags specify the username and password for authentication. The '--legacy' flag specifies that we want to use legacy authentication.

**Command** ([[StandIn DNS Lookup with Limit of 20]]):

```bash
StandIn.exe --dns --limit 20
```

**Command** ([[StandIn DNS Lookup with SQL Filter and Limit of 10]]):

```bash
StandIn.exe --dns --filter SQL --limit 10
```

**Command** ([[StandIn DNS Lookup with Forest and Credentials]]):

```bash
StandIn.exe --dns --forest --domain redhook --user RFludd --pass Cl4vi$Alchemi4e
```

**Command** ([[StandIn DNS Lookup with Legacy and Credentials]]):

```bash
StandIn.exe --dns --legacy --domain redhook --user RFludd --pass Cl4vi$Alchemi4e
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Gather Victim Network Information|T1590 - Gather Victim Network Information]]
- [[Network Boundary Bridging|T1599 - Network Boundary Bridging]]
- [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

## Commands Used

- [[StandIn DNS Lookup with Forest and Credentials]]
- [[StandIn DNS Lookup with Legacy and Credentials]]
- [[StandIn DNS Lookup with Limit of 20]]
- [[StandIn DNS Lookup with SQL Filter and Limit of 10]]

## Tags

- [[Active Directory Attacks]]
- [[DNS Reconnaissance]]
