path="../resources/secondPic/pic2/pic1.png"


num=int(list(filter(str.isdigit, "../resources/secondPic/pic2/pic1.png".split("/").pop().split(".")[0]))[0])
print(num)