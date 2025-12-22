---
id: 6b21917e-9c1c-45b9-9074-1026ff9a3b0d
name: aws-lambda-function-policy-enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.230530+00:00'
updated_at: '2023-04-10T20:20:05.648573+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
  - '[[techniques/Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
  - '[[sub-techniques/Accessibility Features|T1546.008 - Accessibility Features]]'
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Listing policy information about the function]]'
commands:
  - '[[commands/aws-lambda-get-policy]]'
platforms:
  - AWS
tools: []
validated: true
---

# aws-lambda-function-policy-enumeration

## Summary

This procedure retrieves the resource-based policy associated with a specific AWS Lambda function, revealing permissions that allow invocation and other actions. It is useful for discovering misconfigurations in Lambda access controls during cloud enumeration, identifying overly permissive policies that could enable unauthorized invocation or escalation in AWS environments.

## Description

AWS Lambda functions can have resource-based policies that define who or what can invoke them and under what conditions. This procedure uses the AWS CLI to query these policies, providing a JSON output with statements detailing principals (e.g., IAM roles, users), actions (e.g., lambda:InvokeFunction), and conditions. In an attack scenario, this helps map out potential abuse vectors, such as functions invocable by public or low-privilege entities, leading to code execution or data access. It targets AWS environments where the attacker has initial credentials with lambda:GetPolicy permission, and is commonly used in cloud penetration testing to assess persistence or privilege escalation opportunities via event-triggered functions.

## Requirements

1. Valid AWS credentials with at least lambda:GetPolicy permission on the target function.
2. Network access to AWS API endpoints (no VPC restrictions blocking CLI calls).
3. AWS CLI installed and configured with the appropriate profile or access keys.

## Defense

- Implement least privilege access: Restrict lambda:GetPolicy to only necessary roles and monitor its usage via CloudTrail.
- Use AWS Organizations SCPs to deny broad policy enumeration across accounts.
- Enable GuardDuty for Cloud API activity detection and set up alerts for unusual Lambda policy queries.
- Regularly audit Lambda policies with AWS Config rules to identify permissive statements.

## Objectives

1. Retrieve and analyze the policy statements for a Lambda function to identify invocable principals and actions.
2. Detect vulnerabilities like public access or cross-account permissions that could lead to unauthorized execution.
3. Support broader cloud discovery by chaining with other enumeration techniques.
4. Ensure compliance by documenting and mitigating exposed policies.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure your AWS credentials are active and have the required permissions before querying the policy. This prevents authentication errors during execution.

Run the AWS CLI configure list command to check your current profile:

```bash
aws configure list
```

> If not configured, use `aws configure` to set access key, secret key, region (e.g., us-east-1), and output format (json).

**Expected Output**: Profile details including access keys and region.

### Step 2: Retrieve Lambda Function Policy

**Context**: Use the AWS CLI to fetch the policy for the specified Lambda function. This step directly enumerates the permissions, revealing who can invoke the function and any attached conditions.

**Command** ([[commands/aws-lambda-get-policy]]):

```bash
aws lambda get-policy --function-name my-function-name
```

> Replace `my-function-name` with the actual Lambda function name (e.g., from prior enumeration). The command returns a JSON policy document. If no policy exists, it returns a 404 error.

**Expected Output**: JSON response with policy details, such as:

```json
{
  "Policy": {
    "Id": "default",
    "PolicyName": "default",
    "PolicyDocument": {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "root",
          "Action": "lambda:InvokeFunction",
          "Effect": "Allow",
          "Principal": {
            "AWS": "*"
          }
        }
      ]
    }
  },
  "RevisionId": "abc123"
}
```

### Step 3: Analyze Policy Output

**Context**: Parse the JSON output to identify risks, such as wildcard principals ("*" for public access) or broad actions. This manual review helps decide next steps like attempting invocation.

Use jq to filter statements if installed:

```bash
aws lambda get-policy --function-name my-function-name | jq '.Policy.PolicyDocument.Statement[] | select(.Principal.AWS == "*")'
```

> If jq is unavailable, manually inspect the JSON for permissive entries.

**Expected Output**: Filtered statements highlighting risky permissions, e.g., public invocation allowances.

### Step 4: Verify and Document Findings

**Context**: Confirm the policy's implications by cross-referencing with function details (e.g., via `aws lambda get-function`) and note any escalation paths.

No specific command here; document anomalies like cross-account access.

**Expected Output**: Notes on potential attack paths, such as invocable functions for persistence.
