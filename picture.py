"""
picture.py
Author: Marcus Helble
Credit: None

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
tan = Color(0xcc9900, 1.0)
lightblue = Color(0x00ffff, 1.0)
thinline = LineStyle(1, black)
rectangle = RectangleAsset(5000, 5000, thinline, green)
Sprite(rectangle)
ellipse = EllipseAsset(200, 400, thinline, blue)
Sprite(ellipse)
circle = CircleAsset(40, thinline, lightblue)
Sprite(circle, (1100, 100))
rectangle = RectangleAsset(1500, 150, thinline, black)
Sprite(rectangle, (0, 450))
rectangle = RectangleAsset(1500, 35, thinline, white)
Sprite(rectangle, (0, 510))
polygon = PolygonAsset([(400,175), (600,175), (500,240), (400,175)], thinline, tan)
Sprite(polygon)
polygon = PolygonAsset([(400,125), (600,125), (500,60), (400,125)], thinline, tan)
Sprite(polygon)
rectangle = RectangleAsset(5000, 5000, thinline, blue)
Sprite(rectangle, (0, 600))
polygon = PolygonAsset([(400,640), (420,660), (440,640), (400,640)], thinline, tan)
Sprite(polygon)
circle = CircleAsset(3, thinline, white)
Sprite(circle, (460, 110))











# add your code here /\  /\  /\


myapp = App()
myapp.run()
