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
```commandline
audio = Audio(correlationSyncNoFilter(),invariantAlgorithm(),
                  mongodb_database("mongodb://localhost:27017"),
                  r'/home/tarundecipher/Documents/Music_wav/{}'
                  )
```
