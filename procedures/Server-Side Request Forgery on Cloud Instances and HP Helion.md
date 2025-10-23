---
id: d40ac8ac-aad8-4511-9c82-f4b539108c2e
name: Server-Side Request Forgery on Cloud Instances and HP Helion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.649342+00:00'
updated_at: '2023-04-10T20:24:08.513718+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Cloud Instances]]'
- '[[SSRF URL for HP Helion]]'
commands:
- '[[Retrieve metadata]]'
---

# Server-Side Request Forgery on Cloud Instances and HP Helion

## Summary

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to send crafted requests from the server-side. In this case, the attacker is targeting cloud instances and HP Helion to gain access to sensitive data or perform unauthorized actions. The attacker can exploit this vulnerab

## Description

# Description

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to send crafted requests from the server-side. In this case, the attacker is targeting cloud instances and HP Helion to gain access to sensitive data or perform unauthorized actions. The attacker can exploit this vulnerability by sending a crafted request to the target server, which in turn will send a request to a third-party server specified by the attacker. The response from the third-party server will be sent back to the attacker, allowing them to access information or perform actions that they should not be able to. This can include accessing metadata, credentials, or other sensitive information.

Technical Explanation: The attacker sends a crafted request to the server, which in turn sends a request to a third-party server specified by the attacker. The response from the third-party server is sent back to the attacker, allowing them to access information or perform actions that they should not be able to.

Business Value: An attacker can gain access to sensitive data, credentials, or other information that can be used for further attacks or sold on the black market.

 

## Requirements

1. Access to the target server

1. Knowledge of a vulnerability that can be exploited

 

## Defense

1. Implement input validation on server-side requests to prevent crafted requests from being sent

1. Use a Web Application Firewall (WAF) to block requests that match known SSRF patterns

1. Restrict access to sensitive data and credentials to only authorized users and applications

 

## Objectives

1. Gain access to sensitive data or credentials

1. Perform unauthorized actions

 

# Instructions

1. To retrieve metadata about an EC2 instance, use the above URL and append the desired metadata category and specific data item to the end of the URL. For example, to retrieve the instance ID, use the URL http://169.254.169.254/2009-04-04/meta-data/instance-id

 



**Code**: [[http://169.254.169.254/2009-04-04/meta-data/]]



> The EC2 instance metadata provides information about the instance such as its ID, hostname, public and private IP addresses, and more. The metadata is available to any application running on the instance and can be accessed using the above URL. Some metadata categories include ami-id, instance-type, and security-groups. To retrieve a specific data item, append it to the end of the URL separated by forward slashes. It is important to note that the metadata is only available from within the instance and cannot be accessed from outside the instance.



**Command** ([[Retrieve metadata]]):

```bash
http://169.254.169.254/2009-04-04/meta-data/
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]

## Commands Used

- [[Retrieve metadata]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for Cloud Instances]]
- [[SSRF URL for HP Helion]]


