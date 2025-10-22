---
id: 40c17768-34cb-40ad-8f18-a0bd1018a52e
name: guestmount Mount a VHD file
type: command
executor: bash
data: guestmount --add $_IMAGE.vhd --inspector --ro $_DEST_DIRECTORY
output: guestmount --add 5c2dcac3-335e-14a3-a34c-604e6b6e6969.vhd  --inspector --ro
  /mnt
created_at: '2019-10-11T22:11:00.200134+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# guestmount Mount a VHD file

```bash
guestmount --add $_IMAGE.vhd --inspector --ro $_DEST_DIRECTORY
```

## Expected Output

```
guestmount --add 5c2dcac3-335e-14a3-a34c-604e6b6e6969.vhd  --inspector --ro /mnt
```
