# #23 HackHeads
#make loops so people learn
#if time do try catch block for responses
print("Go through your day, and see your daily choices impact on the environment");
choice = input("Do you want to start: yes or no?")
print();

#morning coffee
while (choice == "yes"):
    print("Good morning! You wake up at 7 AM to get ready for class. Hitting the")
    print("snooze button for the fifth time since 6:30," + " you decide")
    print("you could use a cup of coffee. Do you…");
    print("a. Go to Starbucks?");
    print("b. Go to the dining hall");
    print("c. Make your own");
    response = input("What is your choice?");
    if (response == "a." or response == "a"):
        print("You go to starbucks. You order an Iced Caffe Mocha to really")
        print("kickstart your day. You’re handed your cup and a straw. Do you…");
        print("a. accept the straw");
        print("b. Whip out your fancy metal straw?");
        response1 = input("What is your choice?");
        if (response1 == "a." or "a"):
            print("Congrats! You killed a turtle! (What are the odds right?")
            print("According to The Sea Turtle Conservancy, 100 million marine")
            print("animals die every year from ingesting debris. What’s more,")
            print("over half of the world’s sea turtles have ingested plastic!");
        elif (response1 == "b." or response1 == "b"):
            print("Congrats! It may not seem like much, but using a metal straw is")
            print("a small step towards living a more sustainable life!");
    elif (response == "b." or response == "b"):
        print("You go to the dining hall. After happily wasting a swipe to get in,")
        print("you head towards the coffee. Do you…");
        print("a. Use a styrofoam cup");
        print("b. Use a reusable cup/mug");
        response2 = input("What is your choice?");
        if (response2 == "a." or response == "a"):
            print("Wow! Here’s a fact to make you rethink your life choices:")
            print("According to the National Bureau of Standards Center for")
            print("Fire Research, 57 chemical byproducts are released during the")
            print("creation of styrofoam, which pollutes the air. These chemicals")
            print("are shown to have a negative effect on the ozone layer.");
        elif (response2 == "b."):
            print("Phew! Good for you! Even better if you brought your own mug too!")
            print("Protip: If you’d like to bring your own mug, but you don’t have")
            print("one, or need one for cheap, consignment shops are a great place")
            print("to find used items for cheap, and is also better for the environment")
            print("as you reuse old products instead of letting them be tossed!");
    elif (response == "c." or response == "c"):
        print("You make your own coffee. Do you use…");
        print("a. A coffee filter?");
        print("b. Or a k-cup?");
        response3 = input("What is your choice?");
        if (response3 == "a." or response3 == "a"):
            print("Using a filter can sometimes be problematic, especially if")
            print("they are bleached with oxygen or chlorine; this, again, deals with")
            print("the problem of releasing unwanted chemicals into the atmosphere.")
            print("If you absolutely want to keep using a coffee filter,")
            print("you can always invest in a reusable one!");
        elif (response3 == "b." or response3 == "b"):
            print("Yikes. I get it; fast, easy coffee is great.")
            print("K-cups, on the other hand, are not! K-cups, that aren’t recycled,")
            print("will take thousands of years to decompose in a landfill.")
            print("Thousands of years? You won’t be here by then,")
            print("but your great-great-great-great…etc. Grandchildren will.");
    print()
    print("Do you want to go back and choose another option ")
    print("This is allows you to explore different actions")
    choice = input("yes or no?")
print();

#Way to class
choice2 = True
while (choice2 == True):
    print("Time for class! You were so caught up enjoying your coffee that you")
    print("seem to be running behind! You now have to absolutely book it to class.")
    print("Do you… (For the sake of this program, let’s say your")
    print("college campus is a relatively medium-sized)");
    print("a. Drive?");
    print("b. Take the bus?");
    print("c. Ride your bike?");
    print("d. Walk?");
    response4 = input("What is your choice?");
    if (response4 == "a." or response4 == "a"):
        print("You drove your car to class!");
        print("Oh boy, that’s a doozy. Look, cars are great. Karl Benz, Henry Ford,")
        print("they are absolute geniuses, I know. However, convenience won’t matter")
        print("when the earth decays. In fact, car pollutants play a big part in global")
        print("warming, and have immediate and long-term effects on the environment.")
        print("If you’re adamant about driving, though, perhaps consider looking at")
        print("an electric car in the future! Until then, carpooling isn’t a horrible idea!");
    if(response4 == "b." or response4 == "b"):
        print("Buses aren’t great for the environment. The pollutants from buses")
        print("play a role in global warming, and have immediate and long-term")
        print("effects on the environment. Nevertheless, it’s better than driving")
        print("your car on your own, in a sense. By taking the bus,")
        print("you are carpooling and, if you’re the only one on the bus,")
        print("that’s at least one less car off the roads.");
    if(response4 == "c." or response4 == "c"):
        print("Look at you! Riding your bike is great. No vehicle emissions,")
        print("and you’re getting your cardio in! Keep this up, and not only")
        print("will Mother Nature be thankful, but your calves will be ripped.");
    if(response4 == "d." or response4 == "d"):
        print("You walked!");
        print("Wow! Kudos to you! Walking is great, since there are no")
        print("vehicle emissions involved and you’re getting your steps in! Go you!");
    print();
    print("Do you want to redo this part?")
    choiceTwo = input("yes or no?")
    if (choiceTwo == "no"):
        choice2 = False
