---
id: c4425000-12d2-4360-bfaa-4c7767c9dd4c
name: AWS IAM Role Listing Manager Policies
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.006501+00:00'
updated_at: '2023-04-10T20:19:59.250263+00:00'
tags:
- '[[Cloud - AWS]]'
- '[[Listing manager policies attached to the IAM role]]'
- '[[Persistence]]'
commands:
- '[[List Attached Role Policies]]'
---

# AWS IAM Role Listing Manager Policies

## Summary

The AWS IAM Role Listing Manager Policies procedure involves listing the policies attached to a specific IAM role. This can be useful for understanding the permissions granted to a particular role, and can be used to identify potential areas of privilege escalation. To execute this procedure, the u

## Description

# Description

The AWS IAM Role Listing Manager Policies procedure involves listing the policies attached to a specific IAM role. This can be useful for understanding the permissions granted to a particular role, and can be used to identify potential areas of privilege escalation. To execute this procedure, the user must have the necessary permissions to view the policies attached to the role.

From an offensive perspective, an attacker could use this information to identify roles with overly permissive policies and exploit them to gain access to sensitive resources. From a defensive perspective, this procedure can be used to identify and remediate overly permissive policies attached to roles.

 

## Requirements

1. IAM permissions to view policies attached to the role

 

## Defense

1. Ensure that IAM roles have the minimum necessary permissions to perform their intended function

1. Regularly review and audit IAM roles and attached policies for overly permissive permissions

1. Use AWS Config to monitor and enforce compliance with security best practices

 

## Objectives

1. Identify the policies attached to a specific IAM role

1. Understand the permissions granted to a particular role

1. Identify potential areas of privilege escalation

 

# Instructions

1. To list all the attached policies for a specific IAM role, use the following command:

 

This command will return a list of all the policies that are attached to the specified IAM role. The output will include the policy name, policy ARN, and the policy description. This can be useful for reviewing the permissions that are associated with a specific IAM role.



**Command** ([[List Attached Role Policies]]):

```bash
aws iam list-attached-role-policies --role-name name
```



## Commands Used

- [[List Attached Role Policies]]

## Tags

- [[Cloud - AWS]]
- [[Listing manager policies attached to the IAM role]]
- [[Persistence]]


