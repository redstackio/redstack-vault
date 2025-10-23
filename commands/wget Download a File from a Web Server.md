---
id: 0fee6e18-062c-4e13-983b-fdbb1a4a6f54
name: wget Download a File from a Web Server
type: command
executor: bash
data: wget http://$_TARGET_IP/$_FILE
output: "root@kali:~/# wget http://10.10.10.10/secrets.txt\n--2020-02-19 20:07:45--\
  \  http://10.10.10.10/secrets.txt\nConnecting to 10.10.10.10:80... connected.\n\
  HTTP request sent, awaiting response... 200 OK\nLength: 26325 (26K) [text/plain]\n\
  Saving to: ‘secrets.txt’\n\nsecrets.txt                                100%[=====================================================================================>]\
  \  25.71K  --.-KB/s    in 0s      \n\n2020-02-19 20:07:45 (155 MB/s) - ‘secrets.txt’\
  \ saved [26325/26325]"
created_at: '2020-03-23T19:45:50.957965+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# wget Download a File from a Web Server

```bash
wget http://$_TARGET_IP/$_FILE
```

## Expected Output

```
root@kali:~/# wget http://10.10.10.10/secrets.txt
--2020-02-19 20:07:45--  http://10.10.10.10/secrets.txt
Connecting to 10.10.10.10:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 26325 (26K) [text/plain]
Saving to: ‘secrets.txt’

secrets.txt                                100%[=====================================================================================>]  25.71K  --.-KB/s    in 0s      

2020-02-19 20:07:45 (155 MB/s) - ‘secrets.txt’ saved [26325/26325]
```


