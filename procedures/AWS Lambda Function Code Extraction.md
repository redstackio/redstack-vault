---
id: 831d0f25-f41d-4cf9-801c-53962e04e073
name: AWS Lambda Function Code Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.670742+00:00'
updated_at: '2023-04-10T20:19:52.646957+00:00'
tags:
- '[[AWS - Lambda - Extract function''s code]]'
- '[[Cloud - AWS]]'
commands:
- '[[Download AWS Lambda Function Code]]'
- '[[Download AWS Lambda Function Code]]'
- '[[Get AWS Lambda Function Code Location]]'
---

# AWS Lambda Function Code Extraction

## Summary

AWS Lambda Function Code Extraction is a technique used by attackers to extract the code of an AWS Lambda function. AWS Lambda is a serverless computing service provided by Amazon Web Services. This technique can be used to gain access to sensitive information, such as API keys, database credential

## Description

# Description

AWS Lambda Function Code Extraction is a technique used by attackers to extract the code of an AWS Lambda function. AWS Lambda is a serverless computing service provided by Amazon Web Services. This technique can be used to gain access to sensitive information, such as API keys, database credentials, or other secrets that may be stored in the code of the function. Attackers can then use this information to further compromise the target environment.

To extract the code of an AWS Lambda function, an attacker can use the AWS Lambda Function Code Download command. This command allows the attacker to download the code of the function in a zip file. The attacker can then extract the code and search for sensitive information.

The business value of this technique is that it allows attackers to gain access to sensitive information stored in AWS Lambda functions. This information can be used to further compromise the target environment, leading to potential data breaches and financial losses.

## Requirements

1. Valid AWS credentials

1. Access to the AWS Lambda service

## Defense

1. Restrict access to AWS credentials and AWS services to authorized personnel only

1. Monitor AWS Lambda function downloads for suspicious activity

1. Encrypt sensitive information stored in AWS Lambda functions

## Objectives

1. Extract the code of an AWS Lambda function

1. Search for sensitive information in the code of the function

# Instructions

1. To download the code of an AWS Lambda function, follow the below steps:

**Code**: [[# https://blog.appsecco.com/getting-shell-and-data]]

> 1. Use the command `aws lambda list-functions --profile uploadcreds` to list all the available AWS Lambda functions.
2. Use the command `aws lambda get-function --function-name "LAMBDA-NAME-HERE-FROM-PREVIOUS-QUERY" --query 'Code.Location' --profile uploadcreds` to get the location of the code of the desired Lambda function.
3. Use the `wget` command to download the code to a file with the `.zip` extension. Replace `url-from-previous-query` with the URL obtained from the previous command. The final command should look like `wget -O lambda-function.zip url-from-previous-query --profile uploadcreds`.

**Command** ([[Download AWS Lambda Function Code]]):

```bash
$ aws lambda list-functions --profile uploadcreds
```

**Command** ([[Get AWS Lambda Function Code Location]]):

```bash
$ aws lambda get-function --function-name "LAMBDA-NAME-HERE-FROM-PREVIOUS-QUERY" --query 'Code.Location' --profile uploadcreds
```

**Command** ([[Download AWS Lambda Function Code]]):

```bash
$ wget -O lambda-function.zip url-from-previous-query --profile uploadcreds
```

## Commands Used

- [[Download AWS Lambda Function Code]]
- [[Download AWS Lambda Function Code]]
- [[Get AWS Lambda Function Code Location]]

## Tags

- [[AWS - Lambda - Extract function's code]]
- [[Cloud - AWS]]
