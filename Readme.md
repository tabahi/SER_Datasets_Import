# SER corpus import module


 This module reads the wav files in DB folders to create clip file class objects
 All import functions read the DB folders in their original (downloaded as is from their sources) format.

`create_DB_file_objects((string)db_name, (string)db_path)` creates a list of file objected of all the wav files present in the db_path, as long as they are according to the formant of relevant 'db_name's original source and returns a list of `Clip_file_Class` objects.

```python
# in example.py
import SER_DB_Parsing.SER_DB as SER_DB

list_of_clips = SER_DB.create_DB_file_objects("EmoDB", "path\\EMO-DB\\wav\\")
```

Each item in the list is created by the class: `Clip_file_Class(db_id, filepath, speaker_id, scenario, sex, emotion_cat=None, intensity_cat=None, valance=None, arousal=None, dominance=None, naturalness=None, statement=None, repetition=None, n_raters=None, n_possible_emotions=None)`

Get clip properties as:
```python
print("First clip path:", list_of_clips[0].filepath)
print("First clip emotion category:", list_of_clips[0].emotion_cat)
```


Currently supports these DBs
```python
db_name="EmoDB", db_path="C:\\DB\\EMO-DB\\wav\\"
# First file path: C:\DB\EMO-DB\wav\03a01Fa.wav

db_name="RAVDESS", db_path="C:\\DB\\RAVDESS\\"
# First file: C:\DB\RAVDESS\Speech\Actor_01\03-01-01-01-01-01-01.wav

db_name="IEMOCAP", db_path="C:\\DB\\IEMOCAP_noVideo\\"
# First file: C:\DB\IEMOCAP_noVideo\Session1\sentences\wav\Ses01F_script01_1\Ses01F_script01_1_F001.wav
# Evaluation file: C:\DB\IEMOCAP_noVideo\Session1\dialog\EmoEvaluation\Ses01F_impro01.txt

db_name="ShemoDB", db_path="C:\\DB\\shemo\\"
# First file: C:\DB\shemo\F\F01A01.wav

db_name="DEMoS", db_path="C:\\DB\\wav_DEMoS\\DEMOS\\"
# First file: C:\DB\wav_DEMoS\DEMOS\NP_f_01_col07b.wav

db_name="MSIMPROV", db_path="C:\\DB\\MSP-IMPROV\\"
# First file: C:\DB\MSP-IMPROV\session2\S01A\R\MSP-IMPROV-S01A-F02-R-FF01.wav
# Evaluation file: C:\DB\MSP-IMPROV\Evalution.txt
```
Change the `db_path` according to wherever you have stored the databases.




> Standardized emotional category labels (single char) `emotion_cat: {'N':'neutral', 'H':'happy', 'S':'sad', 'A':'anger',  'F':'fear', 'D':'disgust', 'U':'surprise', 'C':'calm', 'R':'frustuated', 'E':'excited', 'Y':'happy-excited', 'G':'guilty', 'X': 'unknown'}`

> Standardized scenario labels (int) : `0=unknown, 1=script, 2=improv, 3=radio/TV, 4=elicited, 5=natural, 6=script-in-improv`

> Standardized sexes (single char) : `'M'=males, 'F'=females`

EmoDB
<http://emodb.bilderbar.info/docu/#docu>

RAVDESS
<https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0196391>

IEMOCAP
<https://sail.usc.edu/iemocap/iemocap_release.htm>

ShEMO-DB
<https://github.com/pariajm/Persian-Emotional-Speech-Database-ShEMO>

DEMoS
<https://zenodo.org/record/2544829>

MSP-IMPROV
<https://ecs.utdallas.edu/research/researchlabs/msp-lab/MSP-Improv.html>

