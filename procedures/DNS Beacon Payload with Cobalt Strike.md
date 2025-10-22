---
id: 957d33cb-3aa0-4bb0-9b70-a808e87091d1
name: DNS Beacon Payload with Cobalt Strike
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.309848+00:00'
updated_at: '2023-04-10T20:36:21.438432+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Dynamic Resolution|T1568 - Dynamic Resolution]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
sub_techniques:
- '[[Domain Generation Algorithms|T1568.002 - Domain Generation Algorithms]]'
- '[[Web Protocols|T1071.001 - Web Protocols]]'
tags:
- '[[Cobalt Strike]]'
- '[[DNS Beacon]]'
- '[[Payloads]]'
commands:
- '[[Disable systemd-resolved and update resolv.conf]]'
- '[[DNS record for campaigns.example.com]]'
- '[[DNS record for example.com]]'
- '[[DNS record for polling.campaigns.example.com]]'
---

# DNS Beacon Payload with Cobalt Strike

## Summary

The DNS Beacon payload is a command and control (C2) technique used by adversaries to maintain persistence and evade detection. This technique uses DNS traffic for communication between the compromised host and the C2 server, making it difficult to detect and block. Cobalt Strike is a popular tool 

## Description

# Description

The DNS Beacon payload is a command and control (C2) technique used by adversaries to maintain persistence and evade detection. This technique uses DNS traffic for communication between the compromised host and the C2 server, making it difficult to detect and block. Cobalt Strike is a popular tool used by red teams and threat actors to simulate attacks and test defenses. The DNS Beacon payload with Cobalt Strike allows users to simulate this technique and test their defenses against it.

Technical Explanation: The DNS Beacon payload with Cobalt Strike works by setting up a DNS server on the compromised host that will be used for communication with the C2 server. The payload will periodically send DNS queries to the C2 server, which will respond with encoded data containing commands for the payload to execute. The payload will then execute the commands and send the results back to the C2 server using DNS queries. This technique is effective because DNS traffic is usually allowed through firewalls and is rarely inspected.

Business Value: The DNS Beacon payload with Cobalt Strike can be used by organizations to test their defenses against this technique and improve their security posture. By simulating attacks, organizations can identify weaknesses in their defenses and take steps to mitigate them before they are exploited by real attackers.

## Requirements

1. Access to a Linux host

1. Cobalt Strike installed on the host

1. Ability to modify DNS server configuration on the host

## Defense

1. Implement network segmentation to restrict access to critical systems

1. Monitor DNS traffic for suspicious activity

1. Use threat intelligence to identify known C2 servers and block them at the network perimeter

## Objectives

1. Test the effectiveness of defenses against the DNS Beacon payload

1. Identify weaknesses in the security posture of an organization

1. Improve the overall security posture of an organization

# Instructions

1. To configure DNS, use the following commands:
1. NS: This command is used to specify the name servers for a domain.
2. A: This command is used to specify the IP address for a domain.

Example:
NS example.com directs to 10.10.10.10. 86400
A campaigns.example.com directs to 10.10.10.10 3600

**Code**: [[NS  example.com directs to 10.10.10.10. 86400
NS  ]]

> Arguments:
1. NS: Name server record type
   - example.com: The domain name to be associated with the name server.
   - directs to 10.10.10.10: The IP address of the name server.
   - 86400: The time to live for the record.
2. A: Address record type
   - campaigns.example.com: The domain name to be associated with the IP address.
   - directs to 10.10.10.10: The IP address to be associated with the domain name.
   - 3600: The time to live for the record.

**Command** ([[DNS record for example.com]]):

```bash
NS  example.com directs to 10.10.10.10. 86400
```

**Command** ([[DNS record for polling.campaigns.example.com]]):

```bash
NS  polling.campaigns.example.com directs to campaigns.example.com. 3600
```

**Command** ([[DNS record for campaigns.example.com]]):

```bash
A campaigns.example.com directs to 10.10.10.10 3600
```

2. To change the DNS servers on a Linux machine, run the following commands:

**Code**: [[systemctl disable systemd-resolved
systemctl stop ]]

> This command will disable and stop the systemd-resolved service, remove the current resolv.conf file, and create a new resolv.conf file with the Google DNS servers (8.8.8.8 and 8.8.4.4) as the nameservers. This is useful when troubleshooting DNS issues or when you want to use a specific DNS server instead of the default one provided by your ISP.

**Command** ([[Disable systemd-resolved and update resolv.conf]]):

```bash
systemctl disable systemd-resolved
systemctl stop systemd-resolved
rm /etc/resolv.conf
echo "nameserver 8.8.8.8" >  /etc/resolv.conf
echo "nameserver 8.8.4.4" >>  /etc/resolv.conf
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Dynamic Resolution|T1568 - Dynamic Resolution]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

### Sub-Techniques

- [[Domain Generation Algorithms|T1568.002 - Domain Generation Algorithms]]
- [[Web Protocols|T1071.001 - Web Protocols]]

## Commands Used

- [[Disable systemd-resolved and update resolv.conf]]
- [[DNS record for campaigns.example.com]]
- [[DNS record for example.com]]
- [[DNS record for polling.campaigns.example.com]]

## Tags

- [[Cobalt Strike]]
- [[DNS Beacon]]
- [[Payloads]]
