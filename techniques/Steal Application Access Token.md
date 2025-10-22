---
id: 77aa22f7-3f6d-4d52-a6e3-be0da82cc500
name: Steal Application Access Token
type: technique
mitre_id: T1528
mitre_url: null
created_at: '2023-04-06T00:31:26.533339+00:00'
updated_at: '2023-05-24T07:31:24.825795+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[AWS Credential Export]]'
- '[[AWS KMS Key Listing]]'
- '[[AWS Lambda Backdoor Persistence]]'
- '[[AWS Managed Policies Enumeration]]'
- '[[AWS Privilege Escalation via Attached User Policies]]'
- '[[AWS Privilege Escalation via Default Policy Information]]'
- '[[Azure Device Management and Token Generation with SharpAzToken]]'
- '[[Azure Key Vault Access and Query with PowerShell]]'
- '[[Azure Token Generation and Authentication with SharpAzToken]]'
- '[[Compromise of Personal Access Token for Gitlab Source Code Management and CI/CD]]'
- '[[Gitlab Personal Access Token API Key Leak]]'
- '[[Gitlab Personal Access Token API Key Leak]]'
- '[[Gitlab Personal Access Token API Key Leak]]'
- '[[Illicit Consent Grant - User Consent Permissions]]'
- '[[JWT Signature Key Injection Attack]]'
- '[[Linux Privilege Escalation via NFS Root Squashing]]'
- '[[OAuth Misconfiguration and CSRF Vulnerability]]'
- '[[Slack API Token Leakage]]'
- '[[Slack API Token Leakage]]'
- '[[Slack API Token Leakage]]'
---

# Steal Application Access Token

**MITRE ID**: T1528

## Description

Adversaries can steal application access tokens as a means of acquiring credentials to access remote systems and resources.

Application access tokens are used to make authorized API requests on behalf of a user or service and are commonly used as a way to access resources in cloud and container-based applications and software-as-a-service (SaaS).(Citation: Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019) OAuth is one commonly implemented framework that issues tokens to users for access to systems. Adversaries who steal account API tokens in cloud and containerized environments may be able to access data and perform actions with the permissions of these accounts, which can lead to privilege escalation and further compromise of the environment.

In Kubernetes environments, processes running inside a container communicate with the Kubernetes API server using service account tokens. If a container is compromised, an attacker may be able to steal the container’s token and thereby gain access to Kubernetes API commands.(Citation: Kubernetes Service Accounts)

Token theft can also occur through social engineering, in which case user action may be required to grant access. An application desiring access to cloud-based services or protected APIs can gain entry using OAuth 2.0 through a variety of authorization protocols. An example commonly-used sequence is Microsoft's Authorization Code Grant flow.(Citation: Microsoft Identity Platform Protocols May 2019)(Citation: Microsoft - OAuth Code Authorization flow - June 2019) An OAuth access token enables a third-party application to interact with resources containing user data in the ways requested by the application without obtaining user credentials. 

Adversaries can leverage OAuth authorization by constructing a malicious application designed to be granted access to resources with the target user's OAuth token.(Citation: Amnesty OAuth Phishing Attacks, August 2019)(Citation: Trend Micro Pawn Storm OAuth 2017) The adversary will need to complete registration of their application with the authorization server, for example Microsoft Identity Platform using Azure Portal, the Visual Studio IDE, the command-line interface, PowerShell, or REST API calls.(Citation: Microsoft - Azure AD App Registration - May 2019) Then, they can send a [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002) to the target user to entice them to grant access to the application. Once the OAuth access token is granted, the application can gain potentially long-term access to features of the user account through [Application Access Token](https://attack.mitre.org/techniques/T1550/001).(Citation: Microsoft - Azure AD Identity Tokens - Aug 2019)

Application access tokens may function within a limited lifetime, limiting how long an adversary can utilize the stolen token. However, in some cases, adversaries can also steal application refresh tokens(Citation: Auth0 Understanding Refresh Tokens), allowing them to obtain new access tokens without prompting the user.  

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (20)

- [[AWS Credential Export]]
- [[AWS KMS Key Listing]]
- [[AWS Lambda Backdoor Persistence]]
- [[AWS Managed Policies Enumeration]]
- [[AWS Privilege Escalation via Attached User Policies]]
- [[AWS Privilege Escalation via Default Policy Information]]
- [[Azure Device Management and Token Generation with SharpAzToken]]
- [[Azure Key Vault Access and Query with PowerShell]]
- [[Azure Token Generation and Authentication with SharpAzToken]]
- [[Compromise of Personal Access Token for Gitlab Source Code Management and CI/CD]]
- [[Gitlab Personal Access Token API Key Leak]]
- [[Gitlab Personal Access Token API Key Leak]]
- [[Gitlab Personal Access Token API Key Leak]]
- [[Illicit Consent Grant - User Consent Permissions]]
- [[JWT Signature Key Injection Attack]]
- [[Linux Privilege Escalation via NFS Root Squashing]]
- [[OAuth Misconfiguration and CSRF Vulnerability]]
- [[Slack API Token Leakage]]
- [[Slack API Token Leakage]]
- [[Slack API Token Leakage]]
