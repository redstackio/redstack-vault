---
id: 1217b482-462d-47ba-9949-dac6e4658c3f
name: Cross-Site Request Forgery with File Upload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:55.481148+00:00'
updated_at: '2023-04-06T03:55:55.494984+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[SSH Hijacking|T1184 - SSH Hijacking]]'
tags:
- '[[Cross-Site Request Forgery]]'
- '[[HTML POST - multipart/form-data with file upload - Requiring User Interaction]]'
- '[[Payloads]]'
---

# Cross-Site Request Forgery with File Upload

## Summary

Cross-Site Request Forgery with File Upload is a type of attack where an attacker tricks a victim into submitting a form that contains malicious code to a targeted web application. The malicious code is usually embedded in a file upload field, which the attacker convinces the victim to upload. Once

## Description

# Description

Cross-Site Request Forgery with File Upload is a type of attack where an attacker tricks a victim into submitting a form that contains malicious code to a targeted web application. The malicious code is usually embedded in a file upload field, which the attacker convinces the victim to upload. Once the victim uploads the file, the malicious code is executed, and the attacker can perform actions on behalf of the victim. This attack requires the victim to be authenticated to the targeted web application, and the attacker to have knowledge of the victim's session cookie.

 

## Requirements

1. Access to a vulnerable web application.

1. Knowledge of the victim's session cookie.

 

## Defense

1. Implement and enforce the use of anti-CSRF tokens to prevent unauthorized form submissions.

1. Implement and enforce the use of Content Security Policy (CSP) to prevent the execution of malicious code.

1. Monitor web application logs and network traffic for suspicious activity.

 

## Objectives

1. To perform unauthorized actions on behalf of the victim on the targeted web application.

1. To steal sensitive information from the targeted web application.

 

# Instructions

1. Fill in the <target> field with the URL of the targeted web application.

 



**Code**: [[<script>
function launch(){
    const dT = new Dat]]



> This command generates an HTML form with a file upload field that contains malicious code. The victim is tricked into uploading the file, which executes the malicious code and performs unauthorized actions on behalf of the victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[SSH Hijacking|T1184 - SSH Hijacking]]

## Tags

- [[Cross-Site Request Forgery]]
- [[HTML POST - multipart/form-data with file upload - Requiring User Interaction]]
- [[Payloads]]


