saveaction = dict( # save player card
             RisenfromtheSea =            ("Risen from the Sea", "0e42b4fb-8a0e-40d1-a398-fd9c0f7912a4", "Event", "Hand", "Greyjoy.", "Event"),
             Bodyguard =                  ("Bodyguard", "f5173e6f-1ec3-4ee0-8274-755160c57c0e", "sacrifice", "table", "all", "Attachment"),
             MaesterAemon =               ("Maester Aemon", "157ee453-9a78-480a-bf0e-93d74c49dc88", "kneel", "table", "Night's Watch.", "Character"))

counterevent = dict( # cancel card
             Treachery =                  ("Treachery", "3fbc7d75-3d0b-49df-8841-c92566a8c6d3", "Event", "Hand","Location/Character/Attachment", "Lannister.","Yes","all"),
             TheHandsJudgment =           ("The Hand's Judgment", "c5d78fb6-ff52-4012-ac95-547ed9feec0f","Event", "Hand", "Event", "all","","opponent"),
             BranStark =                  ("Bran Stark", "9e56783a-c133-4f81-9914-4e81b92ba5d1", "sacrifice", "table", "Event", "all","","opponent"))

cardability = dict( # save card ability
             Bodyguard =                  ("Bodyguard", "f5173e6f-1ec3-4ee0-8274-755160c57c0e", "Attachment", "sacrifice", "", ""),
             RisenfromtheSea =            ("Risen from the Sea", "0e42b4fb-8a0e-40d1-a398-fd9c0f7912a4", "Attachment", "Greyjoy", "savetarget"))

cardkill = dict( # leave ability
             BenjenStark =            ("Benjen Stark", "dcbbfe54-078f-44c9-88e7-02efe235911c", "me", "2 power",""),
             SerDavosSeaworth =       ("Ser Davos Seaworth", "813fb666-b32f-4ae9-b2ac-3fe09adccf9a", "none", "",""),
             ViserysTargaryen =       ("Viserys Targaryen", "6580b898-de89-4a6d-89b4-72cfc3b505e6", "all", "discard", "Attachment"),
             SerWaymarRoyce =         ("Ser Waymar Royce", "e65c6d16-075b-4634-a490-a200bb75e3be", "other", "discard", "card"),
             ShireenBaratheon =       ("Shireen Baratheon", "6967fd81-f9f9-4077-8d5a-c9ca189a5e41", "all", "kneel", "Character"),
             BastardDaughter =        ("Bastard Daughter", "fcba07e6-a15f-46d8-821c-8a14a4983284", "other", "discard", "other", "Bastard Daughter"),
             TheRedViper =            ("The Red Viper", "73a43b0f-8337-4e71-96b7-9553d5d57ddf", "link", "discard", "other", "", "Bastard Daughter"))
leavedeck = dict( # leave prosition
             BenjenStark =            ("Benjen Stark", "dcbbfe54-078f-44c9-88e7-02efe235911c", "deck"),
             SerDavosSeaworth =       ("Ser Davos Seaworth", "813fb666-b32f-4ae9-b2ac-3fe09adccf9a", "deck"))

leavereacion = dict( # leave reaction
             JoffreyBaratheon =       ("Joffrey Baratheon", "df79718d-b01d-4338-8907-7b6abff58303", "Traits", "Lord./Lady.", "1 power", 3),
             RobbStark =              ("Robb Stark", "d892faa0-09c4-41ec-8705-abe2c1c87c83", "Faction", "Stark.", "stand", 1))

afterchallengereacion = dict( # 4.2 reaction
             TyrionLannister =       ("Tyrion Lannister", "102c0746-2205-425a-ab85-90dc41a031e3", "2", "all", "2 gold", 2),
             Ghost =                 ("Ghost", "9c0f0dce-2809-4ad9-bc27-ba5bb15484ee", "all", "", "stealth", 1),
             DornishParamour =       ("DornishParamour", "f70034a0-01a1-4e77-8dde-44c1cd7d3f40", "all", "", "makedefender", 1),
             EddardStark =           ("Eddard Stark", "aee0eeeb-97a7-4b48-82e7-03141663e346", "all", "defender", "stand", 1))

