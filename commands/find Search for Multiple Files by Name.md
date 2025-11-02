---
id: fa95c869-e0e8-432a-8cf5-694899e91028
name: find Search for Multiple Files by Name
type: command
executor: ''
data: find $_DIRECTORY -name $_FILE1 -o name $_FILE2 -o -name $_FILE3 2>/dev/null
output: 'root@hackers:~# find . -name "user.txt" -o -name "root.txt" -o -name "proof.txt"
  2>/dev/null

  ./user.txt

  ./proof.txt

  ./root.txt

  '
created_at: '2019-09-17T06:24:10.223849+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[find]]'
---

# find Search for Multiple Files by Name

```bash
find $_DIRECTORY -name $_FILE1 -o name $_FILE2 -o -name $_FILE3 2>/dev/null
```

## Expected Output

```
root@hackers:~# find . -name "user.txt" -o -name "root.txt" -o -name "proof.txt" 2>/dev/null
./user.txt
./proof.txt
./root.txt

```


