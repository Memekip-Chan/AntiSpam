# AntiSpam

The scripts in this repo are made to attempt to block spam on reddit. This is ultimately a futile endeavor as spammers will always think of new ways to peddle their products and avoid detection, but it is a fun programming challenge to try and tackle these problems as they come!

Be sure to **evaluate these scripts for yourself** before deploying them long term to be sure there's no security risks, as these are mostly just short term scripts that took no more than an hour or two to develop

## title_rulegen.py

The problems being addressed by this script are spammers who circumvent automoderator rules by using special unicode characters in titles within crossposts. This is a problem because:
* In reddit's automod, whenever you try to post non-standard unicode characters into a rule, it errors out
* Not everybody knows the syntax for removing based on crosspost title

This addresses both of those things by allowing the user to paste the strange non-standard unicode part of a spam title into the script, then generates an automod rule that blocks posts with Regex that can successfully match that non-standard unicode text

## spamByColor.py

This script attempts to address spam images that have captions inserted on one of their borders. With this method, simple automoderator rules won't cut it, and some image processing needs to be done to detect it (although I am a bit wary of implementing something like this, for fear of recieving a malicious image from a spammer). The strategy this script takes is 
* Divide an image into 5 regions: left border, right border, top border, bottom border, center
* Calculate the average color of each of those regions
* For each region, compare it to the average of all other regions. If it's different enough, flag the post as spam

these sorts of spammers often times just use text on black background along one of the borders when inserting their captions, which makes this method somewhat effective against them
