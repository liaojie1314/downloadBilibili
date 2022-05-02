import moviepy.editor as mp


def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)
    my_clip.audio.write_audiofile(f'{videos_file_path[:-4]}.mp3')

extract_audio('E:\\python\\download_bilibili\\video.mp4')
