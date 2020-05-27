def rps_analysis(data_base):
    # print(data_base)
    F = []
    Data_sort1 = ''
    Data_sort2 = []
    finished = []
    for m in range(len(data_base)):
        if data_base[m] == '-':
            F.append(m)
    between = 0
    for index in F:
        for sort1 in [data_base[between:index]]:
            for sort2 in sort1:
                if sort2 != '\n' and sort2 != '-':
                    Data_sort1 += sort2
            for sort3 in range(int(len(Data_sort1) / 2)):
                Data_sort2.append(Data_sort1[2 * sort3:2 * sort3 + 2])
            finished.append(Data_sort2)
        Data_sort1 = ''
        Data_sort2 = []
        between = index
    return finished


def rps_probability(data_base):
    R = 0
    P = 0
    S = 0
    data_base = str(data_base)
    for el in data_base:
        if el == 'R':
            R += 1
        elif el == 'P':
            P += 1
        elif el == 'S':
            S += 1

    RPS_Probability = {'R_Probability': str(R / (R + P + S) * 100)[:5] + ' %',
                       'P_Probability': str(P / (R + P + S) * 100)[:5] + ' %',
                       'S_Probability': str(S / (R + P + S) * 100)[:5] + ' %'}
    return RPS_Probability


def rps_start_rps_probability(data_base):
    R = 0
    P = 0
    S = 0
    for el in data_base:
        if el[0][0] == 'R':
            R += 1
        elif el[0][0] == 'P':
            P += 1
        elif el[0][0] == 'S':
            S += 1
        elif el[0][1] == 'R':
            R += 1
        elif el[0][1] == 'P':
            P += 1
        elif el[0][1] == 'S':
            S += 1
    RPS_Start_probability = {'R_Start_Probability': str(R / (R + P + S) * 100)[:5] + ' %',
                             'P_Start_Probability': str(P / (R + P + S) * 100)[:5] + ' %',
                             'S_Start_Probability': str(S / (R + P + S) * 100)[:5] + ' %'}
    return RPS_Start_probability


if __name__ == '__main__':
    with open('RPS DataBase.txt', 'r') as f:
        d = rps_analysis(f.read())
        RPS_probability = rps_probability(d)
        RPS_Start_probability = rps_start_rps_probability(d)
        print(RPS_probability)
        print(RPS_Start_probability)
