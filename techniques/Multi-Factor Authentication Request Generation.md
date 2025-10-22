---
id: 918ac3f4-0ef7-4e9b-a1b1-0d6d245c190b
name: Multi-Factor Authentication Request Generation
type: technique
mitre_id: T1621
mitre_url: null
created_at: '2023-04-06T00:31:26.593134+00:00'
updated_at: '2023-04-06T00:31:27.845464+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Multi-Factor Authentication Request Generation

**MITRE ID**: T1621

## Description

Adversaries may attempt to bypass multi-factor authentication (MFA) mechanisms and gain access to accounts by generating MFA requests sent to users.

Adversaries in possession credentials to [Valid Accounts](https://attack.mitre.org/techniques/T1078) may be unable to complete the login process if they lack access to the 2FA or MFA mechanisms required as an additional credential and security control. To circumvent this, adversaries may abuse the automatic generation of push notifications to MFA services such as Duo Push, Microsoft Authenticator, Okta, or similar services to have the user grant access to their account.

In some cases, adversaries may continuously repeat login attempts in order to bombard users with MFA push notifications, SMS messages, and phone calls, potentially resulting in the user finally accepting the authentication request in response to “MFA fatigue.”(Citation: Russian 2FA Push Annoyance - Cimpanu)(Citation: MFA Fatigue Attacks - PortSwigger)(Citation: Suspected Russian Activity Targeting Government and Business Entities Around the Globe)

## Tactics

- [[Credential Access|TA0006 - Credential Access]]
