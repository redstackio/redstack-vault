---
id: 83ac42d3-9820-471d-8d22-f18b1c20a861
name: Clone and Build Hashcat
type: command
executor: bash
data: git clone https://github.com/hashcat/hashcat.git && cd hashcat && make -j 8
  && make install
output: null
created_at: '2023-04-06T03:56:17.538016+00:00'
updated_at: '2023-04-06T03:56:17.546420+00:00'
---

# Clone and Build Hashcat

```bash
git clone https://github.com/hashcat/hashcat.git && cd hashcat && make -j 8 && make install
```
