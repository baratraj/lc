if __name__ == '__main__':
    names = []
    scores = []
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        records.append([name, score])

    scores_list = list(set(scores))
    scores_list.sort()
    second_low = scores_list[1]
    output_names = []
    # for i in records:
    #     if i[1] == second_low:
    #         output_names.append(i[0])
    # output_names.sort()

    out = [i[0] for i in records if i[1] == second_low]
    out.sort()


