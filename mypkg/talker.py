import rclpy                     #ROS2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.msg import Person 

class Talker():
    def__init__(self):
        self.pub = node.create_publisher(Int16, "count_up", 10)
        self.n = 0

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Person, "Person", 10)   #パブリッシャのオブジェクト作成
n = 0 #カウント用変数

def cb():          #17行目で定期実行されるコールバック関数
    msg = Int16()
    msg.data = talker.n
    talker.pub.publish(msg)       
    talker.n += 1
    
node.create_timer(0.5, cb)  #タイマー設定
rclpy.spin(node)            #実行（無限ループ）