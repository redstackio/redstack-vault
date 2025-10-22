---
id: 3c89f835-61ef-426a-8cd3-854091fc0f61
name: Hashcat Generate a Wordlist Using a Mask
type: command
executor: bash
data: hashcat -a 3 --stdout ?d?s?b?a > $OUTPUT.txt
output: hashcat -a 3 --stdout ?d?s?b?a > output.txt
created_at: '2019-10-18T01:13:22.970030+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Hashcat Generate a Wordlist Using a Mask

```bash
hashcat -a 3 --stdout ?d?s?b?a > $OUTPUT.txt
```

## Expected Output

```
hashcat -a 3 --stdout ?d?s?b?a > output.txt
```
