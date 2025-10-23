---
id: e3a1cae5-7017-4b84-8562-8aa7e4eaceab
name: Extract name and sha1 from .git/index using gin and egrep
type: command
executor: bash
data: "$ gin .git/index | egrep -e \"name|sha1\" \nname = AWS Amazon Bucket S3/README.md\n\
  sha1 = 862a3e58d138d6809405aa062249487bee074b98\n\nname = CRLF injection/README.md\n\
  sha1 = d7ef4d77741c38b6d3806e0c6a57bf1090eec141"
output: null
created_at: '2023-04-06T03:55:59.852793+00:00'
updated_at: '2023-04-10T20:33:54.205231+00:00'
---

# Extract name and sha1 from .git/index using gin and egrep

```bash
$ gin .git/index | egrep -e "name|sha1" 
name = AWS Amazon Bucket S3/README.md
sha1 = 862a3e58d138d6809405aa062249487bee074b98

name = CRLF injection/README.md
sha1 = d7ef4d77741c38b6d3806e0c6a57bf1090eec141
```


