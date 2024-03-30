# o objetivo deste código é colocar um audio em um video.

# biblioteca
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip

# cortando video de 0s até 21s.
clipe1 = VideoFileClip('video1.mp4').subclip(0, 21)

# cortando audio de 90s até 110s.
audioClip = AudioFileClip('Empire-state.mp3').subclip(90, 110)

# junta todos os videos, mas nesse caso apenas 1.
video = concatenate_videoclips([clipe1])

# coloca o audio no video.
video.audio = audioClip

# cria o arquivo mp4.
video.write_videofile('videoEditado.mp4')