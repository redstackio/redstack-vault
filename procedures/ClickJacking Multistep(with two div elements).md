---
id: 43d94c91-f8ab-45b3-9d5e-2cf14ed0be53
name: ClickJacking Multistep(with two div elements)
type: procedure
verified: true
submitted: true
created_at: '2020-08-30T19:03:28.331412+00:00'
updated_at: '2023-05-26T15:58:46.530261+00:00'
platforms:
- Web
tags:
- '[[Clickjacking]]'
- '[[Web Applications]]'
---

# ClickJacking Multistep(with two div elements)

**Status**: ✓ Verified

## Summary

In this kind of attack , an attacker will design more than one div elament to trick the user to click on them one after other to make him perform malicious activity. 

## Description

# Description

In this kind of attack , an attacker will design more than one div elament to trick the user to click on them one after other to make him perform malicious activity.



# Instructions



1. Login to the account with the credentials provided





![d536cfea-892f-4463-884c-8f5202e544c9.png](_assets/images/Mash/d536cfea-892f-4463-884c-8f5202e544c9.png)





2.Navigate to the account actions and intercept the *Delete account* request using burp . Copy the url of the delete account request.





![2aad5522-b73b-47b9-9db1-1b3f19f85d3b.png](_assets/images/Mash/2aad5522-b73b-47b9-9db1-1b3f19f85d3b.png)





3.Use the below code to create a clickjacking iframe with two div elements.Make sure to aligh the two div elements  with DELETE Account button and account deletion confirmation button. 







**Code**: [[<style>
   iframe {
       position:relative;
 ]]







4.Deliver the above exploit to the victim. Victim unknowingly clicks on* test me first *which is aligned with*** Delete Account** *in the iframe(not visible to victim since its opacity is set to minimal) and then it asks for the confirmation to delete the account . The confirmation button is aligned with* test me next* button of the iframe and when clicked by victim will delete his account 







## Platforms

- Web

## Tags

- [[Clickjacking]]
- [[Web Applications]]