print()  #where I am 
    

#after class activity
choice3 = True
while( choice3 == True):
    print("Classes are over for the day, and you’re feeling a bit tired.")
    print("You decide it’s time for a break before you get to the studying grind.")
    print("What do you do?");
    print("a. Watch Netflix");
    print("b. Practice a hobby (draw, read, exercise, etc.)");
    print("c. Go to the library and read up on Climate Change");
    response5 = input("What is your choice?");
    if (response5 == "a." or response5 == "a"):
        print("You decide to watch Netflix! What do you want to watch?");
        print("a. Friends");
        print("b. Victorius");
        print("c. The Office");
        response6 = input("What is your choice?");
        if (response6 == "a." or response6 == "a"):
            print("Wow great! Except, here’s the thing, the internet has an affect on our climate,")
            print("so your choice of show doesn’t really matter in the end! According to the")
            print("New Republic website, streaming one hour of Netflix for a week requires more")
            print("electricity for a year than that of the yearly output of two ")
            print("brand-spanking-new refrigerators, which leads to greater carbon emissions.")
            print("Think of that next time you stream.");
        elif (response6 == "b." or response6 == "b"):
            print("Wow great! Except, here’s the thing, the internet has an affect on our climate,")
            print("so your choice of show doesn’t really matter in the end! According to the")
            print("New Republic website, streaming one hour of Netflix for a week requires more")
            print("electricity for a year than that of the yearly output of two ")
            print("brand-spanking-new refrigerators, which leads to greater carbon emissions.")
            print("Think of that next time you stream.");
        elif (response6 == "c." or response6 == "c"):
            print("Wow great! Except, here’s the thing, the internet has an affect on our climate,")
            print("so your choice of show doesn’t really matter in the end! According to the")
            print("New Republic website, streaming one hour of Netflix for a week requires more")
            print("electricity for a year than that of the yearly output of two ")
            print("brand-spanking-new refrigerators, which leads to greater carbon emissions.")
            print("Think of that next time you stream.");
    elif (response5 == "b." or response5 == "b"):
        print("You decide to practice a hobby! Do you...");
        print("a. Draw?");
        print("b. Read?");
        print("c. Exercise");
        print("d. Other?");
        response7 = input("What is your choice?");
        if (response7 == "a." or response7 == "a"):
            print("Great! Drawing is a wonderful hobby and shows you have quite the creativity!")
            print("And, unless you’re scrolling through Pinterest for references all the time,")
            print("you’re impact through electricity on climate change is minimal!")
            print("If you’re looking to really up your sustainability game,")
            print("why not try finding sketchbooks that are made from recycled materials?");
        elif (response7 == "b." or response7 == "b"):
            print("Whether you’re reading fantasy or archived newspapers,")
            print("reading is great for the brain! Worried about sustainability?")
            print("Instead of buying books from the Barnes and Noble,")
            print("why not try a consignment shop or the library? Let’s reuse our resources!");
        elif (response7 == "c." or response7 == "c"):
            print("Yes, get that grind! Not only will you be avoiding any activities")
            print("that are bad for the environment, you are also getting fit!");
        elif (response7 == "d." or response7 == "d"):
            print("There are so many hobbies to pursue, and it doesn’t hurt to");
            print("try something environmentally friendly, or see how you can")
            print("make your hobbies more sustainable! Try recycled products,")
            print("reuse old products, or maybe trying picking up litter as a hobby!");
    elif (response5 == "c." or response5 == "c"):
        print("You decide to read up on climate change at the library!");
        print("Wow! We’re proud of you! Just remember to check your facts")
        print("and make sure you aren’t jumping the gun on ideas that")
        print("seem a little wacky! Keep up the good work!");
    print();
    print("Do you want to redo this part?")
    choiceThree = input("yes or no?")
    if (choiceThree == "no"):
        choice3 = False
print()

