---
id: b8d49e7d-de84-48e9-82bb-c7aea8c6296d
name: JWT Header Manipulation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.474590+00:00'
updated_at: '2023-04-10T20:22:32.748314+00:00'
tags:
- '[[Header]]'
- '[[JWT Format]]'
- '[[JWT - JSON Web Token]]'
commands:
- '[[Add JWT headers]]'
---

# JWT Header Manipulation

## Summary

JWT Header Manipulation is a technique used to modify the header of a JSON Web Token (JWT). JWTs are used to securely transmit information between parties as a JSON object. The header of a JWT contains information about the algorithm used to sign the token and the type of token. By manipulating the

## Description

# Description

JWT Header Manipulation is a technique used to modify the header of a JSON Web Token (JWT). JWTs are used to securely transmit information between parties as a JSON object. The header of a JWT contains information about the algorithm used to sign the token and the type of token. By manipulating the header, an attacker can change the algorithm used to sign the token, which can result in the token being accepted as valid when it is not. This technique can be used to gain unauthorized access to a system or to elevate privileges.

## Requirements

1. Access to a JWT

1. Knowledge of the JWT header structure

1. jwt_tool.py installed

## Defense

1. Use a strong algorithm to sign JWTs

1. Verify the signature of a JWT before accepting it as valid

1. Implement proper input validation to prevent header manipulation

## Objectives

1. Modify the header of a JWT to bypass authentication or elevate privileges

1. Gain unauthorized access to a system

# Instructions

1. 

**Code**: [[{
    "typ": "JWT",
    "alg": "HS256"
}]]

> 

2. To modify the header of a JWT, run the following command:

**Code**: [[python3 jwt_tool.py JWT_HERE -I -hc header1 -hv te]]

> This command will modify the header of the JWT by setting the value of 'header1' to 'testval1' and the value of 'header2' to 'testval2'.

**Command** ([[Add JWT headers]]):

```bash
python3 jwt_tool.py JWT_HERE -I -hc header1 -hv testval1 -hc header2 -hv testval2
```

## Commands Used

- [[Add JWT headers]]

## Tags

- [[Header]]
- [[JWT Format]]
- [[JWT - JSON Web Token]]
