from gtts import gTTS
from moviepy.editor import *

def text_to_speech(text, language='en', output_file='output.mp3'):
    tts = gTTS(text=text, lang=language)
    tts.save(output_file)

def generate_video(text, audio_file, output_file='output.mp4', background_video='background_video.mp4'):
    audio = AudioFileClip(audio_file)
    video = VideoFileClip(background_video).set_duration(audio.duration)
    txt_clip = TextClip(text, fontsize=50, color='white')
    txt_clip = txt_clip.set_duration(audio.duration).set_position('center')
    final_clip = CompositeVideoClip([video, txt_clip.set_start(0)])
    final_clip = final_clip.set_audio(audio)
    final_clip.write_videofile(output_file, fps=24)

if __name__ == "__main__":
    text = "Hello, welcome to my video with voice speech."
    text_to_speech(text)
    generate_video(text, 'output.mp3', background_video='your_background_video.mp4')