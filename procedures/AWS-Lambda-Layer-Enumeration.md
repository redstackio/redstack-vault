---
id: 4bb05c04-2b87-430c-92c2-3222efe71cc7
type: procedure
name: AWS-Lambda-Layer-Enumeration
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.276887+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Listing Lambda Layers (Dependencies)]]'
commands:
  - '[[commands/aws-lambda-list-layers]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS-Lambda-Layer-Enumeration

## Summary

AWS Lambda Layer Enumeration is a technique used to identify and list all Lambda Layers in a target AWS account. Lambda Layers are deployment packages that manage shared dependencies across multiple functions, and enumerating them can reveal libraries or dependencies that may contain exploitable vulnerabilities, such as outdated versions or known security flaws.

## Description

In cloud environments, attackers with compromised AWS credentials can enumerate Lambda Layers to map the server's dependencies and identify potential entry points for further exploitation. This procedure uses the AWS CLI to query Lambda Layers, which are essentially ZIP archives containing code and libraries. By listing layers and their versions, an attacker can assess the runtime environment, spot misconfigurations, or download layers for offline analysis to find vulnerabilities like deserialization issues or insecure library usage. This is particularly useful in post-compromise scenarios where initial access has been gained via IAM roles or stolen keys.

## Requirements

1. Valid AWS credentials with at least `lambda:ListLayers`, `lambda:GetLayerVersion`, and `lambda:GetLayerVersionByArn` permissions.
2. AWS CLI installed and configured with the target account's credentials (e.g., via `aws configure` or environment variables).
3. Network access to AWS endpoints (no VPC restrictions blocking CLI calls).

## Defense

Defensive measures and detection strategies:

- Implement least privilege access: Restrict IAM policies to deny `lambda:List*` and `lambda:GetLayerVersion*` actions unless necessary.
- Enable AWS CloudTrail logging for Lambda API calls and monitor for unusual enumeration patterns (e.g., frequent `ListLayers` from unexpected IPs).
- Use AWS Config rules to audit Lambda Layers for outdated dependencies and enforce patching.
- Rotate credentials regularly and monitor for anomalous API activity via Amazon GuardDuty.

## Objectives

1. Identify all Lambda Layers in the target AWS account.
2. Retrieve details on layer versions, including ARNs and compatible runtimes.
3. Analyze layers for dependencies and potential vulnerabilities in libraries.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is set up with credentials that have the necessary permissions to query Lambda services. This prevents authentication errors during enumeration.

**Command** ([[commands/aws-lambda-list-layers]]):
```bash
aws sts get-caller-identity
```

> This command verifies your current identity and permissions. If it fails with an access denied error, update your IAM policy to include Lambda read permissions.

### Step 2: List All Lambda Layers

**Context**: Query the AWS Lambda service to retrieve a list of all layers in the account, including their latest versions and compatible runtimes. This provides an overview of shared dependencies across functions.

**Command** ([[commands/aws-lambda-list-layers]]):
```bash
aws lambda list-layers
```

> The command returns a JSON array of layers. Each entry includes LayerName, LayerArn, and LatestMatchingVersion. Review for layers with names indicating sensitive libraries (e.g., those using vulnerable versions of Log4j).

### Step 3: Retrieve Detailed Layer Version Information

**Context**: For each discovered layer, fetch specific version details to obtain download URLs or metadata. This allows deeper inspection of contents without downloading immediately.

**Command** ([[commands/aws-lambda-list-layers]]):
```bash
aws lambda get-layer-version --layer-name $_LAYER_NAME --version-number $_VERSION_NUMBER
```

> Replace $_LAYER_NAME and $_VERSION_NUMBER with values from Step 2. Expected output includes Content.Location (S3 URL for download) and CompatibleRuntimes. Use this to identify runtime-specific vulnerabilities.

### Step 4: Download and Analyze Layer Content (Optional)

**Context**: If a layer appears vulnerable, download its ZIP content for offline analysis using tools like unzip or dependency scanners to check for known CVEs.

**Instructions**: Use the Content.Location URL from Step 3 with curl or wget to download the layer ZIP. Then, extract and scan:
```bash
curl -o layer.zip $_CONTENT_LOCATION
unzip layer.zip -d layer_contents
```

> Scan extracted files with tools like `pip-audit` for Python dependencies or `npm audit` for Node.js. Look for outdated packages that could lead to RCE or data exposure.

### Step 5: Document and Validate Findings

**Context**: Compile the enumerated data and cross-reference with vulnerability databases to confirm exploitable weaknesses.

**Instructions**: Save outputs to files (e.g., `aws lambda list-layers > layers.json`) and use jq for parsing:
```bash
aws lambda list-layers | jq '.Layers[].LayerName'
```

> This extracts layer names for quick review. Success is confirmed if layers are listed without permission errors and analysis reveals potential issues.
