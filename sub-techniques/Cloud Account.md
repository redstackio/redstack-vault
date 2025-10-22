---
id: d216d302-0179-48b8-b29e-394fbaa9da86
name: Cloud Account
type: sub-technique
mitre_id: T1136.003
mitre_url: null
created_at: '2023-04-06T00:31:26.645454+00:00'
updated_at: '2023-04-06T00:31:26.645454+00:00'
parent_technique: '[[Create Account|T1136 - Create Account]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Cloud Account

**MITRE ID**: T1136.003

**Parent Technique**: [[Create Account|T1136 - Create Account]]

This is a sub-technique of T1136 - Create Account.

## Summary

Adversaries may create a cloud account to maintain access to victim systems. With a sufficient level of access, such accounts may be used to establish secondary credentialed access that does not require persistent remote access tools to be deployed on the system.(Citation: Microsoft O365 Admin Roles

## Description

Adversaries may create a cloud account to maintain access to victim systems. With a sufficient level of access, such accounts may be used to establish secondary credentialed access that does not require persistent remote access tools to be deployed on the system.(Citation: Microsoft O365 Admin Roles)(Citation: Microsoft Support O365 Add Another Admin, October 2019)(Citation: AWS Create IAM User)(Citation: GCP Create Cloud Identity Users)(Citation: Microsoft Azure AD Users)

Adversaries may create accounts that only have access to specific cloud services, which can reduce the chance of detection.

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
