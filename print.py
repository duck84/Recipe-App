import pickle

recipes = pickle.load( open('database.pkl', 'rb'))

missed = []

miss = total = apple = bananas = oranges = blueberries = raspberries = strawberries = grapes = watermelon = melon = 0
broccoli = cauliflower = carrots = cucumbers = garlic = lettuce = mushrooms = onions = scallions = 0
green_onions = jalapeno = bell_pepper = potatoes = tomatoes = zucchini = squash = beans = 0
beef = steak = chicken_breast = chicken_thighs = chicken_wings = pork = lamb = turkey = 0
salmon = trout = crab = shrimp = bacon = sausage = peanut_butter = jelly = honey = mayonnaise = mustard = 0
ketchup = pickles = bbq_sauce = oil = vinegar = soy_sauce = maple_syrup = tofu = walnuts = pecans = peanuts = 0
pine_nuts = bread = bread_crumbs = salsa = raisins = pitas = tortillas = apple_juice = orange_juice = 0
soda = coffee = tea = milk = butter = eggs = mozzarella = cheddar = parmesan = cream_cheese = yogurt = 0
spaghetti = rice = sugar = flour = vanilla = granola = bay_leaves = cinnamon = coriander = turmeric = 0
red_pepper_flakes = paprika = oregano = nutmeg = cumin = basil = thyme = rosemary = cayenne = cloves = 0
lemons = limes = radishes = fish_sauce = mint = peas = cilantro = olives = cream = broth = chocolate = 0
red_wine = white_wine = almonds = peaches = chili_powder = sage = clams = parsley = sesame_seeds = baking_powder = 0
cardamom = whiskey = 0

for key in recipes:
    for value in recipes[key][1:]:
        value = value.lower()
        if 'apple' in value and not 'juice' in value:
            apple += 1
        elif 'bananas' in value:
            bananas += 1
        elif 'orange' in value and not 'juice' in value:
            oranges += 1
        elif 'blueberries' in value:
            blueberries += 1
        elif 'raspberries' in value:
            raspberries += 1
        elif 'strawberries' in value:
            strawberries +=1
        elif 'grapes' in value:
            grapes += 1
        elif 'watermelon' in value:
            watermelon += 1
        elif 'melon' in value:
            melon += 1
        elif 'broccoli' in value:
            broccoli += 1
        elif 'cauliflower' in value:
            cauliflower += 1
        elif 'carrot' in value:
            carrots += 1
        elif 'cucumbers' in value:
            cucumbers += 1
        elif 'garlic' in value:
            garlic += 1
        elif 'lettuce' in value:
            lettuce += 1
        elif 'mushroom' in value:
            mushrooms += 1
        elif 'onion' in value:
            onions += 1
        elif 'scallion' in value:
            scallions += 1
        elif 'green onion' in value:
            green_onion += 1
        elif 'jalapeno' in value or ' jalapeño' in value:
            jalapeno += 1
        elif 'bell pepper' in value:
            bell_pepper += 1
        elif 'potato' in value:
            potatoes += 1
        elif 'tomato' in value:
            tomatoes += 1
        elif 'zucchini' in value:
            zucchini += 1
        elif 'squash' in value:
            squash += 1
        elif 'beans' in value:
            beans += 1
        elif 'ground beef' in value:
            beef += 1
        elif ' steak' in value:
            steak += 1
        elif 'chicken breast' in value:
            chicken_breast += 1
        elif 'chicken thighs' in value:
            chicken_thighs += 1
        elif 'chicken wings' in value:
            chicken_wings += 1
        elif 'pork' in value:
            pork += 1
        elif 'lamb' in value:
            lamb += 1
        elif 'turkey' in value:
            turkey += 1
        elif 'salmon' in value:
            salmon += 1
        elif 'trout' in value:
            trout += 1
        elif 'crab' in value:
            crab += 1
        elif 'shrimp' in value:
            shrimp += 1
        elif 'bacon' in value:
            bacon += 1
        elif 'sausage' in value:
            sausage += 1
        elif 'peanut butter' in value:
            peanut_butter += 1
