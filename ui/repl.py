from commands import app
import shlex

def repl():
    baseUrl = "solon > "
    exitBase = "exit"

    while True:
        try:
            raw = input(baseUrl).strip()
            if not raw:
                continue

            args = shlex.split(raw)
            if(exitBase in args):
                break

            try:
                app(args)
            except SystemExit as e:
                print("here")
                if e.code != 0:
                    print(f"Command failed with error code: {e.code}")

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        except Exception as e:
            print("Some error occurred:", e)
        

if __name__ == "__main__":
    repl()
