def read_file(file_name):
    numbers = []
    with open(file_name, 'r') as f:
        for line in f:
            numbers.append(int(line))
    return numbers


def write_file(l):
    with open('helper/response.txt', 'w') as f:
        for n in l:
            f.write('{}\n'.format(n))


if __name__ == '__main__':
    list_of_files = ['helper/1.txt', 'helper/2.txt', 'helper/3.txt']
    response = []
    for f in list_of_files:
        response += read_file(f)
    write_file(sorted(response))
