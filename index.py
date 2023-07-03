def reward_function(params):
    reward = 1.0

    abs_steering_angle = abs(params['steering_angle']) # 絶対値、0からの値。-15でも15でも15が返る。
    speed = params['speed']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    track_width_half = track_width * 0.5

    # 車体の中心がコース幅を超えていれば減点（少しだけ超えててもok）
    if track_width_half - distance_from_center < -0.05:
        return 1e-3
    
    reward = speed_reward(reward, speed)
    reward = prevent_zigzag(reward, abs_steering_angle)
    
    return float(reward)


def prevent_zigzag(reward, abs_steering_angle):
    ABS_STEERING_THRESHOLD = 18
    if abs_steering_angle > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    return reward


def speed_reward(reward, speed):
    if speed <= 1:
        reward *= 0.3
    elif speed <= 1.5:
        reward *= 0.5
    elif speed <= 2:
        reward *= 0.6
    elif speed <= 2.5:
        reward *= 0.7
    elif speed <= 3:
        reward *= 0.8
    elif speed <= 3.5:
        reward *= 0.9
    elif speed <= 4:
        reward *= 1.0
    else:
        reward = reward

    return reward