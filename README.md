# SpaceProgram-Bot-7402
Stone Monkeys' BAS Hackathon bot entry.

The bot is designed to build a spaceship from scratch. A spaceship consists of 4 sections:
1) The hull.
2) The engine.
3) The cockpit.
4) The boosters.
5) The accessory.

Each section has a list with all the different parts available for building. 
A facebook post is made for each section in the order aforementioned. The script will pull 4 different parts from the list and put them on the facebook post for voting using the facebook reacts. 
After a certain amount of time has passed, the bot will read the amount of reacts in the post and use them to pick the winning part of the 4. It will then be added to the spaceship.
Another post will then be made for the next section, and so on until the ship is finally built. 

After the ship is built, the next post will be the launch. At the moment, the results are randomly generated. Two factors come into play here:
1) Distance travelled.
2) Mission result.

The distance is a random number selected between 0 and 2,147,483,600. 
The mission result is randomly selected from a list. 


Post Frequency: 
The post frequency will be 1 post per day, with the first post being on Monday at 00:00. This way, people from all timezones will have a chance to vote on all segments. The launch sequence will be made on Saturday. On Sunday, the bot will not post because it is attending church. 


Scalability: 
The lists of each segment can be increased as time passes. New entries can be added non-disruptively as they are separate files from the script. The script will only read from them before making the post. 


Future improvements (AFTER HACKATHON):
1) The use of images. Each part with its own image will be used to "build" the rocket. Similar to how Bottlebot1904 works. 
2) The launch sequence image could show a map of the solar system and a visual representation of the distance travelled. 
3) Each part has "stats" that will influence the outcome of the mission. This would make the bot more interesting, but less RNG-ish (funny haha factor).
  a) Hull defines integrity (ship exploding or not)
  b) cockpit defines crew integrity
  c) engine defines distance travelled 
  d) boosters define takeoff success (ship exploding or not)
  e) Accessory defines mission success rate (difficult, depends on mission which is RNG by nature so cannot make accessories be 100% RNG)
  

