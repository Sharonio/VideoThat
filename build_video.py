import os
import pandas as pd
from pathlib import Path
import librosa
from IPython.display import HTML
# from moviepy.editor import *
import moviepy.video.VideoClip
import moviepy.editor as mpy
from moviepy.editor import VideoFileClip, concatenate_videoclips

from tqdm import tqdm_notebook as tqdm

def locate_videoclips(video_db_path):
    # Create a list of desired artist song folder paths:
    desired_artist = [path for path in video_db_path.glob('Taylor Swift*') if path.is_dir()]
    # Locate the heaviest files (which are the videoclips) 
    paths_to_videoclips = [max(artist_clip.glob('*'), key=lambda f: f.stat().st_size) for artist_clip in desired_artist]
    return paths_to_videoclips

def load_videoclips(paths_to_videoclips):
    videoclips = dict()

    for i in paths_to_videoclips:
        v = mpy.VideoFileClip(str(i))
        videoclips[i.stem] = v

    print('Number of videoclips found in database = ', len(videoclips))
        
    return videoclips

def assemble_video(videoclips, chosen_scenes, input_song):
    final_visuals= []

    for index, row in chosen_scenes.iterrows():
        v_time = [row.start, row.end]
        v = videoclips[row['name']]

        final_visuals.append(v.subclip(*v_time).resize(width=720, height = 406))   #TODO: we force height to be even, this is all hardcoded :()
    
    # visuals & audio:
    final_video = mpy.concatenate_videoclips(final_visuals, method='compose')
    final_video.audio = input_song

    return final_video

def save_video(final_video):
    final_video.write_videofile("videoThat.mp4")
    return

def main():
    chosen_scenes_path = 'chosen_scenes.pkl'
    chosen_scenes = pd.read_pickle(chosen_scenes_path)

    input_song_path = 'Arctic Monkeys - '\
                    'Do I Wanna Know (Official Video)-bpOSxM0rNPM.webm.mp3'
    input_song = mpy.AudioFileClip(str(input_song_path))

    video_db_path = Path('data/taylor')
    paths_to_videoclips = locate_videoclips(video_db_path)
    videoclips = load_videoclips(paths_to_videoclips)

    final_video = assemble_video(videoclips, chosen_scenes, input_song)
    save_video(final_video)

if __name__=='__main__':
    main()