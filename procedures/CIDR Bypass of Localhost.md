---
id: 15685e32-c539-4947-8249-bcfe3826366b
name: CIDR Bypass of Localhost
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.349404+00:00'
updated_at: '2023-04-10T20:24:03.616156+00:00'
tags:
- '[[Bypassing filters]]'
- '[[Bypass localhost with CIDR]]'
- '[[Server-Side Request Forgery]]'
---

# CIDR Bypass of Localhost

## Summary

CIDR Bypass of Localhost is a technique used to bypass filters in a Server-Side Request Forgery (SSRF) attack. The attacker can bypass filters that block requests to localhost by using CIDR notation. This technique allows the attacker to access internal resources on the target system, such as datab

## Description

# Description

CIDR Bypass of Localhost is a technique used to bypass filters in a Server-Side Request Forgery (SSRF) attack. The attacker can bypass filters that block requests to localhost by using CIDR notation. This technique allows the attacker to access internal resources on the target system, such as databases and other sensitive information. The attacker can use this technique to pivot to other systems on the network and gain access to additional resources.

Technical Explanation:
CIDR notation is a way of representing IP addresses and their associated network masks. By using CIDR notation, an attacker can specify a range of IP addresses that includes the localhost address (127.0.0.1). This allows the attacker to bypass filters that block requests to localhost. The attacker can then use this technique to access internal resources on the target system.

Business Value:
This technique can be used by attackers to steal sensitive information from a target system, such as customer data, financial information, and intellectual property. This can result in financial losses, loss of reputation, and legal action against the company.

 

## Requirements

1. Access to the target system

1. Knowledge of CIDR notation

 

## Defense

1. Implement network filtering to block requests to localhost from external sources

1. Implement input validation to prevent SSRF attacks

1. Implement access controls to restrict access to sensitive resources

 

## Objectives

1. Bypass filters that block requests to localhost

1. Access internal resources on the target system

1. Pivot to other systems on the network and gain access to additional resources

 

# Instructions

1. To retrieve IP addresses from the loopback network interface, use the 'Get-NetIPAddress' command in PowerShell. The loopback interface has the IPv4 address of 127.0.0.1 and the IPv6 address of ::1.

 



**Code**: [[http://127.127.127.127
http://127.0.1.3
http://127]]



> The IP addresses listed in the 'data' field are all part of the loopback network interface, which allows a computer to communicate with itself. The IP address range 127.0.0.0/8 is reserved for this purpose and is not routable on the internet. The 'lang' field indicates that the command is written in PowerShell, a command-line shell and scripting language developed by Microsoft. The 'text' field provides a brief description of the data in the 'data' field. The 'instruction' field provides guidance on how to retrieve this information using a PowerShell command, and the 'explain' field provides additional context on the purpose of the loopback interface and the IP address range used for it.

## Tags

- [[Bypassing filters]]
- [[Bypass localhost with CIDR]]
- [[Server-Side Request Forgery]]


