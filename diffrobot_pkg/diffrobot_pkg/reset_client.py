# Command-line tool that calls the reset service.
# Tasks:
# - Calls /reset_pose with values from CLI args and prints the result. 

import sys #To use command line values
import rclpy
from rclpy.node import Node
from diffrobot_interfaces.srv import SetPose

class ResetClient(Node):
    
    def __init__(self):
        super().__init__("reset_client")
        self.cli = self.create_client(SetPose, 'reset_pose') # srv type, srv comm channel name, have to match

        #Time it will wait for, and if this function doesn't come back true aka the service is not active/available, it will keep in this loop.. waiting
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        
        # Makes object of the request section, After service is confirmed available
        self.request = SetPose.Request()
    
    def send_request(self):
        # Store the command line values in the request attributes correspondent
        #Convert it to an integer, from command line input
        self.request.x = float(sys.argv[1]) 
        self.request.y = float(sys.argv[2])
        self.request.theta = float(sys.argv[3])

        # Sends the request to server and stores 
        self.future = self.cli.call_async(self.request) #Stores status of if process done or not; also stores result as attribute here

def main(args=None):
    rclpy.init(args=args) #Allows that ROS2 commands given at command line pass to ROS itself
    reset_client = ResetClient()
    reset_client.send_request() 
    while rclpy.ok():
        rclpy.spin_once(reset_client) #Use established name attribute
        if reset_client.future.done(): #Accesing the attributes with self aka the name
            try:
                response = reset_client.future.result() #future stores result after request to server
            except Exception as e: #If the 
                reset_client.get_logger().info(
                    'Service call failed %r' %(e,))
            else:
                reset_client.get_logger().info(
                    f'Result of reset_client: Requested position [x:{reset_client.request.x}, y:{reset_client.request.y}, theta:{reset_client.request.theta}]; Request has been accepted?: {response.accepted}; Status of the Robot: {response.status}'
                    #Use values of srv not actual for x,y,theta for node
                    # Need to give value to status in the server and the accepted also, 
                    # Just put the pure response variables as info for the logger
                )
            break

    reset_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()