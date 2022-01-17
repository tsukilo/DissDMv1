from time import sleep
import subprocess
import sys
try:
    import discum
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "discum"])

print('''
       _             _         _           _            _            _   _       
      /\ \          /\ \      / /\        / /\         /\ \         /\_\/\_\ _   
     /  \ \____     \ \ \    / /  \      / /  \       /  \ \____   / / / / //\_\ 
    / /\ \_____\    /\ \_\  / / /\ \__  / / /\ \__   / /\ \_____\ /\ \/ \ \/ / / 
   / / /\/___  /   / /\/_/ / / /\ \___\/ / /\ \___\ / / /\/___  //  \____\__/ /  
  / / /   / / /   / / /    \ \ \ \/___/\ \ \ \/___// / /   / / // /\/________/   
 / / /   / / /   / / /      \ \ \       \ \ \     / / /   / / // / /\/_// / /    
/ / /   / / /   / / /   _    \ \ \  _    \ \ \   / / /   / / // / /    / / /     
\ \ \__/ / /___/ / /__ /_/\__/ / / /_/\__/ / /   \ \ \__/ / // / /    / / /      
 \ \___\/ //\__\/_/___\/ \/___/ /  \ \/___/ /     \ \___\/ / \/_/    / / /       
  \/_____/ \/_________/ \_____\/    \_____\/       \/_____/          \/_/        
                                                                                 
''')

print("Written by Bea")
print("V2 coming soon!")

bot = discum.Client(token=input("What is your token?: "), log=False)

guild_id = input("What is the ID of the guild you would like to MassDM?: ")
channel_id = input("What is the main channel ID of the guild?: ")

bot.gateway.fetchMembers(guild_id, channel_id, method="overlap")


@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()


bot.gateway.run()

message = input("What message would you like to send?: ")

for memberID in bot.gateway.session.guild(guild_id).members:
    newDM = bot.createDM([memberID]).json()["id"]
    sleep(2)
    bot.sendMessage(newDM, message)
    sleep(2)
