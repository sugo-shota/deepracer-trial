def reward_function(params):
    reward = 10.0

    abs_steering_angle = abs(params['steering_angle']) # 絶対値、0からの値。-15でも15でも15が返る。
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    reward = reward * speed_coefficient(speed)
    reward = reward * zigzag_coefficient(abs_steering_angle)
    reward = reward * shortest_path_coefficient(progress, steps)
    reward = reward * center_coefficient(distance_from_center, track_width)
    
    return float(reward)

def center_coefficient(distance_from_center, track_width):
    coefficient = 1.0
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    if distance_from_center <= marker_1:
        coefficient = 1.2
    elif distance_from_center <= marker_2:
        coefficient = 0.8
    elif distance_from_center <= marker_3:
        coefficient = 0.2
    else:
        coefficient = 1e-3  # likely crashed/ close to off track

    return coefficient

def speed_coefficient(speed):
    coefficient = 1.0
    if speed <= 1:
        coefficient = 0.1
    elif speed <= 1.5:
        coefficient = 0.2
    elif speed <= 2:
        coefficient = 0.5
    elif speed <= 2.5:
        coefficient = 0.8
    elif speed <= 3:
        coefficient = 1.0
    elif speed <= 3.5:
        coefficient = 1.2
    elif speed <= 4:
        coefficient = 1.5

    return coefficient

def zigzag_coefficient(abs_steering_angle):
    coefficient = 1.0
    ABS_STEERING_THRESHOLD = 18
    if abs_steering_angle > ABS_STEERING_THRESHOLD:
        coefficient = 0.8
    return coefficient


def shortest_path_coefficient(progress, steps):
    # 少ない歩幅でできるだけ遠い距離へ到達することに報酬を与える
    coefficient = 1.0
    if steps > 0:
        coefficient = ((progress * 10) / steps) ** 2 # 10は係数
    else:
        coefficient = 1.0
    
    return coefficient