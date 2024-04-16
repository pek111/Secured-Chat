menu_prompt = """\033[0m\033[38;2;35;209;139m
██████╗ ███████╗ █████╗      ██████╗██╗  ██╗ █████╗ ████████╗
██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║  ██║██╔══██╗╚══██╔══╝
██████╔╝███████╗███████║    ██║     ███████║███████║   ██║
██╔══██╗╚════██║██╔══██║    ██║     ██╔══██║██╔══██║   ██║
██║  ██║███████║██║  ██║    ╚██████╗██║  ██║██║  ██║   ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝

                      \033[38;2;229;229;229mMade by \033[38;2;205;49;49mVoximir
\033[38;2;35;209;139m
Select an option:

\033[38;2;245;245;67m╭───╮  ╭───────────────────╮
│ \033[38;2;229;229;229m1 \033[38;2;245;245;67m├──┤   \033[38;2;229;229;229mHost a server   \033[38;2;245;245;67m│
╰───╯  ╰───────────────────╯
\033[38;2;245;245;67m╭───╮  ╭───────────────────╮
│ \033[38;2;229;229;229m2 \033[38;2;245;245;67m├──┤ \033[38;2;229;229;229mConnect to server \033[38;2;245;245;67m│
╰───╯  ╰───────────────────╯

\033[38;2;229;229;229mChoice: \033[2m"""

unknown_ip_port = """\033[0m\033[38;2;35;209;139mInformation:

\033[38;2;245;245;67m╭──────╮  ╭───────────────────╮
│  \033[38;2;229;229;229mIP  \033[38;2;245;245;67m├──┤        \033[38;2;229;229;229m╶─╴        \033[38;2;245;245;67m│
╰──────╯  ╰───────────────────╯
\033[38;2;245;245;67m╭──────╮  ╭───────────────────╮
│ \033[38;2;229;229;229mPort \033[38;2;245;245;67m├──┤        \033[38;2;229;229;229m╶─╴        \033[38;2;245;245;67m│
╰──────╯  ╰───────────────────╯

\033[38;2;229;229;229mEnter the IP address: \033[2m"""

unknown_port = """\033[0m\033[38;2;35;209;139mInformation:

\033[38;2;245;245;67m╭──────╮  ╭───────────────────╮
│  \033[38;2;229;229;229mIP  \033[38;2;245;245;67m├──┤\033[38;2;229;229;229m{}\033[38;2;245;245;67m│
╰──────╯  ╰───────────────────╯
\033[38;2;245;245;67m╭──────╮  ╭───────────────────╮
│ \033[38;2;229;229;229mPort \033[38;2;245;245;67m├──┤        \033[38;2;229;229;229m╶─╴        \033[38;2;245;245;67m│
╰──────╯  ╰───────────────────╯

\033[38;2;229;229;229mEnter the port: \033[2m"""

server_starting = """\033[0m\033[38;2;35;209;139mInformation:

\033[38;2;245;245;67m╭──────╮  ╭───────────────────╮
│  \033[38;2;229;229;229mIP  \033[38;2;245;245;67m├──┤\033[38;2;229;229;229m{}\033[38;2;245;245;67m│
╰──────╯  ╰───────────────────╯
\033[38;2;245;245;67m╭──────╮  ╭───────────────────╮
│ \033[38;2;229;229;229mPort \033[38;2;245;245;67m├──┤\033[38;2;229;229;229m{}\033[38;2;245;245;67m│
╰──────╯  ╰───────────────────╯

"""

client_connecting = """\033[0m\033[38;2;35;209;139mInformation:

\033[38;2;245;245;67m╭──────╮  ╭───────────────────╮
│  \033[38;2;229;229;229mIP  \033[38;2;245;245;67m├──┤\033[38;2;229;229;229m{}\033[38;2;245;245;67m│
╰──────╯  ╰───────────────────╯
\033[38;2;245;245;67m╭──────╮  ╭───────────────────╮
│ \033[38;2;229;229;229mPort \033[38;2;245;245;67m├──┤\033[38;2;229;229;229m{}\033[38;2;245;245;67m│
╰──────╯  ╰───────────────────╯

"""

client_failed_intrnt = """\033[0m\033[38;2;241;76;76mError:

\033[38;2;245;245;67m╭───────╮       ╭────────╮       ╭────────╮
│  \033[38;2;229;229;229mYou  \033[38;2;245;245;67m├───\033[38;2;35;209;139m✓\033[38;2;245;245;67m───┤ \033[38;2;229;229;229mRouter \033[38;2;245;245;67m├┄┄┄\033[38;2;241;76;76m✗\033[38;2;245;245;67m┄┄┄┤  \033[38;2;229;229;229mHost  \033[38;2;245;245;67m│
╰───────╯       ╰────────╯   │   ╰────────╯
                           \033[38;2;241;76;76mError

Failed to connect to the server: \033[38;2;229;229;229mUnknown host.\033[0m"""

client_failed_no_intrnt = """\033[0m\033[38;2;241;76;76mError:

\033[38;2;245;245;67m╭───────╮       ╭────────╮       ╭────────╮
│  \033[38;2;229;229;229mYou  \033[38;2;245;245;67m├┄┄┄\033[38;2;241;76;76m✗\033[38;2;245;245;67m┄┄┄┤ \033[38;2;229;229;229mRouter \033[38;2;245;245;67m├┄─┄\033[38;2;204;204;204m\033[2m?\033[0m\033[38;2;245;245;67m┄─┄┤  \033[38;2;229;229;229mHost  \033[38;2;245;245;67m│
╰───────╯   │   ╰────────╯   │   ╰────────╯
          \033[38;2;241;76;76mError           \033[38;2;204;204;204m\033[2mUnknown\033[0m

\033[38;2;241;76;76mFailed to connect to the server: \033[38;2;229;229;229mNo internet connection.\033[0m"""

server_bad_ip_or_port = """\033[38;2;241;76;76mError:

\033[0m\033[38;2;241;76;76mFailed to start the server: \033[38;2;229;229;229mPlease enter valid IP address and port number.\033[0m"""

server_no_intrnt = """\033[38;2;241;76;76mError:

\033[0m\033[38;2;241;76;76mFailed to start the server: \033[38;2;229;229;229mPlease check your internet connection.\033[0m"""

client_connected = """\033[0m
\033[38;2;245;245;67m╭──────────────────────────────────╮
│  \033[38;2;35;209;139m██████╗██╗  ██╗ █████╗ ████████╗\033[38;2;245;245;67m│
│ \033[38;2;35;209;139m██╔════╝██║  ██║██╔══██╗╚══██╔══╝\033[38;2;245;245;67m│
│ \033[38;2;35;209;139m██║     ███████║███████║   ██║   \033[38;2;245;245;67m│
│ \033[38;2;35;209;139m██║     ██╔══██║██╔══██║   ██║   \033[38;2;245;245;67m│
│ \033[38;2;35;209;139m╚██████╗██║  ██║██║  ██║   ██║   \033[38;2;245;245;67m│
│  \033[38;2;35;209;139m╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   \033[38;2;245;245;67m│
╰──────────────────────────────────╯

\033[48;2;245;245;67m\033[38;2;0;0;0m\033[1m Control \033[0m \033[38;2;229;229;229mPartner connected."""

help_cmd = """\033[0m\033[48;2;214;112;214m\033[38;2;0;0;0m\033[1m Command \033[0m \033[38;2;229;229;229m/exit - Exit the chat
          /help - Show this message
          Enter \"\"\" to start and end a multiline message."""

if __name__ == "__main__":
    print("This is a module. Import this module in main.py.")
