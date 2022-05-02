# downloadBilibili
下载bilibili视频

### 安装you-get第三方库

```
pip3 install you-get
```

### 下载视频

```
you-get xxxx      
## xxxx为要下载视频的网址
```

### 查看下载视频的具体信息 

```
you-get -i xxxxxxx
# xxxxxxx为下载视频的网址
```

如果要下载清晰度为720p，格式为MP4的视频，则只需要执行上图红框的代码（[URL]需替换成对应视频的网址，即下面的代码:） 

```
you-get --format=dash-flv720 https://www.bilibili.com/video/BV1EE411v7iQ?spm_id_from=333.999.0.0
```



