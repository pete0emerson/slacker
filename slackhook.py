#!/usr/bin/env python

import ConfigParser
import requests
import json
import os
import sys

class Slackhook:

  def _set_element(self, element, value):
    # This automagically calls the right self.set_{ELEMENT}
    unpack_options = { 'username':self.set_username, 'company':self.set_company, 'token':self.set_token, 'channel':self.set_channel, 'icon':self.set_icon}
    if element in unpack_options:
      unpack_options[element](value)

  def _load_config(self, config_file):
    config_file = os.path.abspath(os.path.expanduser(config_file))
    if not os.access(config_file, os.R_OK):
      return
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    options = config.options('slackhook')
    for element in ['username', 'company', 'token', 'channel', 'icon']:
      if element in options:
        self._set_element(element, config.get('slackhook', element))

  def _load_env_vars(self):
    if 'SLACK_COMPANY' in os.environ:
      self.set_company(os.environ['SLACK_COMPANY'])
    if 'SLACK_TOKEN' in os.environ:
      self.set_token(os.environ['SLACK_TOKEN'])
    if 'SLACK_CHANNEL' in os.environ:
      self.set_channel(os.environ['SLACK_CHANNEL'])
    if 'SLACK_USERNAME' in os.environ:
      self.set_username(os.environ['SLACK_USERNAME'])
    if 'SLACK_ICON' in os.environ:
      self.set_icon(os.environ['SLACK_ICON'])

  def set_company(self, company):
    self.company = company
    self.url = 'https://' + self.company + '.slack.com/services/hooks/incoming-webhook'

  def set_token(self, token):
    self.token = token

  def set_channel(self, channel):
    if not channel.startswith('#'):
      channel = '#' + channel
    self.channel = channel

  def set_username(self, username):
    self.username = username

  def set_icon(self, icon):
    if not icon.startswith(':') or not icon.endswith(':'):
      icon = ':' + icon + ':'
    self.icon = icon

  def __init__(self, config_files=None, company=None, token=None, channel=None, username=None, icon=None):
    # Precidence order is command argument > ENV variable > file
    self.company = None
    self.token = None
    self.channel = None
    self.username = None
    self.icon = None
    for config_file in config_files:
      self._load_config(config_file)
    self._load_env_vars()
    for element in ['company', 'token', 'channel', 'username', 'icon']:
      value = locals()[element]
      if value:
        self._set_element(element, value)

  def send(self, message):
    if not self.token:
      return 1, 'No token set.'
    if not self.channel:
      return 1, 'No channel set.'
    if not self.username:
      return 1, 'No username set.'
    if not self.icon:
      return 1, 'No icon set.'
    if not message:
      return 1, 'No message set.'
    params = {'token':self.token}
    payload = {'channel':self.channel, 'username':self.username, 'icon_emoji':self.icon, 'text':message}
    r = requests.post(self.url, params=params, data=json.dumps(payload))
    return r.status_code, r.content
