---
id: bd20f96b-5857-4e69-a256-520d67e7794c
name: Search for JS files and old links
type: command
executor: bash
data: curl -sX GET "http://web.archive.org/cdx/search/cdx?url=<targetDomain.com>&output=text&fl=original&collapse=urlkey&matchType=prefix"
output: null
created_at: '2023-04-06T03:56:21.737347+00:00'
updated_at: '2023-04-10T20:21:17.936731+00:00'
---

# Search for JS files and old links

```bash
curl -sX GET "http://web.archive.org/cdx/search/cdx?url=<targetDomain.com>&output=text&fl=original&collapse=urlkey&matchType=prefix"
```


