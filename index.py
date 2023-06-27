def reward_function(params):
    reward = 0

    all_wheels_on_track = params['all_wheels_on_track']
    is_left_of_center = params['is_left_of_center']
    steering_angle = params['steering_angle']
    speed = params['speed']
    # is_reversed = params['is_reversed']
    # is_offtrack = params['is_offtrack']


    if not all_wheels_on_track:
        return 1e-3
    
    if is_left_of_center and steering_angle > 20:
        # 左車線で左に急ハンドル == コースアウト
        return 1e-3
    elif not is_left_of_center and steering_angle < -20:
        # 右車線で右に急ハンドル == コースアウト
        return 1e-3

    if speed <= 4:
        reward = 1.0
    elif speed <= 3:
        reward = 0.7
    elif speed <= 2:
        reward = 0.3
    elif speed <= 1:
        reward = 1e-3
    
    return float(reward)