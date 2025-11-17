

import zipfile
import os
from pathlib import Path


def backzip(folder):
  folder = Path(folder)

  number = 1
  while True:
    zipname = Path(f'{folder.parts[-1]}_{str(number)}.zip')
    if not zipname.exists():
      break
    number = number + 1

  print(f'Creating {zipname}') 
  backup = zipfile.ZipFile(zipname, 'w')

  for folder_name, subfolders, filenames in os.walk(folder):
    folder_name = Path(folder_name)
    print(f'Adding files in folder {folder_name}')

    for filename in filenames:
      print(f'Adding file {filename}...')
      backup.write(folder_name / filename)  
  backup.close()
  print('done')


backzip(input())





















