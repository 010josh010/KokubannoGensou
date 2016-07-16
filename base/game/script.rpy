#images
image School_hallway= "School_Hallway.png"
image School = "School.png"
image Akiko_normal = "Akiko_normal.png"
image Tsumi="Tsumi.png"
image Tsumi_eyes_closed="Tsumi_eyes_closed.png"
image Tsumi_plain="Tsumi_plain.png"
image Tsumi_dark="Tsumi_dark.png"
image Tsumi_dark_smile="Tsumi_dark_smile.png"
image Tsumi_plain_ec="Tsumi_plain_ec.png"
image Tsumi_plain_mo="Tsumi_plain_mo.png"
image Tsumi_explanation="Tsumi_explanation.png"
image Tsumi_mouth_open="Tsumi_mouth_open.png"
image Maria_normal="Maria_normal.png"
image Maria_grin="Maria_grin.png"
image Maria_confused="Maria_confused.png"
image Maria_hey="Maria_hey.png"
image Maria_smile="Maria_smile.png"
image Maria_smile_eyes_closed="Maria_smile_eyes_closed.png"
image Maria_kyaa="Maria_kyaa.png"
image Maria_eeh="Maria_eeh.png"
image Maria_troubled_open="Maria_troubled_open.png"
image Maria_smile_notice="Maria_smile_notice.png"
image Maria_embarrassed="Maria_embarrassed.png"
image Maria_shikatanai="Maria_shikatanai.png"
image Maria_indifferent="Maria_indifferent.png"
image Classroom="Classroom.jpg"
image Classroom_afternoon="Classroom_afternoon.jpg"
image Library="Library.png"
image Locker="School_Locker.png"
image Pool="Pool.png"
image Bedroom="Bedroom.png"
image Schoolgrounds="School_Grounds.png"
image School_Courtyard = "School_Courtyard.jpg"
image Bathroom = "bathroom.jpg"

# Characters
define m = Character('Maria', color="#1F7A7A")
define t = Character('Tsumi', color="#FFFFC2")
define a = Character('Akiko', color = "#FF0000")
define y= Character('You')
define q= Character("???")


#Items
init python:
    notebook = {'Name': 'notebook', 'Value': None}
    letter = {'Name': 'letter', 'Value': None}


#Modules
init python:
   def chance_50(event, item, place):
    number = renpy.random.randint(1,2)
    if number ==1:
        event(item, place)
    elif number ==2:
        item['Value'] = False
        pass

init python:
    def chance_10(event, item, place):
        number = renpy.random.randint(1,10)
        if number ==7:
            event(item, place)
        else:
            item['Value'] =False
            pass
init python:
    
    def itemFind(item, place):
        narrator("You found a %s in the %s"%(item['Name'], place), interact=True)
        item['Value'] = True

