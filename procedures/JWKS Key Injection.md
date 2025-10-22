---
id: ebaa8c52-cc54-44d0-8610-db22a9b1e54b
name: JWKS Key Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.822697+00:00'
updated_at: '2023-04-10T20:22:37.630586+00:00'
tags:
- '[[JWKS - jku header injection]]'
- '[[JWT Claims]]'
- '[[JWT - JSON Web Token]]'
---

# JWKS Key Injection

## Summary

JWKS Key Injection is a technique used by attackers to sign a JWT token with an attacker-controlled Public Key. By injecting a URL pointing to a malicious JWKS file in the "jku" header, the attacker can trick the service into verifying the token with the malicious Public Key. This technique can be 

## Description

# Description

JWKS Key Injection is a technique used by attackers to sign a JWT token with an attacker-controlled Public Key. By injecting a URL pointing to a malicious JWKS file in the "jku" header, the attacker can trick the service into verifying the token with the malicious Public Key. This technique can be used to bypass authentication and authorization controls, allowing an attacker to impersonate a legitimate user and gain access to sensitive data or systems.

## Requirements

1. Access to the target service

## Defense

1. Implement proper input validation and sanitization to prevent injection attacks

1. Use a secure algorithm to sign the JWT token

1. Use a secure method to store and retrieve the Public Key, such as a Hardware Security Module (HSM)

## Objectives

1. Sign a JWT token with an attacker-controlled Public Key

1. Bypass authentication and authorization controls

1. Impersonate a legitimate user

# Instructions

1. 

**Code**: [[{
    "keys": [
        {
            "kid": "beae]]

> The "jku" header value points to the URL of the JWKS file. By replacing the "jku" URL with an attacker-controlled URL containing the Public Key, an attacker can use the paired Private Key to sign the token and let the service retrieve the malicious Public Key and verify the token.

## Tags

- [[JWKS - jku header injection]]
- [[JWT Claims]]
- [[JWT - JSON Web Token]]