#        elif 'jelly' in value:
#            jelly += 1
        elif 'honey' in value:
            honey += 1
        elif 'mayonnaise' in value:
            mayonnaise += 1
        elif 'mustard' in value:
            mustard += 1
        elif 'ketchup' in value:
            ketchup += 1
        elif 'pickles' in value:
            pickles += 1
        elif 'bbq sauce' in value or 'barbecue sauce' in value:
            bbq_sauce += 1
        elif ' oil' in value:
            oil += 1
        elif 'vinegar' in value:
            vinegar += 1    
        elif 'soy sauce' in value:
            soy_sauce += 1
        elif 'maple syrup' in value:
            maple_syrup += 1
        elif 'tofu' in value:
            tofu += 1
        elif 'walnuts' in value:
            walnuts += 1
        elif 'pecans' in value:
            pecans += 1
        elif 'peanuts ' in value:
            peanuts += 1
        elif 'pine nuts' in value:
            pine_nuts += 1
        elif ' bread ' in value and not 'crumbs' in value:
            bread += 1
        elif ' bread crumbs' in value:
            bread_crumbs += 1
        elif 'salsa' in value:
            salsa += 1
        elif 'raisins' in value:
            raisins += 1
        elif 'pitas' in value:
            pitas +=1
        elif 'tortillas' in value:
            tortillas += 1
        elif 'apple juice' in value:
            apple_juice += 1
        elif 'orange juice' in value:
            orange_juice += 1
        elif 'soda' in value:
            soda += 1
        elif 'coffee' in value:
            coffee += 1
        elif 'tea' in value:
            tea += 1
        elif 'milk' in value:
            milk += 1
        elif 'butter' in value and not 'peanut' in value:
            butter += 1
        elif 'egg' in value:
            eggs += 1
        elif ' mozzarella' in value:
            mozzarella += 1
        elif ' cheddar' in value:
            cheddar += 1
        elif 'parmesan' in value:
            parmesan += 1
        elif ' cream cheese' in value:
            cream_cheese += 1
        elif ' yogurt' in value:
            yogurt += 1
        elif ' spaghetti' in value or 'pasta' in value:
            spaghetti += 1
        elif ' rice' in value:
            rice += 1
        elif 'sugar' in value:
            sugar += 1
        elif ' flour' in value:
            flour += 1
        elif ' vanilla' in value:
            vanilla += 1
        elif ' granola' in value:
            granola += 1
        elif ' bay leaves' in value:
            bay_leaves += 1
        elif 'cinnamon' in value:
            cinnamon += 1
        elif ' coriander' in value:
            coriander += 1
        elif ' turmeric' in value:
            turmeric += 1
        elif ' red pepper flakes' in value:
            red_pepper_flakes += 1
        elif ' paprika' in value:
            paprika += 1
        elif ' oregano' in value:
            oregano += 1
        elif 'nutmeg' in value:
            nutmeg += 1
        elif 'cumin' in value:
            cumin += 1
        elif 'basil' in value:
            basil += 1
        elif 'thyme' in value:
            thyme += 1
        elif 'rosemary' in value:
            rosemary += 1
        elif 'cayenne' in value:
            cayenne += 1
        elif 'cloves' in value:
            cloves += 1
        elif 'lemon' in value:
            lemons += 1
        elif 'lime' in value:
            limes += 1
        elif 'radish' in value:
            radishes+= 1
        elif 'fish sauce' in value:
            fish_sauce += 1
        elif 'mint' in value:
            mint += 1
        elif ' peas' in value:
            peas += 1
        elif 'cilantro' in value:
            cilantro += 1
        elif 'olives' in value:
            olives += 1
        elif 'cream' in value:
            cream += 1
        elif 'broth' in value or ' stock' in value:
            broth += 1
        elif 'chocolate' in value:
            chocolate += 1
        elif ' red wine' in value:
            red_wine += 1
        elif ' white wine' in value:
            white_wine += 1
        elif 'almonds' in value:
            almonds += 1
        elif 'peach' in value:
            peaches += 1
        elif ' chili powder' in value:
            chili_powder += 1
        elif ' sage' in value:
            sage += 1
        elif ' clam' in value:
            clams += 1
        elif 'parsley' in value:
            parsley += 1
        elif 'sesame seeds' in value:
            sesame_seeds += 1
        elif 'baking powder' in value:
            baking_powder += 1
        elif 'cardamom' in value:
            cardamom += 1
        elif 'bourbon' in value or 'whiskey' in value:
            whiskey += 1
        elif 'salt' in value:
            pass
        elif 'pepper' in value:
            pass
        elif 'water' in value:
            pass
        elif 'ice' in value:
            pass
        elif 'for the' in value:
            pass
        elif 'grill heat' in value:
            pass
        elif 'to serve' in value:
            pass
        elif 'type of fire' in value:
            pass
        else:
            miss += 1
            missed.append(value)
        total +=1

#    print(key)
#    x += 1
#    for value in recipes[key]:
#        print("   {}".format(value))

missed.sort()
for thing in missed:
    print (thing)
print("Total: {}\nMissed: {}\nHit: {}\n".format(total, miss, total - miss))
print (apple , bananas , oranges , blueberries , raspberries , strawberries , grapes , watermelon , melon , 
broccoli , cauliflower , carrots , cucumbers , garlic , lettuce , mushrooms , onions , scallions , 
green_onions , jalapeno , bell_pepper , potatoes , tomatoes , zucchini , squash , beans , 
beef , steak , chicken_breast , chicken_thighs , chicken_wings , pork , lamb , turkey , 
salmon , trout , crab , shrimp , bacon , sausage , peanut_butter , jelly , honey , mayonnaise , mustard , 
ketchup , pickles , bbq_sauce , oil , vinegar , soy_sauce , maple_syrup , tofu , walnuts , pecans , peanuts , 
pine_nuts , bread , bread_crumbs , salsa , raisins , pitas , tortillas , apple_juice , orange_juice , 
soda , coffee , tea , milk , butter , eggs , mozzarella , cheddar , parmesan , cream_cheese , yogurt , 
spaghetti , rice , sugar , flour , vanilla , granola , bay_leaves , cinnamon , coriander , turmeric , 
red_pepper_flakes , paprika , oregano , nutmeg , cumin , basil , thyme , rosemary , cayenne , cloves,
lemons, limes, radishes, fish_sauce, mint, peas, cilantro, olives, cream, broth, chocolate, red_wine,
white_wine, almonds, peaches, chili_powder, sage, clams, parsley, sesame_seeds, baking_powder, cardamom,
whiskey)


