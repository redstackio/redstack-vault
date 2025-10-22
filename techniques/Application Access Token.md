---
id: ad629e48-6048-4e84-9957-61ff7f65acc5
name: Application Access Token
type: technique
mitre_id: T1527
mitre_url: null
created_at: '2023-04-06T00:31:25.762283+00:00'
updated_at: '2023-04-06T03:56:41.209808+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
procedures:
- '[[AWS EKS Service Account Token Theft]]'
- '[[AWS IAM Group Managed Policies Enumeration]]'
- '[[AWS IAM Inline Policy Enumeration]]'
- '[[AWS IAM Policy Version Information Retrieval]]'
- '[[AWS IAM Role Inline Policy Enumeration]]'
- '[[AWS IAM User Policy Enumeration]]'
- '[[AWS Lambda Backdoor Persistence]]'
- '[[AWS S3 Bucket Configuration]]'
- '[[AWS S3 Bucket Configuration]]'
- '[[AWS User Policy Enumeration]]'
- '[[Azure - Illicit Consent Grant Prevention]]'
- '[[Azure Managed Identity Token Retrieval]]'
- '[[Azure Resource Management and Privilege Checking with PowerShell]]'
- '[[EKS Fargate Profile Enumeration]]'
- '[[HockeyApp API Token Exploitation]]'
- '[[HockeyApp API Token Exploitation]]'
- '[[HockeyApp API Token Exploitation]]'
- '[[Jetty RCE via Insecure XML File Upload]]'
- '[[JWT Signature Key Confusion Attack RS256 to HS256 (CVE-2016-5431)]]'
- '[[LDAP Server Statistics Retrieval via SSRF Exploitation]]'
- '[[MYSQL Time Based Injection using SLEEP in a subselect]]'
---

# Application Access Token

**MITRE ID**: T1527

## Description

Adversaries may use application access tokens to bypass the typical authentication process and access restricted accounts, information, or services on remote systems. These tokens are typically stolen from users and used in lieu of login credentials.

Application access tokens are used to make authorized API requests on behalf of a user and are commonly used as a way to access resources in cloud-based applications and software-as-a-service (SaaS).(Citation: Auth0 - Why You Should Always Use Access Tokens to Secure APIs Sept 2019) OAuth is one commonly implemented framework that issues tokens to users for access to systems. These frameworks are used collaboratively to verify the user and determine what actions the user is allowed to perform. Once identity is established, the token allows actions to be authorized, without passing the actual credentials of the user. Therefore, compromise of the token can grant the adversary access to resources of other sites through a malicious application.(Citation: okta)

For example, with a cloud-based email service once an OAuth access token is granted to a malicious application, it can potentially gain long-term access to features of the user account if a "refresh" token enabling background access is awarded.(Citation: Microsoft Identity Platform Access 2019) With an OAuth access token an adversary can use the user-granted REST API to perform functions such as email searching and contact enumeration.(Citation: Staaldraad Phishing with OAuth 2017)

Compromised access tokens may be used as an initial step in compromising other services. For example, if a token grants access to a victim’s primary email, the adversary may be able to extend access to all other services which the target subscribes by triggering forgotten password routines. Direct API access through a token negates the effectiveness of a second authentication factor and may be immune to intuitive countermeasures like changing passwords. Access abuse over an API channel can be difficult to detect even from the service provider end, as the access can still align well with a legitimate workflow.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

## Related Procedures (21)

- [[AWS EKS Service Account Token Theft]]
- [[AWS IAM Group Managed Policies Enumeration]]
- [[AWS IAM Inline Policy Enumeration]]
- [[AWS IAM Policy Version Information Retrieval]]
- [[AWS IAM Role Inline Policy Enumeration]]
- [[AWS IAM User Policy Enumeration]]
- [[AWS Lambda Backdoor Persistence]]
- [[AWS S3 Bucket Configuration]]
- [[AWS S3 Bucket Configuration]]
- [[AWS User Policy Enumeration]]
- [[Azure - Illicit Consent Grant Prevention]]
- [[Azure Managed Identity Token Retrieval]]
- [[Azure Resource Management and Privilege Checking with PowerShell]]
- [[EKS Fargate Profile Enumeration]]
- [[HockeyApp API Token Exploitation]]
- [[HockeyApp API Token Exploitation]]
- [[HockeyApp API Token Exploitation]]
- [[Jetty RCE via Insecure XML File Upload]]
- [[JWT Signature Key Confusion Attack RS256 to HS256 (CVE-2016-5431)]]
- [[LDAP Server Statistics Retrieval via SSRF Exploitation]]

*...and 1 more*
