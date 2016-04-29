import rospy
from sensor_msgs.msg import NavSatFix

class copter_data_grabber:
	def __init__(self):
		self.nav_sub = rospy.Subscriber("/mavros/global_position/raw/fix", NavSatFix, self.NavSatFixCallback)
	
	def NavSatFixCallback(self,data):
		print data.status
		print ""

if __name__ == "__main__":
	copData = copter_data_grabber()
	rospy.init_node("Copter_data", anonymous=True)
	rospy.spin()
	
