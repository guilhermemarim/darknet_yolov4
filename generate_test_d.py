import os

image_files = []
os.chdir(os.path.join("data", "test_d"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("data/test_d/" + filename)
os.chdir("..")
with open("test_d.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
