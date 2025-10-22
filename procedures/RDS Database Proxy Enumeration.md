---
id: b310c5d2-3a71-405e-b7ba-ced1a12d5fb5
name: RDS Database Proxy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.943596+00:00'
updated_at: '2023-04-10T20:20:39.979275+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Enumeration]]'
- '[[Listing information about database proxies]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[Retrieve information about all RDS database proxies]]'
---

# RDS Database Proxy Enumeration

## Summary

The RDS Database Proxy Enumeration procedure involves listing information about database proxies in order to gain a better understanding of the target environment. This procedure can be used offensively to identify potential targets for further attacks, and defensively to monitor for any unauthoriz

## Description

# Description

The RDS Database Proxy Enumeration procedure involves listing information about database proxies in order to gain a better understanding of the target environment. This procedure can be used offensively to identify potential targets for further attacks, and defensively to monitor for any unauthorized access to database proxies.

The RDS Database Proxy Description command is used to retrieve information about a specific database proxy. This includes the proxy's name, status, endpoint, engine family, and VPC security group. By enumerating the database proxies in a target environment, an attacker can identify potential targets for further attacks, such as brute-forcing login credentials or exploiting vulnerabilities in the database engine.

From a defensive perspective, monitoring for unauthorized access to database proxies can help detect and prevent potential attacks before they can cause damage.

## Requirements

1. Valid AWS credentials with permissions to access RDS resources

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Implement network security controls such as firewalls and network segmentation to limit access to database proxies

1. Regularly monitor access logs for suspicious activity and investigate any anomalies

## Objectives

1. Identify potential targets for further attacks

1. Monitor for unauthorized access to database proxies

# Instructions

1. This command is used to describe the details of one or more database proxies in your AWS account.

The 'describe-db-proxies' command provides information about the specified database proxies including the proxy endpoint, engine family, VPC security groups, and the database instances that the proxy connects to. This command takes no arguments and returns a JSON object with details about the specified database proxies. If no database proxy is specified, then details for all proxies in the account are returned.

**Command** ([[Retrieve information about all RDS database proxies]]):

```bash
aws rds describe-db-proxies
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Retrieve information about all RDS database proxies]]

## Tags

- [[Enumeration]]
- [[Listing information about database proxies]]
- [[RDS - Relational Database Service]]
