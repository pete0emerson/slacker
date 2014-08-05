# Introduction

Slacker is a simple python class and CLI that makes sending a [Slack](http://www.slack.com) Incoming WebHook easy.
The class takes its configuration from environment variables, configuration file(s), or passed in arguments. The CLI
is a small wrapper around the class that parses the command line arguments to initialize the class and then sends a message.

# Installation

    $ git clone https://github.com/pete0emerson/slacker.git
    $ cd slacker
    $ python setup.py install

# Configuration

## Environment variables

Slacker will load configuration variables from environment variables. Slacker environment variables are:

    SLACK_COMPANY
    SLACK_USERNAME
    SLACK_TOKEN
    SLACK_ICON
    SLACK_CHANNEL

## Configuration file(s)

Slacker will also load configuration variables from files. The CLI by default will try to load `~/.slacker.cfg`
and `./.slacker.cfg` by default. Here is a sample .slacker.cfg file:

    [slacker]
    username=my_clever_username
    company=company_name
    token=this_is_your_integration_token
    channel=#general
    icon=:ghost:

# Class Usage

The slacker [binary](bin/slacker) is very simple and is a good example to follow. Here's the simplest slacker example,
which assumes that configuration has been done either via environment variables or a configuration file.

    import slacker

    s = slacker.Slacker()
    status, content = s.send('Hello, World!')

# CLI Usage

    $ slacker --help
    usage: slacker [-h] [--config CONFIG] [--company COMPANY] [--channel CHANNEL]
                   [--token TOKEN] [--username USERNAME] [--icon ICON] --message
                   MESSAGE

    Slack CLI to Incoming WebHook

    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG, -c CONFIG
                            Config file(s)
      --company COMPANY, -co COMPANY
                            Company
      --channel CHANNEL, -ch CHANNEL
                            Channel
      --token TOKEN, -t TOKEN
                            Token
      --username USERNAME, -u USERNAME
                            Username
      --icon ICON, -i ICON  Emoji Icon
      --message MESSAGE, -m MESSAGE
                            Message to send

    The following environment variables may be also used: SLACK_COMPANY,
    SLACK_TOKEN, SLACK_CHANNEL, SLACK_USERNAME, SLACK_ICON
