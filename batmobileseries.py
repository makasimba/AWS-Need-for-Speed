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
    # Reward for staying on the track and penalizing for going off track
    reward = 1 if all_wheels_on_track or not is_offtrack else -1

    # Calculate optimal path through direction difference between car
    # and next waypoint
    direction_delta = calculate_direction_difference(
        waypoints, closest_waypoints, heading)

    # Reward for closely following waypoints
    if direction_delta < math.pi/4:
        reward += 1
    else:
        reward -= 1e-3

    if distance_from_center < (0.2 * track_width):
        reward += 2

    # The need-for-speed reward
    if speed > 0.90:
        reward += 1 + (speed / 5.0)
    elif speed > 0.95:
        reward += 2 + (speed / 5.0)
    elif speed > 1.0:
        reward += 3 + (speed / 5.0)
    else:
        reward -= 1

    # Penalize for steering too much
    if steering > 15:
        reward *= 0.90

    # Reward for making progress
    return max(float(reward), 0)


def calculate_direction_difference(waypoints, closest_waypoints, heading):
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.atan2(
        next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    direction_diff = abs(track_direction - heading)
    return direction_diff
