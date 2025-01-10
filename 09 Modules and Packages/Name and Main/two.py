import one

print(f"Top level inside two.py")

one.func()

if __name__ == '__main__':
    print(f"two.py ran directy")
else:
    print(f"two.py imported")