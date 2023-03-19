import math


def reward_function(params):
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = abs(params['steering_angle'])
    speed = params['speed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    progress = params['progress']
    is_offtrack = params['is_offtrack']
    all_wheels_on_track = params['all_wheels_on_track']

    # Initialize reward
    reward = 1e-3

    # Reward for staying on the track
    if all_wheels_on_track or not is_offtrack:
        reward += 1
    else:
        reward -= 1

    # Calculate optimal path through direction difference between car
    # and next waypoint
    direction_diff = calculate_direction_difference(waypoints, closest_waypoints, heading)

    # Reward for closely following waypoints
    if direction_diff < math.pi/4:
        reward += 1
    else:
        reward -= 1

    # The need-for-speed reward
    if speed < 2:
        reward -= 1
    else:
        reward += (speed / 5) + 1

    # Penalize for steering too much
    if steering > 15:
        reward *= 0.8

    # Reward for sticking close to the center
    if distance_from_center < (0.1 * track_width):
        reward += 2
    elif distance_from_center < (0.2 * track_width):
        reward += 1
    else:
        reward -= 1

    return max(float(reward), 0) + (progress / 100.0)

def calculate_direction_difference(waypoints, closest_waypoints, heading):
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.atan2(
        next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    direction_diff = abs(track_direction - heading)
    return direction_diff
