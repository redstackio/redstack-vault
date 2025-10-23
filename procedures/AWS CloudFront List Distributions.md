---
id: d8a07911-d9f8-4100-9181-cb160da767d6
name: AWS CloudFront List Distributions
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:16.157383+00:00'
updated_at: '2023-05-25T20:07:17.295732+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Network Connections Discovery|T1049 - System Network Connections Discovery]]'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws cloudfront list distributions]]'
- '[[aws configure cloudfront preview]]'
---

# AWS CloudFront List Distributions

**Status**: ✓ Verified

## Summary

Listing all of the cloudfront distributions can identify the external endpoints, domains and sub-domains And the internal assets they point to, like S3 Buckets, EKS containers, and more. 

## Description

# Description

Listing all of the cloudfront distributions can identify the external endpoints, domains and sub-domains

And the internal assets they point to, like S3 Buckets, EKS containers, and more.

##  Instructions

1. (Optional) Configure cloudfront preview to true



**Command** ([[aws configure cloudfront preview]]):

```bash
aws configure set preview.cloudfront true

```





2. List the disributions



**Command** ([[aws cloudfront list distributions]]):

```bash
aws cloudfront list-distributions

```





## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Network Connections Discovery|T1049 - System Network Connections Discovery]]

## Commands Used

- [[aws cloudfront list distributions]]
- [[aws configure cloudfront preview]]

## Tags

- [[AWS]]
- [[Cloud]]


