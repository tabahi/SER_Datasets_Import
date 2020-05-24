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

list_of_clips = SER_DB.create_DB_file_objects("MSPIMPROV", "C:\\DB\\MSP-IMPROV\\")



#Create a list of Clip_file_Class objects


print("First clip path:", list_of_clips[0].filepath)
print("First clip emotion category:", list_of_clips[0].emotion_cat)
print("First clip emotion valance:", list_of_clips[0].valance)
print("First clip emotion arousal:", list_of_clips[0].arousal)
print("First clip emotion dominance:", list_of_clips[0].dominance)
print("First clip emotion naturalness:", list_of_clips[0].naturalness)

'''
Output:

Creating file info objects
Total Clips 8438
First clip path: C:\DB\MSP-IMPROV\session2\S01A\R\MSP-IMPROV-S01A-F02-R-FF01.wav
First clip emotion category: A
First clip emotion valance: 3.333333
First clip emotion arousal: 2.333333
First clip emotion dominance: 3.0
First clip emotion naturalness: 3.666667

'''



