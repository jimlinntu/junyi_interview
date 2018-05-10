def f(string):
    string = string.strip("\"")
    return "\"" + " ".join(list(map(lambda x: x[::-1], string.split(" ")))) + "\""

if __name__ == '__main__':
    string = input()
    print(f(string))