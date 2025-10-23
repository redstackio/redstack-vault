---
id: 448b18d5-cbee-4108-9c61-cb58285f0561
name: SSRF for Cloud Instances with Packet Metadata Userdata
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.526367+00:00'
updated_at: '2023-04-10T20:24:04.274390+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Cloud Instances]]'
- '[[SSRF URL for Packetcloud]]'
commands:
- '[[Retrieve User Data]]'
---

# SSRF for Cloud Instances with Packet Metadata Userdata

## Summary

This procedure involves exploiting a Server-Side Request Forgery (SSRF) vulnerability to send a malicious request to a cloud instance's metadata service. Specifically, the SSRF URL is crafted to target the Packetcloud metadata service. This can result in the attacker gaining access to sensitive inf

## Description

# Description

This procedure involves exploiting a Server-Side Request Forgery (SSRF) vulnerability to send a malicious request to a cloud instance's metadata service. Specifically, the SSRF URL is crafted to target the Packetcloud metadata service. This can result in the attacker gaining access to sensitive information about the cloud instance, such as access keys or credentials. The technical details of this attack involve manipulating the URL used to make a request to the metadata service, which can be achieved through a vulnerable application or by manipulating user input. The business value of this attack is significant, as it can result in the compromise of the entire cloud infrastructure and the data stored within it.

 

## Requirements

1. Access to a vulnerable application or ability to manipulate user input

 

## Defense

1. Implement input validation and sanitization to prevent SSRF attacks

1. Use firewalls and access control lists to restrict access to metadata services

1. Monitor network traffic for suspicious activity and investigate any anomalies

 

## Objectives

1. Gain access to sensitive information about the cloud instance

1. Compromise the cloud infrastructure and data stored within it

 

# Instructions

1. To retrieve metadata about your Packet server, make a GET request to the URL provided in the 'data' field. This will return a JSON object containing various details about your server.

 



**Code**: [[https://metadata.packet.net/userdata]]



> The 'data' field contains the URL to retrieve metadata about your Packet server. This metadata includes information such as the server's hostname, IP addresses, and SSH keys. To retrieve this metadata, simply make a GET request to the URL provided in the 'data' field. The response will be a JSON object containing the metadata. This command is useful for automating server configuration and management tasks.



**Command** ([[Retrieve User Data]]):

```bash
https://metadata.packet.net/userdata
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Share Discovery|T1135 - Network Share Discovery]]

## Commands Used

- [[Retrieve User Data]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for Cloud Instances]]
- [[SSRF URL for Packetcloud]]


