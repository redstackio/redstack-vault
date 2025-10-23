---
id: 96ed686b-3be6-412e-bc3e-45f489b79ae8
name: JWT Token Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.494269+00:00'
updated_at: '2023-04-10T20:22:33.109807+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[JWT Format]]'
- '[[JWT - JSON Web Token]]'
- '[[Payload]]'
---

# JWT Token Creation

## Summary

JWT tokens are used to securely transmit information between parties. They are commonly used in web applications to authenticate users and transmit sensitive information. A JWT token consists of three parts - header, payload, and signature. The payload contains the actual data that is transmitted. 

## Description

# Description

JWT tokens are used to securely transmit information between parties. They are commonly used in web applications to authenticate users and transmit sensitive information. A JWT token consists of three parts - header, payload, and signature. The payload contains the actual data that is transmitted. This procedure involves creating a JWT token with a specified payload. The token can then be used to authenticate a user or transmit sensitive information.

 

## Requirements

1. Access to a system or application that can generate JWT tokens

 

## Defense

1. Use secure JWT libraries and tools to generate tokens

1. Encrypt sensitive information before transmitting it using a JWT token

1. Implement proper token validation and expiration to prevent unauthorized access

 

## Objectives

1. Create a JWT token with a specified payload

1. Authenticate a user or transmit sensitive information using the JWT token

 

# Instructions

1. To create a JWT token, use a JWT library or tool to generate a token with the desired payload. The payload should include the necessary information for authentication or transmission of sensitive information. In this example, we are creating a token with a subject (sub) of 1234567890, a name of Amazing Haxx0r, an expiration time (exp) of 1466270722, and an admin flag set to true.

 



**Code**: [[{
    "sub":"1234567890",
    "name":"Amazing Haxx]]



> The payload of a JWT token contains the data that is transmitted. In this example, we are creating a token with a subject (sub) of 1234567890, a name of Amazing Haxx0r, an expiration time (exp) of 1466270722, and an admin flag set to true. This payload can be customized to include any data that needs to be transmitted.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Tags

- [[JWT Format]]
- [[JWT - JSON Web Token]]
- [[Payload]]


