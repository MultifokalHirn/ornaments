# pragma: no cover
import os


def print_logo(terminal_width: int = 80) -> None:  # pragma: no cover
    """
    Prints the logo of the project.

    Logo was generated using ascii-image-converter (https://github.com/TheZoraiz/ascii-image-converter):
        $ ascii-image-converter ornaments.png --dimensions 40,17

    """
    try:
        terminal_width = os.get_terminal_size().columns
    except Exception:
        terminal_width = 80

    logo_width = 40
    padding = int((terminal_width - logo_width) / 2) * " "
    print("\n")

    print(padding + "             .::=+=--++=::.             ")
    print(padding + "         .-+++*-+++ =*+*=++=-:          ")
    print(padding + "       :+#+-=:-.:+--+++=.=+:=**=.       ")
    print(padding + "     .+#==::--+#*-...:=%%+-:**==*=      ")
    print(padding + "    .@%=*=+:*#*.       .#@#-==-==-*.    ")
    print(padding + "    #@--+=-##::          %@#=:=:+::=    ")
    print(padding + "   -@@:==+:%+-.          =@=:++=:: -.   ")
    print(padding + "   *@@:-==:%*-.          =@*+=+-+-.-.   ")
    print(padding + "   :@@:.-==+@%-          %@===+==: =.   ")
    print(padding + "    #@-++-=--#%=       :%%----=:. :=    ")
    print(padding + "     #@=.:-:+++++==:--++=.::=++..:+     ")
    print(padding + "     :*%#*=:*+: -==:#%#*.==+::..--      ")
    print(padding + "     ::-+**=++-:=--.*%%%==--.:::.       ")
    print(padding + "          :--:==-:--:--:-:::::          ")
    print(padding + "              . . :  : ...              ")