aftercalculate = dict( # 4.2.2 reaction
             RattleshirtsRaiders =   ("Rattleshirt's Raiders", "be9304f2-bb5d-4d19-8fbe-4efb6ee24f29", "all", "attacker", "disotherattachment", 1, "table", ""),
             PuttotheSword =         ("Put to the Sword", "38dd5d15-7214-4c68-9cc4-0d2abd1b2140", "1", "attacker", "kill", 1, "Hand", 5),
             PuttotheTorch =         ("Put to the Torch", "997f1584-7092-4895-ac40-fc9fd98891bc", "1", "attacker", "disotherloaction", 1, "Hand", 5),
             SuperiorClaim =         ("Superior Claim", "8e9b06da-991e-4608-a16b-caf96209641a", "3", "all", "2 power", 1, "Hand", 5),
             TearsofLys =            ("Tears of Lys","b29c7bb5-7b84-4e94-a30b-8332fad51c2a","2","attacker","addmarker",1,"Hand",""),
             AshaGreyjoy =           ("Asha Greyjoy","41367a9d-b751-4632-9973-97d2e4df7087","all","attacker","stand",1,"table","uo"),
             TheonGreyjoy =          ("Theon Greyjoy","9a29f7bb-baa9-4475-8e35-55b845618822","all","attacker","addpowself",1,"table","uo"),
             GreatKraken =           ("Great Kraken","014da37c-9903-418d-a043-ee2191b9d169","all","attacker","drawcardorpower",1,"table","uo"),
             ThrowingAxe =           ("Throwing Axe","c3eeb001-e6a1-48ae-b310-cbd0d2c84653","all","attacker","attkilldef",1,"table",""),
             WeDoNotSow =            ("We Do Not Sow","62570a84-3203-468d-9529-37dbbc6d191c","all","attacker","disotherloactionattachment",1,"Hand","uo"),
             Lannisport =            ("Lannisport","5702d5f9-ae1e-435b-ae86-01c14817431a","2","all","drawcard",1,"table",""),
             MaesterCaleotte =       ("Maester Caleotte","4f58fa4d-7172-4466-86eb-32b2bb91b516","all","all","submarker",1,"table",""),
             TheRedViper =           ("The Red Viper","73a43b0f-8337-4e71-96b7-9553d5d57ddf","all","attacker","5pwinpow",1,"table",5),
             GhastonGrey =           ("Ghaston Grey","982acc7e-86c0-4bdd-84da-3b05e53dffa1","all","defender","returndefender",1,"table",""),
             Sunspear =              ("Sunspear","f2772a6e-2ed4-4fb9-8699-5497aee496e3","all","defender","addclaim",1,"table",""),
             DoransGame =            ("Doran's Game","427a5213-1be5-4b36-94be-04a5b3486575","2","all","addusedplotpow",1,"Hand",5),
             UnbowedUnbentUnbroken = ("Unbowed, Unbent, Unbroken","ad97966b-2d52-4b03-a8f4-f51c8a63a8c9","all","defender","cant1challenge",1,"Hand",""),
             TheSwordintheDarkness = ("The Sword in the Darkness","18715d47-dbe1-4f02-a5b3-e1d7f6943287","all","defender","cantchallenge",1,"Hand",5),
             LikeWarmRain =          ("Like Warm Rain","ef7d8bdf-1c56-4895-be9a-7a3ed059dcd3","2","defender","losekill",1,"Hand",""),
             Rhaegal =               ("Rhaegal","ac263d0d-d7db-49e7-bdc4-2e131d95aad4","all","all","standstm",1,"table",""),
             PlazaofPunishment =     ("Plaza of Punishment","06803230-d3a4-46f7-935a-1a7314839b9e","3","all","subability2",1,"table",""),
             DothrakiSea =           ("Dothraki Sea","1916c9ad-78da-42c7-9d22-8f059438dadc","3","all","addplayer",1,"table",""),
             MaesterLomys =          ("Maester Lomys","54111e34-4bec-4415-a562-fbd3f1ebbb77","2","defender","discard",1,"table",""),
             TheQueenofThorns =      ("The Queen of Thorns","0b5ca49f-5270-4b9f-84d4-391b59a2d4bc","2","all","addplayer6",1,"table",""),
             TheMander =             ("The Mander","bf44916f-cc99-4f0a-87f0-b529a426df7b","all","all","draw2card",1,"table","5"),
             OlennasCunning =        ("Olenna's Cunning","3fd0054d-0a3c-4ab9-9ea5-96b0a1ac4628","23","all","addhand",1,"Hand",""),
             Ice =                   ("Ice","e6059d34-2c23-41a1-a1c2-f299dee662e7","1","all","kill",1,"table",""),
             AClashofKings =         ("A Clash of Kings","de88edda-f5a4-4985-8ac1-2b8205c13416","3","all","movepow",1,"table",""),
             SerJorahMormont =       ("Ser Jorah Mormont","1de2665b-53be-4e48-8c5c-42f93fdf40a3","all","all","addred",1,"table",""),
             TheWall =               ("The Wall","5d20e021-5d12-4338-8bdd-42d008bff919","all","all","kneel",1,"table","uo"))

