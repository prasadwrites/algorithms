
#!/usr/bin/env python3
import os
from PIL import Image

# Open background and foreground and ensure they are RGB (not palette)


list_of_files_bg = []
list_of_files_fg = []
for (dirpath, dirnames, filenames) in os.walk("."):
            for filename in filenames:
                if dirpath == ".\\bg":
                    if (filename.endswith('.png') or filename.endswith('.jpg')):
                        list_of_files_bg.append(os.sep.join([dirpath, filename]))
                elif dirpath == ".\\fg":
                    if (filename.endswith('.png') or filename.endswith('.jpg')) : 
                       list_of_files_fg.append(os.sep.join([dirpath, filename]))
print(list_of_files_fg)
print(list_of_files_bg)
count = 0
for fg_file in list_of_files_fg:
    for bg_file in list_of_files_bg:
        count = count + 1
        bg = Image.open(bg_file).convert('RGB')
        fg = Image.open(fg_file).convert('RGBA')

        # Resize foreground down from 500x500 to 100x100
        fg_resized = fg.resize((1450,1450))

        # Overlay foreground onto background at top right corner, using transparency of foreground as mask
        bg.paste(fg_resized,box=(0,400),mask=fg_resized)

        print(count)
        # Save result
        bg.save('D:\\Toolbox\\python\\campaign\\ouput\\'+str(count) + '.png','PNG' )