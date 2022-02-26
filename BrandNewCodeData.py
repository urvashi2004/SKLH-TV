import mysql.connector as ms

db = ms.connect(host="localhost",user="root",passwd="urvashi22")

if db.is_connected():
    print("Connection Established")
else:
    print("Connection Not Connected")

cs = db.cursor()

cs.execute("drop database sklh_tv;")
cs.execute("create database sklh_tv;")
cs.execute("use sklh_tv;")

cs.execute("create table users(Username varchar(20) primary key not null, Name varchar(40) not null, Password varchar(40) not null);")
cs.execute("insert into users values ('admin','adminsname','password');")

cs.execute("create table content(ID char(4) primary key not null, Title varchar(40) not null, Type varchar(10) not null,Year int not null,Country varchar(40),Genre varchar(40),Summary varchar(2000));")
cs.execute("insert into content values ('101M','Your Name','Movie',2016,'Japan','Fantasy','Two teenagers share a profound, magical connection upon discovering they are swapping bodies. Things manage to become even more complicated when the boy and girl decide to meet in person.');")
cs.execute("insert into content values ('102S','Blood And Water','TV Show',2021,'South Africa','Drama','After crossing paths at a party, a Cape Town teen sets out to prove whether a private-school swimming star is her sister who was abducted at birth.');")
cs.execute("insert into content values ('103M','Intrusion','Movie',2021,'United States','Thriller','When a husband and wife move to a small town, a home invasion leaves the wife traumatized and suspicious that those around her might not be who they seem.');")
cs.execute("insert into content values ('104M','King of Boys','Movie',2018,'Nigeria','Thriller','Her insatiable appetite for power drives Eniola, a businesswoman and philanthropist, into politics. As she is drawn into a struggle for power her criminal baggage will prove a heavy burden.');")
cs.execute("insert into content values ('105S','Castle','TV Show',2009,'United state','Crime','After a serial killer imitates the plots of his novels, successful mystery novelist Richard Rick Castle receives permission from the Mayor of New York City to tag along with an NYPD homicide investigation team for research purposes.');")
cs.execute("insert into content values ('106S','Bangkok Breaking','TV Show',2021,'Thailand','Drama','Struggling to earn a living in Bangkok, a man joins an emergency rescue service and realizes he must unravel a citywide conspiracy.');")
cs.execute("insert into content values ('107S','Jaguar','TV Show',2021,'Spain','Thriller','In the 1960s, a Holocaust survivor joins a group of self-trained spies who seek justice against Nazis fleeing to Spain to hide after WWII.');")
cs.execute("insert into content values ('108S','Dharmakshetra','TV Show',2002,'India','Mythology','After the ancient Great War, the god Chitragupta oversees a trial to determine who were the true heroes and villains.');")
cs.execute("insert into content values ('109S','Hotel Del Luna','TV Show',2019,'South Korea','Comedy','When he is invited to manage a hotel for dead souls, an elite hotelier gets to know the ancient owner and her strange world.');")
cs.execute("insert into content values ('110M','Cold Mountain','Movie',2003,'United States','Drama','This drama follows a wounded Civil War soldier making the long journey home, while his faraway love fights for survival on her farm.');")
cs.execute("insert into content values ('111M','Shikara','Movie',2020,'India','Romantic','Shiv and Shanti, a young couple, chronicle their love story amid the exodus of Kashmiri Hindus from Kashmir; forced to leave their homes and live as refugees in their own country, the couple, among thousand others, struggle to keep their hopes alive.');")
cs.execute("insert into content values ('112S','Kurokos Basketball','TV Show',2015,'Japan','Manga','Five middle school basketball stars went to separate high schools, and now Tetsuya Kuroko and Seirin High are making their play for glory.');")
cs.execute("insert into content values ('113M','Level sixteen','Movie',2018,'Canada','Thriller','In a bleak academy that teaches girls the virtues of passivity, two students uncover the ghastly purpose behind their training and resolve to escape.');")
cs.execute("insert into content values ('114M','Krishna Cottage','Movie',2004,'India','Horror','True love is put to the test when another woman comes between a pair of star-crossed young lovers in this thriller.');")
cs.execute("insert into content values ('115S','Rebellion','TV Show',2016,'Ireland','Fiction','As World War I rages, three women and their families in Dublin choose sides in the violent Easter Rising revolt against British rule.');")
cs.execute("insert into content values ('116M','La diosa del asfalto','Movie',2020,'Mexico','Drama','A woman from a tough neighborhood outside Mexico City comes home a rock star, inadvertently provoking a confrontation with the ghosts of her past.');")
cs.execute("insert into content values ('117S','The crowned clown','TV Show',2019,'South Korea','Romance','Standing in for an unhinged Joseon king, a look-alike clown plays the part but increasingly becomes devoted to protecting the throne and the people.');")
cs.execute("insert into content values ('118S','Squid game','TV Show',2021,'South Korea','Horror','Hundreds of cash-strapped players accept a strange invitation to compete in games. Inside, a tempting prize awaits with deadly high stakes.');")
cs.execute("insert into content values ('119M','Flower girl','Movie',2013,'Nigeria','Romance','When a young florist who has long dreamed of her wedding day gets dumped by her boyfriend, she sets out to win him back with help from a handsome actor.');")
cs.execute("insert into content values ('120S','Dogs','TV Show',2021,'United states','Documentary','These six intimate stories explore the abiding emotional bonds that form between dogs and their caregivers, no matter the circumstances.');")
cs.execute("insert into content values ('121S','Cat people','TV Show',2021,'United States','Documentary','Cat people come in all shapes and sizes, but they share a love for their enchanting, unique feline friends. This docuseries reveals their tales.');")
cs.execute("insert into content values ('122S','Cuckoo','TV Show',2019,'United Kingdom','Comedy','Rachel shocks her proper British parents when she marries an American hippie, but it is just the first in a series of surprises for the family.');")
cs.execute("insert into content values ('123S','Girl from nowhere','TV Show',2021,'Thailand','Horror','A mysterious, clever girl named Nanno transfers to different schools, exposing the lies and misdeeds of the students and faculty at every turn.');")
cs.execute("insert into content values ('124S','Shtisel','TV Show',2021,'Israel','Drama','A Haredi family living in an ultra-Orthodox neighborhood of Jerusalem reckons with love, loss and the doldrums of daily life.');")
cs.execute("insert into content values ('125S','Undercover','TV Show',2020,'Belgium','Drama','Undercover agents infiltrate a drug kingpin operation by posing as a couple at the campground where he spends his weekends. Inspired by real events.');")
cs.execute("insert into content values ('126M','Ujala','Movie',1959,'India','Action','An honest man dreams of a better life for his family, but a childhood friend leads him into a world of crime that keeps happiness just out of reach.');")
cs.execute("insert into content values ('127S','Mortel','TV Show',2019,'France','Drama','After making a deal with a supernatural figure, two high schoolers emerge with extraordinary powers and join forces to solve a murder.');")
cs.execute("insert into content values ('128M','Sword of Trust','Movie',2019,'United States','Comedy','An offbeat foursome takes a wild journey through the Southern belt of denial to sell a relic purporting to prove the South won the Civil War.');")
cs.execute("insert into content values ('129M','Wonder boy','Movie',2019,'France','Documentary','This revealing documentary follows Balmain creative director Olivier Rousteing as he brings his bold designs to life and goes in search of his origins.');")
cs.execute("insert into content values ('130M','Life of Crime','Movie',2013,'United States','Crime','After two small-time crooks kidnap and ransom wife of a rich businessman, they discover a flaw in their plan: Her cheating husband does not want her back.');")
cs.execute("insert into content values ('131S','Locombianos','Tv Show',2021,'Colombia','Comedy','Four of funniest and bawdiest comedians perform before a post-quarantine audience hungry for their stories.');")
cs.execute("insert into content values ('132M','Sweet and sour','Movie',2021,'South Korea','Romance','Faced with real-world opportunities and challenges, a couple endures the highs and lows of trying to make a long-distance relationship survive.');")
cs.execute("insert into content values ('133M','Carnaval','Movie',2021,'Brazil','Comedy','After a breakup, an influencer takes her friends on a free trip to Bahia vibrant Carnival, where she learns life is not just about social media likes.');")
cs.execute("insert into content values ('134M','The wedding guest','Movie',2018,'United Kingdom','Thriller','Hired to extract a bride-to-be before her arranged wedding in Pakistan, a hired gun goes on the run with his hostage when his plan unravels.');")
cs.execute("insert into content values ('135M','Collateral Beauty','Movie',2016,'United States','Romance','An advertising executive wrestling with grief finds meaning by writing letters to unconventional recipients as caring colleagues plot a ruse.');")
cs.execute("insert into content values ('136S','Magic school bus','TV Show',1997,'Canada','Sci-fi','Join Ms. Frizzle as the Magic School Bus travels to outer space, under the sea, through an anthill and even inside the human body');")
cs.execute("insert into content values ('137M','Cinema Bandi','Movie',2021,'India','Comedy','The life of a struggling rickshaw driver takes a rollicking turn when he comes upon an expensive camera and decides to make a film with his fellow villagers.');")
cs.execute("insert into content values ('138M','Table manners','Movie',2018,'South Africa','Comedy','When picture-perfect life of a housewife comes crashing down, she finds solace and hope through cooking, family and love.');")
cs.execute("insert into content values ('139M','Monster','Movie',2021,'United States','Horror','A talented teen implicated in a robbery-turned-murder fights for his innocence and integrity against a criminal justice system that has already judged him.');")
cs.execute("insert into content values ('140M','Milestone','Movie',2020,'India','Drama','Recently marking 500,000 kilometers on the road, a newly bereaved trucker faces the threat of losing the job that has come to define him to a new intern.');")

cs.execute("create table request(Title varchar(40) not null, Year int not null, Type varchar(10) not null);")

db.commit()

query="select * from content"
cs.execute(query)
x=cs.fetchall()
print("%10s"%"ID","%20s"%"Name","%20s"%"Type","%20s"%"Year","%20s"%"Country","%20s"%"Genre","%20s"%"Summary")
for i in x:
    print("%10s"%i[0],"%20s"%i[1],"%20s"%i[2],"%20s"%i[3],"%20s"%i[4],"%20s"%i[5],"%20s"%i[6])