# Game Start
label start:
    scene School 
    play music "Happy.mp3" fadein 5.0
    
    "Its your first day at a new school, and you arrive early."
    scene School_hallway
    "You walk up to the second floor and find a long stretching hallway leading to your class"
    "You take notice of the lush school grounds outside the hallway windows until you are approached by a distinguished looking girl in frilly clothing."
    show Tsumi with easeinright
    t   "Welcome to Otsuka High, My name is Tsumi Morigawa. I am the Student Council Vice President."
    t   " I will be showing you around on your first day."
    t   "I'm sure you will find our facilities here top notch. As Vice President of the student body , I can assure you that everyone here takes great pride in the appearance of our most wonderful school."
    t   "So welcome yourself, Mr. transfer student, and feel honored to be here"
    hide Tsumi
    show Tsumi_mouth_open
    t   "*Ahem*"
    t   "Well, we'd better get going, Do you have any questions for me before we begin our tour?"
    hide Tsumi_mouth_open
    show Tsumi
    menu:
        "Whats in that book you're holding, it looks old?":
            jump whatsthatbook
        "Yeah, where's the bathroom , i've gotta take a leak like....bad!":
            jump wheresthebathroom
        "Nope, no questions here":
            jump scene2

    label whatsthatbook:
        
            t   "Oh this......a friend let me borrow it before they..... "
            y   "........."
            hide Tsumi
            show Tsumi_dark_smile
            t   "I suppose you could say that it is something really important to me...."
            y   "its ok, I was just curious because of the weird writing on the front"
            t   "right........weird huh..."
            jump scene2

    label wheresthebathroom:
            hide Tsumi
            show Tsumi_mouth_open
            t "Its down the hall and to the right, after you pass the nurse's office "
            t "hurry up though, we do not have all day."

            hide Tsumi_mouth_open
            scene Bathroom with fade
            
            "You hurry into a stall to relive yourself"
            python:
                chance_50(itemFind, notebook, "stall")
            
            scene School_hallway with fade
            jump scene2

    label scene2:
        hide Tsumi_dark_smile
        hide Tsumi_mouth_open
        show Tsumi
        t   "Well if there won't be any more questions...Lets start our tour by showing you to our homeroom."
        
        t   "Follow me, I will the way."
        hide Tsumi
        "You follow Tsumi to class." 
      
        scene Classroom

        play music "Lounge.mp3" fadein 7.0
        "You enter an empty classroom. "
        y       "hmmm... where's the rest of our class, shouldn't there be at least one other person here by now?"
        show Tsumi_dark
        t       ".........."
        hide Tsumi_dark
        show Tsumi_explanation
        t       "There is a memorial this morning for one of our former classmates. Most of the class is there in observance."
        t       "It will be just you and I for the time being."
    menu:
            "A memorial..... What happened?":
                jump whathappened
            "Don't say anything":
                jump dontsayanything

    label whathappened:
            t   "........ I can't say."
            t  "no one really knows....."
            y  "sounds like something terrible happened to them"
            t   "....its... well...... "
            t   "its difficult to explain, so don't go asking anyone about it ok?"
            y   "ok ok.... got it"
            jump scene3
    label dontsayanything:
            jump scene3
    label scene3:
        hide Tsumi_explanation
        show Tsumi_plain_mo
        t       "For now, Let's go get you a locker and show you around the rest of the campus."    
        hide Tsumi_plain_mo
        "You follow Tsumi around to see the rest of the school."
        scene Schoolgrounds with fade
        "You are struck by the natural beauty of the school grounds."
        y  "wow you weren't kidding about this school, its really amazing"
        t   "What did you think, i was lying to you.... now keep up, theres a little more ground to cover before class begins"
        
        "*Suddenly you feel a tug on your right sleeve*"
        
        show Maria_normal with easeinright
        q       "Nice to meet you! You must be the new student."
        m       "My name is Maria." 
        "*Maria hands you a letter*"
    menu:
        "Take the letter":
            jump taketheletter
        "Don't take the letter":
            jump donttaketheletter
        "Start doing the robot":
            jump robot
    

    label taketheletter:
        python:
            letter['Value'] = True
        y       "What's this for?"
        jump scene4_1

    label donttaketheletter:
        python:
            letter['Value'] = False
        m       "...... I see."
        jump scene4_2
    label robot:
        python:
            letter['Value'] = None
        "*You start doing the robot*"
        jump scene4_3
        
    label scene4_1:
        hide Maria_normal
        show Maria_smile
        m       "Don't open it until you're all alone okay?"
        "*you scratch your head and are puzzled*"
        hide Maria_smile
        show Maria_grin
        m       "Its a secret okay?"
        y       "a secret..........."
        hide Maria_grin
        show Maria_smile_eyes_closed
        m       "Thats right....and if you show anybody else....I will kill you..."
        y       "Okay okay.......I got it." 
        hide Maria_smile_eyes_closed
        show Maria_smile_notice
        m       "Good....... I'll be waiting...hehehe."
        hide Maria_smile_notice
        show Maria_normal
        m       "Bye Bye"
        hide Maria_normal 
        "*Maria walks away*"
        "*she seems to be humming a tune that sounds strangely familiar as she fades into the distance*"
        "*you put the note in your pocket*"
        jump scene5
        
    label scene4_2:
        hide Maria_normal
        show Maria_hey
        m       "You know what.......... I think I like you."
        y       "huh..........?"
        hide Maria_hey
        show Maria_kyaa
        m       "I said I like you silly."
        y       "But we just met.... I'm sorry but I don't understand."
        hide Maria_kyaa
        show Maria_shikatanai
        m       "Look... when a girl tells you her feelings....nevermind......."
        hide Maria_shikatanai
        show Maria_troubled_open
        m       "The least you could do is acknowledge me."
        y       "I'm sorry...this is just so sudden. I mean......."
        y       "thanks....."
        hide Maria_troubled_open 
        show Maria_embarrassed
        m       "Well you'd better not forget it.....okay?"
        hide Maria_embarrassed
        show Maria_grin
        y       "uh....okay......I won't."
        m       "Lets talk sometime during lunch okay?"
        y       "ok..."
        m       "meet me on the rooftop, i'll be waiting"
        m       "Well....see you around. Hehehehe."
        y       "........."
        m       "Bye Bye"
        hide Maria_grin
        "*Maria walks away*"
        "*she seems to be humming a tune that sounds strangely familiar as she fades into the distance*"     
     
        jump scene5
        
    label scene4_3:
        hide Maria_normal
        show Maria_confused
        m       "............"
        hide Maria_confused
        show Maria_eeh
        m       "You're weird.........."
        hide Maria_eeh
        show Maria_smile_eyes_closed at right
        show Tsumi_mouth_open at left with easeinleft
        t       "Ahem.."
        t       "That was quite a show you put on there, have you thought of trying out for our school's interpretive dance club?"
        hide Tsumi_mouth_open
        show Tsumi_eyes_closed at left
        hide Maria_smile_eyes_closed
        show Maria_shikatanai at right
        m       "As if....this guy dances like a total creep "
        hide Tsumi_eyes_closed
        show Tsumi at left
        t       "Well, we had better get to class, the bell is going to ring soon and all the other students should be returning right about now."
        hide Maria_shikatanai
        show Maria_indifferent at right
        t       "Excuse us......We had better get going."
        hide Tsumi
        "*Tsumi walks away*"
        hide Maria_indifferent
        show Maria_hey
        m       "Hey...... meet me on the rooftop during lunch break....ok?"
        y       ".......uh........okay."
        hide Maria_hey
        show Maria_grin
        m       "Hehehehe...."
        m       "Bye Bye.."
        hide Maria_grin
        "*Maria walks away*"
        "*she seems to be humming a tune that sounds strangely familiar as she fades into the distance*"
        jump scene5
        
    label scene5:
        stop music fadeout 2.0
        play music "schoolbell.mp3" noloop 
        "*The school bell starts to ring*"

    menu:
        "Go to class":
            jump gotoclass
        
        "Go to the library":
            jump gotolibrary
    
        "See whats in the courtyard":
            jump gotocourtyard

    label gotoclass:
        "*You hurry to the classroom*"
        jump scene5_1
        
    label gotolibrary:
        "*You decide to go to the library"
        jump scene5_2

    label gotocourtyard:
        "*You decide to see whats in the courtyard"
    
    label scene5_1:
        scene Classroom
        play music "Lounge.mp3" fadein 7.0
        "You take your seat in the classroom"
        "The rest of the class has arrived and they are all talking amongst themselves."
        show Tsumi_plain_mo with easeinleft
        t "Oh good, you made it... i was beginning to worry about you."
        t "What did that kouhai want with you anyway?"
        if letter['Value'] == True:
            y "She handed me a note, I haven't opened it yet"
            t "I'm curious as to what the kouhai has written, I think you should open it."
            menu:
                "Open it":
                    jump openLetter
                "Open it later":
                    jump openLater
        elif letter['Value'] == False:
            y"She wanted to give me a letter, but i didn't take it"
            t "Why not? "
            y "I don't know, it just didn't feel right"
            t "Completely understandable, kouhai should know thier place!"
            y " i guess......"
            jump scene6
        elif letter['Value'] == None:
            y" She wanted to give me a letter, I didn't know what to do so I just started dancing"
            t "You are an odd one, but glad to have you at our school."
            y "thanks..... i guess"
            jump scene6


    label openLetter:
        y "ok.... here goes"
        "You open the letter"
        t "Well.. what does it say?"
        "The letter reads: Dear transfer student, you are in danger! I can't explain everything now, but meet me on the rooftop during lunch. Make sure you are alone."
        t "Hahahaha, its a prank, the kouhais try to prank every new transfer student that comes here"
        t "don't do what the letter says, you should ignore it"
        y  "but it sounds serious"
        t "you will regret it, trust me"
        

    label openLater:
        y "no....i'd better not. She told me to wait until I was all alone."
        y "She said it contained a secret."
        t "oh well, the importance of that will be determined in your isolation."
        t "best to keep secrets away from prying eyes."
        y "yeah, i agree."
        jump scene6

        
    label scene5_2:
        scene Library
        play music "Mysterious.mp3" fadein 7.0
        "The library appears to be vaccant, but there is an  errie prescence in the room."
        "There appears to be a book pulled out fr"
        "You go to see"
        show Akiko_normal with easeinleft
        "A mysterious girl appears"
        q "Hi , you must be the new student everyone is talking about"
        y "Everyone is talking about me?"
        q "Well sure, we haven't gotten a transfer student since....."
        a "Well where are my manners, my name is Akiko Teruya"
        "The library door opens"
        a "I'd better go.... see you around."
        y "hey wai...."
        hide Akiko_normal
        t "Why there you are"
        show Tsumi_eyes_closed
        t "tardiness is not acceptable on your first day mr. transfer student"
        y "sorry, i was just looking around and this girl showed up so..."
        t "Well theres no one in here now, what was her name, Ill be sure to report her to the faculty as well"
        y "it was aki...something.....oh... akiko... teruya.... yeah that was it"
        t "surely you are mistaken, a girl with that name does not exist at this school. I have a roster of every class for the year in my schoolbag and  never once did I see a name like that."
        y "hmmmmm I'm certain of it"
        t "nevermind, i'm sure you don't want to get her in trouble too. I get it."
        y "but..."
        t "i'll let you slide this time since i was giving you a tour, but next time you are late, you will have to answer to sensei."
        t "lets go.... we've already missed the inroductory lecture."
        hide Tsumi_eyes_closed
        "You hurry with tsumi to class"
        jump scene6


    label scene5_3:
        scene School_Courtyard
        play music "Errie.mp3" fadein 5.0
        "You take a moment to look around the courtyard. The weather is sunny and you enjoy the nice cool breeze that is blowing in your direction."
        "You hear a rustling noise behind you"
        jump scene6

#class start
    label scene6:
        "WIP"
        return

        
        





    
    
  
        
        

        


        
    
    

            
        
        

                
        

        
            
            
        

        
        
    

        

        




