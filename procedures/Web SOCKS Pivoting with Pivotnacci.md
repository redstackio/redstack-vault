---
id: 54533bb8-1ded-4be7-9583-cc3f20306412
name: Web SOCKS Pivoting with Pivotnacci
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:22.606427+00:00'
updated_at: '2023-04-10T20:25:18.043696+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
sub_techniques:
- '[[Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]'
tags:
- '[[Network Pivoting Techniques]]'
- '[[Web SOCKS - pivotnacci]]'
commands:
- '[[Install pivotnacci package]]'
- '[[Run pivotnacci with password argument]]'
- '[[Run pivotnacci with polling interval argument]]'
---

# Web SOCKS Pivoting with Pivotnacci

## Summary

Web SOCKS Pivoting with Pivotnacci is a technique used for lateral movement within a network. This technique involves using a compromised web server as a pivot point to redirect network traffic through a SOCKS proxy. This technique can be used to bypass network security controls and gain access to 

## Description

# Description

Web SOCKS Pivoting with Pivotnacci is a technique used for lateral movement within a network. This technique involves using a compromised web server as a pivot point to redirect network traffic through a SOCKS proxy. This technique can be used to bypass network security controls and gain access to systems that are not directly accessible from the attacker's initial point of entry.

To implement this technique, the attacker first compromises a web server and installs a SOCKS proxy server on it. The attacker then uses the compromised web server as a pivot point to redirect network traffic through the SOCKS proxy. This can be done using tools such as Pivotnacci.

From a technical standpoint, this technique involves modifying the network routing tables to redirect traffic through the compromised web server. This technique can be difficult to detect, as the traffic appears to be coming from a legitimate source.

 

## Requirements

1. Compromised web server with a SOCKS proxy installed

1. Access to network routing tables

 

## Defense

1. Deploy network segmentation to limit the attacker's ability to move laterally within the network

1. Monitor network traffic for signs of network pivoting techniques such as traffic redirection

1. Implement strong authentication and access controls to limit the attacker's ability to compromise web servers

 

## Objectives

1. To gain access to systems that are not directly accessible from the attacker's initial point of entry

1. To bypass network security controls

 

# Instructions

1. To use Pivotnacci, first install it using pip. Then, use the `pivotnacci` command followed by the URL of the HTTP agent you want to use. You can also specify a password using the `--password` option and set the polling interval using the `--polling-interval` option.

 



**Code**: [[pip3 install pivotnacci
pivotnacci https://domain.]]



> Pivotnacci is a tool that allows you to create a SOCKS proxy through an HTTP agent. This can be useful for pivoting through a compromised web server, for example. The `pivotnacci` command takes the URL of the HTTP agent as its first argument. If the agent requires a password, you can specify it using the `--password` option. The `--polling-interval` option allows you to set the interval at which Pivotnacci polls the HTTP agent for new connections. This value is specified in milliseconds.



**Command** ([[Install pivotnacci package]]):

```bash
pip3 install pivotnacci
```





**Command** ([[Run pivotnacci with password argument]]):

```bash
pivotnacci https://domain.com/agent.php --password "s3cr3t"
```





**Command** ([[Run pivotnacci with polling interval argument]]):

```bash
pivotnacci https://domain.com/agent.php --polling-interval 2000
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]

### Sub-Techniques

- [[Multi-hop Proxy|T1090.003 - Multi-hop Proxy]]

## Commands Used

- [[Install pivotnacci package]]
- [[Run pivotnacci with password argument]]
- [[Run pivotnacci with polling interval argument]]

## Tags

- [[Network Pivoting Techniques]]
- [[Web SOCKS - pivotnacci]]


