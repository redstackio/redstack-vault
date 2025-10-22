---
id: f4503bd6-ad71-4663-9d24-2cbec7ffde73
name: Credential Harvesting from DynamoDB
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.838415+00:00'
updated_at: '2023-04-10T20:20:03.754126+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]'
- '[[Credentials In Files|T1552.001 - Credentials In Files]]'
tags:
- '[[Cloud - AWS]]'
- '[[DynamoDB]]'
commands:
- '[[Scan DynamoDB table for users]]'
---

# Credential Harvesting from DynamoDB

## Summary

Credential harvesting from DynamoDB involves the extraction of sensitive information such as user credentials from the NoSQL database service provided by AWS. This technique is often used by attackers to gain access to cloud resources and sensitive data. Attackers typically use tools to scan the Dy

## Description

# Description

Credential harvesting from DynamoDB involves the extraction of sensitive information such as user credentials from the NoSQL database service provided by AWS. This technique is often used by attackers to gain access to cloud resources and sensitive data. Attackers typically use tools to scan the DynamoDB database to identify tables with sensitive information and then extract the data using techniques such as credentials from web browsers or password stores. This technique can be used to compromise the confidentiality and integrity of the data stored in DynamoDB.

From a technical standpoint, attackers can use the AWS SDKs or APIs to interact with DynamoDB and retrieve data. Business value of this technique is that it can be used to steal sensitive information such as user credentials, which can then be used to gain access to other cloud resources and data.

## Requirements

1. Access to the DynamoDB database

1. Credentials with appropriate permissions

1. Tools to extract sensitive information

## Defense

1. Use strong authentication mechanisms such as multi-factor authentication to protect credentials

1. Monitor DynamoDB access logs for suspicious activity

1. Encrypt sensitive data stored in DynamoDB to protect against unauthorized access

## Objectives

1. Extract sensitive information such as user credentials from DynamoDB

1. Gain access to other cloud resources and data using the stolen credentials

# Instructions

1. The above command retrieves the user credentials from a DynamoDB table named `users` and uses `jq` to parse the output. The `--endpoint-url` flag specifies the URL of the DynamoDB service endpoint. The `scan` command is used to retrieve all items from the `users` table. The `jq` command is used to extract the `username` and `password` fields from the output.

**Code**: [[$ aws --endpoint-url http://s3.bucket.htb dynamodb]]

> The `aws` command-line interface (CLI) is used to interact with Amazon Web Services (AWS) services. In this case, the `dynamodb` command is used to interact with DynamoDB, a NoSQL database service provided by AWS. The `scan` command is used to retrieve all items from the `users` table. The `--table-name` flag specifies the name of the table to scan. The `jq` command is used to parse the output and extract the `username` and `password` fields. The `--endpoint-url` flag is used to specify the URL of the DynamoDB service endpoint, which in this case is `http://s3.bucket.htb`. The `username` and `password` fields are stored as `S` (string) data types in DynamoDB.

**Command** ([[Scan DynamoDB table for users]]):

```bash
$ aws --endpoint-url http://s3.bucket.htb dynamodb scan --table-name users | jq -r '.Items[]'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]
- [[Credentials In Files|T1552.001 - Credentials In Files]]

## Commands Used

- [[Scan DynamoDB table for users]]

## Tags

- [[Cloud - AWS]]
- [[DynamoDB]]
