---
id: 95594862-d4bc-45b3-af0f-e62318eac0c4
name: Cloud Instance Metadata API
type: sub-technique
mitre_id: T1552.005
mitre_url: null
created_at: '2023-04-06T00:31:25.641199+00:00'
updated_at: '2023-04-06T00:31:25.641199+00:00'
parent_technique: '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Twitter API Key Leak Exploitation]]'
- '[[Twitter API Key Leak Exploitation]]'
- '[[Twitter API Key Leak Exploitation]]'
---

# Cloud Instance Metadata API

**MITRE ID**: T1552.005

**Parent Technique**: [[Unsecured Credentials|T1552 - Unsecured Credentials]]

This is a sub-technique of T1552 - Unsecured Credentials.

## Summary

Adversaries may attempt to access the Cloud Instance Metadata API to collect credentials and other sensitive data.

Most cloud service providers support a Cloud Instance Metadata API which is a service provided to running virtual instances that allows applications to access information about the run

## Description

Adversaries may attempt to access the Cloud Instance Metadata API to collect credentials and other sensitive data.

Most cloud service providers support a Cloud Instance Metadata API which is a service provided to running virtual instances that allows applications to access information about the running virtual instance. Available information generally includes name, security group, and additional metadata including sensitive data such as credentials and UserData scripts that may contain additional secrets. The Instance Metadata API is provided as a convenience to assist in managing applications and is accessible by anyone who can access the instance.(Citation: AWS Instance Metadata API) A cloud metadata API has been used in at least one high profile compromise.(Citation: Krebs Capital One August 2019)

If adversaries have a presence on the running virtual instance, they may query the Instance Metadata API directly to identify credentials that grant access to additional resources. Additionally, adversaries may exploit a Server-Side Request Forgery (SSRF) vulnerability in a public facing web proxy that allows them to gain access to the sensitive information via a request to the Instance Metadata API.(Citation: RedLock Instance Metadata API 2018)

The de facto standard across cloud service providers is to host the Instance Metadata API at <code>http[:]//169.254.169.254</code>.

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 3 procedures using this sub-technique:

- [[Twitter API Key Leak Exploitation]]
- [[Twitter API Key Leak Exploitation]]
- [[Twitter API Key Leak Exploitation]]
