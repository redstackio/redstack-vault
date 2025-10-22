---
id: 0887bac5-1ca8-4498-9ddd-6d8ab2ef0839
name: Additional Cloud Roles
type: sub-technique
mitre_id: T1098.003
mitre_url: null
created_at: '2023-04-06T00:31:25.814620+00:00'
updated_at: '2023-04-06T00:31:25.814620+00:00'
parent_technique: '[[Account Manipulation|T1098 - Account Manipulation]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Persistence|TA0003 - Persistence]]'
---

# Additional Cloud Roles

**MITRE ID**: T1098.003

**Parent Technique**: [[Account Manipulation|T1098 - Account Manipulation]]

This is a sub-technique of T1098 - Account Manipulation.

## Summary

An adversary may add additional roles or permissions to an adversary-controlled cloud account to maintain persistent access to a tenant. For example, adversaries may update IAM policies in cloud-based environments or add a new global administrator in Office 365 environments.(Citation: AWS IAM Polici

## Description

An adversary may add additional roles or permissions to an adversary-controlled cloud account to maintain persistent access to a tenant. For example, adversaries may update IAM policies in cloud-based environments or add a new global administrator in Office 365 environments.(Citation: AWS IAM Policies and Permissions)(Citation: Google Cloud IAM Policies)(Citation: Microsoft Support O365 Add Another Admin, October 2019)(Citation: Microsoft O365 Admin Roles) With sufficient permissions, a compromised account can gain almost unlimited access to data and settings (including the ability to reset the passwords of other admins).(Citation: Expel AWS Attacker)
(Citation: Microsoft O365 Admin Roles) 

This account modification may immediately follow [Create Account](https://attack.mitre.org/techniques/T1136) or other malicious account activity. Adversaries may also modify existing [Valid Accounts](https://attack.mitre.org/techniques/T1078) that they have compromised. This could lead to privilege escalation, particularly if the roles added allow for lateral movement to additional accounts.

For example, in Azure AD environments, an adversary with the Application Administrator role can add [Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001) to their application's service principal. In doing so the adversary would be able to gain the service principal’s roles and permissions, which may be different from those of the Application Administrator.(Citation: SpecterOps Azure Privilege Escalation) Similarly, in AWS environments, an adversary with appropriate permissions may be able to use the <code>CreatePolicyVersion</code> API to define a new version of an IAM policy or the <code>AttachUserPolicy</code> API to attach an IAM policy with additional or distinct permissions to a compromised user account.(Citation: Rhino Security Labs AWS Privilege Escalation)

Similarly, an adversary with the Azure AD Global Administrator role can toggle the “Access management for Azure resources” option to gain the ability to assign privileged access to Azure subscriptions and virtual machines to Azure AD users, including themselves.(Citation: Azure AD to AD) 

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
- [[Persistence|TA0003 - Persistence]]