keywordslib = dict( # 4.2.5 keywords
            WildlingHorde =          ("Wildling Horde","21dda206-536e-4944-8158-b3d174e2b872","Pillage."),
            RobertBaratheon =        ("Robert Baratheon","78ca6089-6d16-4e41-8df7-40042e3dc077","Initimidate.Renown."),
            BalonGreyjoy =           ("Balon Greyjoy","9bc99c98-4cbd-467b-b31c-1bec686370ea","Renown."),
            EuronCrowsEye =          ("Euron Crow's Eye","912e5447-89b3-4896-903c-6f5ed78113e1","Pillage. Renown."),
            BlackWindsCrew =         ("Black Wind's Crew","4675c354-8fc6-4fbe-bbab-fb9318cce036","Pillage."),
            GrandMaesterPycelle =    ("Grand Maester Pycelle","66e4dd85-8a1d-4ea1-b3c6-3d3c7069a783","Insight."),
            TywinLannister =         ("Tywin Lannister","390a8cf7-8bc4-45c1-bea5-e6a694e9f2d5","Renown."),
            DoranMartell =           ("Doran Martell","295184b5-9b32-45d7-a870-c2a5580e1f75","Insight."),
            SamwellTarly =           ("Samwell Tarly","aab739f7-aae2-4228-a446-89c4e7f91ea2","Insight."),
            EddardStark =            ("Eddard Stark","aee0eeeb-97a7-4b48-82e7-03141663e346","Renown."),
            GreyWind =               ("Grey Wind","c8777aab-2cd5-45c0-a59f-7d291aea9435","Initimidate."),
            RobbStark =              ("Robb Stark","d892faa0-09c4-41ec-8705-abe2c1c87c83","Renown."),
            DaenerysTargaryen =      ("Daenerys Targaryen","a2f21413-0272-47dc-a197-e364aa942d4c","Insight."),
            KhalDrogo =              ("Khal Drogo","09903f79-6155-4a63-9b52-e10fb2e69898","Renown."),
            SerJorahMormont =        ("Ser Jorah Mormont","1de2665b-53be-4e48-8c5c-42f93fdf40a3","Renown."),
            RandyllTarly =           ("Randyll Tarly","dd950122-b92e-4d6b-b1f4-d8a3f623a99a","Renown."),
            TheKnightofFlowers =     ("The Knight of Flowers","dfb7512e-0d80-4dff-8fdf-4807d93ba159","Renown."))

