from PIL import Image
yPixel = 0
xPixel = 0
image = Image.open("turtle.webp", "r")
print(image.size)
open("data.txt", "w").close()
file = open("data.txt", "a")
xPrev=[34,15,17]
data=['']
w,h=image.size
up=False;
for x in list(image.getdata()):
    print(str(xPixel)+","+str(yPixel))
    if xPrev!=x:
      data.append("penRGB" + str(x) + ";\n")
      
    data.append("moveTo(" + str(xPixel) + "*w+x," + str(yPixel) + "*h+y);\n")
  
    if up==True:
      data.append("penDown();\n")
      up=False

    if xPixel > w-1:
      data.append("penUp();\n")
      up=True
      xPixel = 0
      yPixel = yPixel + 1

    if xPixel==w-1 and yPixel==h-1:
      
      file.write("//This code was generated using a python script \n")
      file.write("myFunction(10,50,2,2);\n")
      file.write("myFunction(10,50,2,2);\n")
      file.write("myFunction(10,51,2,2);\n")
      file.write("myFunction(10,51,2,2);\n")
      file.write('function myFunction(x,y,w,h) {\n')
      file.write(data[2])
      file.write("penDown();\n")
      file.write("show();")
      file.writelines(data)
      file.write("penUp();\n")
      file.write("hide()\n;")
      file.write("}")
      
    xPixel = xPixel + 1
    xPrev=x
file.close()
