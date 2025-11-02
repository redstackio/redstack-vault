---
id: 074c76c5-56de-49ac-b522-4c7621c8a549
name: Docker Mount a Host's Root Directory in a Container
type: command
executor: bash
data: docker run -v /:/root_fs -i -t bash bash
output: "alice@kali:~$ docker run -v /:/root_fs -i -t bash bash\nUnable to find image\
  \ 'bash:latest' locally\nlatest: Pulling from library/bash\n9d48c3bd43c5: Pull complete\
  \ \n7dd01fd971d4: Pull complete \n691cfbca5227: Pull complete \nDigest: sha256:b7648de8f07dd0de784e19f058f3e30c4b2890ef7be3994b4226cdd194871d78\n\
  Status: Downloaded newer image for bash:latest\nbash-5.0# ls /root_fs/\nbin    \
  \         etc             initrd.img.old  lib64           media           proc \
  \           run             sys             var\nboot            home          \
  \  lib             libx32          mnt             retdec          sbin        \
  \    tmp             vmlinuz\ndev             initrd.img      lib32           lost+found\
  \      opt             root            srv             usr             vmlinuz.old"
created_at: '2019-10-09T19:15:07.838000+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Docker]]'
- '[[find]]'
- '[[host]]'
- '[[mount]]'
---

# Docker Mount a Host's Root Directory in a Container

```bash
docker run -v /:/root_fs -i -t bash bash
```

## Expected Output

```
alice@kali:~$ docker run -v /:/root_fs -i -t bash bash
Unable to find image 'bash:latest' locally
latest: Pulling from library/bash
9d48c3bd43c5: Pull complete 
7dd01fd971d4: Pull complete 
691cfbca5227: Pull complete 
Digest: sha256:b7648de8f07dd0de784e19f058f3e30c4b2890ef7be3994b4226cdd194871d78
Status: Downloaded newer image for bash:latest
bash-5.0# ls /root_fs/
bin             etc             initrd.img.old  lib64           media           proc            run             sys             var
boot            home            lib             libx32          mnt             retdec          sbin            tmp             vmlinuz
dev             initrd.img      lib32           lost+found      opt             root            srv             usr             vmlinuz.old
```


