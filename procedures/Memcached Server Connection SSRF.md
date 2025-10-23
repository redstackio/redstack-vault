---
id: 9af58dc1-132f-4a9a-b63d-7163a40198ce
name: Memcached Server Connection SSRF
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.446619+00:00'
updated_at: '2023-04-10T20:23:55.306102+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypass using malformed urls]]'
- '[[Server-Side Request Forgery]]'
---

# Memcached Server Connection SSRF

## Summary

Memcached is a distributed memory object caching system that is often used to speed up websites and web applications. However, if an attacker gains access to a Memcached server, they can use it to launch a Server-Side Request Forgery (SSRF) attack. By sending a specially crafted request to the Memc

## Description

# Description

Memcached is a distributed memory object caching system that is often used to speed up websites and web applications. However, if an attacker gains access to a Memcached server, they can use it to launch a Server-Side Request Forgery (SSRF) attack. By sending a specially crafted request to the Memcached server, the attacker can trick the server into making a request to a target server, effectively bypassing any filters that may be in place. This can allow the attacker to access sensitive information or launch further attacks against the target.

 

## Requirements

1. Access to a Memcached server

1. Knowledge of how to craft a specially crafted request to the Memcached server

 

## Defense

1. Ensure that the Memcached server is properly secured and only accessible to authorized personnel

1. Implement network segmentation to prevent unauthorized access to the Memcached server

1. Regularly monitor the server for any suspicious activity or requests

 

## Objectives

1. Gain access to a Memcached server

1. Use the Memcached server to launch a Server-Side Request Forgery (SSRF) attack

1. Trick the server into making a request to a target server to bypass filters and access sensitive information

 

# Instructions

1. To connect to a Memcached server, use the following command:

$memcached = New-Object MemcachedClient()
$memcached.Connect('localhost', 11211)

Replace 'localhost' with the IP address or hostname of your Memcached server. Replace '11211' with the port number on which your Memcached server is running, if it is different from the default port 11211.

 



**Code**: [[localhost:+11211aaa
localhost:00011211aaaa]]



> This command creates a new MemcachedClient object and connects it to the specified Memcached server. The IP address or hostname and port number of the server are passed as arguments to the Connect() method. Once the connection is established, you can use the various methods and properties of the MemcachedClient object to interact with the Memcached server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[Bypassing filters]]
- [[Bypass using malformed urls]]
- [[Server-Side Request Forgery]]


