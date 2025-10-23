---
id: d489492e-1a45-4547-82fa-f5c5312de3a6
name: DOM Based Open Redirection
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T17:11:33.744195+00:00'
updated_at: '2023-05-26T18:29:40.266104+00:00'
platforms:
- Web
tags:
- '[[DOM Based Open Redirection]]'
- '[[Open Redirection]]'
- '[[Web Applications]]'
---

# DOM Based Open Redirection

**Status**: ✓ Verified

## Summary

An attacker will manipulate a script which can be overwritten that triggers the cross-domain navigation. 

## Description

# Description

An attacker will manipulate a script which can be overwritten that triggers the cross-domain navigation. 



# Instructions

# 

1. Navigate the bottom of the page where there is a option to click on* back to blog *which takes you to the home page of the application. Right click on *back to blog*  and select *inspec*t in chrome web browser.



Observe that *location.href* doesn't have any validation checks in place which can be used to trigger the cross-domain navigation.



Few sinks that can be used are:



*location
location.host
location.hostname
location.href
location.pathname
location.search*





![0023b349-d734-4f0c-a1e3-00b815f168e5.PNG](_assets/images/Mash/0023b349-d734-4f0c-a1e3-00b815f168e5.PNG)







2.  Craft a url as below to have cross-domain navigation.







**Code**: [[https://ac331f0d1eed796680651b22000b0008.web-secur]]







3. Load the url from step 2 in the browser . After the page is loaded , navigate to bottom of the page where *back to blog  *is visible.





![c34eea48-521c-42cb-91bb-334e722eaa3f.PNG](_assets/images/Mash/c34eea48-521c-42cb-91bb-334e722eaa3f.PNG)





4. Click on the *back to blog * which is supposed to take to home page of the application will make a cross-domain request to the attacker specified url. In this case the modified url is* www.blackhat.com.*







![eec6f921-8c81-45a8-8a83-ac57df95a0b3.PNG](_assets/images/Mash/eec6f921-8c81-45a8-8a83-ac57df95a0b3.PNG)





## Platforms

- Web

## Tags

- [[DOM Based Open Redirection]]
- [[Open Redirection]]
- [[Web Applications]]


