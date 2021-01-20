# convert-m3u8-to-mkv

## Build The Container

```bash
sudo docker build --tag convert-m3u8-to-mkv .
```

## Run The Container

### Template

```bash
docker run -it --name container-name script-in-container-to-target --input url-path.m3u8 --output name-of-video.mkv
```

### Example

```bash
docker run -it --name convert-m3u8-to-mkv convert-m3u8-to-mkv --input url-path.m3u8 --output name-of-video.mkv
```

## Copy The File From The Container To Your Host Machine

### Template
```bash
docker cp name-of-container:/container/path/target-file /host/path/target-file
```

### Example

```bash
docker cp convert-m3u8-to-mkv:/usr/src/app/temp/nightmare-before-christmas.mkv /Users/loganconnor44/Downloads/nightmare-before-christmas.mkv
```

## Copy The File From A Local Machine To A Remote Machine On The Same Network Through SSH

### Template

```bash
scp /local/path/target-file.txt remote-user@network-address:/remote/pate/target-file.txt
```

### Example

```bash
scp ./nightmare-before-christmas.mkv pi@192.168.1.2:/media/exfat/media/chinese-videos/movies/nightmare-before-christmas.mkv
```

## Stop The Container And Delete The Temporary Video File

### Template

```bash
docker rm name-of-container
```

### Example

```bash
docker rm convert-m3u8-to-mkv
```