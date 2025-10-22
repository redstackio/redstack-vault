---
id: 9b302fce-45a8-4f81-99e0-b28c15ab1862
type: code
language: JavaScript
verified: false
created_at: '2023-04-06T03:56:40.534332+00:00'
updated_at: '2023-04-06T03:56:40.549324+00:00'
---

# Code Snippet 9b302fce

**Language**: JavaScript

```javascript
1. Attacker posts a link to a website under his control that contains the following JS code: window.opener.location = "http://evil.com"
2. He tricks the victim into visiting the link, which is opened in the browser in a new tab.
3. At the same time the JS code is executed and the background tab is redirected to the website evil.com, which is most likely a phishing website.
4. If the victim opens the background tab again and doesn't look at the address bar, it may happen that he thinks he is logged out, because a login page appears, for example.
5. The victim tries to log on again and the attacker receives the credentials
```
