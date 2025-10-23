---
id: 01774f0d-8c64-4893-a8a1-98fc91c25402
name: Open Redirects (Burp)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T14:16:33.054961+00:00'
updated_at: '2023-05-26T01:23:25.867376+00:00'
platforms:
- Web
tags:
- '[[Open Redirection]]'
- '[[Open Redirects]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Open Redirects (Burp)

**Status**: ✓ Verified

## Summary

Open redirects can be tested through the parameters that accept URLs/files as input and redirect to the specified website. 

## Description

# Description

Open redirects can be tested through the parameters that accept URLs/files as input and redirect to the specified website.

# 

# Instructions



1. Login into the application





![ba878855-9e33-45a5-a8b6-890886f587da.PNG](_assets/images/Mash/ba878855-9e33-45a5-a8b6-890886f587da.PNG)





2. Configure Burp proxy in the browser and turn off the intercept option. Browse through the application pages.





![2f598d8f-1684-4135-bdd3-bc013b438e2d.PNG](_assets/images/Mash/2f598d8f-1684-4135-bdd3-bc013b438e2d.PNG)





3. In Burp, under Target tab, click on the application URL as shown below. The pages accessed in the browser can be observed in the right panel.





![a845395b-bc0a-4746-b601-e516e8b2139f.PNG](_assets/images/Mash/a845395b-bc0a-4746-b601-e516e8b2139f.PNG)











4. Under the sitemap, filter the status code to display only the responses with status code 3xx. 







![59b78b8a-b96d-46c1-9a05-8826593c5613.PNG](_assets/images/Mash/59b78b8a-b96d-46c1-9a05-8826593c5613.PNG)



5. Filtered list with 302 response code can be observed in the below screenshot





![3677ce81-4d44-4a3a-b83f-0a07ff58ff85.PNG](_assets/images/Mash/3677ce81-4d44-4a3a-b83f-0a07ff58ff85.PNG)





6. Right-click on any URL and send it to repeater.







![d2292f83-336e-460d-bd83-f9e862807837.PNG](_assets/images/Mash/d2292f83-336e-460d-bd83-f9e862807837.PNG)













![aaaffee3-459f-4dae-9674-4a8bfedd288b.PNG](_assets/images/Mash/aaaffee3-459f-4dae-9674-4a8bfedd288b.PNG)





8. Replace the existing *url* parameter value with some malicious URL and click on follow redirection.











9. Right-click on the response window and select *Copy URL* option 









![bd435d0b-6ead-4575-ba6b-d1d133f9cdc6.jpg]()









10. Paste the copied URL in the browser window









![33a750df-3c94-43de-9d29-c66891f37dca.jpg]()







11. It can be observed that the original request is redirected to modified malicious website.









![dd93033e-d420-4a1d-bf1f-79ea9067f35a.jpg]()













## Platforms

- Web

## Tags

- [[Open Redirection]]
- [[Open Redirects]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


