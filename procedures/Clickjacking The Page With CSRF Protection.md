---
id: 4834f5d8-9b59-401c-91fb-c461f6e8920a
name: Clickjacking The Page With CSRF Protection
type: procedure
verified: true
submitted: true
created_at: '2020-08-05T19:10:56.237124+00:00'
updated_at: '2023-05-26T01:32:33.498880+00:00'
platforms:
- Web
tags:
- '[[Clickjacking]]'
- '[[Web Applications]]'
---

# Clickjacking The Page With CSRF Protection

**Status**: ✓ Verified

## Summary

Using clickjacking attack technique , an attacker will create a malicious site  and embed the application into the malicious site. Malicious site link will be sent to victim through social engineering techniques.Upon accessing the malicious site ,victim  will perform the actions that he didn't inte

## Description

# Description

Using clickjacking attack technique , an attacker will create a malicious site  and embed the application into the malicious site. Malicious site link will be sent to victim through social engineering techniques.Upon accessing the malicious site ,victim  will perform the actions that he didn't intend to do. In this case , victim was made to delete his account through clickjacking even though CSRF protection for the page is enabled.



# Instructions





1. Create a legitimate account as user of the application and login.







![9e5d31ec-1264-4aef-987a-ff2ea4bd0b5b.PNG](_assets/images/Mash/9e5d31ec-1264-4aef-987a-ff2ea4bd0b5b.PNG)





2. Click on* Account actions *after successful login.









![f6624d88-940a-4f1d-8eab-81932965c7b0.PNG](_assets/images/Mash/f6624d88-940a-4f1d-8eab-81932965c7b0.PNG)









3.  *Account actions* has *Delete account* option . Right click on the page and select inspect element to look into *delete account* button. Observe that *Delete account* button has CSRF token hidden in the post login form.









![ed517df8-b5f4-4b39-add4-dc2091c884d9.PNG](_assets/images/Mash/ed517df8-b5f4-4b39-add4-dc2091c884d9.PNG)





4. Frame the malicious website in such a way that the *click me  *should exactly align with *Delete account *of the application. Observe that opacity is set to 0.1 to make the actual application invisible to the victim. Save the code as HTML.







**Code**: [[<style>
   iframe {
       position:relative;
 ]]







5. Sent the malicious HTML page to the victim through social engineering. Observe that whenever you hover on to click me for prize money , hand symbol is displayed indicating the div element.









![4fe5e20d-364e-49ed-b0cf-531934978cc6.PNG]()









6.Upon clicking on *Click me for prize money, *logged in victim will unknowingly deletes his account from the application. When the victim tries to access the valid account , he can no longer access it .It displays Unauthorized message







![99c8b887-16d4-4ffb-9f6d-3f9cb36fc44f.PNG](_assets/images/Mash/99c8b887-16d4-4ffb-9f6d-3f9cb36fc44f.PNG)









## Platforms

- Web

## Tags

- [[Clickjacking]]
- [[Web Applications]]


