# pragma: no cover
import os


def print_logo(padded: bool = True) -> None:  # pragma: no cover
    """
    Prints the logo of the project.

    Logo was generated using ascii-image-converter (https://github.com/TheZoraiz/ascii-image-converter):
        $ ascii-image-converter ornaments.png --dimensions 40,17

    """
    try:
        term_width = os.get_terminal_size().columns
    except Exception:
        term_width = 80

    logo_width = 40
    padding = int((term_width - logo_width) / 2) * " "
    if padded:

        def print_func(to_print: str) -> None:
            print(padding + to_print)
    else:

        def print_func(to_print: str) -> None:
            print(to_print)

    print()
    print_func(r"             .::=+=--++=::.             ")
    print_func(r"         .-+++*-+++ =*+*=++=-:          ")
    print_func(r"       :+#+-=:-.:+--+++=.=+:=**=.       ")
    print_func(r"     .+#==::--+#*-...:=%%+-:**==*=      ")
    print_func(r"    .@%=*=+:*#*.       .#@#-==-==-*.    ")
    print_func(r"    #@--+=-##::          %@#=:=:+::=    ")
    print_func(r"   -@@:==+:%+-.          =@=:++=:: -.   ")
    print_func(r"   *@@:-==:%*-.          =@*+=+-+-.-.   ")
    print_func(r"   :@@:.-==+@%-          %@===+==: =.   ")
    print_func(r"    #@-++-=--#%=       :%%----=:. :=    ")
    print_func(r"     #@=.:-:+++++==:--++=.::=++..:+     ")
    print_func(r"     :*%#*=:*+: -==:#%#*.==+::..--      ")
    print_func(r"     ::-+**=++-:=--.*%%%==--.:::.       ")
    print_func(r"          :--:==-:--:--:-:::::          ")
    print_func(r"              . . :  : ...              ")


if __name__ == "__main__":  # pragma: no cover
    print_logo(padded=False)
