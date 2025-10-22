---
id: 901f52e9-5d9a-4dc8-8485-7129353f7147
name: AWS Lambda Function Invocation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.960443+00:00'
updated_at: '2023-04-10T20:20:51.960804+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Execution through API|T1106 - Execution through API]]'
tags:
- '[[Cloud - AWS]]'
- '[[Invoke the Function]]'
- '[[Persistence]]'
commands:
- '[[Send Curl Request]]'
---

# AWS Lambda Function Invocation

## Summary

AWS Lambda is a serverless computing service that allows you to run code without provisioning or managing servers. This procedure explains how to invoke an AWS Lambda function using the AWS API. This can be useful for persistence, as attackers can maintain a foothold in the target environment by in

## Description

# Description

AWS Lambda is a serverless computing service that allows you to run code without provisioning or managing servers. This procedure explains how to invoke an AWS Lambda function using the AWS API. This can be useful for persistence, as attackers can maintain a foothold in the target environment by invoking the function periodically. Technical details of this procedure include authenticating with AWS API credentials, identifying the target Lambda function, and invoking the function with the desired payload. The business value of this procedure is that it allows attackers to maintain a persistent presence in the target environment without the need for a physical server or VM.

## Requirements

1. Valid AWS API credentials

1. Access to the target Lambda function

## Defense

1. Monitor AWS API logs for suspicious activity

1. Restrict access to AWS API credentials

1. Implement least privilege access control for AWS Lambda functions

## Objectives

1. Invoke an AWS Lambda function using the AWS API

1. Maintain persistence in the target environment

# Instructions

1. To invoke the Example API, use the following command:

This command will send an HTTP request to the specified API endpoint and return the response. The 'curl' command is a tool to transfer data from or to a server, using one of the supported protocols (HTTP, HTTPS, FTP, FTPS, SCP, SFTP, TFTP, DICT, TELNET, LDAP or FILE). In this case, we are using it to send an HTTP GET request to the Example API endpoint. The response will contain the data returned by the API in JSON format.

**Command** ([[Send Curl Request]]):

```bash
curl https://uj3948ie.execute-api.us-east-2.amazonaws.com/default/EXAMPLE
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Execution through API|T1106 - Execution through API]]

## Commands Used

- [[Send Curl Request]]

## Tags

- [[Cloud - AWS]]
- [[Invoke the Function]]
- [[Persistence]]
