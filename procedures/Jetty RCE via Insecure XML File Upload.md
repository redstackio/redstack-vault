---
id: bf1d6127-c7e6-4dd8-b269-bd2f6742f32c
name: Jetty RCE via Insecure XML File Upload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.204353+00:00'
updated_at: '2023-04-10T20:24:34.944345+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
- '[[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]'
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
tags:
- '[[Exploits]]'
- '[[Jetty RCE]]'
- '[[Upload Insecure Files]]'
commands:
- '[[View Jetty Base Webapps Directory]]'
---

# Jetty RCE via Insecure XML File Upload

## Summary

The Jetty RCE via Insecure XML File Upload is an attack that targets the Jetty web server. The attacker uploads a specially crafted XML file that contains a malicious payload. The server processes the file and executes the payload, resulting in remote code execution. This attack can be used to gain

## Description

# Description

The Jetty RCE via Insecure XML File Upload is an attack that targets the Jetty web server. The attacker uploads a specially crafted XML file that contains a malicious payload. The server processes the file and executes the payload, resulting in remote code execution. This attack can be used to gain a foothold in the target network, escalate privileges, and exfiltrate sensitive data.

Technical Explanation: The Jetty web server has a vulnerability that allows arbitrary file uploads. An attacker can use this vulnerability to upload a specially crafted XML file that contains a malicious payload. The server processes the file and executes the payload, resulting in remote code execution. This attack can be used to gain a foothold in the target network, escalate privileges, and exfiltrate sensitive data.

Business Value: This attack can be used to gain access to a target network and exfiltrate sensitive data. It can also be used to escalate privileges and gain access to critical systems, which can result in financial loss and damage to the target's reputation.

 

## Requirements

1. Access to the target's Jetty web server

1. Ability to upload files to the server

 

## Defense

1. Ensure that the Jetty web server is up-to-date and patched against known vulnerabilities

1. Implement strict access controls and authentication mechanisms to prevent unauthorized access to the server

1. Use a web application firewall (WAF) to detect and block malicious file uploads

 

## Objectives

1. Gain access to the target network

1. Escalate privileges

1. Exfiltrate sensitive data

 

# Instructions

1. To upload the XML file, use the following command:

`curl -X POST -H 'Content-Type: application/xml' -d @filename.xml http://localhost:8080/upload`

 



**Code**: [[$JETTY_BASE/webapps/]]



> This command uploads an XML file to the specified location. The `curl` command is used with the `-X` flag to specify the HTTP method as `POST`. The `-H` flag is used to specify the `Content-Type` header as `application/xml`. The `-d` flag is used to specify the data to be uploaded, which in this case is the contents of the `filename.xml` file. The URL specified in the command is the location where the file will be uploaded to, in this case `http://localhost:8080/upload`.



**Command** ([[View Jetty Base Webapps Directory]]):

```bash
$JETTY_BASE/webapps/
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]
- [[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]
- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

## Commands Used

- [[View Jetty Base Webapps Directory]]

## Tags

- [[Exploits]]
- [[Jetty RCE]]
- [[Upload Insecure Files]]


