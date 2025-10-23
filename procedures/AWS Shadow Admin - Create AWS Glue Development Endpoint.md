---
id: fbee1ff8-c58a-49e9-8083-81de4cd7d932
name: AWS Shadow Admin - Create AWS Glue Development Endpoint
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.445498+00:00'
updated_at: '2023-04-10T20:20:36.530953+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Internal Spearphishing|T1534 - Internal Spearphishing]]'
tags:
- '[[Admin equivalent permission]]'
- '[[AWS - Shadow Admin]]'
- '[[Cloud - AWS]]'
---

# AWS Shadow Admin - Create AWS Glue Development Endpoint

## Summary

This procedure involves the creation of an AWS Glue Development Endpoint by a shadow admin with admin equivalent permissions. This endpoint can be used to escalate privileges and gain access to sensitive data stored in AWS. AWS Glue is a fully managed ETL (extract, transform, and load) service that

## Description

# Description

This procedure involves the creation of an AWS Glue Development Endpoint by a shadow admin with admin equivalent permissions. This endpoint can be used to escalate privileges and gain access to sensitive data stored in AWS. AWS Glue is a fully managed ETL (extract, transform, and load) service that makes it easy to move data between data stores. By creating a development endpoint, an attacker can run arbitrary code and execute commands on the AWS infrastructure, potentially leading to a full compromise of the environment.

Technical Description: An attacker with admin equivalent permissions can create an AWS Glue Development Endpoint using the 'Create AWS Glue Development Endpoint' command. This endpoint can be used to run arbitrary code and execute commands on the AWS infrastructure. The attacker can then use this access to escalate privileges and gain access to sensitive data stored in AWS.

Business Value: An attacker can gain access to sensitive data stored in AWS using this procedure. This can lead to data theft, financial loss, and damage to the organization's reputation.

 

## Requirements

1. Admin equivalent permissions

 

## Defense

1. Limit the number of users with admin equivalent permissions

1. Monitor for the creation of AWS Glue Development Endpoints

1. Implement least privilege access controls

 

## Objectives

1. Create an AWS Glue Development Endpoint

1. Escalate privileges

1. Gain access to sensitive data stored in AWS

 

# Instructions

1. To create a new AWS Glue Development Endpoint, run the following command in your terminal:

 



**Code**: [[$ aws glue create-dev-endpoint –endpoint-name my_d]]



> This command creates a new development endpoint in AWS Glue. The endpoint name should be unique within your account. The role ARN should be the ARN of an existing IAM role that has the necessary permissions for Glue. The public key file should be a valid public SSH key that can be used to connect to the development endpoint. This command requires the user to have the `iam:PassRole` and `glue:CreateDevEndpoint` permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Internal Spearphishing|T1534 - Internal Spearphishing]]

## Tags

- [[Admin equivalent permission]]
- [[AWS - Shadow Admin]]
- [[Cloud - AWS]]