actionchallenge =  dict( # 4.2 action
            WildlingHorde =          ("Wildling Horde","21dda206-536e-4944-8158-b3d174e2b872","kneelhouse+2str","table",1,""),
            SelyseBaratheon =        ("Selyse Baratheon","88de8a8f-4d15-415c-96c8-38edc8f8fe99","addinticon","table",1,""),
            OursistheFury =          ("Ours is the Fury","9d1702a8-32c9-41c2-bbd4-2ce00885e20a","adddef","Hand",1,"defender"),
            SeenInFlames =           ("Seen In Flames","50402306-cc27-4e3e-9924-aa13f430cb60","dischand","Hand",1,""),
            IronFleetScout =         ("Iron Fleet Scout","6357f740-5434-4d09-957a-87af33f9b57b","addstr","table",1,""),
            TheKrakensGrasp =        ("The Kraken's Grasp","80300190-96a8-4fa7-be7f-1a2bea691978","ignorestr","Hand",1,"fplay"),
            TheThingsIDoForLove =    ("The Things I Do For Love","6d93075c-8517-44ef-8580-f4fdfe1967da","kneelhousereturnhand","Hand",1,"Lord./Lady."),
            GatesofWinterfell =      ("Gates of Winterfell","14fb9ce4-6d48-4c9f-a8d0-5ded218714dc","drawstark","table",1,""),
            FortheNorth =            ("For the North","764fd244-f0f0-4b61-a435-9cf73ef074ce","addstrdraw","Hand",1,""),
            WinterIsComing =         ("Winter Is Coming","18f549b8-eda2-4a40-8196-d952f5a4874f","addclaim","Hand",1,""),
            Dracarys =               ("Dracarys","aae782b7-cd97-4818-b56a-d1dafe6f80de","burn","Hand",1,""),
            FireandBlood =           ("Fire and Blood","06a715e0-f26c-4894-8610-63353d73e0fd","returndead","Hand",1,""),
            MargaeryTyrell =         ("Margaery Tyrell","9e0df853-1c6d-4be2-b799-fe69524a6057","addstr3","table",1,""),
            Heartsbane =             ("Heartsbane","4c8a114e-106c-4460-846b-28f73914fc11","attaddstr3","table",1,""),
            Highgarden =             ("Highgarden","15ae647f-bc30-4cca-aeed-bb675c8096c7","standremovechallenge","table",1,""),
            GrowingStrong =          ("Growing Strong","92d9670d-d842-4c6c-990c-e1e5cb05759d","3playeraddstr2","Hand",1,""),
            OlennasInformant =       ("Olenna's Informant","e1278811-db3b-4097-9f7c-54d9bab37f91","choosechallenge","Hand",1,"ambush"),
            AreoHotah =              ("Areo Hotah","7412a0da-c314-4852-ab1f-04bb163dac39","removechallenge","Hand",1,"ambush"))


keywordsreaction = dict(
             EuronCrowsEye =         ("Euron Crow's Eye","912e5447-89b3-4896-903c-6f5ed78113e1","all","both","controlllocation",1,"table",""))

plotdict =  dict( # plot
            # AGameofThrones =         ("A Game of Thrones","c6d4c560-873d-425e-a05c-7dd2eb57c324","winint",""),
            # ANobleCause =            ("A Noble Cause","0fb3ad4b-5cf3-49e9-a33f-484ecafeabf8","firstll",""),
            # AStormofSwords =         ("A Storm of Swords","a02bce64-e292-487e-a666-cd07b4a11e59","addmilcount",""),
            BuildingOrders =         ("Building Orders","34e54ffc-9806-49da-a8a0-d38a17f6753d","10searchatloc",""),
            CallingtheBanners =      ("Calling the Banners","3a3577a4-5ee1-4e9f-a674-49e9f9e81568","1c1g",""),
            CalmOverWesteros =       ("Calm Over Westeros","4ee52602-89fa-4048-accc-dffdb78bee69","subclaim",""),
            Confiscation =           ("Confiscation","446ac0b9-746f-4aa3-b8bf-f132d2b29499","discattachment","1"),
            CountingCoppers =        ("Counting Coppers","1b362220-c8c2-4600-b204-06342e58b09c","draw3",""),
            FilthyAccusations =      ("Filthy Accusations","ac8effb7-76cb-42e4-ab33-d88a407c0dda","kneel","1"),
            HeadsonSpikes =          ("Heads on Spikes","424194c0-ad9c-473b-b254-40b1274152ba","discplayer",""),
            # JoustingContest =        ("Jousting Contest","0b94080f-2207-4663-8990-f9370ab77709","challenge1player",""),
            # MarchingOrders =         ("Marching Orders","d526faac-594d-4f40-9da5-42300d44c12e","cantuselia",""),
            # NavalSuperiority =       ("Naval Superiority","68448806-ca58-496d-b010-2794fd372744","gold0",""),
            Rebuilding =             ("Rebuilding","fedb6fe6-2f55-4c42-9798-3e091b2b2573","adddisc3",""),
            # SneakAttack =            ("Sneak Attack","d4576f9d-16a6-430e-9f73-217216fd43b9","1challenge",""),
            Summons =                ("Summons","a380b0e0-610c-47f9-ac9f-ae12163b45fd","10searchcha",""),
            Reinforcements =         ("Reinforcements","5de352a4-c6fd-478c-bac0-39b78de1e68c","search5c",""),
            # MarchedtotheWall =       ("MarchedtotheWall","a9f2fccd-11f3-4562-aa5a-76d606712311","disc1player",""),
            # WildfireAssault =        ("Wildfire Assault","d10a1ced-df94-419b-af8e-4eadc2eb4688","kill3player",""),
            PowerBehindtheThrone =   ("Power Behind the Throne","12f6e8de-5627-4e71-90f6-1f79f17be44e","addstandicon",""),
            TradingwiththePentoshi = ("Trading with the Pentoshi","bc3547ae-82fc-4da1-a375-209ba0c07748","gain3gold",""),
            HeretoServe =            ("Here to Serve","f68a9d16-dea2-4eae-a03f-8fbc48e2c85c","search3maester",""))
            # PoliticalDisaster =      ("Political Disaster","bc45b0f8-21ae-4ae2-b86d-f78008f25566","select2location",""),
            # FortifiedPosition =      ("Fortified Position","79877d2a-5b23-4c16-86df-9453c065835b","allnoprint",""))


