# Command-line tool that calls the reset service.
# Tasks:
# - Calls /reset_pose with values from CLI args and prints the result. 

import sys #To use command line values
import rclpy
from rclpy.node import Node
from diffrobot_interfaces import SetPose

class ResetClient(Node):
    
    def __init__(self):
        super.__init__("reset_client")
        self.cli = self.create_client(SetPose, 'reset_pose') # srv type, srv comm channel name, have to match

        #~?? Time it will wait for, and if this function doesnt come back true aka the service is not active/available, it will keep in this loop.. waiting
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...') #Stores in logger, not print TODO VERIFY
        
        # Makes object of the request section, After service is confirmed available
        self.request = SetPose.Request()
    
    def send_request(self):
        # Store the command line values in the request attributes correspondent
        #Convert it to an integer, from command line input
        self.request.x = int(sys.argv[1]) 
        self.request.y = int(sys.argv[2])
        self.request.theta = int(sys.argv[3])

        # Sends the request to server and stores 
        self.future = self.cli.call_async(self.request) #Stores status of if process done or not; also stores result as attribute here

def main(args=None):
    rclpy.init(args=args) #Allows that ROS2 commands given at command line pass to ROS itself
    reset_client = ResetClient()
    reset_client.send_request() 
    while rclpy.ok():
        rclpy.spin.once(reset_client) #Use established name attribute
        if reset_client.futute.done(): #Accesing the attributes with self aka the name
            try:
                response = reset_client.future.result() #future stores result after request to server
            except Exception as e:
                reset_client.get_logger().info(
                    'Service call failed %r' %(e,))
            else:
                reset_client.get_logger().info(
                    'Result of result client: Requested position [x:%d, y:%d, theta:%d]; Request has been accepted: %d; Status of the Robot: %d' %
                    (reset_client.request.x, reset_client.request.y, reset_client.request.theta, response.accepted, response.status)
                    
                    #Use values of srv not actual for x,y,theta for node
                    # Need to give value to status in the server and the accepted also, 
                    # Just put the pure response variables as info for the logger
                )
            break

    reset_client.destroy_node()
    rclpy.shutdown()

    if __name__ == '__main__':
        main()