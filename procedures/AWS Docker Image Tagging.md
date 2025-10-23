---
id: f5754e05-336b-432a-887b-0170cdba5f2e
name: AWS Docker Image Tagging
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.166540+00:00'
updated_at: '2023-04-10T20:21:04.111492+00:00'
tags:
- '[[Cloud - AWS]]'
- '[[Persistence]]'
- '[[Tagging the docker image]]'
commands:
- '[[Tag Docker Image]]'
---

# AWS Docker Image Tagging

## Summary

The AWS Docker Image Tagging procedure involves adding tags to Docker images in order to easily identify and manage them. This can be useful for version control, organization, and automation purposes. Attackers can also use this technique to evade detection by changing the image tags to avoid detec

## Description

# Description

The AWS Docker Image Tagging procedure involves adding tags to Docker images in order to easily identify and manage them. This can be useful for version control, organization, and automation purposes. Attackers can also use this technique to evade detection by changing the image tags to avoid detection by security tools. To implement this procedure, the 'Docker Tagging Command' is used to add tags to the Docker image. This command takes in two parameters, the name of the image and the tag to be added. By default, the 'latest' tag is added to the image if no tag is specified. 

From a technical perspective, this procedure involves using the Docker CLI to add tags to Docker images. The 'docker tag' command is used to add tags to the image. This can be done either locally or remotely, depending on the user's requirements. The business value of this procedure lies in the ability to easily manage and organize Docker images, making it easier to deploy and manage applications in the cloud.

 

## Requirements

1. Access to Docker CLI

1. Authenticated access to AWS

 

## Defense

1. Implement access controls to prevent unauthorized access to Docker images and tags

1. Monitor Docker image tags for suspicious or unauthorized changes

1. Implement security tools to detect and prevent Docker image tampering

 

## Objectives

1. To add tags to Docker images in AWS

1. To easily identify and manage Docker images

1. To automate version control and organization of Docker images

 

# Instructions

1. This command is used to tag a Docker image with a new name and a repository address. The command takes two arguments: 
1. image_name: The name of the Docker image that needs to be tagged. 
2. ecr_addr: The repository address where the image needs to be tagged. The repository address should be in the format of 'aws_account_id.dkr.ecr.region.amazonaws.com'.

Once the command is executed, the Docker image will be tagged with the new name and the repository address.

 



**Code**: [[docker tag image_name ecr_addr:Image_Name]]



> For example, if you want to tag a Docker image named 'my_image' with a new name 'new_image' and a repository address '123456789012.dkr.ecr.us-west-2.amazonaws.com', you can execute the following command:

docker tag my_image 123456789012.dkr.ecr.us-west-2.amazonaws.com/new_image

This command will tag the Docker image 'my_image' with the new name 'new_image' and the repository address '123456789012.dkr.ecr.us-west-2.amazonaws.com'.



**Command** ([[Tag Docker Image]]):

```bash
docker tag image_name ecr_addr:Image_Name
```



## Commands Used

- [[Tag Docker Image]]

## Tags

- [[Cloud - AWS]]
- [[Persistence]]
- [[Tagging the docker image]]


