---
id: f163a194-d0c2-4d1b-a26f-d79431c7554e
name: Copying EC2 Instances using AMI Image in AWS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.586221+00:00'
updated_at: '2023-04-10T20:19:44.881825+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Inhibit System Recovery|T1490 - Inhibit System Recovery]]'
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[Windows Remote Management|T1021.006 - Windows Remote Management]]'
tags:
- '[[AWS - Copy EC2 using AMI Image]]'
- '[[Cloud - AWS]]'
commands:
- '[[Create EC2 instance]]'
- '[[Create Image for instance]]'
- '[[Describe EC2 instance]]'
- '[[Import key pair]]'
- '[[List EC2 images in eu-west-1 region]]'
- '[[Modify instance attribute]]'
- '[[Stop EC2 instance]]'
- '[[Terminate EC2 instance]]'
---

# Copying EC2 Instances using AMI Image in AWS

## Summary

Copying an EC2 instance using an AMI image is a common practice in AWS for creating multiple instances with the same configuration. This procedure involves creating an AMI image of the source EC2 instance and then launching a new instance from that AMI. This can be useful for scaling out an applica

## Description

# Description

Copying an EC2 instance using an AMI image is a common practice in AWS for creating multiple instances with the same configuration. This procedure involves creating an AMI image of the source EC2 instance and then launching a new instance from that AMI. This can be useful for scaling out an application, creating backup instances, or creating a test environment. From an offensive perspective, an attacker could use this procedure to gain access to additional instances and move laterally within the network. 

Technical Explanation: The procedure involves creating a new AMI image from the source EC2 instance, and then launching a new instance from that image. The new instance will have the same configuration as the source instance, including the same security groups, IAM roles, and storage volumes. The new instance will also have a new IP address and hostname. 

Business Value: This procedure can save time and resources when creating multiple instances with the same configuration. It can also be used to create backup instances and test environments, which can improve business continuity and reduce downtime.

 

## Requirements

1. Access to the AWS Management Console

1. Permissions to create an AMI image and launch new instances

1. Access to the source EC2 instance

 

## Defense

1. Limit access to the AWS Management Console to authorized personnel only

1. Implement least privilege access controls to limit the permissions of IAM roles

1. Regularly monitor EC2 instances for unauthorized access and suspicious activity

 

## Objectives

1. Create a new EC2 instance with the same configuration as the source instance

1. Scale out an application by creating multiple instances

1. Improve business continuity by creating backup instances

1. Create test environments to reduce downtime

 

# Instructions

1. To describe the available Amazon Machine Images (AMIs), you can use the describe-images command. This command will return a list of all the available AMIs in the specified region, along with their details such as ID, name, description, architecture, and creation date.

 



**Code**: [[aws ec2 describe-images --region eu-west-1]]



> The --region parameter specifies the region in which to describe the images. If this parameter is not specified, the default region will be used. You can also use filters to narrow down the search results by specifying criteria such as the image owner, image type, or image state. For more information on the available filters, please refer to the AWS documentation.



**Command** ([[List EC2 images in eu-west-1 region]]):

```bash
aws ec2 describe-images --region eu-west-1
```



2. To create an AWS Audit Instance, follow these steps:
1. Create a new image for the instance-id using the command 'aws ec2 create-image'.
2. Add the key to AWS using the command 'aws ec2 import-key-pair'.
3. Create ec2 using the previously created AMI, use the same security group and subnet to connect easily using the command 'aws ec2 run-instances'.
4. Check the instance using the command 'aws ec2 describe-instances'.
5. If needed, edit groups using the command 'aws ec2 modify-instance-attribute'.
6. To avoid any useless cost, stop and terminate the instance using the commands 'aws ec2 stop-instances' and 'aws ec2 terminate-instances' respectively.

 



**Code**: [[# create a new image for the instance-id
$ aws ec2]]



> The 'create-image' command is used to create a new image for the instance-id. The 'import-key-pair' command is used to add the key to AWS. The 'run-instances' command is used to create ec2 using the previously created AMI, use the same security group and subnet to connect easily. The 'describe-instances' command is used to check the instance. The 'modify-instance-attribute' command is used to edit groups. The 'stop-instances' and 'terminate-instances' commands are used to stop and terminate the instance respectively.



**Command** ([[Create Image for instance]]):

```bash
$ aws ec2 create-image --instance-id i-0438b003d81cd7ec5 --name "AWS Audit" --description "Export AMI" --region eu-west-1
```





**Command** ([[Import key pair]]):

```bash
$ aws ec2 import-key-pair --key-name "AWS Audit" --public-key-material file://~/.ssh/id_rsa.pub --region eu-west-1
```





**Command** ([[Create EC2 instance]]):

```bash
$ aws ec2 run-instances --image-id ami-0b77e2d906b00202d --security-group-ids "sg-6d0d7f01" --subnet-id subnet-9eb001ea --count 1 --instance-type t2.micro --key-name "AWS Audit" --query "Instances[0].InstanceId" --region eu-west-1
```





**Command** ([[Describe EC2 instance]]):

```bash
aws ec2 describe-instances --instance-ids i-0546910a0c18725a1
```





**Command** ([[Modify instance attribute]]):

```bash
aws ec2 modify-instance-attribute --instance-id "i-0546910a0c18725a1" --groups "sg-6d0d7f01"  --region eu-west-1
```





**Command** ([[Stop EC2 instance]]):

```bash
aws ec2 stop-instances --instance-id "i-0546910a0c18725a1" --region eu-west-1
```





**Command** ([[Terminate EC2 instance]]):

```bash
aws ec2 terminate-instances --instance-id "i-0546910a0c18725a1" --region eu-west-1
```



## MITRE ATT&CK Mapping

### Tactics

- [[Impact|TA0040 - Impact]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Inhibit System Recovery|T1490 - Inhibit System Recovery]]
- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[Windows Remote Management|T1021.006 - Windows Remote Management]]

## Commands Used

- [[Create EC2 instance]]
- [[Create Image for instance]]
- [[Describe EC2 instance]]
- [[Import key pair]]
- [[List EC2 images in eu-west-1 region]]
- [[Modify instance attribute]]
- [[Stop EC2 instance]]
- [[Terminate EC2 instance]]

## Tags

- [[AWS - Copy EC2 using AMI Image]]
- [[Cloud - AWS]]


