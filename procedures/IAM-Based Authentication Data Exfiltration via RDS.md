---
id: 3bf18aca-8f10-4e1f-a2ac-9a42ee41957b
name: IAM-Based Authentication Data Exfiltration via RDS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.046450+00:00'
updated_at: '2023-04-10T20:20:11.480076+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
sub_techniques:
- '[[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol|T1048.002 - Exfiltration
  Over Asymmetric Encrypted Non-C2 Protocol]]'
- '[[Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 - Exfiltration Over Unencrypted
  Non-C2 Protocol]]'
tags:
- '[[Data exfiltration]]'
- '[[IAM Based authentication]]'
- '[[RDS - Relational Database Service]]'
commands:
- '[[AWS Get Caller Identity]]'
- '[[Generate RDS DB Auth Token]]'
- '[[Get IAM policy version]]'
- '[[List attached role policies]]'
---

# IAM-Based Authentication Data Exfiltration via RDS

## Summary

IAM-based authentication data exfiltration via RDS is a technique used by attackers to steal sensitive data from an AWS RDS instance. By exploiting IAM-based authentication, attackers can gain access to the RDS instance and exfiltrate data using temporary tokens. This technique involves the use of 

## Description

# Description

IAM-based authentication data exfiltration via RDS is a technique used by attackers to steal sensitive data from an AWS RDS instance. By exploiting IAM-based authentication, attackers can gain access to the RDS instance and exfiltrate data using temporary tokens. This technique involves the use of AWS CLI commands to list attached role policies, retrieve AWS IAM policy version information, and generate RDS temporary tokens. By using these commands, attackers can bypass traditional authentication methods and gain access to sensitive data.

This technique can be used by attackers to steal sensitive data such as customer data, financial data, and intellectual property. It can also be used to gain a foothold in an organization's network and move laterally to other systems.

Businesses that use AWS RDS should be aware of this technique and take steps to secure their RDS instances and prevent data exfiltration.

 

## Requirements

1. Access to an AWS RDS instance

1. AWS CLI access

1. IAM-based authentication

 

## Defense

1. Implement strong access controls and limit access to AWS RDS instances

1. Monitor AWS CLI activity and look for suspicious activity

1. Implement encryption at rest and in transit to protect sensitive data

 

## Objectives

1. Exfiltrate sensitive data from an AWS RDS instance

1. Bypass traditional authentication methods

1. Gain access to sensitive data

 

# Instructions

1. This command retrieves the account ID and the ARN of the IAM user or role whose credentials are used to call the command.

 

The `aws sts get-caller-identity` command is used to identify the user or role whose credentials are being used to make the AWS API call. This command is useful in scenarios where you have multiple users or roles with different levels of access to AWS services and you want to ensure that the right user or role is being used to execute the command. The output of this command includes the account ID and the ARN of the user or role. This information can be used to troubleshoot issues related to permissions and access control in AWS.



**Command** ([[AWS Get Caller Identity]]):

```bash
aws sts get-caller-identity
```



2. To list all policies attached to a specific IAM role, use the `aws iam list-attached-role-policies` command followed by the `--role-name` parameter and the name of the role you want to check.

 

This command will return a list of all policies that are attached to the specified IAM role. This is useful when you need to see which policies are currently in effect for a particular role, or when you need to troubleshoot issues related to role permissions. The `--role-name` parameter specifies the name of the role you want to check. If the role has no policies attached, the command will return an empty list. Note that this command only lists policies that are attached directly to the role, not policies that are attached to any of the role's groups or users.



**Command** ([[List attached role policies]]):

```bash
aws iam list-attached-role-policies --role-name name
```



3. Use this command to retrieve information about a specific version of an AWS IAM policy.

 



**Code**: [[aws iam get-policy-version --policy-arn arn --vers]]



> - `--policy-arn` : The Amazon Resource Name (ARN) of the policy you want information about.
- `--version-id` : The identifier for the version of the policy you want information about.



**Command** ([[Get IAM policy version]]):

```bash
aws iam get-policy-version --policy-arn arn --version-id ID
```



4. Use this command to generate a temporary token for accessing the RDS instance. The token is valid for 15 minutes and can be used to authenticate against the database.

 

This command generates a temporary token that can be used to authenticate against an RDS instance. The token is generated using the AWS SDK or CLI and is valid for 15 minutes. The token can be used to authenticate against the database, and it can be revoked at any time. The `--hostname` parameter specifies the hostname of the RDS instance, the `--port` parameter specifies the port number, the `--username` parameter specifies the username, and the `--region` parameter specifies the AWS region where the RDS instance is located.



**Command** ([[Generate RDS DB Auth Token]]):

```bash
aws rds generate-db-auth-token --hostname hostname --port port --username username --region region
```



## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

### Sub-Techniques

- [[Exfiltration Over Asymmetric Encrypted Non-C2 Protocol|T1048.002 - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol]]
- [[Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 - Exfiltration Over Unencrypted Non-C2 Protocol]]

## Commands Used

- [[AWS Get Caller Identity]]
- [[Generate RDS DB Auth Token]]
- [[Get IAM policy version]]
- [[List attached role policies]]

## Tags

- [[Data exfiltration]]
- [[IAM Based authentication]]
- [[RDS - Relational Database Service]]


