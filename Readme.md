# Audio Synchronization and Fingerprinting package
## Example
run.py contains various examples of using the package.

## Setting up database
Execute following commands to run a mongodb instance 
where the fingerprints will be stored and queried from.
Make sure you have docker installed.
```commandline
docker run -p 27017:27017 mongo
```
Once the mongo container is up and running following 
connection string needs to be passed while building the
Audio object
```python
audio = Audio(correlationSyncNoFilter(),invariantAlgorithm(),
                  mongodb_database("mongodb://localhost:27017"),
                  r'/home/tarundecipher/Documents/Music_wav/{}'
                  )
```

## Example code snippet to fingerprint audio in /music folder
```python
    import os
    Songs = os.listdir(r'/home/tarundecipher/Documents/Music_wav')
    for song in Songs:
        audio.fingerprint_to_database(song,"mongodb://localhost:27017")
```

## Example code snippet to sync recorded audio with the one passed as arguement
```python
audio.sync_audio('Eminem - The Monster (Audio) ft. Rihanna [LoudTronix] [HQ].wav')
```