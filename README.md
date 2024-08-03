# configs-and-dotfiles

### Command to find microarch:
```shell
gcc -march=native -Q --help=target|grep march
```
### Archive YT videos (req aria2):
```shell
yt-dlp --downloader aria2c --embed-metadata  --embed-subs  --sub-lang "en.*" --write-auto
-sub   --convert-subs 'srt' --embed-thumbnail <insert url here>
```
