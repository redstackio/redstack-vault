---
id: 1741c202-2e4b-4efb-a8bd-e47ff89a3e9a
name: AWS Userdata Retrieval via Instance Metadata Service
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.406705+00:00'
updated_at: '2023-04-10T20:20:31.247449+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[AWS Userdata]]'
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Remote code execution]]'
commands:
- '[[Retrieve AWS EC2 User Data]]'
- '[[Retrieve User Data]]'
---

# AWS Userdata Retrieval via Instance Metadata Service

## Summary

AWS Userdata Retrieval via Instance Metadata Service is a technique that can be used by an attacker to obtain sensitive information such as credentials, keys, and other secrets that are passed to an EC2 instance at launch time. This technique can be used to escalate privileges, move laterally, or e

## Description

# Description

AWS Userdata Retrieval via Instance Metadata Service is a technique that can be used by an attacker to obtain sensitive information such as credentials, keys, and other secrets that are passed to an EC2 instance at launch time. This technique can be used to escalate privileges, move laterally, or exfiltrate data from the target environment. To retrieve the Userdata, the attacker can use the instance metadata service, which is a RESTful API that can be accessed from within the EC2 instance. By sending a GET request to the metadata service, the attacker can retrieve the Userdata that was passed to the instance at launch time. This technique requires no authentication and can be automated at scale.

## Requirements

1. Access to an EC2 instance within the target environment.

1. Ability to send HTTP requests to the instance metadata service.

## Defense

1. Ensure that sensitive information is not passed to EC2 instances as Userdata.

1. Implement network segmentation to limit access to the instance metadata service.

1. Monitor network traffic for suspicious HTTP requests to the instance metadata service.

## Objectives

1. Retrieve sensitive information such as credentials, keys, and other secrets passed to an EC2 instance at launch time.

1. Escalate privileges, move laterally, or exfiltrate data from the target environment.

# Instructions

1. To retrieve user data from an EC2 instance metadata, run the following command in your terminal:

**Code**: [[curl http://169.254.169.254/latest/user-data/]]

> This command uses the curl utility to retrieve the user data associated with the EC2 instance. The user data is data that you can pass to an EC2 instance when you launch it. This can be useful for passing configuration information or scripts to the instance. The user data is stored in the instance metadata service and can be accessed using the URL provided in the command. The command sends an HTTP request to the URL and prints the response body to the terminal. Note that the user data is limited to 16 KB in size and is only available to the instance during its first boot cycle.

**Command** ([[Retrieve User Data]]):

```bash
curl http://169.254.169.254/latest/user-data/
```

2. To retrieve user data from an EC2 instance using the instance metadata service, follow these steps:
1. Set the TOKEN variable using the curl command to get a temporary security token.
2. Use the TOKEN variable in the curl command to retrieve the user data from the metadata service.

**Code**: [[TOKEN=`curl
X PUT "http://169.254.169.254/latest/ ]]

> The 'curl' command is used to interact with the instance metadata service on an EC2 instance. The first 'curl' command retrieves a temporary security token from the metadata service and sets it to the TOKEN variable. The 'X-aws-ec2-metadata-token-ttl-seconds' header specifies the time-to-live for the token in seconds. The second 'curl' command uses the TOKEN variable in the 'X-aws-ec2-metadata-token' header to retrieve the user data from the metadata service. The 'v' option is used to display the response in verbose mode.

**Command** ([[Retrieve AWS EC2 User Data]]):

```bash
TOKEN=`curl
X PUT "http://169.254.169.254/latest/ api /token" H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
&& curl H "X-aws-ec2-metadata-token: $TOKEN" v http://169.254.169.254/latest/user-data/
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Retrieve AWS EC2 User Data]]
- [[Retrieve User Data]]

## Tags

- [[AWS Userdata]]
- [[Cloud - AWS]]
- [[Exploitation]]
- [[Remote code execution]]
