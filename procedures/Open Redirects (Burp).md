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

2. Configure Burp proxy in the browser and turn off the intercept option. Browse through the application pages.

3. In Burp, under Target tab, click on the application URL as shown below. The pages accessed in the browser can be observed in the right panel.

4. Under the sitemap, filter the status code to display only the responses with status code 3xx. 

5. Filtered list with 302 response code can be observed in the below screenshot

6. Right-click on any URL and send it to repeater.

8. Replace the existing *url* parameter value with some malicious URL and click on follow redirection.

9. Right-click on the response window and select *Copy URL* option 

10. Paste the copied URL in the browser window

11. It can be observed that the original request is redirected to modified malicious website.

## Platforms

- Web

## Tags

- [[Open Redirection]]
- [[Open Redirects]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
