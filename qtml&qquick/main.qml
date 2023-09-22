import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {

    visible: true
    width: 450
    height: 700
    title: "Cingöz"
    property string currTime: "00:00:00"
    property QtObject backend

    Connections {
        target: backend

        function onUpdated(msg) {
            currTime = msg;
        }
    }
    

    function onUpdated(msg) {

        currTime = msg;
    
    }
    

     Rectangle {
        anchors.fill: parent

        Image {
            anchors.fill: parent
            source: "file:///C:/Users/byemi/OneDrive/Masaüstü/Qt/qt6/qtml&qquick/images/background.webp"
            fillMode: Image.PreserveAspectCrop
        }

        Rectangle {
            
            anchors { bottom: parent.bottom
            bottomMargin: 57
            left: parent.left
            leftMargin: 12

            }

            Text {
                text: currTime
                font.pixelSize: 33
                color: "white"
            }

        }

    }
    
}
