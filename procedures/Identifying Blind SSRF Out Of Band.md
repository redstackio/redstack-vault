---
id: 14f90ae4-8fca-4514-9e15-3a68ff8ae9b0
name: Identifying Blind SSRF Out Of Band
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T10:00:54.169116+00:00'
updated_at: '2023-05-26T01:10:01.246777+00:00'
platforms:
- Web
tags:
- '[[Outof Band]]'
- '[[SSRF]]'
- '[[Web Applications]]'
---

# Identifying Blind SSRF Out Of Band

**Status**: ✓ Verified

## Summary

An attacker can exploit the ssrf by issuing backend HTTP request to the application , but the response from the backend request is not returned in the application's response. 

## Description

# Description

An attacker can exploit the ssrf by issuing backend HTTP request to the application , but the response from the backend request is not returned in the application's response.

# Instructions

1. Start the Collaborator in Burp Suite  professional and click on *copy to clipboard* to copy the collaborator URL.

2. Intercept the following request and right click on the request and select *send to repeater*

3.Modify the referer header to the* colloborator URL*  from step 1 and send the request to server in repeater tab .

4.Go back to the Burp Collaborator client window, and click "Poll now". You should see some DNS and HTTP interactions that were initiated by the application as the result of your payload.

## Platforms

- Web

## Tags

- [[Outof Band]]
- [[SSRF]]
- [[Web Applications]]
