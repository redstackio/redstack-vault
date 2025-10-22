---
id: b1893f72-b12e-4cc2-b030-7bac4182c1a1
name: Cloud Instance SSRF through OpenStack Metadata URL
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.622498+00:00'
updated_at: '2023-04-10T20:23:59.109216+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
- '[[External Remote Services|T1133 - External Remote Services]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Cloud Instances]]'
- '[[SSRF URL for OpenStack/RackSpace]]'
commands:
- '[[Access metadata API]]'
---

# Cloud Instance SSRF through OpenStack Metadata URL

## Summary

Cloud Instance SSRF through OpenStack Metadata URL is a technique used by attackers to gain access to sensitive information or resources on a cloud instance. This technique involves sending a specially crafted request to the OpenStack metadata URL, which is used by cloud instances to retrieve infor

## Description

# Description

Cloud Instance SSRF through OpenStack Metadata URL is a technique used by attackers to gain access to sensitive information or resources on a cloud instance. This technique involves sending a specially crafted request to the OpenStack metadata URL, which is used by cloud instances to retrieve information about themselves. By exploiting this vulnerability, an attacker can steal sensitive data, such as authentication credentials or other metadata, and use it to gain access to other resources on the cloud instance or in the cloud environment. This technique can be used to further compromise the cloud environment or to exfiltrate sensitive data.

Technical Explanation: This technique involves sending a specially crafted request to the OpenStack metadata URL, which is used by cloud instances to retrieve information about themselves. The request is crafted in such a way that it causes the cloud instance to make a request to a URL specified by the attacker. By doing so, the attacker can gain access to sensitive information or resources on the cloud instance.

Business Value: This technique can be used by attackers to gain access to sensitive data, such as authentication credentials or other metadata, and use it to gain access to other resources on the cloud instance or in the cloud environment. This can lead to a complete compromise of the cloud environment, resulting in loss of data, resources, and reputation.

## Requirements

1. Access to an OpenStack metadata URL

1. Knowledge of the cloud environment

## Defense

1. Ensure that the OpenStack metadata URL is not accessible from untrusted networks

1. Implement access controls and authentication mechanisms to restrict access to the OpenStack metadata URL

1. Monitor network traffic for suspicious activity, such as requests to the OpenStack metadata URL

## Objectives

1. Gain access to sensitive information on a cloud instance

1. Steal authentication credentials or other metadata

1. Use stolen data to gain access to other resources on the cloud instance or in the cloud environment

1. Exfiltrate sensitive data

# Instructions

1. To access OpenStack metadata, use the provided URL: http://169.254.169.254/openstack

**Code**: [[http://169.254.169.254/openstack]]

> This URL is used to access metadata information about the OpenStack instance. It can be used to retrieve information such as the instance ID, IP address, and security groups. It is important to note that this URL can only be accessed from within the OpenStack instance and requires authentication headers to be included in the request.

**Command** ([[Access metadata API]]):

```bash
http://169.254.169.254/openstack
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]
- [[External Remote Services|T1133 - External Remote Services]]

## Commands Used

- [[Access metadata API]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for Cloud Instances]]
- [[SSRF URL for OpenStack/RackSpace]]
