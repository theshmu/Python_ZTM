def highest_even(num_list=[]):
    high = None
    if len(num_list) == 0:
        print('There are no numbers in the list')
        return

    for num in num_list:
        if num % 2 == 0 and (high is None or num > high):
            high = num

    if high is None:
        print('There are no even numbers in the list')
    else:
        print(f'The highest even number is {high}')


highest_even([1, 3, 5, -20, 2])
