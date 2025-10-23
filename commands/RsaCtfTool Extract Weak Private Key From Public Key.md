---
id: 76e5cf19-2dd6-43a7-ab4b-826623577ae5
name: RsaCtfTool Extract Weak Private Key From Public Key
type: command
executor: ''
data: RsaCtfTool.py --publickey $_ID_RSA.PUB --private
output: "root@kali:~# RsaCtfTool.py --publickey id_rsa.pub --private \n-----BEGIN\
  \ RSA PRIVATE KEY-----\nMEACAQACCQDD64wMfTAXyQIDAQABAgkAmQ9sWPcrgAECBQDqTOZNAgUA1hCtbQIF\n\
  AOoSU00CBAKc8YECBQC+C9IL\n-----END RSA PRIVATE KEY-----"
created_at: '2019-09-27T21:57:34.945990+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# RsaCtfTool Extract Weak Private Key From Public Key

```bash
RsaCtfTool.py --publickey $_ID_RSA.PUB --private
```

## Expected Output

```
root@kali:~# RsaCtfTool.py --publickey id_rsa.pub --private 
-----BEGIN RSA PRIVATE KEY-----
MEACAQACCQDD64wMfTAXyQIDAQABAgkAmQ9sWPcrgAECBQDqTOZNAgUA1hCtbQIF
AOoSU00CBAKc8YECBQC+C9IL
-----END RSA PRIVATE KEY-----
```


