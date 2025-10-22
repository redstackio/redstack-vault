---
id: e8bad82f-9c87-414b-b192-8d7148f4ec39
name: Git List a Git Repository's Commit History
type: command
executor: bash
data: git log -p
output: "root@kali:~/ git log -p\ncommit 584d5f1a2f95e117244d9128bff7a579ca1d4968\
  \ (HEAD -> master, origin/master)\nAuthor: bob <bob@corp.net>\nDate:   Sat Oct 29\
  \ 12:01:40 2018 +0530\n\n    changed auth\n\ndiff --git a/src/main/java/com/test.java\
  \ b/src/main/java/com/com/test.java\nnew file mode 100644\nindex 0000000..2789c42\n\
  --- /dev/null\n+++ b/src/main/java/com/test.java\n@@ -0,0 +1,16 @@\n- password kittens;\n\
  +@Service\n+}"
created_at: '2019-10-16T22:13:26.080727+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Git List a Git Repository's Commit History

```bash
git log -p
```

## Expected Output

```
root@kali:~/ git log -p
commit 584d5f1a2f95e117244d9128bff7a579ca1d4968 (HEAD -> master, origin/master)
Author: bob <bob@corp.net>
Date:   Sat Oct 29 12:01:40 2018 +0530

    changed auth

diff --git a/src/main/java/com/test.java b/src/main/java/com/com/test.java
new file mode 100644
index 0000000..2789c42
--- /dev/null
+++ b/src/main/java/com/test.java
@@ -0,0 +1,16 @@
- password kittens;
+@Service
+}
```
