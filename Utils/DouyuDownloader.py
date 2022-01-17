import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {}
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegVideoConvertor',
#         # 'preferredcodec': 'mp4',
#         # 'preferredquality': '192',
#     }],
#     'logger': MyLogger(),
#     'progress_hooks': [my_hook],
# }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://v.douyu.com/show/a2JEMJGZ0dqWNxml?ap=1'])
