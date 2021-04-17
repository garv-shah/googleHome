import random
from googlehomepush import GoogleAssistant

bhrQuotes = [
    """Garv: You know that’ll kill you right?
    Zimo: *smoking drugs* Yeah that’s the point.
    Nick: *Drinking alcohol* We’re trying to speed up the process.
    Will: *Eating raw cookie dough*, yEAH""",
    """Will: Where’s Nick?
    Zimo: Off disappointing Jesus""",
    """Zimo: I have this completely under control.
    Garv: Is that why everythings on fire?""",
    """Police: OPEN UP ITS THE POLICE!!!
Nick: I have this secret fear people view me as dumb
Police: We mean open the door you fucking moron""",
    """Will: a-choo!
Nick: Oh my god are you sick *takes off jacket* why didn’t you say something i fucking told you to bring more fucking layers and of course you didn’t fucking listen *piles scarves onto Will* why didn’t you say something we can go get soup now if you’d like jesus now i have to make sure you don’t fucking freeze to death *takes zimos hat* how long have you even been cold for--
Zimo: a-choo!
Nick: Oh my god can you shut up?""",
    """Garv: If you bite it and you die, it’s poisonous. If it bites you and you die, it’s venomous.
Nick: What if it bites me and it dies?
Will: That means YOU’RE poisonous 
Zimo: What if it bites itself and I die?
Garv: That’s voodoo 
Nick: What if it bites me and someone else dies?
Will: That’s correlation not causation!
Zimo: What if we bite each other and neither of us die? 
Garv and Will: thAtS kInkY~""",
    """Nick: I haven’t seen Zimo in like a week, do you guys know where he is?
Garv: nope
Will: Nope, but I think I know how to find him 
Will:DOES ANYONE WANT TO TALK ABOUT THE OSCARS AND THE FLAWS IN THE HOMOSEXUAL AGENDA WITH ME???
Zimo: I do. 
Nick and Garv: *falls over in panic* where the fuck did you come from?
Zimo: I have been summoned""",
    """Will: If I were a drink I’d be a cherry vanilla coke. If you were a drink what would you be?
Zimo: bleach
Nick: sewage 
Will: Alright calm down edgelords""",
    """Nick: How do you politely tell someone you want to hit them with a brick?
Zimo: One wishes to acquaint your facial features with a fundamental item used in building walls. Repeatedly.
Nick: That’s fucking poetic. 
Garv: That was a cry for therapy from both of you"""
]
home = GoogleAssistant(host="192.168.0.102")
# home.volume(1)
home.say(text=random.choice(bhrQuotes), lang='en_Au')
