MAX_DAYS = 80

with open("data.txt") as file:
    data = [int(lfish) for lfish in file.readline().split(",")]

def rec_produce(day, data):
    for i in range(len(data)):
        data[i] -= 1
        if data[i] < 0:
            data[i] = 6
            data.append(8)

    # print(f"After {str(day).rjust(2)} days: {data}")
    if (day < MAX_DAYS):
        return rec_produce(day + 1, data)
    return data

# print(data)

if __name__ == "__main__":
    data = rec_produce(1, data)
    print(len(data))