# Introduction

Slackhook is a simple python class and CLI that makes sending a
[Slack](http://www.slack.com) Incoming WebHook easy. The class takes its
configuration from environment variables, configuration file(s), or passed in
arguments. The CLI is a small wrapper around the class that parses the command
line arguments to initialize the class and then sends a message. Under the hood,
it leverages python's `requests` module to talk to the Slack WebHook. After that,
it's just adding in a couple of ways to manage configuration.

# Installation

    $ git clone https://github.com/pete0emerson/slackhook.git
    $ cd slackhook
    $ python setup.py install

# Configuration

## Environment variables

Slackhook will load configuration variables from environment variables. Slackhook
environment variables are:

    SLACK_COMPANY
    SLACK_USERNAME
    SLACK_TOKEN
    SLACK_ICON
    SLACK_CHANNEL

## Configuration file(s)

Slackhook will also load configuration variables from files. The CLI by default
will try to load `~/.slackhook.cfg` and `./.slackhook.cfg` by default. Here is a
sample .slackhook.cfg file:

    [slackhook]
    username=my_clever_username
    company=company_name
    token=this_is_your_integration_token
    channel=#general
    icon=:ghost:

# Class Usage

The slackhook [binary](bin/slackhook) is very simple and is a good example to
follow. Here's the simplest slackhook example, which assumes that configuration
has been done either via environment variables or a configuration file.

    import slackhook

    s = slackhook.Slackhook()
    status, content = s.send('Hello, World!')

# CLI Help

    $ slackhook --help
    usage: slackhook [-h] [--config CONFIG] [--company COMPANY] [--channel CHANNEL]
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

# Example CLI usage

    $ slackhook -m 'Hello, world' # Assumes conf file or ENV variables have been set
    $ slackhook --company my_company --channel general --token aICln0wZDfQrhM2Jam2Hy3s2 --username mybot --icon ghost --message 'Hello, World!'
    $ SLACK_CHANNEL=general slackhook -m 'Use environment variables, too!'
