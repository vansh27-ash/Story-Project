from random import randint
from typing import List, Any

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html", {})

def about_us(request):
    return render(request, "about_us.html", {})

def create_story(request):
    usetext = request.GET.get('text', 'default')
    return render(request,'create_story.html')
	
def example_1(request):
	return render(request, "examples/cindrella.html", {})
	
def example_2(request):
	return render(request, "examples/ThePigFarmer.html", {})

def show_my_story(request):
    gen = lambda l: l[randint(0, len(l) - 1)]
    def do(text):
        d_var = {'toy': ['dolls', 'car', 'aeroplane', 'balls', 'water-guns'],
                 'play_instrument': ['sitar', 'guitar', 'drums', 'piano', 'music-box'],
                 'part_of_school': ['class', 'ground', 'halls', 'seats'],
                 'eatable': ['pastry', 'ice-cream', 'candy', 'chocolates'],
                 'other_eatable': ['pizza', 'burger', 'french-fries', 'noodles'],
                 'type_of_game': ['eat', 'play', 'think', 'dance'], 'animal': ['cats', 'dogs', 'birds', 'horse'],
                 'item_to_share': ['candies', 'toffies', 'stickers'],
                 'num_pages': ['50', '100', '70', '30'], 'topic': ['haunted', 'science', 'electricity', 'light'],
                 'math_topic': ['multiplication', 'subtraction', 'division', 'addition'],
                 'num_hrs': ['4', '3', '2', '5'], 'vehicle': ['cycles', 'cars', 'bikes'],
                 'other_vehicle': ['trains', 'joyful rides'],
                 'place': ['Paris', 'New York', 'Dalton', 'Nimachi', 'Sinton'],
                 'adj_adventure': ['brave', 'intelligent', 'smart', 'mighty', 'daring', 'decisive', 'determined',
                                   'discreet', 'dynamic', 'easy-going', 'calm'],
                 'name': ['Ken', 'Ti``m', 'Norbu', 'Allan', 'Mark', 'Naple'],
                 'adj_king': ['kind', 'good', 'kind-hearted'],
                 'sacred_object': ['necklace', 'crown', 'lamp', 'stone'],
                 'adj_cave': ['giant', 'small', 'large', 'dark'],
                 'rel_sound': ['loudly', 'with intensity'], 'adj_object': ['golden', 'silver', 'diamond'],
                 'obj_for_exchange': ['necklace', 'stone', 'lamp'],
                 'adj_pigs': ['little', 'mini', 'fat', 'big'], 'work': ['work', 'stay', 'live'],
                 'rel_to_build': ['build', 'make', 'construct'], 'obj_house1': ['leaves', 'stem', 'cotton'],
                 'verb1': ['be free', 'lie', 'roam'], 'verb2': ['sit', 'sleep'], 'verb3': ['roam', 'play', 'sing'],
                 'quality': ['sharp-minded', 'smart', 'witty', 'intelligent'],
                 'obj_house_strong': ['stones', 'bricks'], 'rel_home': ['door', 'home', 'gate'],
                 'rel_damage': ['smashed', 'broke', 'destroyed', 'blowed'],
                 'verb_tried': ['tried', 'dodged'], 'verb_for_ending': ['lived', 'lived thier life'],
                 'up_Body_part': ['Neck', 'Hands'], 'low_body_part': ['Legs', 'Tail'],
                 'sounds': ['creepy Sounds', 'Noisy Sounds'],
                 're_fight_ing': ['kicking'], 'material': ['hammer', 'screwdriver'],
                 'unit': ['kilometres', 'Miles', 'metres'], 'moment': ['moment in their life', 'event happened'],
                 'liquid': ['water', 'cold drink'], 'community': ['people', 'scientists', 'researchers'],
                 'Common_noun': ['Human-being', 'animals'],
                 'number': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                            '18', '19', '20', '21', '22', '23', '24'], 'Adjective': ['large', 'big'],
                 'good_adj': ['great', 'strong', 'nice'],
                 'Read': ['readers'], 'verb_ed': ['jumped'],
                 'number_th': ['5th', '12th', '100th', '63th', '46th', '44th', '26th', '17th', '99th', '25th', '75th'],
                 'rodent_animal': ['rabbit'], 'mad': ['Mad'], 'world': ['Wonderland'],
                 'Sweet_food': ['cake', 'pastries'], 'heart': ['Heart'], 'meet': ['meets'],
                 'transparent_object': ['glass', 'tape', 'water'],
                 'animal': ['horses', 'monkeys'], 'bad_adj': ['ruthless', 'negative', 'merciless', 'dark', 'rough'],
                 'activity': ['run', 'eat', 'sleep', 'play', 'walk', 'jog'],
                 'good_adj': ['talented', 'sucessful', 'accomplished', 'brilliant', 'expert'],
                 'nationality': ['italian', 'mexican', 'american'],
                 'color': ['red', 'green'], 'color2': ['white', 'yellow'],
                 'pizza_types': ['pepper', 'margherita', 'mexican'],
                 'weather': ['summer', 'winter', 'spring', 'autmn'], 'second_name': ['Jack', 'Edward', 'Anna', 'Harry'],
                 'place_trip': ['Puerto Rico', 'Fiji', 'Hawai', 'Mexico'],
                 'weather_adj': ['sunny', 'bright', 'hot', 'mild'],
                 'stay_places': ['hotels', 'beaches', 'forests', 'food hubs'], 'near_places': ['beahes', 'parks'],
                 'beauty_adj': ['beautiful', 'great'],
                 'activities': ['play', 'run', 'play games'], 'num_year': ['5', '4', '6'],
                 'color': ['blue', 'grey', 'white', 'red'], 'cloth': ['pant', 'shirt', 'socks'],
                 'carry_item': ['belt', 'tie'], 'food_item': ['pastries', 'dosa', 'paratha'], 'num': ['7', '8', '9'],
                 'fr_name': ['Tim', 'Ben', 'Michael'], 'bad_adj': ['dusty', 'sharp', 'rusty'],
                 'road_item': ['iron', 'pole', 'element'],
                 'body_part': ['leg', 'hand', 'knee', 'elbow'], 'num_min': ['15', '30', '45', '20'],
                 'sport': ['basketball', 'volleyball', 'table tennis'], 'num_points': ['5', '7', '10', '8'],
                 'instrument': ['sitar', 'guitar', 'drums', 'piano', 'music-box'],
                 'adj_season': ['hot', 'dry', 'enjoyable'], 'adj_fam': ['happy', 'small', 'large'],
                 'adj_mountain': ['large', 'magnificient', 'high', 'great'],
                 'adverb': ['heavily', 'fast', 'regularly'], 'verb_ing': ['swimming', 'trekking'],
                 'noun': ['mountain', 'landscape', 'canyon'], 'city': ['Abenzon', 'Dockming', 'Healamn'],
                 'phy_hills': ['snowy', 'rocky', 'dusty'],
                 'person': ['Lanse', 'Aaron', 'David', 'Tom'], 'thing': ['petrol pump', 'tank with petrol'],
                 'verb_catch': ['catch', 'arrest'], 'woman': ['Lydia', 'Daisy', 'Mona'],
                 'rel_brain': ['brain', 'ideas', 'wise'],
                 'place': ['restaurant', 'staions'], 'area': ['park', 'road'],
                 'monument': ['Staue of Lisa', 'Daron bridge'], 'rel_damage': ['damaged', 'destroyed'],
                 'place_fall': ['garden', 'muddy area'],
                 'country': ['france', 'britain', 'russia']}
        text = list_text[randint(0, len(list_text) - 1)]

        d_var['animal'] =[request.GET.get('animal1', gen(d_var['animal'])), request.GET.get('animal2',gen(d_var['animal'])),
                 request.GET.get('animal3',gen(d_var['animal']))]
        d_var['color'] = [request.GET.get('Colour1',gen(d_var['color'])), request.GET.get('Colour2', gen(d_var['color'])),
                 request.GET.get('Colour3', gen(d_var['color']))]
        d_var['country'] = [request.GET.get('Country1', gen(d_var['country'])), request.GET.get('Country2', gen(d_var['country'])),
                 request.GET.get('Country3', gen(d_var['country']))]
        d_var['place']=[request.GET.get('place1', gen(d_var['place'])), request.GET.get('place2', gen(d_var['place'])),
                 request.GET.get('place3', gen(d_var['place']))]
        d_var['weather_adj']=[request.GET.get('weather1', gen(d_var['weather_adj'])), request.GET.get('weather2', gen(d_var['weather_adj'])),
                 request.GET.get('weather3',  gen(d_var['weather_adj']))]
        d_var['monument']=[request.GET.get('monument1',gen(d_var['monument'])), request.GET.get('monument2',gen(d_var['monument'])),
                 request.GET.get('monument3', gen(d_var['monument']))]
        d_var['food_item'] = [request.GET.get('food1', gen(d_var['food_item'])), request.GET.get('food2', gen(d_var['food_item'])),
                 request.GET.get('food3', gen(d_var['food_item']))]
        d_var['Sweet_food']= [request.GET.get('sweet1', gen(d_var['Sweet_food'])), request.GET.get('sweet2', gen(d_var['Sweet_food'])),
                     request.GET.get('sweet3', gen(d_var['Sweet_food']))]
        d_var['rel_sound']=[request.GET.get('sound1',gen(d_var['rel_sound'] )), request.GET.get('sound2',gen(d_var['rel_sound'] )),
                 request.GET.get('sound3',gen(d_var['rel_sound'] )) ]
        d_var['name']=(request.GET.get('Protagon_Name'),gen(d_var['name']))



        # --------------------------------------------------------------------------------------------vars for input------------------------------------------------------------------------------------##


        color = gen(d_var['color'])
        animal = gen(d_var['animal'])#done
        weather_adj = gen(d_var['weather_adj'])#done
        place = gen(d_var['place'])#done
        country = gen(d_var['country'])#done
        monument = gen(d_var['monument'])#done
        food_item = gen(d_var['food_item'])#done
        sweet_food = gen(d_var['Sweet_food'])
        protagon_name = gen(d_var['name'])
        rel_sound = gen(d_var['rel_sound'])
        new_text = text.format(toy=gen(d_var['toy']), play_instrument=gen(d_var['play_instrument']),
                               part_of_school=gen(d_var['part_of_school']), eatable=gen(d_var['eatable']),
                               other_eatable=gen(d_var['other_eatable']), type_of_game=gen(d_var['type_of_game']),
                               animal=animal, item_to_share=gen(d_var['item_to_share']),
                               num_pages=gen(d_var['num_pages']), topic=gen(d_var['topic']),
                               math_topic=gen(d_var['math_topic']), num_hrs=gen(d_var['num_hrs'])
                               , vehicle=gen(d_var['vehicle']), other_vehicle=gen(d_var['other_vehicle']), place=place,
                               adj_adventure=gen(d_var['adj_adventure']),
                               name=protagon_name, adj_king=gen(d_var['adj_king']),
                               sacred_object=gen(d_var['sacred_object']), adj_cave=gen(d_var['adj_cave']),
                               rel_sound=rel_sound, adj_object=gen(d_var['adj_object']),
                               obj_for_exchange=gen(d_var['obj_for_exchange']), adj_pigs=gen(d_var['adj_pigs']),
                               work=gen(d_var['work']), rel_to_build=gen(d_var['rel_to_build']),
                               obj_house1=gen(d_var['obj_house1']), verb1=gen(d_var['verb1']),
                               verb2=gen(d_var['verb2']),
                               verb3=gen(d_var['verb3']), quality=gen(d_var['quality']),
                               obj_house_strong=gen(d_var['obj_house_strong']), rel_home=gen(d_var['rel_home']),
                               rel_damage=gen(d_var['rel_damage']), verb_tried=gen(d_var['verb_tried']),
                               verb_for_ending=gen(d_var['verb_for_ending']), up_Body_part=gen(d_var['up_Body_part']),
                               low_body_part=gen(d_var['low_body_part']), sounds=gen(d_var['sounds']),
                               re_fight_ing=gen(d_var['re_fight_ing']), material=gen(d_var['material']),
                               unit=gen(d_var['unit']), liquid=gen(d_var['liquid']), community=gen(d_var['community']),
                               Common_noun=gen(d_var['Common_noun']), number=gen(d_var['number']),
                               Adjective=gen(d_var['Adjective']), good_adj=gen(d_var['good_adj']),
                               Read=gen(d_var['Read']), verb_ed=gen(d_var['verb_ed']),
                               number_th=gen(d_var['number_th']), rodent_animal=gen(d_var['rodent_animal']),
                               mad=gen(d_var['mad']), world=gen(d_var['world']), Sweet_food=sweet_food,
                               heart=gen(d_var['heart']), meet=gen(d_var['meet']),
                               transparent_object=gen(d_var['transparent_object']), bad_adj=gen(d_var['bad_adj']),
                               activity=gen(d_var['activity']),
                               nationality=gen(d_var['nationality']), color=color, color2=gen(d_var['color2']),
                               pizza_types=gen(d_var['pizza_types']), num=gen(d_var['num']),
                               weather=gen(d_var['weather']), second_name=gen(d_var['second_name']),
                               place_trip=gen(d_var['place_trip']), weather_adj=weather_adj,
                               stay_places=gen(d_var['stay_places']), near_places=gen(d_var['near_places']),
                               beauty_adj=gen(d_var['beauty_adj']), food_item=food_item,
                               activities=gen(d_var['activities']), num_year=gen(d_var['num_year']),
                               cloth=gen(d_var['cloth']), carry_item=gen(d_var['carry_item']),
                               fr_name=gen(d_var['fr_name']), road_item=gen(d_var['road_item']),
                               body_part=gen(d_var['body_part']),
                               num_min=gen(d_var['num_min']), sport=gen(d_var['sport']),
                               num_points=gen(d_var['num_points']), instrument=gen(d_var['instrument']),
                               adj_season=gen(d_var['adj_season']), adj_fam=gen(d_var['adj_fam']),
                               adj_mountain=gen(d_var['adj_mountain']), adverb=gen(d_var['adverb']),
                               verb_ing=gen(d_var['verb_ing']), noun=gen(d_var['noun']), city=gen(d_var['city']),
                               phy_hills=gen(d_var['phy_hills']), person=gen(d_var['person']),
                               thing=gen(d_var['thing']), verb_catch=gen(d_var['verb_catch']),
                               woman=gen(d_var['woman']), rel_brain=gen(d_var['rel_brain']),
                               area=gen(d_var['area']), monument=monument, place_fall=gen(d_var['place_fall']),
                               moment=gen(d_var['moment']), country=country)
        return new_text

    the_unknown_story = '''{name} is a normal coal miner from {country}.Then one day,
    a {color}bomb explodes,it was a time of {weather_adj} summer
    causing a nearby damage and the {thing} erupts into a wall of flames.
    {name} realises that he's being chased by the government, who's
    trying to {verb_catch} him.While on the run,he teams up with an
    incredibly attractive woman named {woman} ,who has an incredible
    {rel_brain}.She may be from the streets,but she can look like nobody's
    business.The duo decide to turn the tables on there pursuers by blowing
    up a reactor,which triggers a chain reaction ,
    causing the local {place},{area} and  the {monument} to explode.
    Then the bad guys' helicopter gets {rel_damage} by a piece of hard material from  the
    {place} exploded, and the helicopter explodes and falls onto a {place_fall},
    causing it to explode, which shoots a fireball straight into the
    heart of bad guys team and destroys the bad guy leader.Everything is over and
    the two decide that such a {moment} or deal has caused them to
    fall in love with each other.They decide to celebrate everything on
    the {place_fall} ,and they even managed to use a an object
    from the beginning of the movie, to enjoy the whole story together.'''
    vacations = '''Good vacations are worth their weight in that season.A {weather_adj} summer
    vacation for me i.e {name} and your {adj_fam} family who lived in {country} is to visit
    the Rocky Mountains in Colorado.The first time you see these {adj_mountain}
    mountains, your heart will thump {adverb}.If you're into camping
    ,fishing or {verb_ing},visit Arizona's Grand Canyon and enjoy a land
    of great landscapes and rich for their history.Upon sight of
    this mile-deep magnificent 1.5 billion-year old {noun},your mouth
    will drop open and you won't be able to catch your sight.
    And then, there is the city of the golden gate {city} ,San Francisco,
    where you can spend the day watching a cable
    loaded with wide-eyed texhniques or climb the city's {phy_hills} hills .
    A place made famous by Tony Bennett's rendition of 'I
    Left My Heart in San-Francisco.'So will you!'''
    first_day_of_school = '''Today is the first day of school.I am {name},{num_year} old
    and am in the {number_th} grade. I decided to wear my {color} {cloth}
    with my handy {carry_item}.For lunch I packed my favorite sandwich ,
    {food_item} with pizza. I left the house at {num} O' clock and headed to school with my freind {fr_name}.
    On the way there, I tripped over a {bad_adj} {road_item} and scraped my {body_part}.
    I finally got to school {num_min} late. My teacher was busy taking attendance, so i entered the room and
    sat in my seat. At recess I played {sport} with my freinds and scored {num_points}.
    I then went to art and music class where i got to play a {instrument}. Overall it was a good day!'''
    summer_trip = '''Last {weather_adj} summer, my mom and dad took me i.e {name} and {second_name}
    on a trip to {place_trip} in {country}. The weather there is very {weather_adj}! Northern {place_trip}
    has many {stay_places} and they make living there. Many people also go to
    {near_places} to see the {beauty_adj} lanscape. The people that live
    there love to eat {food_item} and are very proud of their big food festival.
    They also like to {activities} in the sun and swim in the water. It was really {beauty_adj} trip!'''
    pizza = '''Pizza was invented by a {good_adj} {nationality} chef named {name}.
    To make a pizza you need to take a lump of flour, and make a thin, round base.
    then you cover it with {color} sauce, {color2} cheeze and fresh chopped veggies.
    Next you have to bake it in a very hot pan. When it is done, cut it into {number} slices.
    Some kids like {pizza_types} pizza the best, but my favorite is the homemade pizza.
    If I could, I would eat pizza {num} times a day!'''
    alice = '''Lewis carroll's classic ,Alice adventures in Wonderland as well as its {number_th} sequel ,
    through the looking {transparent_object}
    have enchanted both the young and the old {Read} for the last {number} years.
    Alice's {adj_adventure} adventures begin when she {verb_ed} down
    a/an {rodent_animal} hole and lands in a strange and topsy-turvy {world}.
    There she discovers she can become a tall {Common_noun} or a small
    {Common_noun} simply by nibbling on alternate sides of a magic {Sweet_food} .
    In her travels through Wonderland,Alice {meet} such remarkable
    characters as the white {rodent_animal} ,the {mad} hatter, the cheshire {animal} ,
    and even the queen of {heart} .Unfortunately ,Alice's
    adventures come to a/an {bad_adj} end when Alice awakens from her {activity}.'''
    giraffe = '''giraffes have aroused the curiosity of {community} since
    earliest times, especially the researcher {name}.
    the giraffe is the tallest of all living {Common_noun} ,
    but scientists are unable to explain how it got
    its long {up_Body_part} .The giraffe's tremendous height,
    which might reach {number} {unit} ,comes mostly from its legs and
    {up_Body_part} .If a giraffe wants to take a drink of {liquid} from the ground,
    it has to spread its {low_body_part} far apart in order to
    reach down and lap up the water with its huge {up_Body_part} .
    The giraffe has {Adjective} ears that are sensitive to the faintest
    {sounds} ,and it has a/an {good_adj} sense of smell and sight.
    When attacked ,a giraffe can put up a/an fight by {re_fight_ing} out with
    its hind legs and using its head like a sledge {material}. Finally,
    a giraffe can gallop at more than thirty {unit} an
    hour when pursued and can outrun the fastest like {animal} .'''
    three_little_pigs = '''Once upon a time, there were three {adj_pigs} pigs lived in {country}.
    One day, their mother said, 'you are all grown up and must {work} on your own.' So they left to {rel_to_build}
    their houses. The first little pig wanted only to {verb1} all day and quickly built his
    house out of {obj_house1} and also painted it with {color}. The second little pig wanted to {verb2} and {verb3}
    all day so he {rel_to_build} his house with {obj_house1}. The third {quality} pig
    knew the wolf lived nearby and worked hard to {rel_to_build} his house out of {obj_house_strong}.
    One day, the wolf knocked on the first pig's {rel_home}. 'Let me in or I'll
    {rel_damage} your house down !'  The pig didn't, so the wolf {rel_damage} down the {rel_home}
    The wolf knocked on the second pig's {rel_home}. 'Let me in or I'll {rel_damage}
    your house down!'  The pig didn't, so the wolf {rel_damage} down the house.Then the wolf knocked
    on the third {quality} pig's door. 'Let me in or I'll blow your house down!'
    The little pig didn't so the wolf {verb_tried} and {verb_tried}. He could not blow the house down. All the pigs
    went to live in the {obj_house_strong} house and they all {verb_for_ending} happily year after.'''
    pri_for_a_day = '''If I was principal of my school, i'd put {toy} and {play_instrument} in every
    {part_of_school} and have the cafeteria serve {eatable} and {other_eatable} for lunch.We
    would have '{type_of_game} and Tell' everyday, where students
    can bring {animal} and {item_to_share} to share in class.
    Students would give teachers homework, like
    {num_pages} page book reports about {topic} and {math_topic} math problems.
    Recess would last for {num_hrs} hours, and instead of buses, I'd have {vehicle} and {other_vehicle} take
    the kids to and from school.'''
    very_brave_adv = '''Once upon a time in the kingdom of {country}, there lived
    a {adj_adventure} adventurer named {name}. It was a time of {weather_adj} autmn. The kingdom was a peaceful
    kingdom, where the animals roamed free and the food was plentiful.
    Ruling over the kingdom was {adj_king} King Nicklaus and Queen
    Lillian. Everyone in the kingdom was happy,until one day a villain
    named Mr. Mean came into the castle and stole the {color} sacred {sacred_object}.
    King Nicklaus and Queen Lillian didn't know what to do. They wandered
    the countryside for days trying to come up with a plan. Finally,
    they met {name}.{name} told Nicklaus not to worry, and set off to take back
    what Mr. Mean had taken back from the kingdom.
    {name} hopped on a {animal} and rode it to the {adj_cave} cave where
    Mr. Mean lived. {name} tip toed into the cave then yelled
    {rel_sound}. Mr. Mean was startled and dropped the sacred item. {name}
    grabbed it and raced back to King Nicklaus. Nicklaus was so
    grateful that he gave {name} a {adj_object} {obj_for_exchange} in
    exchange for his appreciation. Everyone in the kingdom was so happy that they
    celebrated by eating delicious food. Mr. Mean never returned
    to the kingdom again and everyone live happily ever after!'''
    list_text = [the_unknown_story, vacations, first_day_of_school, summer_trip, pizza, alice, giraffe,
                 three_little_pigs, pri_for_a_day, very_brave_adv]
    list_text1 = [the_unknown_story, vacations, first_day_of_school, summer_trip, pizza, alice, giraffe,
                 three_little_pigs, pri_for_a_day, very_brave_adv]
    list_text2 = ['the_unknown_story', 'vacations', 'first_day_of_school', 'summer_trip', 'pizza', 'alice', 'giraffe',
                 'three_little_pigs', 'pri_for_a_day', 'very_brave_adv']
    dicto={}
    dicto['creator'] = request.GET.get("Protagon_Name")
    for _ in range(10):
        dicto[list_text2[_]]=do(list_text[_])

    return render(request,'show_my_story.html',dicto)
