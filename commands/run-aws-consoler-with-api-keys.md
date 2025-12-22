---
id: 9f644b1f-ba7a-4448-8164-f0edfb3ebb44
name: run-aws-consoler-with-api-keys
type: command
executor: bash
data: aws_consoler -v -a $_ACCESS_KEY_ID -s $_SECRET_ACCESS_KEY
output: null
created_at: '2023-04-06T03:56:09.462581+00:00'
updated_at: '2023-04-10T20:20:55.849911+00:00'
platforms:
  - Linux
  - macOS
  - Windows (with Git Bash)
tags:
  - aws
  - console
  - api-keys
verified: true
validated: true
---

# run-aws-consoler-with-api-keys

## Command

```bash
aws_consoler -v -a $_ACCESS_KEY_ID -s $_SECRET_ACCESS_KEY
```

## Description

This command executes the aws_consoler tool to generate a temporary AWS console sign-in URL using provided API credentials. It establishes a Boto3 session, creates a federated token via STS, and outputs a browser-ready login link. Use after cloning and installing the tool.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Enable verbose logging for debugging | No |
| -a $_ACCESS_KEY_ID | AWS Access Key ID (e.g., AKIAIOSFODNN7EXAMPLE) | Yes |
| -s $_SECRET_ACCESS_KEY | AWS Secret Access Key (e.g., wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY) | Yes |

## Examples

### Basic Usage

```bash
aws_consoler -a AKIAIOSFODNN7EXAMPLE -s wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

### Verbose Mode

```bash
aws_consoler -v -a $_ACCESS_KEY_ID -s $_SECRET_ACCESS_KEY
```

## Expected Output

2020-03-13 19:44:57,800 [aws_consoler.cli] INFO: Validating arguments...
2020-03-13 19:44:57,801 [aws_consoler.cli] INFO: Calling logic.
2020-03-13 19:44:57,820 [aws_consoler.logic] INFO: Boto3 session established.
2020-03-13 19:44:58,193 [aws_consoler.logic] WARNING: Creds still permanent, creating federated session.
2020-03-13 19:44:58,698 [aws_consoler.logic] INFO: New federated session established.
2020-03-13 19:44:59,153 [aws_consoler.logic] INFO: Session valid, attempting to federate as arn:aws:sts::123456789012:federated-user/aws_consoler.
2020-03-13 19:44:59,668 [aws_consoler.logic] INFO: URL generated!
https://signin.aws.amazon.com/federation?Action=login&Issuer=consoler.local&Destination=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3Fregion%3Dus-east-1&SigninToken=[TOKEN]

Copy the URL and paste it into a browser to access the AWS console.

## Related

- [[procedures/AWS-Console-Access-via-API-Keys]]
- [[commands/git-clone-aws-consoler]]
