import os

# pick a folder
#TODO: take pathname on command line
#folder = os.getcwd()
homedir = os.path.expanduser('~')
#folder = os.path.join(homedir,'4TB/Movies/unseeded')
#folder = os.path.join(homedir,'4TB/Movies/H-WD500-MOVIES')
folder = os.path.join(homedir,'4TB/Movies/')

def getSize(filename):
    return os.stat(filename).st_size

def getOneLevelSizes(folder):
  folder_list = os.listdir(path=folder)
  paths = [os.path.join(folder, name) for name in folder_list]
  sizes = []
  for path in paths:
    if os.path.isfile(path):
      if ('unseeded' not in path.lower()):
        continue
      blacklist_words = ['sample','.m2ts','.sub','.nfo','.dat','.srt']
      if any(skip in path.lower() for skip in blacklist_words):
        continue
      filetypes = ['.mkv','.mp4','.avi']
      if (t for t in filetypes if t in path.lower()):
        sizes.append((getSize(path), path))
    else: #recurse
      sizes += getOneLevelSizes(path)
  return sizes
sizes = getOneLevelSizes(folder)

def getKey(i):
   return i[0]
sizesSorted = sorted(sizes, key=getKey, reverse=True)

for size,path in sizesSorted:
#   print(size,'\t',path)
   print(str(size) + ',' + path)
