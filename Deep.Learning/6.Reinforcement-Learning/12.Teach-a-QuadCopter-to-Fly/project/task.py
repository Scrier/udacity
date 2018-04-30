import numpy as np
from physics_sim import PhysicsSim
import math

class Task():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None, reward_function=None, angle_penalty=10.):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_low = 0
        self.action_high = 900
        self.action_size = 4
        self.angle_penalty = angle_penalty
        self.max_v_length = 0.

        # Goal
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 
        
        self.distance_to_target = self.vector_length(self.target_pos - self.sim.pose[:3])
        
        if( reward_function == 6 ):
            self.reward_function_str = 'Using Reward Function 6'
            self.reward_function = self.reward_function_6
        elif( reward_function == 5 ):
            self.reward_function_str = 'Using Reward Function 5'
            self.reward_function = self.reward_function_5
        elif( reward_function == 4 ):
            self.reward_function_str = 'Using Reward Function 4'
            self.reward_function = self.reward_function_4
        elif( reward_function == 3 ):
            self.reward_function_str = 'Using Reward Function 3'
            self.reward_function = self.reward_function_3
        elif( reward_function == 2 ):
            self.reward_function_str = 'Using Reward Function 2'
            self.reward_function = self.reward_function_2
        elif( reward_function == 1 ):
            self.reward_function_str = 'Using Reward Function 1'
            self.reward_function = self.reward_function_1
        else:
            self.reward_function_str = 'Using Deafault Reward Function'
            self.reward_function = self.default_reward

    def get_reward(self, done):
        """Uses current pose of sim to return reward."""
        return self.reward_function(done)
    
    def default_reward(self, done):
        return 1.-.3*(abs(self.sim.pose[:3] - self.target_pos)).sum()
    
    def reward_function_1(self, done):
        if done and self.sim.time < self.sim.runtime: 
            return -1
        else:
            return self.sim.v[2] # z velocity
    
    def reward_function_2(self, done):
        return np.tanh(self.reward_function_1(done))
    
    def reward_function_3(self, done):
        rewards = []
        rewards.append(self.check_range(self.reward_function_2(done)))
        rewards.append(self.check_range(self.reward_function_2(done)))
        rewards.append(self.check_range(self.reward_function_2(done)))
        rewards.append(self.check_range(self.reward_gauss(self.sim.pose[3]))) # roll
        rewards.append(self.check_range(self.reward_gauss(self.sim.pose[4]))) # pitch
        return self.check_range(np.average(rewards))
    
    def reward_function_4(self, done):
        if done and self.sim.time < self.sim.runtime: 
            return -1
        else:
            current_pos = self.sim.pose[:3]
            target_vector = self.target_pos - current_pos
            diff_angle = self.angle_between(target_vector, self.sim.v)
            return self.check_range(self.scale(diff_angle))
        
    def reward_function_5(self, done):
        if done and self.sim.time < self.sim.runtime: 
            return -1
        else:
            rewards = []
            rewards.append(self.check_range(self.reward_function_4(done)))
            distance_to_target = self.vector_length(self.target_pos - self.sim.pose[:3])
            rewards.append(self.check_range(self.velocity_activation(distance_to_target)))
            return self.check_range(np.average(rewards))
        
    def reward_function_6(self, done):
        if done and self.sim.time < self.sim.runtime: 
            return -1
        else:
            rewards = []
            rewards.append(self.check_range(self.reward_function_4(done)))
            distance_to_target = self.vector_length(self.target_pos - self.sim.pose[:3])
            if( distance_to_target > 10 ):
                rewards.append(self.check_range(self.velocity_activation(distance_to_target)))
            else:
                rewards.append(self.check_range(self.reward_gauss2(distance_to_target)))
            return self.check_range(np.average(rewards))
        
    # Linear scale that returns negative if less than 0 and distance_to_target / positive with
    # a roof of 1. I.e for velocity I reward -1 if we go away from the target and scale slowly
    # between 0 to 1 if the distance to the target is less than 10 else we return 1.
    def velocity_activation(self, distance_to_target, negative = -1., positive = 10.):
        result = negative if distance_to_target < 0 else distance_to_target / positive
        return 1 if result > 1. else result
    
    # scale a value (I use it for an angle, but anything goes). Where [s_min, s_max] transforms
    # to the range of [t_min, t_max] for the input_angle. We assume that the input will be
    # within s_min to s_max after we take the absolute value of it.
    def scale(self, input_angle, t_max = 1., t_min = -1., s_max = math.pi, s_min = 0.):
        input_angle = math.fabs(input_angle)
        taljare = ((t_min - t_max) * (input_angle - s_min))
        namnare = s_max - s_min
        return (taljare / namnare) + t_max

    # Helper function for angle_between method.
    def unit_vector(self, vector):
        """ Returns the unit vector of the vector.  """
        return vector / np.linalg.norm(vector)

    # Returns the angle between two vectors (v1 and v2) between -pi and pi.
    def angle_between(self, v1, v2):
        """ Returns the angle in radians between vectors 'v1' and 'v2'::

                >>> angle_between((1, 0, 0), (0, 1, 0))
                1.5707963267948966
                >>> angle_between((1, 0, 0), (1, 0, 0))
                0.0
                >>> angle_between((1, 0, 0), (-1, 0, 0))
                3.141592653589793
        """
        v1_u = self.unit_vector(v1)
        v2_u = self.unit_vector(v2)
        return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    
    # Returns the length of a 3 dimenional vector. Used for total velocity speed and the
    # remaining sitance to the target.
    def vector_length(self, velocity):
        return np.sqrt(np.sum(np.power(velocity, 2)))
    
    # Helper method to make sure my reward functions is kept between -1 and 1. This due to
    # me missing the self.action_repeat and plottet rewards between -3 and 3.
    def check_range(self, x):
        if( (1.0 < x) or (x < -1.0) ):
            print(x, 'is out of scope from -1 to 1')
            assert True
        return x
    
    # Change angle from [0, 2pi] -> [-pi, pi]
    def normalize(self, angle):
        return math.atan2(math.sin(angle), math.cos(angle))
    
    # Gaussian reward function.
    def gaussian(self, angle):
        return np.exp(-angle**2)
    
    # Scaling the input angle by a factor of angle_penalty. This will steepen the curve around 
    # 0 the bigger the angle_penalty is.
    def reward_gauss(self, angle):
        return (self.gaussian(self.normalize(angle) * self.angle_penalty) * 2) - 1
    
    def reward_gauss2(self, angle, divider=10):
        return self.gaussian(angle / divider)
        
    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward(done) 
            pose_all.append(self.sim.pose)
            v_length = self.vector_length(self.sim.v)
            self.max_v_length = self.max_v_length if self.max_v_length > v_length else v_length
            self.distance_to_target = self.vector_length(self.target_pos - self.sim.pose[:3])
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state