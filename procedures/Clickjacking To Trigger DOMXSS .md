---
id: 1f1c3fdb-9b71-4cc2-b4e2-a258cc2737f9
name: 'Clickjacking To Trigger DOMXSS '
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T13:44:54.835230+00:00'
updated_at: '2023-05-26T01:08:24.176872+00:00'
platforms:
- Web
tags:
- '[[Clickjacking]]'
- '[[DOM XSS]]'
- '[[Web Applications]]'
---

# Clickjacking To Trigger DOMXSS 

**Status**: ✓ Verified

## Summary

In this attack, an attacker will frame a clickjacking  page that makes the victim to click on the malicious page and trigger the DOM XSS that alerts the document.cookie. 

## Description

# Description

In this attack, an attacker will frame a clickjacking  page that makes the victim to click on the malicious page and trigger the DOM XSS that alerts the document.cookie.





# Instructions



1.   Observe the submit feedback form in the application . 





![c2f91558-5449-471b-a153-5bb08f947e7a.PNG]()



2. Craft a click jacking page for the application considering all the fields in the feedback form.



Adjust the attribute values to display* click me* message on top of the submit button to trick the victim to click on the page. Also adjust the opacity level.



Observe the DOM XSS payload in the name filed .

 



**Code**: [[<style>
   iframe {
       position:relative;
 ]]







3. Save the code as HTML page and deliver it to the victim through social engineering .  Observe the fields being filled with values from code in step 2.



Note: Opacity is increased to show the values in the fields. In real time attacker will keep the opacity level to minimum to hide all the fields.





![3e88c613-e327-46a3-8f61-0a25b523426a.PNG]()







4.  A victim upon clicking the click here for prize will unknowingly trigger the DOMXSS *payload . *In this case payload is* <img src=1 onerror=alert(1) >. *





*Note : If victim is logged into the application and the payload is to steal the cookie using (document .cookie), , an attacker will steal victim's cookies and login into impersonating the victim .*



![68ca024e-65f8-4b25-9869-36d922d49087.PNG]()









## Platforms

- Web

## Tags

- [[Clickjacking]]
- [[DOM XSS]]
- [[Web Applications]]


