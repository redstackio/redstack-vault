---
id: 9e0c8754-6f4c-46bb-8058-889882772681
name: PHP Deserialization POP Chain Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.384748+00:00'
updated_at: '2023-04-06T03:55:59.397307+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Finding and using gadgets]]'
- '[[PHP Deserialization]]'
---

# PHP Deserialization POP Chain Attack

## Summary

A PHP Deserialization POP Chain Attack is a type of attack that involves taking advantage of the PHP deserialization process to execute arbitrary code. This attack involves finding and using gadgets, which are pieces of code that can be chained together to create a payload that can be executed on t

## Description

# Description

A PHP Deserialization POP Chain Attack is a type of attack that involves taking advantage of the PHP deserialization process to execute arbitrary code. This attack involves finding and using gadgets, which are pieces of code that can be chained together to create a payload that can be executed on the target system. The attack can be used to gain access to sensitive data or to take control of the target system.

 

## Requirements

1. Access to the target system

1. Knowledge of PHP deserialization process

1. Knowledge of gadgets

 

## Defense

1. Ensure that all applications are up-to-date and patched

1. Use input validation to ensure that only valid data is deserialized

1. Implement code signing to ensure that only trusted code is executed

 

## Objectives

1. Execute arbitrary code on the target system

1. Gain access to sensitive data

1. Take control of the target system

 

# Instructions

1. 1. Identify a vulnerable application that uses PHP deserialization.
2. Identify a gadget chain that can be used to execute arbitrary code.
3. Craft a payload using the gadget chain.
4. Inject the payload into the vulnerable application.
5. Trigger the deserialization process to execute the payload.

 



**Code**: [[&quot;PHP POP Chains&quot;]]



> The 'PHP POP Chains' command can be used to identify and use gadgets to create a payload that can be executed on the target system. The command requires knowledge of the PHP deserialization process and the ability to identify vulnerable applications. Once a vulnerable application is identified, the command can be used to craft a payload and inject it into the application. The payload can then be triggered to execute the arbitrary code.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Tags

- [[Finding and using gadgets]]
- [[PHP Deserialization]]


