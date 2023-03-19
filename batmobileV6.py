# batmobile V6: modified V4 function
def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])
    track_width = params['track_width']
    distance_from_center = abs(params['distance_from_center'])
    progress = params['progress']
    is_offtrack = params['is_offtrack']

    reward = 0.00

    if all_wheels_on_track:
        reward += 1e-3

        if distance_from_center < (0.10 * track_width):
            reward += 1.0
        elif distance_from_center < (0.20 * track_width):
            reward += 0.5
        elif distance_from_center < (0.30 * track_width):
            reward += 0.25
        else:
            reward -= 0.10

        speed_threshold = 2.0
        if speed > speed_threshold:
            reward += speed / 10.0

        steering_threshold = 15.0
        if steering_angle > steering_threshold:
            reward *= 0.90

        reward = max(reward, 0.0) + (progress / 100.0)

    else:
        reward -= 1e-3

    # Return the reward
    return reward
