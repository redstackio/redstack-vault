---
id: f5733e7c-b6cb-4efb-9597-aecb3f48bea3
name: Bettercap Proxy Spoofing Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.307612+00:00'
updated_at: '2023-04-10T20:25:05.512388+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
- '[[Bettercap]]'
- '[[Network Discovery]]'
commands:
- '[[Bettercap Proxy and Sniffer]]'
---

# Bettercap Proxy Spoofing Procedure

## Summary

The Bettercap Proxy Spoofing Procedure is an offensive technique that allows an attacker to intercept network traffic by spoofing the IP address of a target. This method can be used to collect sensitive information such as login credentials or to perform a man-in-the-middle attack. The attacker can

## Description

# Description

The Bettercap Proxy Spoofing Procedure is an offensive technique that allows an attacker to intercept network traffic by spoofing the IP address of a target. This method can be used to collect sensitive information such as login credentials or to perform a man-in-the-middle attack. The attacker can use Bettercap to scan for target devices and then use the Proxy Spoofing Command to intercept their traffic. This technique is particularly effective in unencrypted networks.

 

## Requirements

1. Access to the target network

1. Bettercap installed on the attacker's machine

 

## Defense

1. Use encryption to protect sensitive traffic

1. Implement network segmentation to limit attack surface

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Intercept network traffic

1. Collect sensitive information

1. Perform man-in-the-middle attacks

 

# Instructions

1. To use this command, open a terminal and run the following command: bettercap -X --proxy --proxy-https -T <target IP>. This command will allow you to perform spoofing, discovery, and sniffing tasks, as well as intercepting HTTP and HTTPS requests. You can also target a specific IP address by specifying it with the -T flag.

 



**Code**: [[bettercap -X --proxy --proxy-https -T <target IP>
]]



> The -X flag enables experimental features, while the --proxy and --proxy-https flags enable the proxy and HTTPS proxy modules, respectively. The -T flag allows you to specify a target IP address. This command is useful for testing network security and analyzing network traffic.



**Command** ([[Bettercap Proxy and Sniffer]]):

```bash
bettercap -X --proxy --proxy-https -T <target IP>
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Bettercap Proxy and Sniffer]]

## Tags

- [[Bettercap]]
- [[Network Discovery]]


