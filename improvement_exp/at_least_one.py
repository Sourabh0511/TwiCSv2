
from nltk.tokenize import word_tokenize
import string
import pandas as pd 
tweets=pd.read_csv("tweets_3k_annotated.csv",sep =',')

my_list=['', 'german', 'netherlands', 'oleks skichko', 'universal health care', 'woodley', 'rio', 'serbia', 'bush', 'clintons', 'australian', 'wango tango', 'dems', 'ca', 'jesus christ', 'djt', 'cbo', 'maia. linking park', 'sc', 'french', 'iaquinta', 'unicorns', 'frankie', "let's go crazy", 'type 1 diabetics', 'jurassic world', 'liberty university', 'masvidal maia', 'twitter', 'house oversight chair', 'kabuki', 'brasil', 'shashlik rap', 'rosneft', 'simpsons', 'cantando', 'white privilege', 'christmas', 'sia', 'amanda', 'rashad coulter', 'france', 'oakley', 'maxine waters', 'juno mission', 'austrian', 'tom clancy', 'obama presidency', 'holy father', 'homophobes', 'ann courter', 'clinton', 'barry', 'trumps', 'democrats', 'trump/russia', 'limousine', 'ruslana', 'kate bush', 'brad pitt', 'tories', 'bruce buffer', 'syria', 'romani', 'yair rodriguez', 'latino', 'healthcare', 'chester', 'gorilla', 'zionist', 'spicer', 'chuck', 'chris pratt', 'rep. joe kennedy', 'aca', 'salvador', 'donald', 'kiev', 'ufc light heavyweight champion daniel cormier', 'lou', 'romania', 'euros', 'jd', 'fitch', 'snakes', 'europeans', 'united states of  east america', 'scaarface', 'hillary clinton', 'medicaid', 'socialist', 'uber', 'vova ostapchuk', 'european', 'hrc', 'bbc', 'wh', 'meia', 'gamebredfighter', 'rus', 'jorge masvidal', 'chris hayes', 'trumpland', 'trousersnake', 'hispanics', 'obamagate', 'jordan fisher', 'fairytale', 'house democrats', 'jason chaffetz', 'rose garden', 'jolene', 'cormier', 'anna wintour', 'chechnya', 'swedish', 'sun', 'manafort', 'republican', 'foreign agent', 'sbs', 'gamebread', 'russia oil', 'petra', 'chipmunk', 'alex caceres', 'champions league', 'titanium', 'lucie jones', 'haille steinfeld', 'james comey', 'solar system', 'paul manafort', 'nialler', 'lisbon', 'evanescence', 'enforcer', 'nunez', 'damian maia', 'raccoon gosha', 'vets', 'spaniard', 'female genital mutilation', 'albert einstein', 'eurovision song contest', 'imperialism', 'hosen schlange', 'louis', 'h8', 'the mich stepping stones daily', 'andrew mccabe', 'siri', 'canada', 'womd', 'copa del rey', 'muslim', 'ireland', 'game of thrones', 'joe', 'white house', 'president', 'chester bennington', 'norway', 'obama', 'mlk', 'hillary', 'darth vader', 'grand ole putin party', 'ivanka', 'mercedes', 'justin', 'steele', 'jews', 'canelo', 'puppet master', 'bill clinton', 'twilight', 'justice department', 'vodka', 'brazilian', 'congressmen', 'wv', 'jacare souza', 'democratic', 'brazillians', 'jamala', 'centrist', 'reichert', 'bill', 'edgar', 'north cork', 'michelle', 'greece', 'migos', 'zayn', 'moldova', 'dana', 'christianity', 'cowboys', 'also-holloway', 'comney', 'brexir', 'nate', 'baywatch', 'arya stark', 'electoral college', 'mma', 'greg leppert', 'uranium', 'niam', 'floridans', 'arab', 'finnish', 'edgar holloway', 'antisemitism', 'sherdog forums', 'ufc hall of fame', 'boa constrictor', 'senate', 'dt', 'david guetta', 'gopher', 'genocide', 'constitution', 'mexican', 'justice', 'john fugelsang', 'sims city', 'kay', 'stoke ohio high school', 'page', 'pro life', 'arriba', 'progressives', 'jackson wink', 'coulter', 'hitler', 'we cant stop', 'africa', 'camila', 'baby elephant', 'iq', 'morgan freeman', 'hpn', 'whites', 'ukraine', 'mike', 'ariel winter', 'george soros', 'big homie stipe', 'sherman', 'president trump', 'ic', 'asthma', 'washington post', 'holocaust denier', 'richie', 'mgk', 'swedens', 'institutional racism', 'yodeling', 'oil deals', 'vladimir', "destiny's child", 'rocky balboa', 'demian maia', 'the arc', 'tb', 'this town', 'lego', 'rep swalwelll', 'wrestlemania', 'jessica andrade', 'antarctica', 'nyc', 'flynn', 'mike dean', 'devin nunes', 'barack obama', 'do joe jonas', 'mississippi mean', 'karma', 'euro', 'payne', 'mary', 'bahamas', 'joevin jones', 'kylo ren', 'bon appétit', 'don', 'muslims', 'officer william stacy', 'lenovo', 'bill nye', 'lee lin', 'pa', 'pro socialism', 'club world cup', 'katy', 'hosue republicans', 'bowie', 'striker', 'rice', 'star wars', 'civil war', 'jj', 'miah', 'e.t. bon appétit', 'hr', 'scared to be lonely', 'jfc', 'british isles', 'wales', 'breitbart', 'moscow', 'senate gop', 'las vegas', 'zedd', 'democracy', 'tower of babel', 'super cup', 'mother russia', 'liberalism', 'jorge', 'sowell', 'martian', 'mccanns', 'american health care act', 'mayo', 'adm levine', 'brexited', 'united states', 'aaron', 'croatia', 'campaign manager manaford', 'malta', 'wapo', 'germany', 'baseball', 'pagie', 'house representatives', 'nial', 'potus', 'americans', 'alessia', 'paul ryan', 'cinnamon roll', 'ceo', 'sean spicer', 'theresa may', 'nonsense karaoke', 'foxnews', 'prince', 'cnn', 'hailee steinfeld', 'le pen', 'rotherham', 'lincoln', 'wee bum', 'sean', 'rep schiff', 'gamebred', 'brazil', 'united airlines', 'normila', 'niall cantando', 'conor mcgregor', 'whittaker', 'senators', 'slovenia', 'fisa/fisc', 'russian intelligence', 'asians', 'ohio', 'stipe', 'poc', 'carter', 'phil', 'healthcare bill', 'jim comey', 'cyprus', 'hold tight', 'session', 'buzina', 'lynch', 'spain', 'onuka', 'gender studies', 'brit', 'russia', 'doj', 'janesville', 'cyrus', 'carlos condit', 'pro-life', 'christians', 'costarica', 'italy', 'kkk', 'america', 'us senate', 'spanish', 'crips', 'sofia carson', 'britain', 'health bill', 'cat', 'russian government', 'christ', 'bad things', 'authoritarian kleptocracy', 'shadow boxing', 'ibs', 'western cape', 'eddie alvarez', 'wnyers moc', 'tomahawks', 'horan', 'nunes', 'risacea', 'eddie', 'donald trump', 'bidet', 'republican fbi director comey', 'tang', 'malibu', 'mayonnaise', 'isil', 'amrican', 'stoke', 'coal mining', 'mt. everest', 'nazi', 'house of representatives', 'stoke greyson', 'macron', 'jorge "gamebread" masvidal', 'kayla', 'tariq', 'darrell issa', 'gigi hadid', 'ces', 'russias', 'liam payne', 'yoongi', 'iraw war', 'israel', 'representatives', 'frankie edgar', 'damien maia', 'warriors', 'henley', 'gentrification', 'cold war', 'june', 'passover', 'moto x4', 'j.j. watt', 'bosnia', 'm5', 'islamic', 'miley', 'lgbt', 'adam levine', 'camila cabello', 'michigan', 'fisa', 'asha', 'cali', 'netanyahu', 'messenger', 'tj', 'libnazi', 'tillerson', 'gop republicans', 'msnbc', 'superbowl', 'native americans', 'marine', 'whitehouse', 'hotdogs', 'acha', 'mcdonalds', 'gitmo', 'frankieedgar', 'australia', 'dr.king', 'dave matthews', 'messer', 'martin luther king', 'hilary', 'luhan', 'emri', 'ukrainian', 'des', 'poland', 'may 13', 'white supremacists', 'avril lavigne', 'comey', 'conservative', 'hocaust centers', 'maryland', 'himmel och hav', 'ronaldo', 'spring', 'scottish', 'holocaust', 'san bernardino', 'united', 'american', 'abortion', 'bananies', 'american government', 'libery university', 'carter page', 'james bond', 'coloradans', 'act 1871', 'trumpcare', 'carl', 'australians', 'bbc news', 'joe-jitsu', 'jds', 'wcs', 'gameb', 'house health bill', 'republican party', 'sam', 'la', 'vienna', 'eminem', 'jim clyburn', 'ag sessions', 'vitalii sediuk', 'canonization', 'jeff sessions', 'california', 'jones', 'azerbaijan', 'putin', 'alexander rybak', 'the korean peninsula', 'u.k', 'dos santos', 'united states foreign intelligence surveillance court', 'roe v. wade', 'collabs', 'halsey', 'trump', 'house republicans', 'hallelujah', 'nina', 'democratic party', 'portuguese', 'christian', 'islam', 'sax', 'salvador sobral', 'dm', 'dark horse', 'demian', 'oaklettes', 'ufc 211', 'earth', 'penicillin', 'congressional house', 'bev hills', 'middle east', 'military', 'taput', 'asia', 'cuban', 'justin timberlake', 'house passage', 'sessions', 'turkish', 'the sleep inducing backpack', 'sheila jackson', 'joanna', 'haim', 'texas', 'real madrid', 'tokio hotel', 'pro abolotion', 'dem', 'russian', 'gignac', 'african americans', 'townhall', 'sweden', 'sorosian', 'united states of flyover america', 'syria strike', 'la la land', 'american people', 'nsa', 'harry', 'united states of west america', 'ncah', 'jim crow', 'mussolini', 'mexico', 'jimmy fallon', 'pbo', 'barfy cam', 'obamacare', 'hybrid theory', 'cankles', 'flint', 'iran deal', 'reps', 'starving', 'red carpet', 'u.s. strike', 'dear white people', 'portugal', 'pepsi', 'prince kushner', 'niall', 'judy', 'racism', 'maroon 5', 'asian', 'rodriguez', 'apocalypse', 'death panel', 'google project tango', 'ruth', 'msm', 'machine gun kelly', 'commonwealth games', 'eurovision', 'sophie turner', 'senate republicans', 'spicy', 'dq', 'election day', 'aldo', 'susan rice', 'haiku', 'snl', 'bryce harper', 'reconstruction south', 'canadian', 'noah', 'affirmative action', 'san diego', 'luisa', 'violet', 'colonialism', 'niall horan', 'europe', 'lincoln park', 'harry cantando', 'nov 2018', 'health care law', 'superior spa', 'junior', 'ostriches', 'south africa', 'cub swanson', 'trump-putin', 'payno', 'breitbarters', 'sjw', 'moon', 'florida', 'gop', 'masvidal', 'frankie edwards', 'gop health bill', 'dustin poirier', 'lord vader', 'armenia', 'italian', 'tomahawk', 'red pill', 'chucklevision', 'united kingdom', 'democrat', 'chase sherman', 'north america', 'lbj', 'july', 'uk', 'dreamworks', 'new york times', 'i want candy', 'rep', 'nathan trent', 'mlk jr', 'rachel', 'planned parenthood', 'nylon', 'switzerland', 'savior', 'gauteng', 'russian agent', 'lp', 'twood', "it's always sunny in philadelphia", 'lynch/obama/rice', 'ron', 'ukranian', 'wp', 'japanese high school', 'health plan', 'congress', 'american christians', 'insulin', 'vegas', 'mendes', 'david branch', 'bsb', 'holloway', 'diaz', 'irs', 'panther', 'fox news', 'ryan gosling', 'sam clovis', 'nkorea', 'liberals', 'george', 'pro-birth', 'adams', 'obama ck', 'bjj', 'arn anderson', 'trumpanzees', 'frankie ed', 'hof', 'instagram', 'timur m', 'mcgregor', 'daniel', 'holocaust centers', 'bloods', 'civil rights movement', 'kendrick lamar', 'thatcher', 'jason blossom', 'libs', 'matt brown', 'pastorjerry', 'panthers', 'urals', 'health care act', 'snapchat', 'vlad putin', 'nc', "we can't stop", 'computer networking', 'eric allen bell', 'acting atty general', 'comrade comey', 'obama admin', 'bradford', 'adele', 'russians', 'liam e niall', 'maia', 'scarface', 'alvarez', 'liam viendo', 'house', 'ptsd', 'avocadies', 'leeds bradford airport', 'blair', 'polonium tea syndrome', 'rick story', 'jason knight', 'family services', 'ufc', "o'care", 'fisa court', 'slow hands', 'mmafighting', 'alessia cara', 'buzzfeed germany', 'meu deus', 'ne', 'jenga', 'us', 'mike flynn', 'hansel robles', 'rokita', 'svoboda', 'anglo celtic', 'weiner', 'tmt', 'joe silva', '2016 presidential campaign', 'liam', 'ed balls', 'dnc', 'fbi', 'india', 'katy perry', 'congressional gop', 'gen. flynn', 'democrat party', 'kyiv', 'wikipedia', 'bulgarian', 'turkey', 'hrw', 'fourth reich', 'yair', 'brazilian fighters', 'el joven diario', 'google', 'ukrainne', 'it security', 'on the loose', 'south america', 'belgium', 'nazis', 'irish', 'liberal', 'joanna jedrzejczyk', 'dolly parton', 'watergate', 'republicans', 'scary clown cars', 'imri', 'manel navarro', 'amar pelos dois', 'stella', 'civil rights laws', 'aussie', 'geli', 'jesus', 'spurs', 'pantera', 'english', 'numb', 'andy biggs', 'ahca', 'diane abbott', 'dc', 'africans', 'wonder world tour', 'the death panel', 'odessa', 'bon appetit', 'otc', 'måns', 'soviet russia', 'chameleon', 'bobby ryan', 'white supremacist', 'krzysztof jotko', 'bulgaria', 'u.s', 'affordable care act', 'disney', 'martin luther king jr', 'ariel g', 'roger pontare', 'ny', 'royce', 'merrill lynch', 'arizona', 'un secgen', 'linkin park', 'gong show', 'salvo', 'carson', 'aussies', 'mira', 'b.j.penn', 'rodgriguez', 'adam', "donna d'erri", 'usa', 'trump tower', 'michael savage', 'foreign policy advisor']
# print(my_list)
print(len(my_list))
flat_tweets=""
for index, row in tweets.iterrows():
    tweetText=str(row['TweetText'])
    flat_tweets=flat_tweets+" "+str(index)+tweetText 


# tokenized_words =word_tokenize(flat_tweets)
# for candidate in my_list:
#     for word in tokenized_words:  
#         if candidate in word:
#             correct_form=string.capwords(candidate)
#             if(correct_form not in word):
#                 print(word)

filtered=[]
for candidate in my_list:
    index=flat_tweets.find(candidate)
    #match found
    # if(index!=1):
        # print(candidate)
    if(candidate in flat_tweets):
        # print(candidate)
        filtered.append(candidate)
        # print(flat_tweets[index])
        # correct_form=string.capwords(candidate)
        # if(correct_form not in flat_tweets):
        #     print(correct_form,candidate)


print(filtered,len(filtered),len(my_list))

# print(list(set(my_list) - set(filtered)))
# print(flat_tweets)