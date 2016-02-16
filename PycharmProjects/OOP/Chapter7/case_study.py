#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@contact: plectrum@outlook.com
@software: PyCharm Community Edition
@file: case_study.py
@time: 2016/2/12 10:55
"""

import smtplib
from email.mime.text import MIMEText
from collections import defaultdict


def send_email(subject, message, from_addr, *to_addrs, host="localhost", port=1025, headers=None):
    headers = {} if headers is None else headers
    email = MIMEText(message)
    email['Subject'] = subject
    email["From"] = from_addr
    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email['To']
        email['To'] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()


class MailingList(object):
    """Manage group of e-mail addresses for sending e-mails."""

    def __init__(self):
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        groups = set(groups)
        # if pass in the group is family, print the groups
        # print(groups)
        # {'friends'}
        return {e for (e, g) in self.email_map.items() if g & groups}

    def send_mailing(self, subject, message, from_addr, *groups, **kwargs):
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, **kwargs)


m = MailingList()
m.add_to_group("friend1@example.com", "friends")
m.add_to_group("friend2@example.com", "friends")
m.add_to_group("friend3@example.com", "friends")
m.add_to_group("friend4@example.com", "friends")
m.add_to_group("friend5@example.com", "friends")
m.add_to_group("friend6@example.com", "friends")
m.add_to_group("friend7@example.com", "friends")
m.add_to_group("family1@example.com", "family")
m.add_to_group("pro1@example.com", "professional")

m.send_mailing("A Party", "Friends and family only: a party", "me@example.com", "friends", "family",
               headers={"Reply-To": "me2@example.com"})

# print(m.email_map)
# # defaultdict(
# # <class 'set'>,
# # {
# # 'family1@example.com': {'family'},
# # 'pro1@example.com': {'professional'},
# # 'friend1@example.com': {'friends'},
# # 'friend2@example.com': {'friends'}
# # }
# # )
# print(m.email_map.items())
# # [('family1@example.com', {'family'}),
# # ('friend2@example.com', {'friends'}),
# # ('pro1@example.com', {'professional'}),
# # ('friend1@example.com', {'friends'})]
# print(m.emails_in_groups("friends"))
# # {'friend1@example.com', 'friend2@example.com'}
