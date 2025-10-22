---
id: 517d957d-9c4c-443c-9c82-2eed220e4e1a
name: 2FA Bypass with Array of OTPs
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.985798+00:00'
updated_at: '2023-04-06T03:55:53.998541+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Two-Factor Authentication Interception|T1111 - Two-Factor Authentication Interception]]'
tags:
- '[[2FA Bypasses]]'
- '[[Account Takeover]]'
- '[[Bypass 2FA with array]]'
commands:
- '[[OTP Verification]]'
---

# 2FA Bypass with Array of OTPs

## Summary

This procedure involves bypassing 2FA protection by using an array of OTPs (One-Time Passwords). Attackers can obtain these OTPs through various means such as phishing, social engineering, or brute-forcing. Once they have a list of valid OTPs, they can use them to bypass 2FA protection and gain una

## Description

# Description

This procedure involves bypassing 2FA protection by using an array of OTPs (One-Time Passwords). Attackers can obtain these OTPs through various means such as phishing, social engineering, or brute-forcing. Once they have a list of valid OTPs, they can use them to bypass 2FA protection and gain unauthorized access to the target account. This technique can be used to steal sensitive information, perform fraudulent transactions, or launch further attacks.

## Requirements

## Defense

1. Implement multi-factor authentication (MFA) that includes additional factors beyond just OTPs, such as biometrics or smart cards.

1. Monitor user accounts for suspicious activity, such as multiple failed login attempts or login attempts from unusual locations.

1. Educate users on the risks of phishing and social engineering attacks, and provide training on how to identify and avoid them.

## Objectives

1. Bypass 2FA protection and gain unauthorized access to the target account

1. Steal sensitive information, perform fraudulent transactions, or launch further attacks

# Instructions

1. 

**Code**: [[{
    "otp":[
        "1234",
        "1111",
    ]]

> This command provides an array of OTPs, which can be obtained through various means such as phishing, social engineering, or brute-forcing. The user is instructed to enter one of the valid OTPs to bypass 2FA protection and gain unauthorized access to the target account.

**Command** ([[OTP Verification]]):

```bash
{
    "otp":[
        "1234",
        "1111",
        "1337", // GOOD OTP
        "2222",
        "3333",
        "4444",
        "5555"
    ]
}
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Two-Factor Authentication Interception|T1111 - Two-Factor Authentication Interception]]

## Commands Used

- [[OTP Verification]]

## Tags

- [[2FA Bypasses]]
- [[Account Takeover]]
- [[Bypass 2FA with array]]
