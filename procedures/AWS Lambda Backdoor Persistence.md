---
id: cac514d5-374f-405e-8e57-096cb413badf
name: AWS Lambda Backdoor Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.933867+00:00'
updated_at: '2023-04-10T20:20:05.986291+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
- '[[Phishing|T1566 - Phishing]]'
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
tags:
- '[[Cloud - AWS]]'
- '[[Persistence]]'
- '[[Uploading the backdoor code to AWS Lambda function]]'
commands:
- '[[Update AWS Lambda function code]]'
---

# AWS Lambda Backdoor Persistence

## Summary

AWS Lambda is a serverless computing service that allows users to run code without provisioning or managing servers. Attackers can upload malicious code to an AWS Lambda function to maintain persistence in the victim's environment. This technique can be used to evade detection and maintain access t

## Description

# Description

AWS Lambda is a serverless computing service that allows users to run code without provisioning or managing servers. Attackers can upload malicious code to an AWS Lambda function to maintain persistence in the victim's environment. This technique can be used to evade detection and maintain access to the victim's environment.

To upload a backdoor code to an AWS Lambda function, the attacker needs to have valid AWS credentials. Once the attacker has access to the victim's AWS account, they can update the Lambda function code with their own malicious code. The backdoor code can be designed to execute arbitrary commands or connect to a remote server controlled by the attacker.

This technique can be used by attackers to maintain access to a victim's environment even if the victim detects and removes the initial compromise.

## Requirements

1. Valid AWS credentials

## Defense

1. Monitor for unauthorized access to AWS accounts and revoke credentials as necessary

1. Implement multi-factor authentication (MFA) for AWS accounts

1. Regularly review and audit AWS Lambda function code for malicious activity

## Objectives

1. Maintain persistence in the victim's environment

1. Evade detection and maintain access to the victim's environment

# Instructions

1. Use the 'aws lambda update-function-code' command to update the code for an existing Lambda function.

This command requires the name of the function to be updated and the location of the updated code in the form of a .zip file. The 'function-name' argument should be replaced with the name of the function you want to update. The 'zip-file' argument should be replaced with the path to the .zip file containing the updated code. Once executed, this command will replace the existing code for the specified function with the code contained in the .zip file.

**Command** ([[Update AWS Lambda function code]]):

```bash
aws lambda update-function-code --function-name function --zip-file fileb://my-function.zip
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]
- [[Phishing|T1566 - Phishing]]
- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Commands Used

- [[Update AWS Lambda function code]]

## Tags

- [[Cloud - AWS]]
- [[Persistence]]
- [[Uploading the backdoor code to AWS Lambda function]]