generalaction =  dict( # generalaction
            HearMeRoar =          ("Hear Me Roar","2ad9b318-4ff7-4ace-91ee-81e223fd176c","addlan","Hand",1,""),
            ArianneMartell =      ("Arianne Martell","fa34ed25-de84-45c9-89c1-1428ec505458","add5returnme","table",1,""),
            EdricDayne  =         ("Edric Dayne","b32b7ea7-7997-4b02-8b2f-25ad4d1072fa","1goldicon","table",99,"gold1"),
            Confinement =         ("Confinement","9aafaad7-3f74-4aff-ba0c-bf19e5de0bdf","loseicon","Hand",1,""),
            OldForestHunter =     ("Old Forest Hunter","89207067-9a33-4689-9b8a-66c85f7c68c1","d1cg1g","table",1,""),
            VeteranBuilder =      ("Veteran Builder","ae0ac552-9668-4df3-a236-49389b7f4cb8","standlocation","table",1,""),
            MagisterIllyrio =     ("Magister Illyrio","f5f343ea-a561-415b-adfd-9afdd65820c2","2gstandc","table",1,"gold2"),
            Handmaiden  =         ("Handmaiden","a575226f-fba6-4d79-bdf7-e5a0c2e0d192","standlady","table",1,""),
            WakingtheDragon =     ("Waking the Dragon","393fb603-c449-4043-a73f-21c4b47be039","standtc","Hand",1,""),
            TheBearandtheMaidenFair =("The Bear and the Maiden Fair","202b37de-c6bf-4c21-93fd-f3cf6bbad04d","5t3b","Hand",1,""),
            Fealty =              ("Fealty","83754e87-8448-49af-a20f-bc4dc72d1dba","kneelfaction","table",1,""),
            PowerBehindtheThrone =   ("Power Behind the Throne","12f6e8de-5627-4e71-90f6-1f79f17be44e","standicon","table",1,""),
            Halder =              ("Halder","ba89a709-fe0b-4c19-bc2e-5a55c1ef4659","manual","table",1,""),
            TheWatchHasNeed =     ("The Watch Has Need","0fcc5481-0631-4e82-a3c4-cca7535241bd","searchbrs","Hand",1,""),
            InDoransName =        ("In Doran’s Name","1d57651e-d2c9-4eea-9ed3-a80894660bb0","addusedplotgold","Hand",1,""),
            WolfDreams =          ("Wolf Dreams","cb5ae535-6b4b-4100-8593-1e231b3da602","searchwolf","Hand",1,""),
            Nightmares =          ("Nightmares","9d81eee2-2281-4bad-933c-9915b9eb9aca","noprint","Hand",1,""),
            Lady =                ("Lady","d4827a8a-6403-4d47-bb47-813073b78b49","changecontroll","table",1,""),
            AGiftofArborRed =     ("A Gift of Arbor Red","a788cd32-5b5b-40d1-a485-629adb2c4b3a","4cardchoose2","Hand",1,""),
            EvenHandedJustice=    ("Even-Handed Justice","69fe7a62-2def-4e6c-9c61-4728ff354ab0","eachkneel","Hand",1,""),
            TourneyGrounds=       ("Tourney Grounds","5183c3de-7174-4f1d-b9cd-67c47a4b7251","reducenextevent","table",1,""))

