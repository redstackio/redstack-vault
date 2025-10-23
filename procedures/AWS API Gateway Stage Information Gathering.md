---
id: 4a39aad6-3916-496b-9e1e-e4ec9cae3ebf
name: AWS API Gateway Stage Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.464870+00:00'
updated_at: '2023-04-10T20:21:02.696112+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Getting information about a specific version]]'
commands:
- '[[Get API Gateway Stage]]'
---

# AWS API Gateway Stage Information Gathering

## Summary

The AWS API Gateway Stage Information Gathering procedure is used to obtain information about a specific version of an API Gateway in AWS. The API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. By obtaining i

## Description

# Description

The AWS API Gateway Stage Information Gathering procedure is used to obtain information about a specific version of an API Gateway in AWS. The API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. By obtaining information about a specific version of an API Gateway, an attacker can gain insights into the API's functionality, configuration, and potential vulnerabilities. This information can be used to plan further attacks against the API or other components of the AWS environment.

Technical Description: The procedure involves using the 'Get API Gateway Stage' command to obtain information about a specific version of an API Gateway. The command requires authentication credentials and access to the AWS environment. Once authenticated, the command can be used to obtain information such as the stage name, deployment ID, and the associated API. This information can be used to gain insights into the API's functionality and configuration.

Business Value: By obtaining information about a specific version of an API Gateway, an attacker can gain valuable insights into the API's functionality and configuration. This information can be used to plan further attacks against the API or other components of the AWS environment, potentially leading to data theft, system compromise, or financial loss.

 

## Requirements

1. Valid authentication credentials for the AWS environment

1. Access to the AWS environment

1. Use of the 'Get API Gateway Stage' command

 

## Defense

1. Ensure that authentication credentials are kept secure and not shared with unauthorized individuals

1. Ensure that access to the AWS environment is restricted to authorized individuals only

1. Implement monitoring and logging solutions to detect and respond to any unauthorized access or activity in the AWS environment

 

## Objectives

1. Obtain information about a specific version of an API Gateway in AWS

1. Gain insights into the API's functionality and configuration

1. Plan further attacks against the API or other components of the AWS environment

 

# Instructions

1. To get information about a specific stage in an API Gateway, use the following command:

 

The 'aws apigateway get-stage' command is used to retrieve information about a specific stage in an API Gateway. The 'res-api-id' parameter specifies the ID of the REST API that the stage belongs to, and the 'stage-name' parameter specifies the name of the stage to retrieve information about. This command can be useful for retrieving information such as the deployment ID, description, and created date of a stage. 



**Command** ([[Get API Gateway Stage]]):

```bash
aws apigateway get-stage --res-api-id ID --stage-name NAME
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get API Gateway Stage]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Getting information about a specific version]]


