import argparse

parser = argparse.ArgumentParser(
        prog='GreeterPy',
        description='Greet user using python',
        epilog="That's all"
        )

parser.add_argument("username")

args = parser.parse_args()
print(f"Greeting for you, {args.username}!!!")
