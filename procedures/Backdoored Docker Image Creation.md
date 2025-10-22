---
id: 12904dd3-bc3b-4075-a4ba-d9694f6d7dcf
name: Backdoored Docker Image Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.142615+00:00'
updated_at: '2023-04-10T20:20:19.081682+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Multi-hop Proxy|T1188 - Multi-hop Proxy]]'
tags:
- '[[Building images with backdoor]]'
- '[[Cloud - AWS]]'
- '[[Persistence]]'
commands:
- '[[Build Docker Image]]'
---

# Backdoored Docker Image Creation

## Summary

Creating backdoored Docker images is a common technique used by attackers to gain persistence in a target environment. By building an image with a backdoor, attackers can ensure that their access to the environment is maintained even if other security measures are put in place. The technical proces

## Description

# Description

Creating backdoored Docker images is a common technique used by attackers to gain persistence in a target environment. By building an image with a backdoor, attackers can ensure that their access to the environment is maintained even if other security measures are put in place. The technical process involves adding malicious code to the Dockerfile or other image files, which is then executed when the image is run. The business value of this attack is that it allows attackers to maintain a foothold in a target environment, which can be used for further attacks or data exfiltration.

## Requirements

1. Access to Docker build environment

1. Knowledge of Dockerfile syntax

1. Ability to execute commands on the target environment

## Defense

1. Ensure that Dockerfiles and other image files are carefully reviewed for malicious code

1. Use tools such as Docker Content Trust to verify the integrity of images before deployment

1. Monitor Docker image creation and deployment for suspicious activity

## Objectives

1. Create a backdoored Docker image

1. Ensure that the image is successfully built and deployed in the target environment

# Instructions

1. To build a Docker image, use the 'docker build' command followed by the '-t' flag and the desired name for the image. This command will look for a Dockerfile in the current directory and use it to build the image.

The '-t' flag allows you to specify a name for the image. This name should follow the format 'repository/image_name:tag', where 'repository' is the Docker registry you want to use (if any), 'image_name' is the name you want to give to your image, and 'tag' is an optional tag to differentiate between different versions of the same image. For example, 'my-registry/my-image:latest'.

**Command** ([[Build Docker Image]]):

```bash
docker build -t image_name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Multi-hop Proxy|T1188 - Multi-hop Proxy]]

## Commands Used

- [[Build Docker Image]]

## Tags

- [[Building images with backdoor]]
- [[Cloud - AWS]]
- [[Persistence]]
