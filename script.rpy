# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define adam = Character("Adam")
define johanna = Character("Johanna")
define matilde = Character("Matilde")
define artur = Character("Artur")
define male_student_a = Character("Male Student")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene adam_room

    "*beep beep* *beep beep*"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show adam_placeholder at left with dissolve

    adam "*yawn* *groan* Hmm?"

    "I look at the clock next to me. The time reads 07:35."

    adam "Mmh. I've still got time…"

    "…I overslept."

    adam "7:35!?"

    "I jump out of bed, frantically looking for my clothes."
    "Shirt? Check. Socks? On. Pants?"
    "Wait… I forgot them in the dryer!"
    "I rush to it and take a pair of my half wet jeans out."
    "Beats running out pantsless."
    "I can't be bothered to wash them whenever I need them, so I usually just wash everything in one go as soon as I run out."
    "No time to straighten my hair."
    "I put on my sunglasses, lock the door and rush to my car."

    hide adam_placeholder at left with dissolve
    scene street with dissolve
    show adam_placeholder at left with dissolve

    adam "Shit. It's cloudy."

    hide adam_placeholder with dissolve
    "Driving's gonna be a pain in the ass again."
    "I don't wanna go in the first place, but it'd look bad to be missing on my first day of college, and being late already probably won't make me any more popular with the profs either."

    scene campus_front
    "It's 8 on the dot now."
    "I'm like 20 minutes late."

    scene campus_hall_A
    "Hopefully the traffic excuse is good enough."

    scene classroom_A
    "I run into the classroom."
    "At this point I can't even tell if I'm actually exhausted or just faking it."

    show johanna_placeholder at right with moveinright
    johanna "Looks like Mr. Garcia finally decided to join us!"

    show adam_placeholder at left
    adam "Guess I'm late for attendance, huh?"

    johanna "You could say that. Don’t worry, someone will fill you in later, just siddown for now."
    hide johanna_placeholder
    hide adam_placeholder

    "I sat down at the first free seat I could see."
    "There's a girl next to me and a bag at my feet."
    show matilde_placeholder at right with dissolve
    "It’s probably hers."
    "I’ll just push it to the side."
    "Kinda pale, looks nervous."
    "Must be a freshman too."
    "Guess she'll need to fill me in, then."
    "She looks like she wants to say something to me but is too scared to speak up."
    "I try to keep my voice down so as to not interrupt the pres."

    show adam_placeholder
    adam "Hey, sorry if I’m bothering you but could you ju-"
    hide matilde_placeholder
    hide adam_placeholder

    "And before I could get in another word the door opens again."

    show artur_placeholder at right with moveinright
    artur "Sorry for taking so long, kinda got lost on the way back from the toilet and man is it s-"

    show johanna_placeholder at left
    johanna "Happens to the best of us, right? Now go take a seat."

    artur "Oh yeah, sure thing. Didn't mean to interrupt."

    hide johanna_placeholder

    "The guy who just walked in looks like he could probably lift me with just one hand if he felt like it, and of course he's walking right towards me."

    artur "Hey uh, I don't mean to be rude but, you happen to be sitting at my seat."

    show adam_placeholder

    adam "I didn't see a sign anywhere. Do you want me to move or?"

    artur "No no it’s fine really, but uh, could you pass me my bag at least? It's the one next to you."

    adam "Of course. My bad, I thought it was hers."

    "I look back at the girl who's gotten so red you'd think she has a fever and is giving me a look like she's trying to hide her face."
    "All I can think to reply is to give a forced smirk back."

    artur "Thanks."

    "He barely moves the bag then just sits down next to me."
    "Why did he even need me to move the bag to begin with?"

    artur "Haven't seen you around before. You new or just a skipper?"

    adam "Last I checked I wasn't a butterfly so I'd say I'm just new."

    artur "Alright, wise guy. If you want I can show you around after this whole thing is done here. Name's artur by the way. Nice to meetcha. And cool shades."

    adam "adam. And thanks, I guess."

    artur "Did matilde fill you in already or-?"

    "Before I could ask whether he meant the girl next to me or not an alarm that sounds like a phone ringtone goes off."
    hide adam_placeholder
    hide artur_placeholder

    show johanna_placeholder at right
    johanna "Well guys, I know how boring and annoying introductions like these can be and I’m pretty sure I got all the important bits across already, so the introductions are over. The student council will stick around the halls for a little longer in case any of you need help getting around until the show starts. Have a nice day and I hope to see you all there!"

    "As she walks out the door I come to a realization. I didn't hear a single word she said."
    "With a look of clear confusion on my face I turn to the girl and before I even have to say anything she answers."

    show matilde_placeholder at left
    matilde "W-well aside from the basics the student council is looking for new members and they're holding a welcome c-concert for the new students in one of the big halls. The auditorium I think."

    show adam_placeholder at center
    adam "She managed to fill 90 minutes just for that?"

    matilde "W-well there's al-"

    "She looks flustered. I guess once artur and I got talking she stopped paying attention too."

    adam "It's fine, thanks. I mean it."

    "I try to show her a reassuring smile but considering her reaction I’m starting to worry it came off as creepy more than anything."
    hide matilde_placeholder
    hide johanna_placeholder
    hide adam_placeholder

    "A welcoming concert, huh? Well, I actually happen to be quite fond of music and I've got nothing better to do so sure, I’ll bite."
    "Only problem is, I have no idea where that 'big hall' is. Maybe I should ask someone for directions."
    "Besides, making some acquaintances along the way can't hurt."

    menu:
        "Ask the Student Council President to accompany you. If anyone knows where it is, it's her.":
            jump choice_a
        "Ask matilde to accompany you. Maybe you can help ease her nerves along the way.":
            jump choice_b
        "Ask artur to accompany you. It would be rude to turn down his offer.":
            jump choice_c

    label choice_a:

        scene campus_hallway_A
        "I walk out the door and look around for a bit but I can't see her anywhere."

        johanna "Are you looking for someone?"

        show johanna_placeholder at right with moveinright
        "Way to give me a heart attack."

        show adam_placeholder at left
        adam "Yeesh, at least make yourself known before sneaking up on someone."

        johanna "Well you seemed like you were looking for someone so I thought I’d help out the new blood."

        adam "Right… Anyway, I was actually looking for you."

        johanna "Good thing I found you first then, huh? What do you need?"

        adam "Well, I wanted to ask you if you would be willing to show me the way to the concert hall."

        johanna "I did say it was in the auditorium, didn't I?"

        adam "Yeah yeah, sure. I just seem to have missed the part where you told us how to get there."

        "Call me crazy, but for a moment I swear I thought I saw her getting nervous."
        "Then immediately she looks as if overcome by even more confidence than before."

        johanna "Having a rough day today Garcia? I’m going to the auditorium myself, so just follow me."

        hide adam_placeholder
        hide johanna_placeholder
        scene campus_hall_A

        "I guess I’ll just walk somewhat behind her."
        "Might be a good call to make some small talk."
        "Too bad it takes me what feels like an eternity to say something."

        show adam_placeholder at left
        adam "You know, we’ve been walking for a while and I don't think I caught your name yet."

        show johanna_placeholder
        johanna "Johanna. Johanna Medina. But please, just call me johanna. And your name was adam, right?"

        "Way to remind me I was late for attendance."

        adam "This campus sure is big. Is the auditorium really that far away?"

        johanna "Why the sudden questions? Don't you trust me? I know exactly where it is!"

        "What’s with the attitude all of a sudden?"
        "Better to play along if she gets this heated."

        adam "Alright alright, I trust you. No need to raise your voice. Sorry for doubting you."

        johanna "But this reminds me. What are the glasses for? Fashion statement?"

        adam "Oh you know. I just don't like the sun in my eyes."

        johanna "It's cloudy and you had them indoors as well."

        "Note for next time, get better excuses."

        adam "I just have sensitive eyes, no need for an interrogation."

        johanna "So you're insecure about your face. You’re a pretty weird guy."

        "I guess I did make it kind of obvious."
        "And what does she mean 'noted'?"
        "How much longer is she gonna make me walk?"
        "I’d better change the subject."

        adam "So, concert. Are we there soon, or?"

        johanna "We’ll be there when we’re there, patience is a virtue!"

        "If I wasn't sure we were lost already I'm definitely sure of it now."

        adam "Say, johanna, what kind of music are they gonna be playing there? Something you like?"

        "Convo about music here. johanna replies with her favorite genre then asks adam for his. He goes 'I'm fine with anything.' She asks for a specific band. He goes 'I like some of their stuff.' She mentions one song and he talks about how he likes it or dislikes it."

        "At this point I've lost track of how long we've been walking but these streets are starting to look familiar."

        johanna "Aha! There we are! I told you I knew the way!"

        "At this point I’m too tired from walking so much to point out that I saw the massive sign saying 'Building B12: West Campus Auditorium'."
        "I'm also too tired to get upset for making us walk so much even though it was right across from the building we started at."

        adam "Well, it took longer than I expected, but you did take me there, so thanks."

        johanna "Hahaha. Of course, don't mention it! I told you you can trust me! I’ve gotta get back to council duties now so please excuse me. I'll see you around."

        adam "Yeah same. Thanks again."

        hide adam_placeholder
        hide johanna_placeholder
        "As annoying as that walk was, at least talking to her was fun."
        "Now for what I actually came here for."

        scene auditorium
        return

    label choice_b:

        "After some thinking I look back at the girl."

        show adam_placeholder at left
        adam "Say, are you interested in checking it out?"

        show matilde_placeholder at right
        matilde "H-huh?"

        "It’s like she's actively avoiding my eyes."
        "Either she's really awkward about that sort of thing or I'm uglier than I thought."

        adam "The concert, I mean."

        matilde "Oh uh, a little."

        adam "If you'd like we can go check it out together."

        "She's getting red again, it’s kind of cute."

        matilde "Uhm, okay."

        adam "Great. The name’s adam, by the way. What's yours?"

        matilde "M-Matilde…"

        "At this point her looking at my face then away might as well be routine."

        adam "You know where it is, right?"

        matilde "I-I think so."

        adam "Alright, in that case I'm in your hands."

        "Okay now I'm just teasing her. It's cute how easily she gets embarrassed."

        matilde "So it should be that way. I think. No, maybe it was that way? No wait! Was it this way?"

        scene campus_hallway_A

        "Of course the moment we step outside she's as aimless as me. Figures."

        adam "Hey, no rush. I'm sure we'll find a way if we keep looking. How big can this campus be?"

        "She doesn't even answer, probably to avoid looking at me."
        "As we're walking she keeps moving her head in all directions, constantly looking like she's unsure where to go but never answering my questions."
        "She's also starting to get fidgety, is something wrong?"

        adam "Is everything okay? You’re shaking."

        "Finally she looks at me again."

        matilde "I-I need to go make an urgent call! C-can you please wait here for a moment?"
        hide matilde_placeholder with moveoutright

        "And now she's run off behind that building to my right."
        "I guess she really doesn't want me to hear her call."
        "That's probably the most active I've ever seen."
        "Whatever it was, it must've been damn important."

        adam "Wonder what it was. Hope she’s okay."
        hide adam_placeholder

        "Really wish I hadn’t left my phone and watch at home."
        "She’s been gone for a while now."
        "8 minutes at least if I had to guess."
        "I guess I’ll go check up on her."

        show matilde_placeholder at right with moveinright
        matilde "Huff huff S-sorry for the wait!"

        "Or I guess not."

        show adam_placeholder at left
        adam "You didn’t have to run on your way back, you know."

        matilde "Sorry, I didn’t want to keep you waiting."

        "I dunno if it's just because of her little sprint or what, but she seems a lot calmer now."
        "Maybe the phone call eased her up."
        "Still no eye contact though."
        "Where’s that weird smell coming from?"

        adam "Okay you’ve been trying to avoid my eyes for a while now, is there something on my face?"

        matilde "Aah! N-no, sorry! P-please, it’s nothing…"

        adam "Alright, alright. I’ll drop the subject. Anyway, what direction did we need to go in, again?"

        matilde "Ah! Yes, uh, I think it’s uhm, this way?"

        "Nevermind I guess that call only eased her up so much."
        "Probably too rude to ask about it and I don’t wanna stress her out again."
        "I didn’t intend to babysit anybody today in the first place."
        "Maybe some small talk will ease this situation."

        adam "Say, do you know what kind of music they’ll be playing?"

        matilde "No. I missed that part too…"

        adam "It’s fine. Whilst we’re on that subject, any music you like?"

        "She’s lighting up."
        "Guess she does."

        "Convo about music here. Matilde replies with her favorite genre then obsessively starts talking about her favorite songs and bands, barely giving adam any time to nod in, him being totally unable to keep up with her."
        "She also drops any and all stutters during this conversation."
        "Every now and then she goes 'wait, it’s this way! No wait, was it that way?' before continuing."

        "It’s been like half an hour and she’s still going."
        "Starting to regret ever asking."
        scene campus_hall_A
        "Eventually we’re back on the hall we started."

        adam "Hey matilde, I really don’t mean to be rude but you made us go in circles."

        matilde "Huh? Oh no! I messed up again…"

        adam "No, it’s fine. Look."

        "I point to a sign reading 'Building B12: West Campus Auditorium'."

        adam "See, we found the right way in the end."

        matilde "Oh! So it was right there from the start? I’m sorry…"

        adam "P-Please don’t worry about it. Haha."

        "I’m forcing a smile as best as I can."
        "If she starts crying I’m going to leave."

        adam "Actually, wait? What time is it?"

        matilde "Uhm it’s…"

        "She pulls out her phone."

        matilde "Oh no, I’m late again! I’m sorry but I have to go!"
        hide matilde_placeholder with moveoutright
        hide adam_placeholder

        "At least answer my question before you run off, will you?"
        "Well, hopefully there’s a clock inside."
        "Now for what I actually came here for."
        scene auditorium
        
        return

    label choice_c:

        "I walk over to Artur."
        "He's fiddling with his phone."

        show adam_placeholder at left
        adam "Hey."

        show artur_placeholder at right
        artur "Yo Shades, ‘sup?"

        adam "Felt like taking you up on your offer."

        artur "Wait seriously? I thought you'd just walk out and head home."

        "Well now I'm considering it."

        adam "Dunno. Felt like checking out the welcoming concert the pres was talking about."

        artur "They're holding a concert?"

        "At least I wasn't the only one who wasn't paying attention."

        adam "The girl next to me said it was in the auditorium. No clue where that is though, and since you offered to show me around I thought you could show me the way."

        artur "Sure, I got like an hour and a half to kill anyway."

        adam "What?"
        hide artur_placeholder with moveoutright
        hide adam_placeholder

        "And he's already out the door."
        "How much energy can a guy have this early in the day?"

        scene campus_hallway_A

        show artur_placeholder at right with moveinright
        show adam_placeholder at left with moveinleft
        adam "So, where even is that auditorium?"

        artur "Beats me."

        adam "Sorry?"

        artur "Yeah I've got no idea."

        "Oh for the love of-"

        adam "If you don't even know then why would you offer to show me around?"

        artur "I said I'd show you around, and I meant it. I just don't know where anything is."

        "He flashes me the kind of smile a kid entering a candy store would make."
        "I can't tell if he's an idiot or if I’m one for trusting him."

        artur "Come on, it's not that bad. Let's just ask others for help."

        adam "No, I really don't think we should bo-"

        "And with that he's off and I'm committed to coming along lest I look like an asshole."
        "The person he’s talking to is clearly trying to tell him something with his head."
        "Must be because his hands are full of books."
        "There’s this thing called a backpack, genius. Look into it."
        "Oh, looks like they’re done."

        artur "Guy says it’s just down the road. See, that wasn’t so bad was it? Hahah."

        "I feel like I lost a piece of my pride just now."

        adam "Let’s just go already."

        "We walk for a bit, then artur starts talking again."

        artur "Hey, mind if I ask you somethin’?"

        adam "Depends on the question."

        artur "Wait really? I thought you were gonna blow me off. Crap, I didn’t think you’d actually be okay with it."

        "Last I checked I didn’t say yes."

        artur "So what’s the deal with the shades?"

        "Almost forgot I was wearing them."

        adam "Why do you ask?"

        artur "Just curious. It’s not every day you run into a guy wearing shades indoors on a cloudy day with dimmed lights. How can you even see in front of you?"

        "You get used to it."

        adam "I’ve got sensitive eyes. Doctor’s orders."

        "Blatant lie."

        artur "What, like the guy from X-Men?"

        "But he seems to have bought it."

        adam "I don’t think that’s why he wears them."

        artur "Oh well, if you don’t wanna tell me that’s fine. I won’t force you."

        "Or maybe not."
        "I need to work on my excuses."
        "Gotta change the subject."

        adam "You said the guy said it was ‘down the street’, no? How come we’ve been walking for like 20 minutes?"

        artur "We have? Ha Ha! I didn’t even notice!"

        "Too bad I can’t see what’s so funny about that."

        artur "It’s fine, I’ll just ask someone to help us out. Plenty of people around."

        adam "No!"

        "Shit."
        "Didn’t mean to raise my voice."
        "He looks startled."

        adam "Sorry, I just-. Do you mind if I do the talking this time?"

        artur "Uh, sure? Go ahead, dude."

        scene campus_hall_A

        "I steel myself for the most shameful thing I’ll do all day and walk up to a student on a bench."

        adam "Hey, sorry, I don’t mean to bother but I’m a bit lost and was wondering if you could help me out. Do you know where to get to the Auditorium with the concert in it today?"

        male_student_a "Oh yeah, sure thing. You just gotta go straight down that road. It’s right across class room building B11. There’s a big sign and everything, can’t miss it."

        "You’ve gotta be kidding me."
        "Trying my damndest here to not explode."

        artur "What’d he say?"

        adam "Artur are you absolutely sure this is the right direction?"

        artur "Well, it’s where the guy was looking when I asked him, so I think so."

        adam "Can you do me a favor and get your eyes checked sometime?"

        artur "What do you mean?"

        adam "The auditorium was right across from where we started!"

        "Deep breaths, adam. You can’t be too mad at idiots."

        artur "I guess that’s what he was looking at. Well, don’t blame me for him just saying ‘oh it’s right there’. I’m no psychic."

        adam "Whatever, I’m going."

        artur "Wait, hold on. Look, as an apology I’ll accompany you over and keep you company. It’s my fault we came all this way to begin with."

        "Better to keep him around me than having him do god knows what on his own I guess."

        adam "Fine."

        artur "Alright, that’s more like it!"

        "I’m pissed, sure, but I’m not unforgiving."
        "Besides, I could use the company anyway."

        artur "So how come you’re interested in that concert? Big music guy or somethin’?"

        adam "Something like that."

        "Convo about music here. Artur and adam casually chat and gradually realize they’ve got a similar 'I’ll try everything attitude' except artur isn't ashamed to talk about liking 'girly pop music' (it’s 2008, you get what I mean). During this adam gradually warms up to him."

        artur "Well, I guess we’re back now. Sorry for making you walk so much. I’ll make it up to you sometime."

        adam "It’s fine. Just glad I got there in the end."

        artur "Alright. Take care dude."

        adam "What, you not comin’ in?"

        artur "Nah. Got stuff to do. I’ll see you around."
        hide artur_placeholder with moveoutright
        hide adam_placeholder

        "And with that he’s off."
        "What a weird guy."
        "Now for what I actually came here for."

        scene auditorium
        return

    return
