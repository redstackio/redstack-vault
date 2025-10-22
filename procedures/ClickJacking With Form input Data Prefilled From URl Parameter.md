---
id: 3f3c90bf-f871-46dd-806a-d334a030c7fb
name: ClickJacking With Form input Data Prefilled From URl Parameter
type: procedure
verified: true
submitted: true
created_at: '2020-08-30T17:52:59.129259+00:00'
updated_at: '2023-05-26T01:37:07.208976+00:00'
platforms:
- Web
tags:
- '[[Clickjacking]]'
- '[[Web Applications]]'
---

# ClickJacking With Form input Data Prefilled From URl Parameter

**Status**: ✓ Verified

## Summary

An attacker can change the emailID of the user using clickjacking with the emailID provided in the exploit code that is sent to victim 

## Description

# Description

 An attacker can change the emailID of the user using clickjacking with the emailID provided in the exploit code that is sent to victim

# Instructions

1. Login to account using given credentials.

2. Access Change email tab and observe the parameters and url while sending request to change the email.

3.Now, with observations from above step craft a malicious frame that will have a form with prefilled data which when accessed by the victim will change the victim's emailID.

**Code**: [[<style>
   iframe {
       position:relative;
 ]]

4. Deliver this malicious exploit to the victim. When victim clicks on the *clickme *which is aligned to *update email* button of the application , emailId of the victim gets changed with the emailID from the code in step3.

## Platforms

- Web

## Tags

- [[Clickjacking]]
- [[Web Applications]]
