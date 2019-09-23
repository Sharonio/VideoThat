import librosa
from pathlib import Path
import pandas as pd
import numpy as np

def silly_segment_matcher(target_segment, length_power=0.75):
    def silly_match(seg):
        min_length = min(len(seg), len(target_segment))
        # original clip was with length_power 0.5
        return np.sum(np.dot(seg[:min_length], target_segment[:min_length])) / min_length**length_power
    return silly_match

def build_song_segments(target_song, segments_df, songs_df): # segments_df = all of tailor swift scenes, songs_df = a list of all of tailor's songs in db
    matches = []
    wave_segments = []
    target_remaining_samples = target_song
    while len(target_remaining_samples) > 10000:
        # TODO: only necessary to calculate onsets up to max length of segment, not entire remaining song
        # fix if too slow
        target_onset_envelope = librosa.onset.onset_strength(target_remaining_samples)
        # dot prod - correlate segments, penalize by sqrt of length, which makes longer segments better
        onset_silly_match = segments_df.onset_envelope.map(silly_segment_matcher(target_onset_envelope))
        best_match_index = onset_silly_match.idxmax()
        best_match = segments_df.loc[best_match_index]
        matching_song = songs_df[songs_df['name'] == best_match['name']]
        wave = matching_song.song_wave.values[0]
        start_times = matching_song.scene_start_times_sec.values[0]
        start_time = start_times[best_match.index_in_song]
        # end of song if index_in_song is the last one
        end_time = start_times[best_match.index_in_song + 1] if best_match.index_in_song + 1 < len(start_times) \
                    else librosa.samples_to_time(len(wave))
        start_sample = librosa.time_to_samples(start_time)
        end_sample = librosa.time_to_samples(end_time)
        
        matches.append((best_match['name'], start_time, end_time))
        consumed_samples = end_sample - start_sample
        target_remaining_samples = target_remaining_samples[consumed_samples:]
        # don't reuse samples
        segments_df = segments_df.drop(best_match_index)
        wave_segments.append(wave[start_sample : end_sample])
    return matches, np.concatenate(wave_segments)

def main():

    target_song = librosa.load('Arctic Monkeys - '\
                    'Do I Wanna Know (Official Video)-bpOSxM0rNPM.webm.mp3')
    target_song = target_song[0]
    segments_df = pd.read_pickle('scene_db.pkl')
    onset_strengths = segments_df.segment.apply(librosa.onset.onset_strength)
    segments_df["onset_envelope"] = onset_strengths

    songs_df = pd.read_pickle('song_db.pkl')
    matches, _ = build_song_segments(target_song, segments_df, songs_df)
    names, starts, ends = list(zip(*matches))
    matches = pd.DataFrame({'name': names, 'start': starts, 'end': ends})
    matches.to_pickle('chosen_scenes.pkl')
if __name__=='__main__':
    main()