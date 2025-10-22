---
id: 1905bafa-2be4-4c39-a837-1e5809b1f180
name: dir Recursive Search for Files and Folders
type: command
executor: command_prompt
data: dir /s "$_FILENAME"
output: "C:\\Users>dir /s \"secrets.txt\"\n Volume in drive C has no label.\n Volume\
  \ Serial Number is 8A74-7377\n\n Directory of C:\\Users\\Bob\\Desktop\n\n11/26/2019\
  \  08:19 AM             1,328 secrets.txt\n               1 File(s)         1,328\
  \ bytes\n\n     Total Files Listed:\n               1 File(s)              8 bytes\n\
  \               0 Dir(s)  34,972,065,792 bytes free"
created_at: '2019-11-26T16:37:00.743722+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# dir Recursive Search for Files and Folders

```command_prompt
dir /s "$_FILENAME"
```

## Expected Output

```
C:\Users>dir /s "secrets.txt"
 Volume in drive C has no label.
 Volume Serial Number is 8A74-7377

 Directory of C:\Users\Bob\Desktop

11/26/2019  08:19 AM             1,328 secrets.txt
               1 File(s)         1,328 bytes

     Total Files Listed:
               1 File(s)              8 bytes
               0 Dir(s)  34,972,065,792 bytes free
```