dominancestart =  dict( # dominancestart
            FieryFollowers =      ("Fiery Followers","21c87233-3c2e-4a66-9ea0-ffaf5ac0594c","stand","table",1,""))

dominancewin =  dict( # dominancewin
            AFeastforCrows =            ("A Feast for Crows","0ed58a09-7482-4632-b88f-309ae5621c2e","2power","table",1,""),
            AeronDamphair =             ("Aeron Damphair","c4fbe19b-fe3b-4f5c-b1c6-065c13c4a9db","returniron","table",1,""),
            ChamberofthePaintedTable =  ("Chamber of the Painted Table","8b8d9c4c-a100-4d95-b68b-5156766035d9","move1pow","table",1,""))

dominanceaction =  dict( # dominanceaction
            TaketheBlack =          ("Take the Black","1a0183ed-61fd-4302-b19b-1640f0c11500","controll6","Hand",1,""),#manual
            MessengerRaven =        ("Messenger Raven","0ebedb0f-d94c-4f8f-a478-2cffc712c6c7","returndraw1","table",1,""),
            TheTickler  =           ("The Tickler","5e826f43-d1d0-4c3c-8939-789ce55bcf1d","disctop","table",1,""))#manual

dominanceend =  dict( # dominanceend
            Varys =               ("Varys","78845c6e-c91a-47a2-9742-d72b19d0ed26","cleartable","table",1,""))#manual

marshalaction = dict( # dominanceend
            TheKingsroad =             ("The Kingsroad","90452d99-6a6f-4d0d-b3a1-bb92e7110d1d","reduce3s","table",1,""),
            MaesterCressen =           ("Maester Cressen","0c97b091-96c0-46df-8442-e904025304fb","discattachmentc","table",1,""),
            DragonstoneFaithful =      ("Dragonstone Faithful","2a669f95-cad1-43eb-b7a5-4aac56b411de","reduce1Baratheoncharacter","table",1,""),
            DragonstonePort =          ("Dragonstone Port","1daa814f-c6b8-4dcc-b4f7-169968be4bc5","reduce1Baratheoncard","table",1,""),
            ConsolidationofPower =     ("Consolidation of Power","b1092dd9-01aa-4622-9026-d905a44dd874","kneel4cadd1power","Hand",1,""),
            IronIslandsFishmonger =    ("Iron Islands Fishmonger","1ea5aae7-d6c0-4589-afe1-c190743ebdbf","reduce1Greyjoycharacter","table",1,""),
            LordsportShipwright =      ("Lordsport Shipwright","23ca65d8-2c23-4d39-8c21-72323af0fc93","kneel2location","table",1,""),
            SeaTower =                 ("Sea Tower","3bcc0681-2362-4c2a-8e17-e20e23dbda3c","reduce1Greyjoycard","table",1,""),
            LannisportMerchant =       ("Lannisport Merchant","d2b926e3-2c0a-4575-b144-bf27ced1e5b3","reduce1Lannistercharacter","table",1,""),
            WesternFiefdom =           ("Western Fiefdom","35c97ac8-de68-4de7-a2a8-f18dbf139041","reduce1Lannistercard","table",1,""),
            DesertScavenger =          ("Desert Scavenger","c549499d-6a95-460a-a075-c4592d2f768f","reduce1Martellcharacter","table",1,""),
            BloodOrangeGrove =         ("Blood Orange Grove","6b6df968-1810-4e4d-b739-9256caac008b","reduce1Martellcard","table",1,""),
            StewardattheWall =         ("Steward at the Wall","420b7dab-f35c-4a07-bdbf-fe1c027bfecd","reduce1NWcharacter","table",1,""),
            Winterfellteward =         ("Winterfell Steward","ea996816-e75f-4c13-ac0f-97b96818b220","reduce1Starkcharacter","table",1,""),
            HeartTreeGrove =           ("Heart Tree Grove","5f5c0380-034b-4fa0-9da5-9c53b098baed","reduce1Starkcard","table",1,""),
            TargaryenLoyalist =        ("Targaryen Loyalist","0e2c6c02-c6c7-4273-825f-1d03b24998a2","reduce1Targaryencharacter","table",1,""),
            IllyriosEstate =           ("Illyrios Estate","bc9a511e-9f90-4b4f-892e-e8ad46103da9","reduce1Targaryencard","table",1,""),
            GardenCaretake =           ("Garden Caretake","8192ab17-f699-45b9-931b-e0933dbc01eb","reduce1Tyrellcharacter","table",1,""),
            RoseGarden =               ("Rose Garden","8f0e7f8b-d08c-4c89-972a-ad765a27a061","reduce1Tyrellcard","table",1,""),
            Bronn =                    ("Bronn","d8f39831-ef30-4f90-a8cb-8bbc4c659c7d","controllb","table",1,"gold1"),
            TotheRoseBanner =          ("To the Rose Banner","4dc05cfc-e71f-49be-9c2c-c383d1332a5f","scgetgold","Hand",1,""))

