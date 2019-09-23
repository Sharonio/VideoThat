import os
import pandas as pd
from pathlib import Path
import librosa
import numpy as np
import tqdm


def create_song_db(video_files, base_path):
    songs = [librosa.load(str(i)) for i in tqdm.tqdm(video_files)] # This is SLOW
    songs_gist = [s[0] for s in songs]
    names = [f.stem for f in video_files]

    scenes = []

    for name in names:
        scenesDf = pd.read_csv(base_path / (name + '-Scenes.csv'), skiprows = 1)
        scenes.append(scenesDf['Start Time (seconds)'])

    df = pd.DataFrame({'name':names, 'song_wave':songs_gist, 'scene_start_times_sec':scenes})
    return df

def create_scene_db(song_df):
    scenes_per_song = song_df.apply(lambda song: np.split(song.song_wave, librosa.time_to_samples(song.scene_start_times_sec[1:])), axis=1)
    all_segments = sum(scenes_per_song.values, [])
    all_song_names = song_df.apply(lambda song: [song['name']] * len(song.scene_start_times_sec), axis=1)
    all_song_names = np.concatenate(all_song_names)
    index_in_song = np.concatenate(song_df.apply(lambda song: list(range(len(song.scene_start_times_sec))), axis=1))
    scenes_df = pd.DataFrame({'segment' : all_segments, 'name' : all_song_names, 'index_in_song' : index_in_song})
    return scenes_df


def main():
    base_path = Path('data/taylor')
    # create a list of taylor song folder paths
    taylor_swifts = [path for path in base_path.glob('Taylor Swift*') if path.is_dir()]
    # look for the largest file which is the video file
    video_files = [max(taylor_song.glob('*'), key=lambda f: f.stat().st_size) for taylor_song in taylor_swifts]

    df = create_song_db(video_files, base_path)
    df.to_pickle("song_db.pkl")

    scenes_df = create_scene_db(df)
    scenes_df.to_pickle('scene_db.pkl')

if __name__=='__main__':
    main()