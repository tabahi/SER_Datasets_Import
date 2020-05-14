# SER corpus import module



 This module reads the wav files in DB folders to create clip file class objects
 All import functions read the DB folders in their original (downloaded as is from their sources) format.

`create_DB_file_objects((string)db_name, (string)db_path)` creates a list of file objected of all the wav files present in the db_path, as long as they are according to the formant of relevant 'db_name's original source and returns a list of `Clip_file_Class` objects

```python
import SER_Datasets_Libs.SER_DB as SER_DB

list_of_augmented_clips = SER_DB.create_DB_file_objects("EmoDB", "path\\EMO-DB\\wav\\")
```

`Clip_file_Class` object contains:
`(string)filepath, (int)speaker_id, (int)accent, (char)sex, (char)emotion, (int)intensity, (int)statement, (int)repetition, (int)db_id, (int)frame_count, (int)signal_len, (int)trimmed_len, (int)file_size`

```python
print("First file path:", list_of_augmented_clips[0].filepath)
print("First file emotion label:", list_of_augmented_clips[0].emotion)
```


Currently supports these DBs
```python
db_name="EmoDB", db_path="C:\\DB\\EMO-DB\\wav\\"

db_name="RAVDESS", db_path="C:\\DB\\RAVDESS\\"

db_name="IEMOCAP", db_path="C:\\DB\\IEMOCAP_noVideo\\"

db_name="ShemoDB", db_path="C:\\DB\\shemo\\"

db_name="DEMoS", db_path="C:\\DB\\wav_DEMoS\\DEMOS\\"
```

EmoDB
<http://emodb.bilderbar.info/docu/#docu>

RAVDESS
<https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0196391>

IEMOCAP
<https://sail.usc.edu/iemocap/iemocap_release.htm>

ShemoDB
<https://github.com/pariajm/Persian-Emotional-Speech-Database-ShEMO>

DEMoS
<https://zenodo.org/record/2544829>