eventeffect = dict(
            PuttotheTorch =            ("Put to the Torch", "997f1584-7092-4895-ac40-fc9fd98891bc","disotherloaction","1"),
            SuperiorClaim =            ("Superior Claim", "8e9b06da-991e-4608-a16b-caf96209641a","2 power",""),
            SeenInFlames =             ("Seen In Flames","50402306-cc27-4e3e-9924-aa13f430cb60","dischand",""),
            TearsofLys =               ("Tears of Lys","b29c7bb5-7b84-4e94-a30b-8332fad51c2a","addmarker","1"),
            WeDoNotSow =               ("We Do Not Sow","62570a84-3203-468d-9529-37dbbc6d191c","disotherloactionattachment","1"),
            HearMeRoar =               ("Hear Me Roar","2ad9b318-4ff7-4ace-91ee-81e223fd176c","addlan","1"),
            TheThingsIDoForLove =      ("The Things I Do For Love","6d93075c-8517-44ef-8580-f4fdfe1967da","kneelhousereturnhand","1"),
            DoransGame =               ("Doran's Game","427a5213-1be5-4b36-94be-04a5b3486575","addusedplotpow",""),
            Confinement =              ("Confinement","9aafaad7-3f74-4aff-ba0c-bf19e5de0bdf","loseicon","1"),
            TaketheBlack =             ("Take the Black","1a0183ed-61fd-4302-b19b-1640f0c11500","controll6","1"),
            FortheNorth =              ("For the North","764fd244-f0f0-4b61-a435-9cf73ef074ce","addstrdraw","1"),
            Dracarys =                 ("Dracarys","aae782b7-cd97-4818-b56a-d1dafe6f80de","burn","1"),
            FireandBlood =             ("Fire and Blood","06a715e0-f26c-4894-8610-63353d73e0fd","returndead",""),
            WakingtheDragon =          ("Waking the Dragon","393fb603-c449-4043-a73f-21c4b47be039","standtc","1"),
            OlennasCunning =           ("Olenna's Cunning","3fd0054d-0a3c-4ab9-9ea5-96b0a1ac4628","addhand",""),
            TheBearandtheMaidenFair =  ("The Bear and the Maiden Fair","202b37de-c6bf-4c21-93fd-f3cf6bbad04d","5t3b",""))

def debug(str):
	mute()
	global debugMode
	if debugMode:
		whisper("Debug Msg: {}".format(str))

def debugmode(group, x = 0, y = 0):
      mute()
      global debugMode
      if debugMode:
            debugMode = False
            notify("Debug Off")
      else:
            debugMode = True
            notify("Debug On")
