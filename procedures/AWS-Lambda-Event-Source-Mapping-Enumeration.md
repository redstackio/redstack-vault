---
id: 12188406-134b-48ae-b473-89d2d122ac68
name: AWS-Lambda-Event-Source-Mapping-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.256023+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud-Service-Dashboard|T1538 - Cloud Service Dashboard]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - aws-lambda
  - event-source-mapping
  - cloud-discovery
commands:
  - '[[commands/aws-lambda-list-event-source-mappings]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# AWS-Lambda-Event-Source-Mapping-Enumeration

## Summary

This procedure enumerates the event source mappings for a specific AWS Lambda function using the AWS CLI, revealing details about triggers such as S3 buckets, SQS queues, or other event sources. This information helps attackers identify dependencies and potential entry points for further exploitation, such as uploading malicious files to trigger functions.

## Description

AWS Lambda event source mappings define how events from sources like S3 object creations or SQS messages invoke Lambda functions. By listing these mappings, an attacker with compromised AWS credentials can discover the ecosystem around a Lambda function, including ARNs of linked resources. This discovery aids in mapping the cloud infrastructure for targeted attacks, such as injecting payloads into event sources to achieve code execution or data exfiltration. The procedure assumes access to the AWS API via CLI and focuses on the `list-event-source-mappings` operation, which returns JSON data including UUID, event source ARN, function ARN, state, and batch size configurations. Use this in scenarios where initial credential access has been gained, and the goal is to expand reconnaissance within the AWS environment.

## Requirements

1. AWS CLI installed and configured with credentials that have `lambda:ListEventSourceMappings` permission (typically via IAM role or access keys).
2. Valid AWS account access with read permissions on Lambda resources.
3. Network connectivity to AWS endpoints (no VPC restrictions blocking API calls).
4. Knowledge of at least one Lambda function name in the target account or region.

## Defense

Defensive measures and detection strategies:

- Implement least privilege IAM policies, restricting `lambda:ListEventSourceMappings` to only necessary roles.
- Enable AWS CloudTrail logging for Lambda API calls and monitor for unusual `ListEventSourceMappings` invocations from unexpected IPs or users.
- Use AWS Config rules to alert on excessive discovery API usage and integrate with SIEM for anomaly detection.
- Rotate credentials regularly and enforce MFA for IAM users with cloud access.

## Objectives

1. Retrieve a list of event source mappings for a specified Lambda function to identify linked resources like S3 buckets or queues.
2. Analyze the output to uncover potential attack vectors, such as modifiable event sources.
3. Map dependencies for planning subsequent exploits, like triggering functions with malicious events.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is set up with the correct profile and region to avoid authentication errors. This step confirms access before querying Lambda resources.

Run the following to check configuration:

```bash
aws configure list
```

> This command displays current settings. If needed, set the region (e.g., us-east-1) using `aws configure set region us-east-1`. Expected output includes profile name, access key status, and default region.

### Step 2: List Event Source Mappings

**Context**: Execute the core command to fetch mappings for the target Lambda function. Replace the function name with the actual identifier to retrieve details on triggers.

**Command** ([[commands/aws-lambda-list-event-source-mappings]]):

```bash
aws lambda list-event-source-mappings --function-name $_FUNCTION_NAME
```

> This retrieves JSON output listing mappings. The `--function-name` parameter specifies the Lambda function. If no mappings exist, an empty list is returned. Review the output for ARNs and states to identify active triggers.

### Step 3: Parse and Analyze Output

**Context**: Examine the JSON response to extract actionable intelligence, such as event source types and URIs, which can guide further reconnaissance or exploitation.

Use `jq` or manual inspection:

```bash
aws lambda list-event-source-mappings --function-name $_FUNCTION_NAME | jq '.EventSourceMappings[] | {UUID: .UUID, EventSourceArn: .EventSourceArn, State: .State}'
```

> Expected output is filtered JSON showing key fields. Look for SQS or S3 ARNs to target those services next. If the state is 'Enabled', the mapping is active and exploitable.
