from src.read import Read
from src.write import Write

read = Read()
write = Write()


def main():
    name = str(input("Name: "))
    age = int(input("Age: "))
    username = str(input("UserName: "))
    password = str(input("Password: "))

    write.add_data(name, age, username, password)
    read.read_data()


if __name__ == '__main__':
    main()
