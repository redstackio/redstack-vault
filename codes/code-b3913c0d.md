---
id: b3913c0d-f70d-4bdd-afde-d74796b01309
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:36.369157+00:00'
updated_at: '2023-04-10T20:24:17.694912+00:00'
---

# Code Snippet b3913c0d

**Language**: Powershell

```powershell
sqlmap -u "http://example.com/" --crawl=1 --random-agent --batch --forms --threads=5 --level=5 --risk=3

--batch = non interactive mode, usually Sqlmap will ask you questions, this accepts the default answers
--crawl = how deep you want to crawl a site
--forms = Parse and test forms
```


