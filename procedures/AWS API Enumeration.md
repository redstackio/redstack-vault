---
id: "5c4deba9-6179-4a73-87de-b37f580269cb"
name: "AWS API Enumeration"
type: procedure
verified: false
submitted: false
created_at: "2023-04-06T03:56:11.348603+00:00"
updated_at: "2023-04-10T20:20:51.266590+00:00"
tactics: ["[[Lateral Movement|TA0008 - Lateral Movement]]"]
techniques: ["[[Application Deployment Software|T1017 - Application Deployment Software]]"]
sub_techniques: []
tags: ["[[Cloud - AWS]]","[[Enumeration]]","[[Listing information about a specific API]]"]
commands: ["[[Get API Gateway REST API ID]]"]
platforms: []
tools: ["[[AWS CLI]]"]
---

# AWS API Enumeration

## Summary

The AWS API Enumeration procedure involves using the AWS CLI to retrieve detailed information about a specific REST API in Amazon API Gateway, enabling attackers or security professionals to gain insights into the target environment. This can help identify potential vulnerabilities, misconfigurations, or deployment details that could be exploited for further lateral movement or reconnaissance.

## Description

The AWS API Enumeration procedure focuses on querying Amazon API Gateway to list information about a specific REST API, providing a deeper understanding of the cloud infrastructure. In an attack scenario, this could be used by adversaries to map out API endpoints, stages, and resources within a compromised AWS account, potentially leading to exploitation of misconfigured APIs for lateral movement. The target environment is typically an AWS account with API Gateway services deployed. The technical approach involves executing AWS CLI commands to fetch API details such as name, description, endpoint configuration, and more. Prerequisites include valid AWS credentials and knowledge of the REST API ID. Expected outcomes include a JSON response containing comprehensive API metadata, which can inform subsequent attack steps or security assessments. From a business perspective, this procedure aids organizations in identifying and mitigating security risks in their AWS API deployments.

## Requirements

1. Valid AWS credentials
2. Access to the target API
3. AWS CLI installed and configured

## Defense

Defensive measures and detection strategies:

- Ensure that AWS credentials are properly secured and not shared
- Implement strong access controls to limit access to the target API
- Monitor AWS CloudTrail logs for any suspicious activity related to the target API

## Objectives

1. Identify potential vulnerabilities or misconfigurations in the target environment
2. Gain a better understanding of the target environment
3. Remediate potential security risks in the AWS environment

## Instructions

### Step 1: Retrieve REST API Details

**Context**: This step retrieves detailed information about a specific REST API in Amazon API Gateway, including its ID, name, description, endpoint configuration, and more, to enumerate the environment.

**Command** ([[Get API Gateway REST API ID]]):
```bash
aws apigateway get-rest-api --rest-api-id ID
```

> Explanation of the command and expected output: The `aws apigateway get-rest-api` command fetches details for the specified REST API ID. Replace `ID` with the actual API ID. The output is a JSON object containing API metadata, which can be used for further analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Deployment Software|T1017 - Application Deployment Software]]

### Sub-Techniques

- [[Sub-Technique Name]]

## Commands Used

- [[Get API Gateway REST API ID]]

## Tools Used

- [[AWS CLI]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing information about a specific API]]