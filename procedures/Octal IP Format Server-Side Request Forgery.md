---
id: 9f2eceb7-fc26-4571-88c4-ac998cdd2bf3
name: Octal IP Format Server-Side Request Forgery
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.395129+00:00'
updated_at: '2023-04-10T20:23:53.710396+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[External Remote Services|T1133 - External Remote Services]]'
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
- '[[Protocol Tunneling|T1572 - Protocol Tunneling]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypass using octal IP]]'
- '[[Server-Side Request Forgery]]'
---

# Octal IP Format Server-Side Request Forgery

## Summary

Octal IP Format Server-Side Request Forgery is a technique used to bypass filters that are designed to block requests to specific IP addresses. By using the octal IP format, an attacker can send requests to a target server using an IP address that would normally be blocked. This technique can be us

## Description

# Description

Octal IP Format Server-Side Request Forgery is a technique used to bypass filters that are designed to block requests to specific IP addresses. By using the octal IP format, an attacker can send requests to a target server using an IP address that would normally be blocked. This technique can be used to perform a Server-Side Request Forgery attack, where an attacker can send requests to a target server on behalf of the server itself, potentially bypassing authentication and gaining access to sensitive data.

To use this technique, an attacker would need to identify a vulnerable server that is susceptible to Server-Side Request Forgery attacks. They would then send a request to the server using the octal IP format, which would allow them to bypass any filters or restrictions that are in place. This technique can be particularly effective against servers that are not properly configured or have weak security controls in place.

The business value of this technique is that it can be used to gain access to sensitive data or systems that are protected by firewalls or other security measures. By bypassing these measures, an attacker can gain a foothold in a target network and potentially launch further attacks.

## Requirements

1. Access to a vulnerable server that is susceptible to Server-Side Request Forgery attacks

1. Knowledge of the octal IP format

1. Ability to send requests to the target server

## Defense

1. Implement proper input validation and sanitization to prevent Server-Side Request Forgery attacks

1. Configure firewalls and other security measures to block requests from known malicious IP addresses

1. Monitor network traffic for suspicious activity and investigate any anomalies

## Objectives

1. Bypass filters and restrictions to perform a Server-Side Request Forgery attack

1. Gain access to sensitive data or systems that are protected by firewalls or other security measures

# Instructions

1. To convert an octal format of ipv4 to decimal format, you can use the following command:

$ echo '0177.0.0.1' | awk -F. '{printf "%d.%d.%d.%d
",$1,$2,$3,$4}'

This will output: 127.0.0.1

**Code**: [[http://0177.0.0.1/ = http://127.0.0.1
http://o177.]]

> In the octal format of ipv4, each octet (segment of the IP address separated by dots) is represented by a number between 0 and 377 (or 0o377 in octal). However, not all implementations of networking software support this format, and some may interpret it as a decimal number instead. To avoid issues, it is recommended to use the standard decimal format for ipv4 addresses (four decimal numbers separated by dots).

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Discovery|TA0007 - Discovery]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[External Remote Services|T1133 - External Remote Services]]
- [[Network Service Scanning|T1046 - Network Service Scanning]]
- [[Protocol Tunneling|T1572 - Protocol Tunneling]]

## Tags

- [[Bypassing filters]]
- [[Bypass using octal IP]]
- [[Server-Side Request Forgery]]
