def reward_function(params):
    # Example of rewarding the agent to follow centre line

    # Read input parameters
    track_width = params['track_width']
    distance_from_centre = params['distance_from_center']

    # Calculate 3 markers that are at varying distances away from the centre line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.35 * track_width

    # Give higher reward if the car is closer to centre line and vice versa
    if distance_from_centre <= marker_1:
        reward = 1.0
    elif distance_from_centre <= marker_2:
        reward = 0.5
    elif distance_from_centre <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3 # likely crashed/ close to off track

    return float(reward)
