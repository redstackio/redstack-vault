---
id: df37c377-90df-45e6-8a97-7ddc72bb7e6f
name: CSRF JSON GET Request
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:55.504495+00:00'
updated_at: '2023-04-06T03:55:55.516080+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Hardware Additions|T1200 - Hardware Additions]]'
tags:
- '[[Cross-Site Request Forgery]]'
- '[[JSON GET - Simple Request]]'
- '[[Payloads]]'
---

# CSRF JSON GET Request

## Summary

A Cross-Site Request Forgery (CSRF) JSON GET Request is an attack that leverages a victim's authenticated session to perform unauthorized requests on their behalf. The attacker crafts a malicious web page that sends a GET request to a JSON API endpoint that requires authentication. The victim must 

## Description

# Description

A Cross-Site Request Forgery (CSRF) JSON GET Request is an attack that leverages a victim's authenticated session to perform unauthorized requests on their behalf. The attacker crafts a malicious web page that sends a GET request to a JSON API endpoint that requires authentication. The victim must be logged into the target website for the attack to succeed. The malicious web page sends a GET request to the JSON API endpoint, which returns the victim's sensitive information. The attacker can then use this information to perform further attacks. This attack can be used to steal sensitive data or perform unauthorized actions on behalf of the victim.

## Requirements

1. Victim must be logged into the target website

## Defense

1. Implement SameSite cookies to prevent CSRF attacks

1. Use anti-CSRF tokens to validate requests

1. Implement rate limiting to prevent brute-force attacks

## Objectives

1. Steal sensitive data

1. Perform unauthorized actions on behalf of the victim

# Instructions

1. 

**Code**: [[<script>
var xhr = new XMLHttpRequest();
xhr.open(]]

> This command crafts a malicious web page that sends a GET request to the target's JSON API endpoint. The attacker can modify the URL to point to the API endpoint they want to target. The victim must be logged into the target website for the attack to succeed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Hardware Additions|T1200 - Hardware Additions]]

## Tags

- [[Cross-Site Request Forgery]]
- [[JSON GET - Simple Request]]
- [[Payloads]]
