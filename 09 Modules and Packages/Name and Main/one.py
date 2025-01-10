def func():
    print(f"func() ran in one.py")

print(f"Top level inside one.py")

if __name__ == '__main__':
    print(f"one.py ran directy")
else:
    print(f"one.py imported")