---
id: 0d258a41-c75a-4be9-a98f-b5a9ef1e7245
name: SSRF Filter Bypass using IP Address Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.538270+00:00'
updated_at: '2023-04-10T20:24:11.623813+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypass using tricks combination]]'
- '[[Server-Side Request Forgery]]'
---

# SSRF Filter Bypass using IP Address Retrieval

## Summary

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to send crafted requests from the server to other internal or external systems. An attacker can use this vulnerability to bypass filters and gain access to sensitive information or systems. In this procedure, we will focu

## Description

# Description

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to send crafted requests from the server to other internal or external systems. An attacker can use this vulnerability to bypass filters and gain access to sensitive information or systems. In this procedure, we will focus on bypassing filters using a combination of tricks and IP address retrieval. This technique can be used to bypass filters that are blocking certain domains or IP addresses.

To exploit this vulnerability, the attacker sends a request to the server with a specially crafted URL that includes the target domain or IP address. The server then sends a request to the target system and returns the response to the attacker. By using IP address retrieval, the attacker can bypass filters that are blocking certain domains or IP addresses. This technique is particularly useful when the attacker does not have direct access to the target system.

The business value of this procedure is that it allows an attacker to bypass filters and gain access to sensitive information or systems. This can result in data theft, system compromise, and financial loss.

## Requirements

1. Access to a vulnerable server

1. Ability to craft a specially crafted URL

1. Knowledge of IP address retrieval techniques

## Defense

1. Implement input validation to prevent crafted URLs from reaching the server

1. Implement network segmentation to limit access to sensitive systems

1. Use a web application firewall (WAF) to detect and block SSRF attacks

## Objectives

1. Bypass filters that are blocking certain domains or IP addresses

1. Gain access to sensitive information or systems

# Instructions

1. To retrieve the IP address of a website, use one of the following commands based on your preference:
1. urllib2: This command retrieves the IP address using urllib2 library in Python.
2. requests + browsers: This command retrieves the IP address using requests library and browsers in Python.
3. urllib: This command retrieves the IP address using urllib library in Python.

**Code**: [[http://1.1.1.1 &@2.2.2.2# @3.3.3.3/
urllib2 : 1.1.]]

> Arguments:
- URL: The URL for which you want to retrieve the IP address.

Example Usage:
urllib2:
import socket
import urllib2
url = 'http://www.example.com'
ip = socket.gethostbyname(urlparse.urlparse(url).hostname)
print ip

requests + browsers:
import socket
import requests
url = 'http://www.example.com'
ip = socket.gethostbyname(urlparse.urlparse(url).hostname)
print ip

urllib:
import socket
import urllib
url = 'http://www.example.com'
ip = socket.gethostbyname(urlparse.urlparse(url).hostname)
print ip

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Tags

- [[Bypassing filters]]
- [[Bypass using tricks combination]]
- [[Server-Side Request Forgery]]
