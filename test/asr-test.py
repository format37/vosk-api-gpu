#!/usr/bin/env python3

# https://raw.githubusercontent.com/alphacep/vosk-server/master/client-samples/python/asr-test.py

import asyncio
import websockets
import sys
import os
import datetime
import pickle
import json

if len(sys.argv) != 4:
    print('Wrong parameters count. Please pass:')
    print('1. Count of files to test')
    print('2. path to files')
    print('3. server address')
    exit()

time_start = datetime.datetime.now()
files_data = {}

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        
        def get_files(path):
            for root, dirs, files in os.walk(path):
                files.sort()
                return files
        counter = 0

        with open('transcribation.txt', 'w') as textfile:
            

            for file in get_files(sys.argv[2]):
                                
                #phrases = transcribe_vosk(sys.argv[1]+'/'+file, model)
                counter += 1
                if counter > int(sys.argv[1]):
                    break
                
                print(' = = [',counter,'] = =',file)
                wf = open(sys.argv[2]+file, "rb")
                
                file_data = []
                textfile.write('=== '+str(file)+'\n')

                while True:
                    data = wf.read(8000)

                    if len(data) == 0:
                        break

                    await websocket.send(data)
                    accept = json.loads(await websocket.recv())
                    #file_data.append(accept)
                    if len(accept)>1 and accept['text'] != '':
                        file_data.append(accept['text'])
                        textfile.write(str(accept['text'])+'\n')
                    else:
                        [[key, value]] = accept.items()
                        if key == 'text' and len(value):
                            file_data.append(value)
                            textfile.write(str(value)+'\n')

                    #print (await websocket.recv())
                files_data[file] = file_data

            await websocket.send('{"eof" : 1}')
            print (await websocket.recv())

asyncio.get_event_loop().run_until_complete(
    hello('ws://'+sys.argv[3]+':2700'))

time_end = datetime.datetime.now()
print('spent', (time_end - time_start).seconds, 'seconds')

pickle.dump(files_data, file=open('files_data.pickle', 'wb'))
print('job complete!')
