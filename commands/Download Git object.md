---
id: 3a25a716-8855-491a-ad5e-d9144019e4eb
name: Download Git object
type: command
executor: bash
data: './diggit.py -u remote_git_repo -t temp_folder -o object_hash [-r=True]

  ./diggit.py -u http://web.site -t /path/to/temp/folder/ -o d60fbeed6db32865a1f01bb9e485755f085f51c1


  -u is remote path, where .git folder exists

  -t is path to local folder with dummy Git repository and where blob content (files)
  are saved with their real names (cd /path/to/temp/folder && git init)

  -o is a hash of particular Git object to download'
output: null
created_at: '2023-04-06T03:55:59.928908+00:00'
updated_at: '2023-04-10T20:33:56.614609+00:00'
---

# Download Git object

```bash
./diggit.py -u remote_git_repo -t temp_folder -o object_hash [-r=True]
./diggit.py -u http://web.site -t /path/to/temp/folder/ -o d60fbeed6db32865a1f01bb9e485755f085f51c1

-u is remote path, where .git folder exists
-t is path to local folder with dummy Git repository and where blob content (files) are saved with their real names (cd /path/to/temp/folder && git init)
-o is a hash of particular Git object to download
```


