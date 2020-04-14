from math import sqrt, pi, sin, cos

ERROR = 0.01


def AlmostEqual(first, second):
    delta = abs(ERROR * first)
    diff = abs(first - second)
    assert diff <= delta


def task1(planets_num: int, check_time: int, bodys: list):
    accelerate_sum = []
    ans = []
    for m in range(check_time):
        for n in range(planets_num):
            accelerate_temp = [0, 0]
            for inde in range(planets_num):
                if inde == n:
                    continue
                accelerate_temp[0] -= (bodys[inde][0]/((bodys[n][1]-bodys[inde][1])**2+(bodys[n][2]-bodys[inde][2])**2)*
                    (bodys[n][1]-bodys[inde][1])/sqrt((bodys[n][1]-bodys[inde][1])**2+(bodys[n][2]-bodys[inde][2])**2))
                accelerate_temp[1] -= (bodys[inde][0]/((bodys[n][1]-bodys[inde][1])**2+(bodys[n][2]-bodys[inde][2])**2)*
                    (bodys[n][2]-bodys[inde][2])/sqrt((bodys[n][1]-bodys[inde][1])**2+(bodys[n][2]-bodys[inde][2])**2))
            else:
                accelerate_sum.append(accelerate_temp)
        for p in range(planets_num):
            bodys[p][3] += accelerate_sum[p][0]
            bodys[p][4] += accelerate_sum[p][1]
            bodys[p][1] += bodys[p][3]
            bodys[p][2] += bodys[p][4]
        accelerate_sum.clear()
    for q in range(planets_num):
        ans.append([bodys[q][1], bodys[q][2]])
    return ans


def task2(check_time: int, bodys: list):
    sun = 0
    accelerate_sum = []
    for m in range(check_time):
        for n in range(4):
            accelerate_temp = [0, 0]
            for inde in range(4):
                if inde == n:
                    continue
                accelerate_temp[0] -= (bodys[inde][0] / (
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2) *
                                       (bodys[n][1] - bodys[inde][1]) / sqrt(
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2))
                accelerate_temp[1] -= (bodys[inde][0] / (
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2) *
                                       (bodys[n][2] - bodys[inde][2]) / sqrt(
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2))
            else:
                accelerate_sum.append(accelerate_temp)
        for p in range(4):
            bodys[p][3] += accelerate_sum[p][0]
            bodys[p][4] += accelerate_sum[p][1]
            bodys[p][1] += bodys[p][3]
            bodys[p][2] += bodys[p][4]
        accelerate_sum.clear()
    for r in range(3):
        if sqrt((bodys[3][1]-bodys[r][1])**2+(bodys[3][2]-bodys[r][2])**2) <= 200:
            sun += 1
    if sun == 0:
        return "Eternal Night"
    elif sun == 1:
        return "Stable Era"
    elif sun == 2:
        return "Double-Solar Day"
    elif sun == 3:
        return "Tri-Solar Day"


def task3(check_time: int, bodys: list):
    S = 0
    accelerate_sum = []
    for m in range(check_time):
        for n in range(4):
            accelerate_temp = [0, 0]
            for inde in range(4):
                if inde == n:
                    continue
                accelerate_temp[0] -= (bodys[inde][0] / (
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2) *
                                       (bodys[n][1] - bodys[inde][1]) / sqrt(
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2))
                accelerate_temp[1] -= (bodys[inde][0] / (
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2) *
                                       (bodys[n][2] - bodys[inde][2]) / sqrt(
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2))
            else:
                accelerate_sum.append(accelerate_temp)
        for p in range(4):
            bodys[p][3] += accelerate_sum[p][0]
            bodys[p][4] += accelerate_sum[p][1]
            bodys[p][1] += bodys[p][3]
            bodys[p][2] += bodys[p][4]
        accelerate_sum.clear()
        suns = 0
        for r in range(3):
            if sqrt((bodys[3][1] - bodys[r][1]) ** 2 + (bodys[3][2] - bodys[r][2]) ** 2) <= 200:
                suns += 1
        if suns == 1:
            S += 2
        else:
            S -= 1
        if S < 0:
            break
    if S < 0:
        return "No civilization"
    elif S < 400:
        return "level 1 civilization"
    elif S < 1200:
        return "level 2 civilization"
    else:
        return "level 3 civilization"


def task_bonus(check_time: int, bodys: list):
    day = 0
    accelerate_sum = []
    for m in range(check_time):
        for n in range(4):
            accelerate_temp = [0, 0]
            for inde in range(4):
                if inde == n:
                    continue
                accelerate_temp[0] -= (bodys[inde][0] / (
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2) *
                                       (bodys[n][1] - bodys[inde][1]) / sqrt(
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2))
                accelerate_temp[1] -= (bodys[inde][0] / (
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2) *
                                       (bodys[n][2] - bodys[inde][2]) / sqrt(
                            (bodys[n][1] - bodys[inde][1]) ** 2 + (bodys[n][2] - bodys[inde][2]) ** 2))
            else:
                accelerate_sum.append(accelerate_temp)
        for p in range(4):
            bodys[p][3] += accelerate_sum[p][0]
            bodys[p][4] += accelerate_sum[p][1]
            bodys[p][1] += bodys[p][3]
            bodys[p][2] += bodys[p][4]
        accelerate_sum.clear()
        suns = 0
        for r in range(3):
            if (bodys[3][1] - bodys[r][1]) ** 2 + (bodys[3][2] - bodys[r][2]) ** 2 <= 40000:
                suns += 1
        if suns != 1:
            continue
        for h in range(3):
            if (bodys[h][1]-bodys[3][1])*sin(m/180*pi)+(bodys[h][2]-bodys[3][2])*cos(m/180*pi) < 0:
                break
        else:
            day += 1
    return day


