import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from random import randint, choice


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Cingöz")
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(700,500)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        # self.draw_object(object_type = "point", position = (150,150), width= 13, pen_color="cyan")
        # self.draw_object(object_type = "multiple_point", pen_color="red", limit = 13000, width= 3, colorful=True)
        # self.draw_object(object_type = "line", pen_color="red", limit = 13000, width= 13, point1 = (70,70), point2=(300, 300))
        # self.draw_object(object_type = "multiple_rect", pen_color="red", limit = 13000, width= 3, n_rect = 7, round_size = 7)
        # self.draw_object(object_type = "ellipse", pen_color="#376F9F", limit = 13000, width= 3, n_shape = 7, round_size = 7)
        # self.draw_object(object_type = "ellipse", centered_ellipse = True, center_point = (270, 270), radius = (50,50), radius_size = (13, 17),pen_color="#376F9F", limit = 13000, width= 3, n_shape = 7, round_size = 7)
        self.draw_object(object_type = "text", text_position = (70, 210), text = "Hello guys. I am Mehmet Emin :)", font_name= "Times", centered_ellipse = True, center_point = (270, 270), radius = (50,50), radius_size = (13, 17),pen_color="#376F9F", limit = 13000, width= 3, n_shape = 7, round_size = 7)

    def draw_object(self, width = 17, pen_color = "black",colorful=False, brush_color= "white"  ,brush = False, font_name = str , *args, **kwargs):
        n_shape = 0
        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']
        canvas = self.label.pixmap()
        my_painter = QtGui.QPainter(canvas)

        try:
            pen = QtGui.QPen()
            pen.setWidth(width)
            pen.setColor(QtGui.QColor(pen_color))

            font = QtGui.QFont()
            font.setBold(True)
            font.setFamily(font_name)
            font.setPointSize(30)


            if brush:
                brush = QtGui.QBrush()
                brush.setColor(QtGui.QColor(brush_color))
                brush.setStyle(Qt.BrushStyle.Dense1Pattern)
                my_painter.setBrush(brush)


            my_painter.setPen(pen)
            my_painter.setFont(font)
        
        except:
            print("Error: Function arguments are not true!")

        
        if kwargs["object_type"] ==  "point":
            try: 
                x_pt, y_pt = kwargs["position"]
                my_painter.drawPoint(x_pt, y_pt)
            
            except:
                print("Error")
        
        if kwargs["object_type"] == "multiple_point" :

            try:
                limit = kwargs["limit"]
                for n in range(limit):

                    if colorful and pen != None:

                        pen.setColor(QtGui.QColor(choice(colors)))
                        my_painter.setPen(pen)
                        
                        
                    my_painter.drawPoint(

                        300 + randint(-130 , 130),
                        250 + randint(-130, 130)
                    )
            
            except:
                print("Error: Multiple points error!")

        if kwargs["object_type"] == "line":
            
            try:
                x1, y1 = kwargs["point1"]
                x2, y2 = kwargs["point2"]

                my_painter.drawLine(QtCore.QPoint(x1, y1), QtCore.QPoint(x2, y2))
            
            except:
                print("Error: Line drawing error!")
        
        if kwargs["object_type"] == "multiple_rect":

            try:
                n_rect = kwargs["n_shape"]
                
                for n in range(n_rect):
                    x1, y1, x2, y2 = list(randint(0,500) for _ in range(4))
                    
                    if kwargs["round_size"]:
                        n_round = kwargs["round_size"] * 10
                        my_painter.drawRoundedRect(x1, y1, x2, y2, n_round, n_round)
                    
                    else:
                        my_painter.drawRect(x1, y1, x2, y2)
                        

            except:
                print("Error: Rectangle drawing error!")
        
        if kwargs["object_type"] == "ellipse":

            try:
                
                if kwargs["n_shape"]:

                    n_ellipse = kwargs["n_shape"]
                
                if kwargs["centered_ellipse"]:
                    
                    c1, c2, = kwargs["center_point"]
                    radiusx, radiusy = kwargs["radius"]
                    rx_size, ry_size = kwargs["radius_size"]
                    for n in range(n_ellipse):
                        
                        my_painter.drawEllipse(QtCore.QPoint(c1, c2), radiusx, radiusy)
                        radiusx += rx_size
                        radiusy += ry_size
                
                else:
                    for n in range(n_ellipse):

                
                        x1, y1, x2, y2 = [randint(0,300) for _ in range(4)]
                        my_painter.drawEllipse(x1, y1, x2, y2)
            
            except:
                print("Error: Ellipse drawing error!")
        
        if kwargs["object_type"] == "text":

            try: 

                text_content = kwargs["text"]
                p1, p2 = kwargs["text_position"]
                # print(p1, p2)
                # my_painter.drawText(p1, p2 , 700, 700, Qt.AlignmentFlag.AlignHCenter,  text_content)
                my_painter.drawText(p1, p2, text_content)


            except:
                print("Error: Text drawing error!")
        my_painter.end()
        self.label.setPixmap(canvas)

def main():

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":

    main()