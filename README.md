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



## 提取视频中的音频



### 安装**ffmpeg**和**MoviePy**

```
pip install ffmpeg moviepy
```

### 读取视频文件

```python
import moviepy.editor as mp

def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)
```

以上代码做的事情是把视频文件读取到`my_clip`中，其中视频的路径可以通过`videos_file_path`来指定。比如，我的电脑里有一个视频文件，它的路径名是E:\\python\\download_bilibili\\video.mp4，那么你可以通过以下方式来读取该视频文件： 

```python
extract_audio('E:\\python\\download_bilibili\\video.mp4')
```

当我们读取视频文件之后，接下来的步骤就是要提取该视频里的音频内容，并存成*mp3*文件。 

### 输出音频文件

我们只需要在extract_audio.py中添加以下指令，就能将视频中的声音提取出来：

```python
my_clip.audio.write_audiofile(f'{videos_file_path[:-4]}.mp3')
```

以上指令的作用是把视频中的声音提取出来，并将声音存储成mp3文件。

