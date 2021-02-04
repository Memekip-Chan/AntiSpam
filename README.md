# AntiSpam

The scripts in this repo are made to attempt to block spam on reddit. This is ultimately a futile endeavor as spammers will always think of new ways to peddle their products and avoid detection, but it is a fun programming challenge to try and tackle these problems as they come!

Be sure to evaluate these scripts for yourself before deploying them long term to be sure there's no security risks, as these are mostly just short term scripts that took no more than an hour or two to develop

## title_rulegen.py

The problems being addressed by this script are:
* In reddit's automod, whenever you try to post non-standard unicode characters into a rule, it errors out
* Not everybody knows the syntax for removing based on crosspost title

This addresses both of those things by allowing the user to paste the strange non-standard unicode part of a spam title into the script, then generates an automod rule that blocks posts with Regex that can successfully match that non-standard unicode text
