---
id: 6b52c8a8-28b4-4008-8932-d353b94d7d11
name: Steghide Embed a File in an Image
type: command
executor: bash
data: steghide embed -ef $_EMBEDDED -cf $_COVER
output: "root@kali:~# steghide embed -ef id_rsa.pub -cf wallpaper.jpg \nEnter passphrase:\
  \ \nRe-Enter passphrase: \nembedding \"id_rsa.pub\" in \"wallpaper.jpg\"... done"
created_at: '2019-10-10T00:28:44.037684+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Steghide Embed a File in an Image

```bash
steghide embed -ef $_EMBEDDED -cf $_COVER
```

## Expected Output

```
root@kali:~# steghide embed -ef id_rsa.pub -cf wallpaper.jpg 
Enter passphrase: 
Re-Enter passphrase: 
embedding "id_rsa.pub" in "wallpaper.jpg"... done
```


