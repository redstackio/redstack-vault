---
id: 07d082fe-909e-4f90-8636-21f3522d117b
name: Active Directory Integrated DNS Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.640933+00:00'
updated_at: '2023-04-10T20:26:13.821810+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Query Registry|T1012 - Query Registry]]'
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Integrated DNS]]'
commands:
- '[[Dump DNS Zones from Active Directory]]'
- '[[Inveigh DNS spoofing and man-in-the-middle attack]]'
---

# Active Directory Integrated DNS Enumeration

## Summary

Active Directory Integrated DNS is a feature in Windows Server that allows DNS zones to be stored and managed in Active Directory. This feature can be used by attackers to gather information about the network and its assets. By querying the DNS server, attackers can enumerate DNS records, including

## Description

# Description

Active Directory Integrated DNS is a feature in Windows Server that allows DNS zones to be stored and managed in Active Directory. This feature can be used by attackers to gather information about the network and its assets. By querying the DNS server, attackers can enumerate DNS records, including A, MX, and SRV records, and discover new hosts and services. This procedure involves using various tools to perform DNS enumeration and reconnaissance on the Active Directory Integrated DNS server.

From an offensive standpoint, this procedure can be used to gather information about the network and identify potential targets for further attacks. From a defensive standpoint, it is important to monitor DNS queries and zone transfers to detect and prevent unauthorized access to sensitive information.

Business value: This procedure can help organizations identify potential security weaknesses in their network infrastructure and improve their overall security posture.

## Requirements

1. Access to the Active Directory Integrated DNS server

1. DNS enumeration tools such as dnstool.py

## Defense

1. Implement network segmentation to limit access to the Active Directory Integrated DNS server

1. Monitor DNS queries and zone transfers for suspicious activity

1. Limit the use of DNS enumeration tools to authorized personnel

## Objectives

1. Enumerate DNS records on the Active Directory Integrated DNS server

1. Discover new hosts and services on the network

1. Identify potential targets for further attacks

# Instructions

1. This command is used to enumerate all DNS zones in a given domain using ADIDNSDump tool. It requires the domain name, username and domain controller details. The --dns-tcp flag is used to force the tool to use TCP instead of UDP for DNS queries.

**Code**: [[adidnsdump -u DOMAIN\\user --print-zones dc.domain]]

> The '-u' parameter is used to specify the username in the format DOMAIN\\user. The '--print-zones' flag is used to print all DNS zones in the domain. The 'dc.domain.corp' parameter is the IP address or hostname of the domain controller to query. This command can be useful in identifying DNS misconfigurations or potential attack vectors.

**Command** ([[Dump DNS Zones from Active Directory]]):

```bash
adidnsdump -u DOMAIN\\user --print-zones dc.domain.corp --dns-tcp
```

2. To perform a DNS query using dnstool.py, use the following command:

dnstool.py -u 'DOMAIN\user' -p 'password' --record '*' --action query $DomainController (--legacy)

Replace 'DOMAIN\user' and 'password' with the appropriate credentials. Replace '*' with the desired DNS record to query. Replace '$DomainController' with the IP address or hostname of the domain controller to query.

**Code**: [[dnstool.py -u 'DOMAIN\user' -p 'password' --record]]

> The 'dnstool.py' command is used to perform DNS queries on a Windows domain. The '-u' flag specifies the user to authenticate as in the format 'DOMAIN\user'. The '-p' flag specifies the password for the user. The '--record' flag specifies the DNS record to query. The '--action' flag specifies the action to perform, in this case 'query'. The '$DomainController' variable specifies the IP address or hostname of the domain controller to query. The '--legacy' flag is optional and may be used if the domain controller is running an older version of Windows Server.

3. To add a DNS record for a node, use the 'dnstool.py' command. Provide the domain user credentials using the '-u' and '-p' options. Specify the record type using the '--record' option and provide the node's IP address and domain controller using the '--data' option. Use the '--action add' option to add the record.

**Code**: [[dnstool.py -u 'DOMAIN\user' -p 'password' --record]]

> -u: Specifies the domain user credentials.
-p: Specifies the password for the domain user.
--record: Specifies the type of DNS record to add.
--data: Specifies the IP address of the node and the domain controller.
--action: Specifies the action to perform on the DNS record.

4. This command will invoke Inveigh to perform passive reconnaissance on ADIDNS. It will output to the console and listen on LLMNR, NBNS, and mDNS protocols. It will also search for combo, ns, and wildcard records with a threshold of 3. Additionally, it will use machine accounts and challenge value 1122334455667788.

**Code**: [[Invoke-Inveigh -ConsoleOutput Y -ADIDNS combo,ns,w]]

> The Invoke-Inveigh command is used to perform passive reconnaissance on ADIDNS. The -ConsoleOutput parameter specifies that the output should be displayed in the console. The -ADIDNS parameter specifies the type of records to search for. In this case, it will search for combo, ns, and wildcard records. The -ADIDNSThreshold parameter sets the threshold for the number of times a record must be found before it is displayed. The -LLMNR, -NBNS, and -mDNS parameters specify which protocols to listen on. The -Challenge parameter sets the challenge value for NTLMv2 authentication. The -MachineAccounts parameter specifies that machine accounts should be used for authentication.

**Command** ([[Inveigh DNS spoofing and man-in-the-middle attack]]):

```bash
Invoke-Inveigh -ConsoleOutput Y -ADIDNS combo,ns,wildcard -ADIDNSThreshold 3 -LLMNR Y -NBNS Y -mDNS Y -Challenge 1122334455667788 -MachineAccounts Y
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Query Registry|T1012 - Query Registry]]
- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Dump DNS Zones from Active Directory]]
- [[Inveigh DNS spoofing and man-in-the-middle attack]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Integrated DNS]]
