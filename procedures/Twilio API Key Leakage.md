---
id: ad1e6e5c-8c3d-4617-b525-9e86cf368b17
name: Twilio API Key Leakage
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.176923+00:00'
updated_at: '2023-04-06T03:55:53.193074+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Credentials In Files|T1552.001 - Credentials In Files]]'
- '[[Private Keys|T1552.004 - Private Keys]]'
tags:
- '[[API Key Leaks]]'
- '[[Exploit]]'
- '[[Twilio Account_sid and Auth token]]'
commands:
- '[[Retrieve Twilio Accounts]]'
---

# Twilio API Key Leakage

## Summary

Twilio is a cloud communications platform that allows users to send and receive text messages and phone calls programmatically. The Twilio Account_sid and Auth_token are used to authenticate requests made to the Twilio API. If an attacker gains access to these credentials, they can use it to make u

## Description

# Description

Twilio is a cloud communications platform that allows users to send and receive text messages and phone calls programmatically. The Twilio Account_sid and Auth_token are used to authenticate requests made to the Twilio API. If an attacker gains access to these credentials, they can use it to make unauthorized calls and messages, which can result in financial loss, reputational damage, and legal consequences. To exploit this vulnerability, attackers can use various techniques such as phishing, social engineering, or searching for credentials in publicly accessible repositories. 

Technical Explanation: An attacker can use the leaked Twilio Account_sid and Auth_token to authenticate requests made to the Twilio API. This can allow them to make unauthorized calls and messages, which can result in financial loss, reputational damage, and legal consequences. 

Business Value: The Twilio API is used by many businesses to communicate with their customers. An attacker who gains access to Twilio API credentials can use it to make unauthorized calls and messages, which can result in financial loss, reputational damage, and legal consequences.

 

## Requirements

1. Access to the internet

1. Knowledge of Twilio API

1. Access to the target's Twilio Account_sid and Auth_token

 

## Defense

1. Use strong and unique passwords for Twilio accounts

1. Enable two-factor authentication for Twilio accounts

1. Monitor Twilio accounts for unauthorized activity

 

## Objectives

1. To obtain the Twilio Account_sid and Auth_token

1. To use the obtained credentials to make unauthorized calls and messages

 

# Instructions

1. Replace ACCOUNT_SID and AUTH_TOKEN with the target's credentials.

 



**Code**: [[curl -X GET 'https://api.twilio.com/2010-04-01/Acc]]



> This command sends a GET request to the Twilio API and returns the Account_sid and Auth_token associated with the provided credentials.



**Command** ([[Retrieve Twilio Accounts]]):

```bash
curl -X GET 'https://api.twilio.com/2010-04-01/Accounts.json' -u ACCOUNT_SID:AUTH_TOKEN
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files|T1552.001 - Credentials In Files]]
- [[Private Keys|T1552.004 - Private Keys]]

## Commands Used

- [[Retrieve Twilio Accounts]]

## Tags

- [[API Key Leaks]]
- [[Exploit]]
- [[Twilio Account_sid and Auth token]]