if __name__ == "__main__":
    '''
    Task 1 Example 1
    <planets-num> = 2, <check-time>  = 1986
    <planet1-mass> = 10000, <planet1-coordinate-x> = 0, <planet1-coordinate-y> = 0, <planet1-speed-x> = 0, <planet1-speed-y> = 0
    <planet2-mass> = 0.1, <planet2-coordinate-x> = 1000, <planet2-coordinate-y> = 0, <planet2-speed-x> = 0, <planet2-speed-y> = sqrt(10)
    '''
    output = task1(
        2,
        1986,
        [
            [10000, 0, 0, 0, 0],
            [0.1, 1000, 0, 0, sqrt(10)]
        ]
    )
    answer = [(-4.568800204932483e-09, 0.06283041322543657), (1000.0004568800274, -2.757889449272592)]
    for i in range(len(answer)):
        for j in (0, 1):
            ans = answer[i][j]
            out = output[i][j]
            AlmostEqual(ans, out)

    '''
    Task 2 Example 1
    <check-time>  = 1986
    <sun1-mass> = 1000, <sun1-coordinate-x> = 0, <sun1-coordinate-y> = 0, <sun1-speed-x> = 0, <sun1-speed-y> = 0
    <sun2-mass> = 1, <sun2-coordinate-x> = 1000000, <sun2-coordinate-y> = 0, <sun2-speed-x> = 0, <sun2-speed-y> = 0
    <sun3-mass> = 1, <sun3-coordinate-x> = -1000000, <sun3-coordinate-y> = 0, <sun3-speed-x> = 0, <sun3-speed-y> = 0
    <planet-mass> = 0.1, <planet-coordinate-x> = 100, <planet-coordinate-y> = 0, <planet-speed-x> = 0, <planet-speed-y> = sqrt(10)
    '''
    output = task2(
        1986,
        [
            [1000, 0, 0, 0, 0],
            [1, 1000000, 0, 0, 0],
            [1, -1000000, 0, 0, 0],
            [0.1, 100, 0, 0, sqrt(10)]
        ]
    )
    assert output == "Stable Era"

    '''
    Task 3 Example 1
    <check-time>  = 600
    <sun1-mass> = 1000, <sun1-coordinate-x> = 0, <sun1-coordinate-y> = 0, <sun1-speed-x> = 0, <sun1-speed-y> = 0
    <sun2-mass> = 0.001, <sun2-coordinate-x> = 148.6, <sun2-coordinate-y> = 0, <sun2-speed-x> = 0, <sun2-speed-y> = -2.59
    <sun3-mass> = 0.001, <sun3-coordinate-x> = 0, <sun3-coordinate-y> = 148.6, <sun3-speed-x> = 2.59, <sun3-speed-y> = 0
    <planet-mass> = 0.001, <planet-coordinate-x> = 0, <planet-coordinate-y> = -148.6, <planet-speed-x> = -2.59, <planet-speed-y> = sqrt(10)
    '''
    omega = 2*pi/360
    R = (1000/omega**2)**(1/3)
    output = task3(
        600,
        [
            [1000, 0, 0, 0, 0],
            [0.001, R, 0, 0, -omega*R],
            [0.001, 0, R, omega*R, 0],
            [0.001, 0, -R, -omega*R, 0]
        ]
    )
    assert output == "level 3 civilization"

    '''
    Task BONUS Example 1
    <check-time>  = 6000
    <sun1-mass> = 1000, <sun1-coordinate-x> = 0, <sun1-coordinate-y> = 0, <sun1-speed-x> = 0, <sun1-speed-y> = 0
    <sun2-mass> = 0.001, <sun2-coordinate-x> = 148.6, <sun2-coordinate-y> = 0, <sun2-speed-x> = 0, <sun2-speed-y> = -2.59
    <sun3-mass> = 0.001, <sun3-coordinate-x> = 0, <sun3-coordinate-y> = 148.6, <sun3-speed-x> = 2.59, <sun3-speed-y> = 0
    <planet-mass> = 0.001, <planet-coordinate-x> = 0, <planet-coordinate-y> = -148.6, <planet-speed-x> = -2.59, <planet-speed-y> = sqrt(10)
    '''
    omega = 2*pi/360
    R = (1000/omega**2)**(1/3)
    output = task_bonus(
        6000,
        [
            [1000, 0, 0, 0, 0],
            [0.001, R, 0, 0, -omega*R],
            [0.001, 0, R, omega*R, 0],
            [0.001, 0, -R, -omega*R, 0]
        ]
    )
    assert output == 6000
