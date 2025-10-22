---
id: 78d0d9dc-6454-4c34-b17b-9fae700d7a65
name: AWS Metadata SSRF Protection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.208841+00:00'
updated_at: '2023-04-10T20:19:51.003851+00:00'
tags:
- '[[AWS - Metadata SSRF]]'
- '[[Cloud - AWS]]'
commands:
- '[[Enable HTTP endpoint and require token for EC2 instance metadata options]]'
---

# AWS Metadata SSRF Protection

## Summary

AWS Metadata SSRF Protection is a procedure that helps protect against Server Side Request Forgery (SSRF) attacks that exploit the AWS instance metadata service. SSRF attacks can be used to escalate privileges and gain unauthorized access to sensitive information. This procedure helps prevent such 

## Description

# Description

AWS Metadata SSRF Protection is a procedure that helps protect against Server Side Request Forgery (SSRF) attacks that exploit the AWS instance metadata service. SSRF attacks can be used to escalate privileges and gain unauthorized access to sensitive information. This procedure helps prevent such attacks by enabling Instance Metadata Service Version 2 and generating and using IMDSv2 tokens. By doing so, the procedure ensures that only authorized requests are made to the metadata service, and that the service is protected from unauthorized access.

## Requirements

1. AWS account with permissions to modify instance metadata service settings

1. Access to the AWS Management Console or AWS CLI

1. Knowledge of AWS instance metadata service and IMDSv2 tokens

## Defense

1. Limit network access to the metadata service by using network access control lists (ACLs) or security groups

1. Implement strong authentication mechanisms to prevent unauthorized access to the metadata service

1. Monitor the metadata service logs for suspicious activity and unauthorized access attempts

## Objectives

1. Protect against Server Side Request Forgery (SSRF) attacks that exploit the AWS instance metadata service

1. Ensure that only authorized requests are made to the metadata service

1. Protect the service from unauthorized access

# Instructions

1. This command enables the use of Instance Metadata Service Version 2 (IMDSv2) on an EC2 instance. IMDSv2 provides enhanced security features compared to IMDSv1, such as mutual TLS authentication and session authentication. To use this command, replace <INSTANCE-ID> with the ID of the instance you want to modify and <AWS_PROFILE> with the name of the AWS CLI profile you want to use.

**Code**: [[aws ec2 modify-instance-metadata-options --instanc]]

> The `aws ec2 modify-instance-metadata-options` command modifies the metadata options for an EC2 instance. The `--http-endpoint` option enables or disables the use of a custom HTTP endpoint for metadata requests. The `--http-token` option requires or disables the use of a session token for metadata requests. By setting both options to `enabled` and `required` respectively, this command enables the use of IMDSv2 on the specified instance. Note that this command only works with IMDSv1, hence the warning message in the `text` field.

**Command** ([[Enable HTTP endpoint and require token for EC2 instance metadata options]]):

```bash
aws ec2 modify-instance-metadata-options --instance-id <INSTANCE-ID> --profile <AWS_PROFILE> --http-endpoint enabled --http-token required
```

2. To generate and use IMDSv2 token, follow these steps:
1. Run the command 'curl -X PUT -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" "http://169.254.169.254/latest/api/token"' to generate a token.
2. Copy the generated token.
3. Run the command 'curl -H "X-aws-ec2-metadata-token:<generated_token>" -v "http://169.254.169.254/latest/meta-data"' to use the generated token.

**Code**: [[export TOKEN=`curl -X PUT -H "X-aws-ec2-metadata-t]]

> The 'curl' command is used to transfer data to or from a server using one of the supported protocols. In this case, it is used to generate and use an IMDSv2 token. The 'export' command is used to set the value of the 'TOKEN' environment variable to the output of the 'curl' command. The '-X' option is used to specify the HTTP request method as 'PUT'. The '-H' option is used to specify the HTTP request headers. The 'X-aws-ec2-metadata-token-ttl-seconds' header specifies the time-to-live for the token. The '-v' option is used to enable verbose output.

## Commands Used

- [[Enable HTTP endpoint and require token for EC2 instance metadata options]]

## Tags

- [[AWS - Metadata SSRF]]
- [[Cloud - AWS]]
