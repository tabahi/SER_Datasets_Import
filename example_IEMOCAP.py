import SER_DB_Parsing.SER_DB as SER_DB

'''
Speech Emotion Recognition (SER) databases augmentation

Currently supports these DBs
{'DB': "EmoDB", 'path' : "C:\\DB\\EMO-DB\\wav\\"},
{'DB': "RAVDESS", 'path' : "C:\\DB\\RAVDESS\\"},
{'DB': "IEMOCAP", 'path' : "C:\\DB\\IEMOCAP_noVideo\\"},
{'DB': "ShemoDB", 'path' : "C:\\DB\\shemo\\"},
{'DB': "DEMoS", 'path' : "C:\\DB\\wav_DEMoS\\DEMOS\\"},
{'DB': "MSPIMPROV", 'path' : "C:\\DB\\MSP-IMPROV\\"}
'''


# List of DB names and directory where wav files are stored:
db_names_paths = [{'DB': "IEMOCAP", 'path' : "C:\\DB\\IEMOCAP_noVideo\\"},]
# Can add more than one DBs to the list


#Create a list of Clip_file_Class objects

list_of_clips = SER_DB.create_DB_file_objects(db_names_paths[0]['DB'], db_names_paths[0]['path'], deselect=['F', 'D', 'U', 'R', 'E', 'X'])



print("First clip path:", list_of_clips[0].filepath)
print("First clip emotion category:", list_of_clips[0].emotion_cat)
print("First clip emotion valance:", list_of_clips[0].valance)
print("First clip emotion arousal:", list_of_clips[0].arousal)
print("First clip emotion dominance:", list_of_clips[0].dominance)
#print("First clip emotion naturalness:", list_of_clips[0].naturalness)


import numpy as np

each_emotion_cat_score = np.mean(list_of_clips[0].raters_labels_cat, axis=0)

#IEMOCAP label indices:
#'N':'neu', 'H':'hap', 'S':'sad', 'A':'ang',  'F':'fea', 'D':'dis', 'U':'sur', 'R':'fru', 'Y':'exc'
print("First clip each_emotion_cat_score:", each_emotion_cat_score)


each_emotion_dim_score = np.mean(list_of_clips[0].raters_labels_dim, axis=0) 

#valance, arousal, dominance, naturalness
print("First clip each_emotion_dim_score:", each_emotion_dim_score)

'''
Output:

Creating file info objects
Total Clips 8038
First clip path: C:\DB\IEMOCAP_noVideo\Session1\sentences\wav\Ses01F_script01_1\Ses01F_script01_1_F001.wav
First clip emotion category: X
First clip emotion valance: 2.0
First clip emotion arousal: 2.3333
First clip emotion dominance: 1.6667
First clip each_emotion_cat_score: [0.04166667 0.         0.         0.         0.04166667 0.
 0.         0.         0.         0.         0.        ]
First clip each_emotion_dim_score: [0.25       0.29166667 0.20833333 0.        ]


'''