#Dinner
choice4 = True
while(choice4 == True):
    print("So after subsequently forgetting to study, and hence procrastinating,")
    print("you decide it’s time to use your second swipe of the day")
    print("and get some dinner. You get...")
    print("a. A nice hearty steak");
    print("b. A good good salad");
    print("c. A healthy, balanced meal comprised of proteins, carbs,")
    print("veggies, and all that jazz.");
    response9 = input("What is your choice?");
    if (response9 == "a." or response9 == "a"):
        print("I don’t blame you. A good steak is hard to turn down!")
        print("Nevertheless, perhaps consider cutting down your steak intake.")
        print("According to PETA, animal agriculture emits more greenhouse gases")
        print("than all the world’s transportation systems combined, not to mention")
        print("it uses an incredibly large amount of resources, as over half of the")
        print("U.S.’s water is used for raising animals. So, if you drove a car")
        print("this morning, at least you’re not emitting as many greenhouse gases")
        print("as a couple of cows! Just remember though, certain meats have a")
        print("bigger impact on the earth than others, so you don’t need to go")
        print("completely vegan or vegetarian in order to make a difference!");
    elif (response9 == "b." or response9 == "b"):
        print("I get it, salads are great, or maybe you’re getting one because")
        print("you feel bad about not working out yesterday. ")
        print("Nevertheless, there is actually a surprising amount of greenhouse")
        print("gases emitted in the production of certain vegetables.")
        print("Surprising? Sounds bad, but don’t completely forego eating veggies")
        print("(I’m looking at you picky eaters). Consider a more balanced approach!");
    elif (response9 == "c." or response9 == "c"):
        print("That’s a great choice! Most things you eat will have an affect on the")
        print("environment, as their production and harvesting will emit many")
        print(" greenhouse gases.By eating balanced foods, you’re making a difference,")
        print("  albeit small.If you really want to step up your game, studying which")
        print(" foods have a smallerimpact on the environment and slowly shaping your")
        print(" diet along thoselines would be a great way to do that! Keep it up!");
    print();
    print("Do you want to redo this part?")
    choiceFour = input("yes or no?")
    if (choiceFour == "no"):
        choice4 = False
print()

#throw away food
choice5 = True
while (choice5 == True):
    print("After eating ypur meal, you...");
    print("a. Throw away the rest of your food.")
    print("b. Make sure you ate every. last. crumb.")
    print("c. Let the dish washers deal with the leftover food")
    response8 = input("What is your choice?");
    if (response8 == "a" or response8 == "a."):
        print("Yikes. Let’s consider what happens to the rest of that food after")
        print("it’s tossed. According to the NRDC, 40 percent of food in America")
        print("isn’t eaten. Also, it’s difficult for 1 of every 8 Americans to put")
        print("food on the table. When you go to eat, plan ahead; focus on portion")
        print("control if you always end up with more than you can handle,")
        print("or work to start a compost system at your college")
    elif (response8 == "b." or response8 == "b"):
        print("This isn’t a bad idea, as long as you are paying attention to")
        print("portions! Food waste is bad, but remember that you and your body")
        print("are important to. No one else is going to focus on your health,")
        print("so make sure to make that a priority.")
    elif (response8 == "c" or response8 == "c."):
        print("First off, I recommend not giving a full plate to the dishwashers")
        print("after dinner. Frankly, it’s a bit rude. Also, the food will typically")
        print("be trashed, leading to more food waste. According to the NRDC,")
        print("40 percent of the food in America doesn’t get eaten,")
        print("and it’s difficult for 1 of every 8 Americans to put food on")
        print("the table. Consider: portion control, and maybe petitioning")
        print("the start of a compost at your school,")
        print("which is great for the environment!");
    print();
    print("Do you want to redo this part?")
    choiceFive = input("yes or no?")
    if (choiceFive == "no"):
        choice5 = False
print()

#sleepy time
choice6 = True
while(choice6 == True):
    print("After a filling dinner with strong portion control,")
    print("you decide you’ve given up on studying, and it’s time for bed.")
    print("You’ve changed into your jammies and you’ve considered looking")
    print("over your notes so as to avoid disappointing yourself too much.")
    print("It’s time to reflect! What have you learned from today?");
    print("a. It’s possible for me to replace and change parts of my")
    print("everyday routine in order to help fight against climate change")
    print("and lower my carbon footprint!");
    print("b. I noticed that even the smallest things can have an impact")
    print("on my environment, and I’d like to consider how I can")
    print("change some of my habits.");
    print("c. I learned nothing.");
    response10 = input("What is your choice?");
    if (response10 == "a." or response10 == "a"):
        print("That’s great! Look at everything you do, and maybe make")
        print("it a habit to think how you can make little things in your")
        print("life more sustainable! Just remember, you don’t have to make")
        print("a big change now, like going straight vegan or going waste-free.")
        print("If you can do that in the future, that’d be awesome.")
        print("Just remember to take things slow! Keep up the great work!");
    elif (response10 == "b." or response10 == "b"):
        print("That’s great! Yes, even small things, things you may not")
        print("have considered, can have an impact on the environment.")
        print("If you’re unsure about what may have an affect on the")
        print("environment in your life, the internet is a great resource")
        print("for studying up on sustainability. Just remember,")
        print("you don’t have to make a big change now,")
        print("like going straight vegan or going waste-free.")
        print("If you can do that in the future, that’d be awesome.")
        print("Just remember to take things slow!");
    elif (response10 == "c." or response10 == "c"):
        print("Since you chose this answer, I’m going to just assume")
        print("you didn’t read the information. If you don’t want to learn,")
        print("then fine! We can’t make you. Just don’t try to say ")
        print("“climate change isn’t my problem.” It is,")
        print("and it’s up to us and the coming generations to fix things.")
    print()
    print("Do you want to redo this part?")
    choiceSix = input("yes or no?")
    if (choiceSix == "no"):
        choice6 = False
print()
print("Thanks for completing this activity.")
print("We hope you learned something new!")





    






        



        

    



    





        
