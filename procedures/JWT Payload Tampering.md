---
id: 1fb3ac43-62f1-4f11-9c90-74c9402fa8e2
name: JWT Payload Tampering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.520091+00:00'
updated_at: '2023-04-10T20:22:38.022701+00:00'
tags:
- '[[JWT Format]]'
- '[[JWT - JSON Web Token]]'
- '[[Payload]]'
commands:
- '[[Decode JWT]]'
---

# JWT Payload Tampering

## Summary

JWT tokens are used for authentication and authorization purposes. An attacker can tamper with the payload of a JWT token to gain unauthorized access to an application or system. By modifying the payload, an attacker can change the user's role or privileges, bypassing access controls and gaining ac

## Description

# Description

JWT tokens are used for authentication and authorization purposes. An attacker can tamper with the payload of a JWT token to gain unauthorized access to an application or system. By modifying the payload, an attacker can change the user's role or privileges, bypassing access controls and gaining access to sensitive data. Technical details include modifying the payload of the JWT token, which is typically encoded in Base64.

## Requirements

1. Access to a JWT token

## Defense

1. Use strong encryption to protect JWT tokens

1. Implement access controls to restrict access to sensitive data

1. Monitor for suspicious activity, such as multiple failed login attempts or unusual user behavior

## Objectives

1. Gain unauthorized access to an application or system

1. Bypass access controls

1. Gain access to sensitive data

# Instructions

1. Modify the payload value of the JWT token

**Code**: [[python3 jwt_tool.py JWT_HERE -I -pc payload1 -pv t]]

> The -I flag tells the tool to modify the token in place. The -pc flag specifies the name of the payload claim to modify, and the -pv flag specifies the new value for the claim.

**Command** ([[Decode JWT]]):

```bash
python3 jwt_tool.py JWT_HERE -I
```

## Commands Used

- [[Decode JWT]]

## Tags

- [[JWT Format]]
- [[JWT - JSON Web Token]]
- [[Payload]]
