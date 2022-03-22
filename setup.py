from setuptools import setup
import os

with open('requirements.txt') as f:
      required = f.read().splitlines()

setup(name="Audio",
      version="0.2",
      packages=['Audio','Audio.SyncAlgorithms','Audio.database',
            'Audio.downSample','Audio.getAudio','Audio.Record','Audio.FingerprintAlgorithms',
                'Audio.fastComputation','Audio.QueueWorker'],
      install_requires=required)