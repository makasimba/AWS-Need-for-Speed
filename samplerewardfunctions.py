
def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    steering_angle = params['steering_angle']
    is_offtrack = params['is_offtrack']
    is_left_of_center = params['is_left_of_center']
    is_crashed = params['is_crashed']
    closest_objects = params['closest_objects']
    closest_waypoints = params['closest_waypoints']

    # Set the reward
    reward = 1.0

    # Reward if the agent stays inside the track's borders
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward += 1.0

    # Penalize if the agent gets too close to objects in front of it
    if closest_objects[0] < 1.5:
        reward -= 1.0

    # Penalize if the agent is off the track
    if is_offtrack:
        reward -= 1.0

    # Penalize if the agent is crashed
    if is_crashed:
        reward -= 1.0

    return reward


# batmobile v2 function
def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    objects_in_front = params['objects_in_front']

    # Set the reward based on the input parameters
    if all_wheels_on_track:
        # Reward for staying on track
        reward = 1.0

        # Reward for speed
        reward += speed / 10.0

        # Penalize for steering too much
        reward -= steering_angle / 25.0

        # Penalize for getting too close to the edge of the track
        reward -= distance_from_center / (track_width / 2.0)

        # Make sure reward is always greater than zero
        reward = max(reward, 0.0)
    else:
        reward = 1e-3

    # Return the reward
    return reward


def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    distance_from_center = params['distance_from_center']

    # Set the reward based on the input parameters
    if all_wheels_on_track:
        # Reward for staying on track
        reward = 1.0

        # Penalize for getting too far from the center of the track
        reward -= distance_from_center / 2.0

        # Make sure reward is always greater than zero
        reward = max(reward, 0.0)
    else:
        reward = 1e-3

    # Return the reward
    return reward


class Reward:

    def __init__(self, verbose=False, track_time=False):
        self.prev_speed = 0

    def reward_function(self, params):
        if self.params['speed'] >= self.prev_speed:
            return 1.0
        return 0.0


reward_object = Reward()


def reward_function(params):
    return reward_object.reward_function(params)


# Functions for getting started

def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = params['steering_angle']
    is_left_of_center = params['is_left_of_center']
    is_reversed = params['is_reversed']

    # Set the reward
    reward = 1e-3

    # Reward if the car stays on the track
    if all_wheels_on_track:
        reward += 1.0

    # Reward for speed
    reward += speed / 10

    # Reward for progress
    reward += progress / 100

    # Penalty for steering angle
    abs_steering_angle = abs(steering_angle)
    if abs_steering_angle > 15:
        reward *= 0.8

    # Penalty for being off center
    if distance_from_center > 0.5 * track_width:
        reward *= 0.5

    # Penalty for going in reverse
    if is_reversed:
        reward *= 0.5

    # Return the reward
    return reward


def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    steps = params['steps']
    is_left_of_center = params['is_left_of_center']
    reward = 1e-3

    # Reward if the car stays on track and goes fast
    if all_wheels_on_track and speed > 3:
        reward += progress * 10
    else:
        reward += progress

    # Penalize if the car goes off track
    if not all_wheels_on_track:
        reward += 1e-3

    # Penalize if the car goes too slow
    if speed < 2:
        reward += 1e-3

    # Penalize if the car steers too much
    if steering_angle > 20:
        reward += 1e-3

    # Penalize if the car is too far from the center
    if distance_from_center > 0.5 * track_width:
        reward += 1e-3

    # Reward if the car is on the left side of the track
    if is_left_of_center:
        reward += 1e-3

    # Reward if the car finishes the track
    if progress == 100:
        reward += 1e3

    return float(reward)


def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    steps = params['steps']
    is_left_of_center = params['is_left_of_center']
    is_reversed = params['is_reversed']
    reward = 1e-3

    # Reward if the car is on the track and moving fast
    if all_wheels_on_track and speed > 0:
        reward += (progress / steps) ** 2

    # Penalize if the car is steering too much
    if steering_angle > 15:
        reward *= 0.8

    # Penalize if the car is too far from the center
    if distance_from_center > 0.4 * track_width:
        reward *= 0.5

    # Penalize if the car is going in reverse
    if is_reversed:
        reward *= 0.5

    # Reward if the car is on the left side of the track
    if is_left_of_center:
        reward += 0.1

    return reward

# function that priotizes rewarding over penalizing


def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = abs(params['steering_angle'])
    is_left_of_center = params['is_left_of_center']
    is_reversed = params['is_reversed']

    # Initialize reward
    reward = 1.0

    # Reward car staying on track
    if all_wheels_on_track:
        reward += 1.0

    # Reward car for speed
    reward += speed / 10.0

    # Reward car for progress
    reward += progress / 100.0

    # Reward car for finishing the race
    if progress == 100:
        reward += 100.0

    # Return reward
    return reward

# Reward over penalization reward function


def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = abs(params['steering_angle'])
    is_left_of_center = params['is_left_of_center']
    is_reversed = params['is_reversed']

    # Initialize reward
    reward = 1.0

    # Reward car staying on track
    if all_wheels_on_track:
        reward += 1.0

    # Reward car for speed
    reward += speed / 10.0

    # Reward car for progress
    reward += progress / 100.0
    # Reward car for finishing the race
    if progress == 100:
        reward += 100.0

    # Penalize car for going off track
    if not all_wheels_on_track:
        reward -= 1.0

    # Penalize car for going too slow
    if speed < 1.0:
        reward -= 1.0

    # Penalize car for going in reverse
    if is_reversed:
        reward -= 1.0

    # Return reward
    return reward
