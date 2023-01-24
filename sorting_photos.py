import os
import shutil
import urllib.request

path = "path"
dir_list = os.listdir(path)

for root, subdirectories, files in os.walk(path):
    for subdirectory in subdirectories:
        # print(os.path.join(root, subdirectory))
        pass
    for file in files:
        print(os.path.join(root, file))
        shutil.move(os.path.join(root, file), "destination/" + file)

with open('[SKIN GLARE] fqa_checked_s3_links.csv', 'r', encoding='utf-8') as file:
    data = file.readlines()[1:]
    for i in data:
        pair = i.split(',')
        file_name = pair[0].split("/")[1]
        file_url = pair[1]
        if file_name in dir_list:
            shutil.copy('destination/photos/' + file_name, "destination/final/" + file_name)
            print("OK: ", file_name)
        else:
            urllib.request.urlretrieve(file_url, "destination/final/" + file_name)
            print("NOT: ", file_name)

shutil.make_archive('final', 'zip', "final")
