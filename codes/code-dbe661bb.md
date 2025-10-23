---
id: dbe661bb-8420-40d8-9776-5f6a02dfa86f
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:59.928836+00:00'
updated_at: '2023-04-10T20:33:56.613253+00:00'
---

# Code Snippet dbe661bb

**Language**: Powershell

```powershell
./diggit.py -u remote_git_repo -t temp_folder -o object_hash [-r=True]
./diggit.py -u http://web.site -t /path/to/temp/folder/ -o d60fbeed6db32865a1f01bb9e485755f085f51c1

-u is remote path, where .git folder exists
-t is path to local folder with dummy Git repository and where blob content (files) are saved with their real names (cd /path/to/temp/folder && git init)
-o is a hash of particular Git object to download
```


