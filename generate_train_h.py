import os

image_files = []
os.chdir(os.path.join("data", "obj_h"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("data/obj_h/" + filename)
os.chdir("..")
with open("train_h.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
