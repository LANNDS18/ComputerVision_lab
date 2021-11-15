def test():
    print('test')


def mini_number(numbers):
    mini = numbers[0]
    for i in numbers:
        if i < mini:
            mini = i
    return mini


def test_mini_number():
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(mini_number(test_numbers))


def dp_mini_number(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return mini_number(numbers[:2])


def test_dp_mini_number():
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(dp_mini_number(test_numbers))

def convolve_images(image1, image2):
    result = []
    for i in range(len(image1)):
        result.append([])
        for j in range(len(image1[0])):
            result[i].append(image1[i][j] + image2[i][j])
    return result
