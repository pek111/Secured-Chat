# Secured Chat

Yes. It's a private chat with two layers* of encryption.

(*The message is encrypted once but uses two encryption types to send data.)

## Installation

It is very easy to install, just follow the steps below.

1. First, you must have [Python](https://www.python.org/) installed. Python version 3.10.1 and above is tested, any version before that is not guaranteed to run properly. (Note: This program was written on Python version 3.12.3)
2. And then you must install all dependencies to run the program. I recommend using Virtual Environments such as [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) and venv.
3. If you wish to use venv, please follow [these instructions](##Installing-dependencies-with-venv).
4. Now it's time to install the required dependencies. Use `pip install -r requirements.txt` to automatically install all required dependencies.
5. After you've installed the required dependencies, you can simply double-click on `main.py` or run `python main.py` to run the program.
6. Well done! You've completed all installation processes and can now proceed to [program usage](##Usage).

### Installing dependencies with venv

1. First, install the venv package with `pip install venv`
2. Then navigate to the folder you want to create the virtual environment and use `python venv .venv`
3. Great job! You've created a virtual environment. You can now proceed to the next step of [installation](##Installation).

## Usage

After you've completed all installation processes, you can now use the program.

You must first choose between hosting a server or connecting to a hosted server. If you choose to host a server, head to [Hosting a Server](###Hosting-a-Server). But if you choose to connect to a hosted server, head to [Connecting to a Server](###Connecting-to-a-Server)

### Hosting a Server

To host a server, you must have at least one open port and your IPv4 address (you can also use IPv6 but I don't guarantee that it will work properly).

You can use your local IP address if your partner is in the same network as you or the same VPN network.

But if not, you can forward a port and use your public IP address (**VERY DANGEROUS**) or use something like [ngrok](https://ngrok.com/), [locahost.run](https://localhost.run/) or [Serveo](https://serveo.net/) (kinda broken but great).

1. First, enter your desired hosting IP address.
2. Then enter your desired hosting port.
3. After that you must choose a password. The password must be strong enough since it's also a part of encryption (e.g. `!qwerty321` is a bad password but `WdqW#CqgY3'1I4lZc-G6g^` isn't). You can also use `passgen.py` to generate a strong password for you.
4. Now that you've done all the steps above, you can wait for your partner to connect with you. After you and your partner are connected, you can use `/help` to see all commands available.

### Connecting to a Server

It is very easy to connect to a server. You can follow the steps below to see how.

1. First, enter the server's (host) IP address.
2. After that, enter the port it is hosted on.
3. Then you must enter the password given by your partner. If you don't have it, you cannot connect to the server.
4. Now that you and your partner are connected, you can use `/help` to see all commands available.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Have fun chatting :)
