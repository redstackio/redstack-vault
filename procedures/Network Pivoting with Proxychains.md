---
id: 2c0cd4a8-3c6a-4bba-a212-f568988eab8e
name: Network Pivoting with Proxychains
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.522993+00:00'
updated_at: '2023-04-10T20:25:17.707809+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
tags:
- '[[Network Pivoting Techniques]]'
- '[[Proxychains]]'
commands:
- '[[Configure ProxyList]]'
- '[[Scan target IP using nmap and proxychains]]'
---

# Network Pivoting with Proxychains

## Summary

Network pivoting with Proxychains is a technique used by attackers to gain access to other systems within a network. Proxychains is a tool that allows an attacker to route their traffic through one or more proxy servers, making it more difficult to trace their activities. This technique can be used

## Description

# Description

Network pivoting with Proxychains is a technique used by attackers to gain access to other systems within a network. Proxychains is a tool that allows an attacker to route their traffic through one or more proxy servers, making it more difficult to trace their activities. This technique can be used to gain access to systems that are not directly accessible from the attacker's machine, bypassing network security measures such as firewalls and network segmentation.

Technical Explanation: Proxychains is a tool that allows an attacker to route their traffic through one or more proxy servers. This can be useful for bypassing network security measures such as firewalls and network segmentation. By using Proxychains, an attacker can make their traffic appear to be coming from a different IP address, making it more difficult to trace their activities.

Business Value: This technique can be used by attackers to gain access to sensitive information or systems within a network. By bypassing network security measures, attackers can gain access to systems that would otherwise be protected.

 

## Requirements

1. Access to a vulnerable system within the target network

1. Proxychains installed on the attacker's machine

 

## Defense

1. Implement network segmentation to limit lateral movement

1. Monitor network traffic for unusual activity

1. Use strong authentication measures to prevent unauthorized access

 

## Objectives

1. Gain access to systems that are not directly accessible from the attacker's machine

1. Bypass network security measures such as firewalls and network segmentation

1. Gain access to sensitive information or systems within a network

 

# Instructions

1. To configure a proxy using proxychains, add the proxy details to the /etc/proxychains.conf file in the format shown in the 'data' field.

 



**Code**: [[[ProxyList]
socks4 localhost 8080]]



> The 'data' field contains the sample configuration for a SOCKS4 proxy running on localhost at port 8080. To configure a different proxy, replace the 'localhost' and '8080' with the IP address and port of the proxy server. The 'lang' field specifies the language used in the example command, which is bash. The 'text' field provides additional information about the configuration file location. 



**Command** ([[Configure ProxyList]]):

```bash
[ProxyList]
socks4 localhost 8080
```



2. To scan a target with Nmap using Proxychains, follow these steps:
1. Install Proxychains and Nmap on your system.
2. Open a terminal and run the following command: proxychains nmap -sT <target_ip_address>
   Replace <target_ip_address> with the IP address of the target you want to scan.
3. Proxychains will automatically route your Nmap traffic through a SOCKS4 proxy, providing an extra layer of anonymity.

 



**Code**: [[proxychains nmap -sT 192.168.5.6]]



> The 'proxychains' command allows you to run other command-line tools through a proxy server. In this case, we are using it to run Nmap through a SOCKS4 proxy. The '-sT' option in the Nmap command tells it to perform a TCP connect scan, which is a basic scan that attempts to connect to the target on each port to determine if it is open or closed. By using Proxychains, we can hide our true IP address and location from the target, making it more difficult for them to track us down. Note that using a proxy server may also slow down the scanning process.



**Command** ([[Scan target IP using nmap and proxychains]]):

```bash
proxychains nmap -sT 192.168.5.6
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]

## Commands Used

- [[Configure ProxyList]]
- [[Scan target IP using nmap and proxychains]]

## Tags

- [[Network Pivoting Techniques]]
- [[Proxychains]]


