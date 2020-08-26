import os
import sys
from pydub import AudioSegment

def convert(rootdir):
    for root, subdirs, files in os.walk(rootdir):
        
    
        for filename in files:
            file_path = os.path.join(root, filename)
            
            _, file_extension = os.path.splitext(filename)
            
            print('\t- file %s (full path: %s)' % (filename, file_extension))
            
            if file_extension == '.wav':
                
                print('(full path: %s)' % (file_path))
                
                audio_file = AudioSegment.from_file(file_path, frame_rate=16000, channels=2, sample_width=2)
                
                audio_file.export(file_path, format="wav", bitrate="16000")


if __name__ == "__main__":
    print("Starting to convert the data")

    convert(sys.argv[1])

    print("Completed successfully")
